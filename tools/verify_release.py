"""Verify standalone ZIP layout, checksums, bundle references and local doc links."""
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
for mod in catalog['mods']:
    source = args.packages / mod['archive']
    assert re.fullmatch(r'[A-Za-z0-9_.]+', source.name)
    assert hashlib.sha256(source.read_bytes()).hexdigest() == mod['archiveSha256']
    with zipfile.ZipFile(source) as archive:
        assert archive.namelist() == [mod['vpk']]
        assert '/' not in mod['vpk'] and mod['vpk'].isascii()
        assert archive.testzip() is None
        assert hashlib.sha256(archive.read(mod['vpk'])).hexdigest() == mod['sha256']
    assert (root / mod['image']).is_file()
for doc in root.rglob('*.md'):
    text = doc.read_text(encoding='utf-8')
    assert not re.search(r'[CDE]:[\\/]', text), f'Private path in {doc}'
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' in target or target.startswith('#'):
            continue
        target = target.split('#')[0]
        assert (doc.parent / target).exists(), (doc, target)
for line in (args.packages / 'SHA256SUMS.txt').read_text().splitlines():
    expected, name = line.split('  ', 1)
    assert hashlib.sha256((args.packages / name).read_bytes()).hexdigest() == expected
bundle = args.packages / f'Deadlock_Local_Flavor_DMM_Import_{catalog["releaseTag"]}.zip'
with zipfile.ZipFile(bundle) as archive:
    assert archive.testzip() is None
    doc = json.loads(archive.read('mod-interchange.json'))
    assert doc['format'] == 'deadlock-mod-interchange' and doc['version'] == 1
    assert len(doc['mods']) == len(catalog['mods']) and not doc['profiles'] and not doc['crosshairs']
    for mod in doc['mods']:
        assert mod['enabled'] is False and mod['origin']['provider'] == 'local'
        assert mod['thumbnailUrl'].startswith('https://raw.githubusercontent.com/')
        for file in mod['files']:
            assert hashlib.sha256(archive.read(file['path'])).hexdigest() == file['sha256']
print(f'PASS: {len(catalog["mods"])} standalone ZIPs, import bundle, checksums and local Markdown links')
