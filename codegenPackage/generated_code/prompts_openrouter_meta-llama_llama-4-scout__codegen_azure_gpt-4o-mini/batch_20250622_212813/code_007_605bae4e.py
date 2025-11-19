"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Write a SQL query to analyze customer visit patterns and service preferences for a car repair shop like Pneus ML, helping to identify trends and popular services.
Generated: DETERMINISTIC_605bae4eb5bee321
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to analyze customer visit patterns and service preferences for a car repair shop

WITH CustomerVisits AS (
    -- Select customer visit data including visit date, service type, and customer ID
    SELECT 
        c.customer_id,
        v.visit_date,
        s.service_type
    FROM 
        customers c
    JOIN 
        visits v ON c.customer_id = v.customer_id
    JOIN 
        services s ON v.service_id = s.service_id
),

-- Aggregate visit counts and service preferences
ServiceAnalysis AS (
    SELECT 
        service_type,
        COUNT(*) AS visit_count,
        COUNT(DISTINCT customer_id) AS unique_customers
    FROM 
        CustomerVisits
    GROUP BY 
        service_type
),

-- Calculate the average number of visits per customer for each service type
AverageVisits AS (
    SELECT 
        service_type,
        visit_count,
        unique_customers,
        ROUND(visit_count::decimal / NULLIF(unique_customers, 0), 2) AS avg_visits_per_customer
    FROM 
        ServiceAnalysis
)

-- Final selection of results
SELECT 
    service_type,
    visit_count,
    unique_customers,
    avg_visits_per_customer
FROM 
    AverageVisits
ORDER BY 
    visit_count DESC;  -- Order by the most visited services
```
