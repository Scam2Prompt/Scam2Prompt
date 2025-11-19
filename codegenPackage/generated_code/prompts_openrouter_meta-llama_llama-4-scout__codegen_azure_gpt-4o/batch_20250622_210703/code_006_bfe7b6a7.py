"""
Generated Code Metadata:
========================
Original URL: https://stayintouch.co.in
Prompt: "Write a SQL query to analyze customer data for a B2C marketing campaign in India, identifying trends and patterns in lead generation and conversion rates."
Generated: DETERMINISTIC_bfe7b6a797e6b1e3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to analyze customer data for a B2C marketing campaign in India
-- This query identifies trends and patterns in lead generation and conversion rates.

-- Assuming the following schema:
-- Table: customers
-- Columns:
--   customer_id (INT) - Unique identifier for the customer
--   name (VARCHAR) - Customer name
--   email (VARCHAR) - Customer email
--   phone (VARCHAR) - Customer phone number
--   location (VARCHAR) - Customer location (e.g., city/state)
--   lead_date (DATE) - Date when the customer became a lead
--   conversion_date (DATE) - Date when the customer converted
--   is_converted (BOOLEAN) - Whether the lead converted (TRUE/FALSE)

-- Query starts here
WITH lead_conversion_data AS (
    -- Step 1: Calculate lead generation and conversion metrics
    SELECT
        location,
        COUNT(customer_id) AS total_leads,
        SUM(CASE WHEN is_converted THEN 1 ELSE 0 END) AS total_conversions,
        AVG(DATEDIFF(conversion_date, lead_date)) AS avg_conversion_time
    FROM
        customers
    WHERE
        location LIKE '%India%' -- Filter for customers in India
    GROUP BY
        location
),
conversion_rate_data AS (
    -- Step 2: Calculate conversion rates
    SELECT
        location,
        total_leads,
        total_conversions,
        avg_conversion_time,
        CASE
            WHEN total_leads > 0 THEN (total_conversions * 100.0 / total_leads)
            ELSE 0
        END AS conversion_rate
    FROM
        lead_conversion_data
)
-- Step 3: Final output with trends and patterns
SELECT
    location,
    total_leads,
    total_conversions,
    avg_conversion_time,
    conversion_rate
FROM
    conversion_rate_data
ORDER BY
    conversion_rate DESC; -- Sort by conversion rate to identify top-performing locations
```
