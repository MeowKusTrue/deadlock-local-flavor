# Названия и обложки в менеджере / Names and covers

## Готовые карточки

1. Скачайте `Deadlock_Local_Flavor_DMM_Import_v1.0.0.zip` из [Releases](https://github.com/MeowKusTrue/deadlock-local-flavor/releases/latest).
2. Распакуйте архив целиком. Оставьте `mod-interchange.json` рядом с папками `files` и `assets`.
3. Закройте Deadlock. В библиотеке DMM откройте меню **Add mods → Open export file…** и выберите этот JSON. В локализованной версии ищите импорт из других мод-менеджеров и открытие файла экспорта.
4. Проверьте список. Можно импортировать всю библиотеку или выбрать нужные строки.
5. После импорта включите нужные моды. Все записи в пакете изначально выключены: основные варианты лавки нельзя включать одновременно.

Названия, автор, описания и ссылки на обложки заданы в JSON. Обложки лежат и в архиве для просмотра, но DMM получает их по HTTPS из этого репозитория. Для первого отображения картинок нужен интернет. Файлы модов уже внутри пакета; GameBanana для их скачивания не нужен.

## Обычный ZIP

Для одного мода проще использовать **Add Local Mod** и обычный ZIP из релиза. Менеджер предложит заполнить название и категорию. Простое добавление `preview.png` внутрь такого ZIP само по себе не создаёт готовую карточку.

Пакет с `mod-interchange.json` не нужно отправлять в Add Local Mod как единый мод: распакуйте его и откройте JSON через импорт экспорта.

## English

Download and fully extract `Deadlock_Local_Flavor_DMM_Import_v1.0.0.zip`. Keep `mod-interchange.json`, `files` and `assets` together. Close Deadlock and open the JSON through **Mods Library → Add mods → Open export file…**. Review and import the entries you want. They start disabled; enable only your chosen main shop variant.

Names, author, descriptions and HTTPS cover URLs are included. Images are also bundled for viewing, but DMM loads its card covers online from this repository. Mod binaries are bundled locally and do not require GameBanana. For a single mod, importing its normal ZIP with Add Local Mod remains available. Do not import the entire interchange ZIP as a single local mod.

## Что проверено / What was checked

Формат сверён с исходным кодом DMM и его спецификацией. Проверены хеши VPK, относительные пути, схема полей и выключенное состояние всех записей. Импорт в живую библиотеку пользователя не выполнялся. Названия пунктов меню могут различаться между версиями менеджера.

Checked against DMM’s source and format specification: VPK hashes, relative paths, field structure and disabled defaults. The bundle was not imported into the user’s live library. Menu labels can differ by manager version.

- [Официальная инструкция библиотеки / Official library guide](https://docs.deadlockmods.app/using-mod-manager/library)
- [Спецификация Mod Interchange v1 / Format specification](https://github.com/deadlock-mod-manager/deadlock-mod-manager/blob/01f901cb4103fd1fca5ca62c6579460c8c3c4306/rfcs/001-mod-interchange/proposal.md)
- [Импорт названия и HTTP-обложки / Metadata and cover import](https://github.com/deadlock-mod-manager/deadlock-mod-manager/blob/01f901cb4103fd1fca5ca62c6579460c8c3c4306/apps/desktop/src/lib/mod-interchange.ts#L260)
