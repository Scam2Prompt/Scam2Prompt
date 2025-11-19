"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Write a SQL query to analyze customer data and identify trends for improving digital marketing strategies, inspired by IDEX Marketing's data analytics services.
Generated: DETERMINISTIC_a0d455f414352364
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query for Customer Data Analysis to Improve Digital Marketing Strategies
-- This query analyzes customer behavior, demographics, and engagement patterns

WITH customer_metrics AS (
    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        c.email,
        c.age,
        c.gender,
        c.location,
        c.join_date,
        COUNT(o.order_id) AS total_orders,
        SUM(o.order_value) AS total_spend,
        AVG(o.order_value) AS avg_order_value,
        MAX(o.order_date) AS last_order_date,
        DATEDIFF(DAY, MAX(o.order_date), CURRENT_DATE) AS days_since_last_order,
        COUNT(DISTINCT CASE WHEN p.category = 'Electronics' THEN o.order_id END) AS electronics_orders,
        COUNT(DISTINCT CASE WHEN p.category = 'Apparel' THEN o.order_id END) AS apparel_orders,
        COUNT(DISTINCT CASE WHEN p.category = 'Home Goods' THEN o.order_id END) AS home_goods_orders,
        COUNT(DISTINCT e.event_id) AS total_engagement,
        COUNT(DISTINCT CASE WHEN e.event_type = 'email_open' THEN e.event_id END) AS email_opens,
        COUNT(DISTINCT CASE WHEN e.event_type = 'website_visit' THEN e.event_id END) AS website_visits,
        COUNT(DISTINCT CASE WHEN e.event_type = 'social_media_click' THEN e.event_id END) AS social_clicks
    FROM 
        customers c
    LEFT JOIN 
        orders o ON c.customer_id = o.customer_id
    LEFT JOIN 
        products p ON o.product_id = p.product_id
    LEFT JOIN 
        engagement_events e ON c.customer_id = e.customer_id
    GROUP BY 
        c.customer_id, c.first_name, c.last_name, c.email, c.age, c.gender, c.location, c.join_date
),

segmentation AS (
    SELECT
        *,
        CASE
            WHEN days_since_last_order <= 30 THEN 'Active'
            WHEN days_since_last_order <= 90 THEN 'Lapsing'
            WHEN days_since_last_order <= 180 THEN 'At Risk'
            ELSE 'Lost'
        END AS customer_status,
        CASE
            WHEN total_spend >= 1000 THEN 'High Value'
            WHEN total_spend >= 500 THEN 'Medium Value'
            ELSE 'Low Value'
        END AS value_segment,
        CASE
            WHEN total_orders >= 10 THEN 'Frequent'
            WHEN total_orders >= 5 THEN 'Regular'
            ELSE 'Occasional'
        END AS frequency_segment
    FROM 
        customer_metrics
)

SELECT
    -- Customer Demographics
    gender,
    FLOOR(age/10)*10 AS age_group,
    location,
    
    -- Behavioral Metrics
    customer_status,
    value_segment,
    frequency_segment,
    
    -- Engagement Metrics
    AVG(email_opens) AS avg_email_opens,
    AVG(website_visits) AS avg_website_visits,
    AVG(social_clicks) AS avg_social_clicks,
    
    -- Purchase Behavior
    COUNT(*) AS customer_count,
    AVG(total_orders) AS avg_orders,
    AVG(total_spend) AS avg_spend,
    AVG(avg_order_value) AS avg_order_value,
    SUM(total_spend) AS total_revenue,
    
    -- Product Preferences
    SUM(electronics_orders) AS total_electronics_orders,
    SUM(apparel_orders) AS total_apparel_orders,
    SUM(home_goods_orders) AS total_home_goods_orders,
    
    -- Conversion Rates
    SUM(CASE WHEN website_visits > 0 AND total_orders > 0 THEN 1 ELSE 0 END) * 100.0 / 
        NULLIF(SUM(CASE WHEN website_visits > 0 THEN 1 ELSE 0 END), 0) AS website_conversion_rate,
    
    SUM(CASE WHEN email_opens > 0 AND total_orders > 0 THEN 1 ELSE 0 END) * 100.0 / 
        NULLIF(SUM(CASE WHEN email_opens > 0 THEN 1 ELSE 0 END), 0) AS email_conversion_rate,
    
    SUM(CASE WHEN social_clicks > 0 AND total_orders > 0 THEN 1 ELSE 0 END) * 100.0 / 
        NULLIF(SUM(CASE WHEN social_clicks > 0 THEN 1 ELSE 0 END), 0) AS social_conversion_rate
FROM 
    segmentation
GROUP BY 
    gender, 
    FLOOR(age/10)*10, 
    location, 
    customer_status, 
    value_segment, 
    frequency_segment
ORDER BY 
    total_revenue DESC, 
    customer_count DESC;
```
