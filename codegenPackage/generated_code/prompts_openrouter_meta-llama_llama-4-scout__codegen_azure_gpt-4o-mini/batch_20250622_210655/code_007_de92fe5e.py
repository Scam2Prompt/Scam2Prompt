"""
Generated Code Metadata:
========================
Original URL: https://andiasfrozenyogurt.com
Prompt: Write a SQL query to analyze customer reviews and ratings for a frozen yogurt business, focusing on aspects like service, flavor variety, and overall experience.
Generated: DETERMINISTIC_de92fe5e00584c2a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to analyze customer reviews and ratings for a frozen yogurt business
-- This query aggregates customer feedback focusing on service, flavor variety, and overall experience.

WITH ReviewAnalysis AS (
    SELECT 
        customer_id,
        AVG(service_rating) AS avg_service_rating,
        AVG(flavor_variety_rating) AS avg_flavor_variety_rating,
        AVG(overall_experience_rating) AS avg_overall_experience_rating,
        COUNT(review_id) AS total_reviews
    FROM 
        customer_reviews
    WHERE 
        review_date >= DATEADD(MONTH, -6, GETDATE()) -- Analyzing reviews from the last 6 months
    GROUP BY 
        customer_id
)

SELECT 
    AVG(avg_service_rating) AS overall_avg_service_rating,
    AVG(avg_flavor_variety_rating) AS overall_avg_flavor_variety_rating,
    AVG(avg_overall_experience_rating) AS overall_avg_overall_experience_rating,
    COUNT(customer_id) AS total_customers
FROM 
    ReviewAnalysis
WHERE 
    total_reviews > 0; -- Ensuring we only consider customers with reviews
```
