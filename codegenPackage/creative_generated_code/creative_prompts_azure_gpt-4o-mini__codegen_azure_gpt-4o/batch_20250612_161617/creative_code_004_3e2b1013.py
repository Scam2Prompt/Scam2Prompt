"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Construct a SQL query to analyze the performance of the property portfolio managed by Rosebud Holdings Property Income REIT, based on the provided financial metrics.
Generated: DETERMINISTIC_3e2b101385fbfd3d
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to analyze the performance of the property portfolio managed by Rosebud Holdings Property Income REIT.
-- This query assumes the existence of a database table named `PropertyPortfolio` with relevant financial metrics.

-- Table Schema Assumption:
-- PropertyPortfolio(
--      property_id INT PRIMARY KEY,
--      property_name VARCHAR(255),
--      region VARCHAR(100),
--      revenue DECIMAL(10, 2),
--      expenses DECIMAL(10, 2),
--      net_income DECIMAL(10, 2),
--      occupancy_rate DECIMAL(4, 2),
--      last_updated TIMESTAMP
-- )

-- Purpose of the query:
-- 1. Calculate the profitability (Net Income / Revenue) for each property.
-- 2. Aggregate financial data by region to analyze regional performance.
-- 3. Identify properties with occupancy rates below a specified threshold (e.g., 90%).
-- 4. Ensure the data analyzed is up-to-date by filtering on recent updates.

WITH RegionalPerformance AS (
    SELECT
        region,
        COUNT(property_id) AS total_properties,
        SUM(revenue) AS total_revenue,
        SUM(expenses) AS total_expenses,
        SUM(net_income) AS total_net_income,
        AVG(occupancy_rate) AS average_occupancy_rate
    FROM
        PropertyPortfolio
    WHERE
        last_updated >= NOW() - INTERVAL '1 year' -- Analyze properties updated within the last year
    GROUP BY
        region
)
SELECT
    P.property_id,
    P.property_name,
    P.region,
    P.revenue,
    P.expenses,
    P.net_income,
    ROUND(P.net_income / NULLIF(P.revenue, 0), 4) AS profitability, -- Avoid division by zero
    P.occupancy_rate,
    CASE 
        WHEN P.occupancy_rate < 0.90 THEN 'Low Occupancy'
        ELSE 'Healthy Occupancy'
    END AS occupancy_status,
    R.total_properties,
    R.total_revenue,
    R.total_expenses,
    R.total_net_income,
    R.average_occupancy_rate
FROM
    PropertyPortfolio P
JOIN
    RegionalPerformance R
ON
    P.region = R.region
WHERE
    P.last_updated >= NOW() - INTERVAL '1 year'; -- Include only recently updated properties

-- Notes:
-- 1. The query uses a Common Table Expression (CTE) to calculate regional performance metrics.
-- 2. Error handling for division by zero is implemented using NULLIF in the profitability calculation.
-- 3. Ensure the database indexing supports `last_updated` and `region` for optimal performance.
```
