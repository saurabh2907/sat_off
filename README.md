# sat_off
WITH monthly_cohorts AS (
    SELECT
        user_id,
        DATEADD(MONTH, DATEDIFF(MONTH, 0, transaction_timestamp), 0) AS cohort_month
    FROM transactions
    GROUP BY 1, 2
),
user_activity AS (
    SELECT
        cohort_month,
        COUNT(DISTINCT user_id) AS active_users
    FROM monthly_cohorts
    GROUP BY 1
),
retained_users AS (
    SELECT
        m1.cohort_month,
        COUNT(DISTINCT m2.user_id) AS retained_users
    FROM monthly_cohorts m1
    JOIN monthly_cohorts m2
        ON m1.user_id = m2.user_id
        AND m2.cohort_month = DATEADD(MONTH, 1, m1.cohort_month)
    GROUP BY 1
)
SELECT
    cohort_month,
    active_users,
    retained_users,
    ROUND(100.0 * retained_users / active_users, 2) AS retention_rate
FROM user_activity
JOIN retained_users USING (cohort_month)
ORDER BY cohort_month;
