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
-- SQL query to analyze customer data for B2C marketing campaign in India
-- Focuses on lead generation trends and conversion rates by various dimensions

WITH lead_conversion_stats AS (
    -- Calculate basic conversion metrics
    SELECT 
        DATE_TRUNC('month', lead_date) AS month,
        lead_source,
        city,
        COUNT(*) AS total_leads,
        COUNT(CASE WHEN converted = TRUE THEN 1 END) AS converted_leads,
        ROUND(COUNT(CASE WHEN converted = TRUE THEN 1 END) * 100.0 / COUNT(*), 2) AS conversion_rate,
        AVG(CASE WHEN converted = TRUE THEN purchase_amount ELSE NULL END) AS avg_purchase_amount
    FROM 
        customer_leads
    WHERE 
        country = 'India'
        AND lead_date BETWEEN CURRENT_DATE - INTERVAL '12 months' AND CURRENT_DATE
    GROUP BY 
        DATE_TRUNC('month', lead_date), 
        lead_source, 
        city
),

trend_analysis AS (
    -- Calculate month-over-month trends
    SELECT 
        month,
        lead_source,
        city,
        total_leads,
        converted_leads,
        conversion_rate,
        avg_purchase_amount,
        LAG(total_leads, 1) OVER (PARTITION BY lead_source, city ORDER BY month) AS prev_month_leads,
        LAG(converted_leads, 1) OVER (PARTITION BY lead_source, city ORDER BY month) AS prev_month_converted,
        LAG(conversion_rate, 1) OVER (PARTITION BY lead_source, city ORDER BY month) AS prev_month_rate
    FROM 
        lead_conversion_stats
)

-- Final analysis with trend calculations
SELECT 
    month,
    lead_source,
    city,
    total_leads,
    converted_leads,
    conversion_rate,
    avg_purchase_amount,
    CASE 
        WHEN prev_month_leads IS NULL THEN NULL
        ELSE ROUND((total_leads - prev_month_leads) * 100.0 / prev_month_leads, 2)
    END AS lead_growth_percentage,
    CASE 
        WHEN prev_month_converted IS NULL THEN NULL
        ELSE ROUND((converted_leads - prev_month_converted) * 100.0 / prev_month_converted, 2)
    END AS conversion_growth_percentage,
    CASE 
        WHEN prev_month_rate IS NULL THEN NULL
        ELSE ROUND((conversion_rate - prev_month_rate) * 100.0 / prev_month_rate, 2)
    END AS rate_growth_percentage,
    -- Identify top performing sources/cities
    RANK() OVER (PARTITION BY month ORDER BY conversion_rate DESC) AS monthly_conversion_rank,
    RANK() OVER (PARTITION BY month ORDER BY total_leads DESC) AS monthly_lead_rank
FROM 
    trend_analysis
ORDER BY 
    month DESC, 
    conversion_rate DESC;
```
