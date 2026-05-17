# api-to-postgres-etl

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