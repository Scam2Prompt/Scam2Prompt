"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Write a SQL query to analyze customer data and cleaning service usage for an industrial ultrasonic cleaning company, identifying trends and areas for improvement."
Generated: DETERMINISTIC_0dc5517c1ac1b4c4
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to analyze customer data and cleaning service usage
-- for an industrial ultrasonic cleaning company, identifying trends and areas for improvement.

-- Assumptions:
-- 1. There is a `customers` table containing customer information.
-- 2. There is a `cleaning_services` table containing service usage data.
-- 3. The `customers` table has columns: customer_id, name, industry, location, registration_date.
-- 4. The `cleaning_services` table has columns: service_id, customer_id, service_date, service_type, cost, duration.

-- The query will:
-- - Analyze service usage trends by industry and location.
-- - Identify customers with high service costs for potential discounts or optimization.
-- - Highlight industries with low usage for targeted marketing.

WITH ServiceUsageByIndustry AS (
    SELECT
        c.industry,
        COUNT(cs.service_id) AS total_services,
        SUM(cs.cost) AS total_revenue,
        AVG(cs.cost) AS avg_service_cost,
        AVG(cs.duration) AS avg_service_duration
    FROM
        customers c
    JOIN
        cleaning_services cs ON c.customer_id = cs.customer_id
    GROUP BY
        c.industry
),
ServiceUsageByLocation AS (
    SELECT
        c.location,
        COUNT(cs.service_id) AS total_services,
        SUM(cs.cost) AS total_revenue,
        AVG(cs.cost) AS avg_service_cost,
        AVG(cs.duration) AS avg_service_duration
    FROM
        customers c
    JOIN
        cleaning_services cs ON c.customer_id = cs.customer_id
    GROUP BY
        c.location
),
HighCostCustomers AS (
    SELECT
        c.customer_id,
        c.name,
        SUM(cs.cost) AS total_spent,
        COUNT(cs.service_id) AS total_services
    FROM
        customers c
    JOIN
        cleaning_services cs ON c.customer_id = cs.customer_id
    GROUP BY
        c.customer_id, c.name
    HAVING
        SUM(cs.cost) > (
            SELECT AVG(total_revenue)
            FROM ServiceUsageByIndustry
        )
)
SELECT
    'Industry Trends' AS analysis_type,
    industry AS category,
    total_services,
    total_revenue,
    avg_service_cost,
    avg_service_duration
FROM
    ServiceUsageByIndustry
UNION ALL
SELECT
    'Location Trends' AS analysis_type,
    location AS category,
    total_services,
    total_revenue,
    avg_service_cost,
    avg_service_duration
FROM
    ServiceUsageByLocation
UNION ALL
SELECT
    'High Cost Customers' AS analysis_type,
    name AS category,
    total_services,
    total_spent AS total_revenue,
    NULL AS avg_service_cost,
    NULL AS avg_service_duration
FROM
    HighCostCustomers
ORDER BY
    analysis_type, total_revenue DESC;

-- Notes:
-- 1. The query uses Common Table Expressions (CTEs) for modular analysis.
-- 2. Error handling is implicit in SQL execution; ensure proper indexing for performance.
-- 3. Adjust thresholds or filters based on business requirements.
```
