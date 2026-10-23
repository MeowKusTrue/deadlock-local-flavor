"""Build an interchange bundle from already verified standalone release ZIPs."""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--packages', type=Path, required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
tag = catalog['releaseTag']
document = {
    'format': 'deadlock-mod-interchange', 'version': 1,
    'source': {'manager': 'deadlock-local-flavor'}, 'contents': ['mods'],
    'mods': [], 'profiles': [], 'crosshairs': [], 'warnings': [],
}
bundle = args.packages / f'Deadlock_Local_Flavor_DMM_Import_{tag}.zip'
with zipfile.ZipFile(bundle, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as target:
    images = set()
    for order, mod in enumerate(catalog['mods']):
        source = args.packages / mod['archive']
        assert re.fullmatch(r'[A-Za-z0-9_.]+', source.name), source
        assert hashlib.sha256(source.read_bytes()).hexdigest() == mod['archiveSha256'], source
        with zipfile.ZipFile(source) as archive:
            assert archive.namelist() == [mod['vpk']] and archive.testzip() is None
            raw = archive.read(mod['vpk'])
        assert hashlib.sha256(raw).hexdigest() == mod['sha256']
        assert len(raw) == mod['size']
        path = 'files/' + mod['vpk']
        target.writestr(path, raw)
        images.add(mod['image'])
        document['mods'].append({
            'key': 'local:sha256:' + mod['sha256'], 'name': mod['name'],
            'enabled': False, 'order': order, 'origin': {'provider': 'local'},
            'author': catalog['author'],
            'description': mod['descriptionRu'] + '\n\n' + mod['descriptionEn'],
            'category': mod['category'], 'hero': None, 'nsfw': False,
            'thumbnailUrl': f'https://raw.githubusercontent.com/MeowKusTrue/deadlock-local-flavor/{tag}/{mod["image"]}',
            'link': catalog['repository'] + '/tree/' + tag + '/mods/' + ('shop' if mod['group'] == 'audio' else mod['group']),
            'files': [{'name': mod['vpk'], 'path': path, 'sha256': mod['sha256'],
                       'size': mod['size'], 'selected': True}],
        })
    assert len({mod['key'] for mod in document['mods']}) == len(document['mods'])
    target.writestr('mod-interchange.json', json.dumps(document, ensure_ascii=False, indent=2) + '\n')
    target.writestr('README_IMPORT.md', (root / 'docs/MOD_MANAGER.md').read_text(encoding='utf-8'))
    for image in sorted(images):
        target.write(root / image, image)
with zipfile.ZipFile(bundle) as archive:
    assert archive.testzip() is None
    saved = json.loads(archive.read('mod-interchange.json'))
    for mod in saved['mods']:
        assert mod['enabled'] is False
        for file in mod['files']:
            assert '..' not in Path(file['path']).parts
            assert hashlib.sha256(archive.read(file['path'])).hexdigest() == file['sha256']
checksums = []
for mod in catalog['mods']:
    checksums.append((mod['archiveSha256'], mod['archive']))
checksums.append((hashlib.sha256(bundle.read_bytes()).hexdigest(), bundle.name))
(args.packages / 'SHA256SUMS.txt').write_text(
    ''.join(f'{digest}  {name}\n' for digest, name in checksums), encoding='ascii')
print(f'Built and verified {bundle.name}: {len(document["mods"])} disabled library entries')
