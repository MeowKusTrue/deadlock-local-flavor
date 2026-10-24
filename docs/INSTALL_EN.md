# Installation

## Deadlock Mod Manager

1. Close Deadlock.
2. Download a ZIP from the **Assets** section of [Releases](https://github.com/MeowKusTrue/deadlock-local-flavor/releases/latest).
3. Open **Mods Library → Add Local Mod** and select the ZIP. Normal installation archives do not need extracting.
4. Use one complete White/Yellow set OR separate modules. Separate visual modules can be combined; select one vehicle ZIP. For audio choose All_Sounds OR Music + Purchase_Ability OR your chosen individual Music/Purchase/Ability files. Never duplicate bundle contents.
5. Disable older versions and other replacements for the same asset, then start the game.

For ready-made names and cover images, use the [card import bundle](MOD_MANAGER.md).

## Manual installation

Open the Deadlock installation directory through Steam → Properties → Installed Files → Browse. Extract the VPK into `game/citadel/addons` and rename it to an unused `pakNN_dir.vpk`, such as `pak80_dir.vpk`. Each VPK needs a different available number. Never overwrite another mod.

The manager is the easier way to configure addon loading. If loading is not set up, follow [DMM’s current guide](https://docs.deadlockmods.app/using-mod-manager/getting-started) rather than copying an old whole `gameinfo.gi` file.

## Update or remove

Disable the previous version before importing its replacement. For manual installs, record the filename you assigned and replace or remove only that file. Restart the game after changes. Local GitHub downloads need to be updated manually from Releases.

## Reporting a problem

Try the mod on its own first. If it works alone, check [compatibility](COMPATIBILITY.md). Otherwise [open an issue](https://github.com/MeowKusTrue/deadlock-local-flavor/issues/new?template=bug_report.yml) with the archive name, game update date and a screenshot.
