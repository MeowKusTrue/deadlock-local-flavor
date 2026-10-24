# Как выпустить обновление / Releasing an update

Версия коллекции и версии отдельных модов независимы. Первый релиз коллекции — `v1.1.0`; лавка в нём остаётся `1.2`, меню и банкомат — `1.0`.

## Через GitHub

1. Подготовьте новый ZIP для изменённого мода: один VPK в корне, без папки, исходников и картинок. Имена ZIP и VPK — латиница, цифры, `_` и точки.
2. Обновите его описание, версию и ссылку в `mods/<мод>/README.md`. Если внешний вид изменился, обновите картинку в `assets`.
3. В `catalog.json` обновите сведения о ZIP, SHA-256 VPK и архива, размер VPK, список путей ресурсов и `releaseTag`. Ссылки на скачивание в страницах модов должны указывать на новый тег релиза.
4. Соберите новый пакет карточек и проверьте все архивы командами ниже. Для удобства положите в рабочую папку весь набор ZIP, который хотите видеть в новом релизе, включая неизменившиеся моды.
5. Сохраните изменения репозитория. Откройте **Releases → Draft a new release**, создайте тег, например `v1.0.1`, на нужном коммите. Так ссылки на картинки этого тега будут работать.
6. Загрузите отдельные ZIP, пакет `DMM_Import` и `SHA256SUMS.txt` в **Assets**. Кратко напишите, что изменилось и какой файл заменить. Опубликуйте релиз.
7. Откройте его без входа в GitHub и проверьте хотя бы одну ссылку на ZIP и обложку.

Не загружайте моды через **Add file** в корень репозитория. Большие бинарные файлы хранятся в Releases. Кнопка Code → Download ZIP готовые моды не содержит.

## Инструменты

Нужен Python 3; сторонних библиотек этим двум скриптам не требуется. Команды запускаются из корня клонированного репозитория. `release_stage` — ваша папка с отдельными ZIP.

```powershell
python tools/build_dmm_bundle.py --packages release_stage
python tools/verify_release.py --packages release_stage
```

Первый скрипт сверяет исходные архивы с каталогом, собирает пакет карточек и пересчитывает `SHA256SUMS.txt`. Второй проверяет обычные ZIP, хеши, ссылки на файлы внутри пакета и локальные ссылки в Markdown. Скрипты не запускают игру и не устанавливают моды.

Если меняется содержимое VPK, отдельно проверьте его внутренние пути на пересечения с остальными модами. В `docs/resource_conflicts.json` записаны пересечения первого релиза: это не автоматически обновляемый отчёт.

## English

Collection versions and individual mod versions are separate. For an update, prepare one root-level VPK per normal ZIP, update the catalog and mod pages, and set the new collection `releaseTag`. Keep the desired unchanged archives in your staging folder as well.

Run the two Python commands above, commit the documentation and catalog, then create a GitHub release tag on that commit. Upload the individual ZIPs, the generated DMM interchange bundle and `SHA256SUMS.txt` as release assets. Write which mod changed and which old file it replaces. Verify public download and cover links after publishing.

Binary archives belong in Releases, not the git history. The tools validate packaging and hashes; they do not compile VPKs, launch Deadlock, test gameplay or install anything.
