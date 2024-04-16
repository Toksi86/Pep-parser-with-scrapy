# Scrapy PEP parser
## Асинхронный парсер PEP документов на базе фреймворка Scrapy

## Описание проекта:

Задача парсера: обработать страницы pep документов с сайта https://www.python.org/ и выписать из них:
- Номер
- Название
- Статус

Также создаётся сводка по статусам PEP — сколько найдено документов в каждом статусе 

Информация сохраняется в папке result в файлы с расширением **csv** в форматах:
- pep_дата_время.csv
- status_summary_дата_время.csv


## Инструкция по установке:

1. Загрузите проект:
```bash
git clone https://github.com/Toksi86/scrapy_parser_pep.git
```

2. Установите и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
```

3. Обновите PIP и установите необходимые зависимости
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Запустите паука pep.
```bash
scrapy crawl pep
```