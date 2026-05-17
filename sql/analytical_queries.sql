-- 1. Количество записей по каждой валюте
SELECT
    quote_currency,
    COUNT(*) AS rows_count
FROM exchange_rates
GROUP BY quote_currency
ORDER BY rows_count DESC;


-- 2. Средний, минимальный и максимальный курс за период
SELECT
    quote_currency,
    ROUND(AVG(rate), 4) AS avg_rate,
    MIN(rate) AS min_rate,
    MAX(rate) AS max_rate
FROM exchange_rates
GROUP BY quote_currency
ORDER BY quote_currency;


-- 3. Динамика курса: разница с предыдущим днем
WITH rates_with_lag AS (
    SELECT
        rate_date,
        base_currency,
        quote_currency,
        rate,
        LAG(rate) OVER (
            PARTITION BY base_currency, quote_currency
            ORDER BY rate_date
        ) AS previous_rate
    FROM exchange_rates
)
SELECT
    rate_date,
    base_currency,
    quote_currency,
    rate,
    previous_rate,
    ROUND(rate - previous_rate, 6) AS rate_change
FROM rates_with_lag
ORDER BY quote_currency, rate_date;


-- 4. Процентное изменение курса относительно предыдущего дня
WITH rates_with_lag AS (
    SELECT
        rate_date,
        base_currency,
        quote_currency,
        rate,
        LAG(rate) OVER (
            PARTITION BY base_currency, quote_currency
            ORDER BY rate_date
        ) AS previous_rate
    FROM exchange_rates
)
SELECT
    rate_date,
    base_currency,
    quote_currency,
    rate,
    previous_rate,
    ROUND(
        ((rate - previous_rate) / previous_rate) * 100,
        4
    ) AS rate_change_pct
FROM rates_with_lag
WHERE previous_rate IS NOT NULL
ORDER BY quote_currency, rate_date;


-- 5. Самые сильные дневные изменения курса
WITH rates_with_lag AS (
    SELECT
        rate_date,
        base_currency,
        quote_currency,
        rate,
        LAG(rate) OVER (
            PARTITION BY base_currency, quote_currency
            ORDER BY rate_date
        ) AS previous_rate
    FROM exchange_rates
),
daily_changes AS (
    SELECT
        rate_date,
        base_currency,
        quote_currency,
        rate,
        previous_rate,
        ROUND(
            ((rate - previous_rate) / previous_rate) * 100,
            4
        ) AS rate_change_pct
    FROM rates_with_lag
    WHERE previous_rate IS NOT NULL
)
SELECT
    *
FROM daily_changes
ORDER BY ABS(rate_change_pct) DESC
LIMIT 10;