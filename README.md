# Exchange Rates ETL

Учебный ETL-проект: загрузка данных из публичного API валютных курсов в PostgreSQL.

## Цель проекта

Показать базовый end-to-end ETL-пайплайн:

- получение JSON-данных из внешнего API;
- обработка и очистка данных через Python/Pandas;
- загрузка данных в PostgreSQL;
- разделение на staging/core-слой;
- аналитические SQL-запросы с CTE и оконными функциями.

## Стек

Python, Pandas, Requests, PostgreSQL, SQLAlchemy, Docker, SQL

## Архитектура

```text
Frankfurter API
      ↓
extract.py
      ↓
transform.py
      ↓
load.py
      ↓
PostgreSQL
      ↓
analytical_queries.sql
```

## Установка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск базы данных

```bash
docker compose up -d
```

PostgreSQL будет доступен на порту `5434`.

Параметры подключения:

- database: `exchange_rates_db`
- user: `etl_user`
- password: `etl_password`
- host: `localhost`
- port: `5434`

## Запуск ETL-пайплайна

```bash
python src/main.py
```

Скрипт загружает курсы валют из Frankfurter API, преобразует данные через Pandas и сохраняет результат в PostgreSQL.

## Структура проекта

```text
.
├── docker-compose.yml
├── requirements.txt
├── README.md
├── sql
│   ├── create_tables.sql
│   └── analytical_queries.sql
└── src
    ├── extract.py
    ├── transform.py
    ├── load.py
    └── main.py
```

## Слои данных

- `stg_exchange_rates` — staging-таблица для первичной загрузки данных.
- `exchange_rates` — основная таблица с уникальными курсами валют по дате, базовой валюте и котируемой валюте.

## Аналитика

Файл `sql/analytical_queries.sql` содержит примеры SQL-запросов:

- количество записей по валютам;
- средний, минимальный и максимальный курс;
- дневное изменение курса;
- процентное изменение курса;
- топ-10 самых сильных дневных изменений.
