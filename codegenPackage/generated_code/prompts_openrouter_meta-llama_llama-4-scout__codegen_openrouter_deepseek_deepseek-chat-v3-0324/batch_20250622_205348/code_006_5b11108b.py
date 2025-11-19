"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Create a SQL query to analyze customer feedback and ratings for آل البيت services, focusing on aspects like timeliness and furniture safety during moves.
Generated: DETERMINISTIC_5b11108b0ff5ea55
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to analyze customer feedback for آل البيت services
-- Focuses on timeliness and furniture safety metrics

SELECT 
    -- Basic customer and service info
    c.customer_id,
    c.customer_name,
    s.service_id,
    s.service_date,
    
    -- Feedback metrics
    f.overall_rating,
    f.timeliness_rating,
    f.furniture_safety_rating,
    f.feedback_comment,
    
    -- Calculated metrics
    AVG(f.timeliness_rating) OVER() AS avg_timeliness_rating,
    AVG(f.furniture_safety_rating) OVER() AS avg_furniture_safety_rating,
    
    -- Comparison to average
    CASE 
        WHEN f.timeliness_rating > AVG(f.timeliness_rating) OVER() THEN 'Above Average'
        WHEN f.timeliness_rating < AVG(f.timeliness_rating) OVER() THEN 'Below Average'
        ELSE 'Average'
    END AS timeliness_performance,
    
    CASE 
        WHEN f.furniture_safety_rating > AVG(f.furniture_safety_rating) OVER() THEN 'Above Average'
        WHEN f.furniture_safety_rating < AVG(f.furniture_safety_rating) OVER() THEN 'Below Average'
        ELSE 'Average'
    END AS safety_performance,
    
    -- Feedback trends
    COUNT(*) OVER(PARTITION BY EXTRACT(MONTH FROM s.service_date)) AS monthly_service_count,
    AVG(f.overall_rating) OVER(PARTITION BY EXTRACT(MONTH FROM s.service_date)) AS monthly_avg_rating
    
FROM 
    customers c
JOIN 
    services s ON c.customer_id = s.customer_id
JOIN 
    feedback f ON s.service_id = f.service_id
    
WHERE 
    s.service_provider = 'آل البيت'
    AND f.feedback_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 YEAR)
    
ORDER BY 
    s.service_date DESC,
    f.overall_rating DESC;
```
