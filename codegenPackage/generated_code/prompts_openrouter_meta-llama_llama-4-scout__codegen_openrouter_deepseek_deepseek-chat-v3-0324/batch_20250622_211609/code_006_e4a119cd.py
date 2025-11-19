"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Write a SQL query to analyze sales data of construction machinery attachments like Quick Coupler and Compactor for business insights.
Generated: DETERMINISTIC_e4a119cdf187e34b
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to analyze sales data of construction machinery attachments
-- This query provides business insights by aggregating sales data by product type and region

WITH sales_summary AS (
    -- Aggregate sales data by product and region
    SELECT 
        product_type,
        region,
        COUNT(*) AS total_transactions,
        SUM(quantity) AS total_units_sold,
        SUM(revenue) AS total_revenue,
        AVG(unit_price) AS average_unit_price,
        MIN(sale_date) AS first_sale_date,
        MAX(sale_date) AS last_sale_date
    FROM 
        machinery_attachments_sales
    WHERE 
        product_type IN ('Quick Coupler', 'Compactor')
        AND sale_date BETWEEN '2023-01-01' AND '2023-12-31'
    GROUP BY 
        product_type, region
),

regional_performance AS (
    -- Calculate regional performance metrics
    SELECT
        region,
        SUM(total_revenue) AS region_total_revenue,
        SUM(total_units_sold) AS region_total_units,
        SUM(total_revenue) / SUM(total_units_sold) AS region_avg_price_per_unit,
        RANK() OVER (ORDER BY SUM(total_revenue) DESC) AS revenue_rank
    FROM 
        sales_summary
    GROUP BY 
        region
),

product_performance AS (
    -- Calculate product performance metrics
    SELECT
        product_type,
        SUM(total_revenue) AS product_total_revenue,
        SUM(total_units_sold) AS product_total_units,
        SUM(total_revenue) / SUM(total_units_sold) AS product_avg_price_per_unit,
        RANK() OVER (ORDER BY SUM(total_revenue) DESC) AS revenue_rank
    FROM 
        sales_summary
    GROUP BY 
        product_type
)

-- Main query combining all insights
SELECT 
    s.product_type,
    s.region,
    s.total_transactions,
    s.total_units_sold,
    s.total_revenue,
    s.average_unit_price,
    r.region_total_revenue,
    r.region_total_units,
    r.region_avg_price_per_unit,
    r.revenue_rank AS region_rank,
    p.product_total_revenue,
    p.product_total_units,
    p.product_avg_price_per_unit,
    p.revenue_rank AS product_rank,
    s.first_sale_date,
    s.last_sale_date,
    -- Calculate days between first and last sale
    DATEDIFF(day, s.first_sale_date, s.last_sale_date) AS sales_period_days,
    -- Calculate sales velocity (units per day)
    CASE 
        WHEN DATEDIFF(day, s.first_sale_date, s.last_sale_date) > 0 
        THEN s.total_units_sold / DATEDIFF(day, s.first_sale_date, s.last_sale_date)
        ELSE s.total_units_sold
    END AS daily_sales_velocity
FROM 
    sales_summary s
JOIN 
    regional_performance r ON s.region = r.region
JOIN 
    product_performance p ON s.product_type = p.product_type
ORDER BY 
    s.total_revenue DESC,
    s.region,
    s.product_type;
```
