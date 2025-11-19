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
-- This query identifies trends and patterns in lead generation and conversion rates

WITH LeadData AS (
    -- Select relevant lead data from the leads table
    SELECT 
        lead_id,
        customer_id,
        created_at AS lead_created_at,
        status AS lead_status,
        source AS lead_source
    FROM 
        leads
    WHERE 
        country = 'India' -- Filter for leads generated in India
),

ConversionData AS (
    -- Select relevant conversion data from the conversions table
    SELECT 
        lead_id,
        converted_at AS conversion_date,
        conversion_value
    FROM 
        conversions
    WHERE 
        conversion_date IS NOT NULL -- Only consider leads that have been converted
)

-- Main query to analyze lead generation and conversion rates
SELECT 
    ld.lead_source,
    COUNT(ld.lead_id) AS total_leads, -- Total number of leads generated
    COUNT(cd.lead_id) AS total_conversions, -- Total number of conversions
    COALESCE(COUNT(cd.lead_id) * 100.0 / NULLIF(COUNT(ld.lead_id), 0), 0) AS conversion_rate, -- Conversion rate calculation
    DATE_TRUNC('month', ld.lead_created_at) AS month -- Group by month
FROM 
    LeadData ld
LEFT JOIN 
    ConversionData cd ON ld.lead_id = cd.lead_id
GROUP BY 
    ld.lead_source, month
ORDER BY 
    month, total_leads DESC; -- Order results by month and total leads

-- Note: Ensure that the leads and conversions tables exist and have the appropriate columns.
-- Adjust the table and column names as necessary to match your database schema.
```
