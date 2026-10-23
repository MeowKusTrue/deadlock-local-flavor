<div align="center">

# Deadlock Local Flavor

**Familiar food, signs and taxis in the streets of Deadlock.**

[Downloads](https://github.com/MeowKusTrue/deadlock-local-flavor/releases/latest) · [Installation](docs/INSTALL_EN.md) · [Mod manager](docs/MOD_MANAGER.md) · [Русский](README.md)

</div>

My cosmetic mods for Deadlock: a Vkusno i Tochka fast-food shop, a matching item-shop menu, a Zber ATM and Yandex Go taxis. Install whichever ones you want; you do not need the whole collection.

## 🍔 The mods

| Mod | Version | Changes |
| --- | --- | --- |
| [Vkusno i Tochka shop](mods/shop/README.md) | 1.2 | Shop model, with optional audio replacements |
| [Vkusno shop menu](mods/menu/README.md) | 1.0 | Dark green item shop, orange price badges and light item names |
| [Zber Soul ATM](mods/atm/README.md) | 1.0 | Sinner’s Sacrifice model, animated screen and audio |
| [Entrance signs](mods/signs/README.md) | 1.0 | Small menu boards and large signs at the shop descents |
| [Yandex Go classic taxi](mods/taxi/README.md) | 1.0 | Livery for the original in-game cab |

Item stats, prices and rewards stay unchanged. No full map replacement is included.

![Shop cover — AI-assisted promotional artwork](assets/shop.jpg)

The shop, menu and ATM covers are AI-assisted promotional artwork, not game screenshots. Some menu and sign illustrations also use AI. Taxi previews are ordinary Blender renders. See [credits](docs/CREDITS.md).

## 📦 Installation

Download the mod ZIP you want from **Assets** on the [Releases page](https://github.com/MeowKusTrue/deadlock-local-flavor/releases/latest). **Code → Download ZIP** only downloads the repository pages and tools.

1. Close Deadlock.
2. Open **Mods Library → Add Local Mod** in Deadlock Mod Manager and select the ZIP.
3. Check the name, add the mod and enable it.
4. Disable older versions of the same mod, then start the game.

Each normal ZIP contains one VPK at its root, with no previews or source assets.

For ready-made library cards with names and covers, download `Deadlock_Local_Flavor_DMM_Import_v1.0.0.zip`, extract it and open `mod-interchange.json` through **Add mods → Open export file…**. This is a separate interchange bundle, not an Add Local Mod ZIP. Entries start disabled; choose what to enable. Covers load online. [Details](docs/MOD_MANAGER.md).

## 🔊 Shop audio choices

Choose one main shop archive:

| Filename ending | Contents |
| --- | --- |
| `01_Original_Sounds` | Shop model, no audio replacements |
| `02_Shop_Sounds` | Shop model, purchase beeps and nine-second ambience loop |
| `03_Ability_Sound` | Shop model and ability upgrade jingle |
| `04_All_Sounds` | Shop model with all three audio replacements |

For a custom mix, use `01_Original_Sounds` plus the `Extra_*_Only` files you want. Extras contain audio only and also work without the shop model. The HUD menu does not replace sounds.

## 🧩 Compatibility and limits

The shop, menu, ATM, entrance signs and classic taxi have no overlapping internal resource paths. Other mods replacing the same model, menu or sound may conflict. See the [compatibility guide](docs/COMPATIBILITY.md).

The ATM has no 115-FZ destruction screen yet. Haval is not in this release: its overlay still leaves parts of the original cab visible. Sign placement may need updating after map changes. Do not enable multiple main shop variants or duplicate an included sound with its Extra file.

To update, disable the previous version and import the new ZIP from Releases. These local GitHub downloads do not receive GameBanana catalog updates automatically. To uninstall, disable the mod. [Manual installation](docs/INSTALL_EN.md).

## 🎨 Credits

Collection by **MeowKusTrue**. Shop and ATM models are handmade. The classic taxi uses Valve’s original car model. Geometry, placement, materials and packaging were prepared manually and with scripts; some artwork uses AI.

Game assets belong to Valve. Brand names, logos, music and sounds belong to their owners. This collection is not affiliated with Valve, Vkusno i Tochka, Yandex or Sber. No blanket license is granted over third-party assets. [Credits and provenance](docs/CREDITS.md).

## 🛠️ Maintaining the collection

Mod binaries live in Releases; this repository holds the catalog, images, documentation and packaging checks. See [releasing](docs/RELEASING.md).

<div align="center">

[Back to top](#deadlock-local-flavor)

</div>
