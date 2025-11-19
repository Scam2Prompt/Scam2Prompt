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
-- SQL query to analyze customer data and cleaning service usage
-- for an industrial ultrasonic cleaning company

WITH customer_usage_stats AS (
    -- Calculate basic usage statistics per customer
    SELECT 
        c.customer_id,
        c.customer_name,
        c.industry_type,
        c.join_date,
        COUNT(s.service_id) AS total_services,
        SUM(s.service_duration_minutes) AS total_duration_minutes,
        SUM(s.cleaning_units_used) AS total_units_used,
        SUM(s.cost) AS total_spend,
        AVG(s.service_rating) AS avg_service_rating,
        MAX(s.service_date) AS last_service_date
    FROM 
        customers c
    LEFT JOIN 
        services s ON c.customer_id = s.customer_id
    GROUP BY 
        c.customer_id, c.customer_name, c.industry_type, c.join_date
),

industry_benchmarks AS (
    -- Calculate industry benchmarks for comparison
    SELECT 
        industry_type,
        AVG(total_services) AS avg_services,
        AVG(total_duration_minutes) AS avg_duration,
        AVG(total_units_used) AS avg_units,
        AVG(total_spend) AS avg_spend,
        AVG(avg_service_rating) AS avg_rating
    FROM 
        customer_usage_stats
    GROUP BY 
        industry_type
),

service_frequency AS (
    -- Analyze service frequency patterns
    SELECT 
        customer_id,
        EXTRACT(MONTH FROM service_date) AS month,
        EXTRACT(YEAR FROM service_date) AS year,
        COUNT(*) AS monthly_services
    FROM 
        services
    GROUP BY 
        customer_id, EXTRACT(MONTH FROM service_date), EXTRACT(YEAR FROM service_date)
),

equipment_analysis AS (
    -- Analyze equipment usage patterns
    SELECT 
        e.equipment_type,
        COUNT(s.service_id) AS total_uses,
        AVG(s.service_duration_minutes) AS avg_duration,
        AVG(s.cleaning_units_used) AS avg_units_used,
        AVG(s.cost) AS avg_cost
    FROM 
        equipment e
    JOIN 
        services s ON e.equipment_id = s.equipment_id
    GROUP BY 
        e.equipment_type
)

-- Main analysis query combining all CTEs
SELECT 
    cus.customer_id,
    cus.customer_name,
    cus.industry_type,
    cus.total_services,
    cus.total_spend,
    ROUND(cus.total_spend / NULLIF(cus.total_services, 0), 2) AS avg_spend_per_service,
    cus.avg_service_rating,
    ib.avg_rating AS industry_avg_rating,
    CASE 
        WHEN cus.avg_service_rating < ib.avg_rating THEN 'Below Industry Avg'
        WHEN cus.avg_service_rating > ib.avg_rating THEN 'Above Industry Avg'
        ELSE 'At Industry Avg'
    END AS rating_comparison,
    CASE 
        WHEN cus.total_services = 0 THEN 'No Services'
        WHEN cus.total_services < ib.avg_services THEN 'Below Avg Usage'
        WHEN cus.total_services > ib.avg_services THEN 'Above Avg Usage'
        ELSE 'At Avg Usage'
    END AS usage_comparison,
    EXTRACT(YEAR FROM AGE(NOW(), cus.join_date)) AS customer_tenure_years,
    EXTRACT(DAY FROM AGE(NOW(), cus.last_service_date)) AS days_since_last_service,
    -- Equipment usage insights
    (SELECT STRING_AGG(equipment_type || ' (' || total_uses || ' uses)', ', ')
     FROM equipment_analysis ea
     JOIN services s ON ea.equipment_type = (SELECT equipment_type FROM equipment WHERE equipment_id = s.equipment_id)
     WHERE s.customer_id = cus.customer_id) AS equipment_usage_summary
FROM 
    customer_usage_stats cus
JOIN 
    industry_benchmarks ib ON cus.industry_type = ib.industry_type
ORDER BY 
    cus.total_spend DESC, 
    cus.avg_service_rating DESC;
```
