# Совместимость / Compatibility

Пути внутри VPK проверены перед выпуском. Между основными группами ниже пересечений нет; это проверка файлов, а не обещание совместимости с любым модом или будущим обновлением игры.

| Группа / Group | Что заменяет / Replaces | С чем конфликтует / Conflicts with |
| --- | --- | --- |
| Лавка / Shop | Модель лавки; необязательные звуки / Shop model; optional audio | Другие лавки; основные варианты между собой / Other shops; other main shop variants |
| Меню / Menu | Panorama/HUD магазина / Item shop interface | Другие темы этого экрана / Other item shop UI themes |
| Банкомат / ATM | Sinner’s Sacrifice и его звуки / Model and sounds | Другие замены автомата / Other replacements of that machine |
| Указатели / Signs | `phone_booth_01a` и собственные материалы / Carrier and own materials | Другие моды той же будки / Other replacements of that booth |
| Такси / Taxi | `endgame_amber_newtruck02` и собственные материалы / Carrier and own materials | Haval, Hyundai, другие версии такси или грузовика / Other taxi variants or truck replacements |

Варианты лавки `01–04` содержат одну и ту же модель и взаимно исключают друг друга. `Extra_Music_Only`, `Extra_Purchase_Only` и `Extra_Ability_Only` можно комбинировать между собой. Они пересекаются с теми основными вариантами, где уже есть соответствующий звук. Проще всего комбинировать их с `01_Original_Sounds`.

Main shop variants `01–04` include the same model; enable only one. The three Extra sound files can be combined with each other, or with `01_Original_Sounds`. Do not duplicate a sound already included in your chosen main variant.

Старые тесты с полной картой, подогнанный Hyundai, Haval и тест скрытия такси **не входят в релиз**. Перед установкой рабочих указателей или классического такси отключите их. Карта целиком не подменяется.

Old full-map tests, the fitted Hyundai, Haval and native taxi hiding diagnostics are **not release assets**. Disable them before using the released signs or classic taxi. No full map is replaced.

Подробный список ожидаемых пересечений между звуковыми вариантами: [resource_conflicts.json](resource_conflicts.json).
