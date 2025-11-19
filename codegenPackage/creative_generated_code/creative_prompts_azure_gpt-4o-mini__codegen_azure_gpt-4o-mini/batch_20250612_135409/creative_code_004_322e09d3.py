"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livesupport.tfryx.xyz
Prompt: Construct a SQL query to analyze customer reviews for electric bikes sold on the Vihreää Voimaa platform, focusing on ratings and feedback.
Generated: DETERMINISTIC_322e09d3c1efec88
Batch ID: 20250612_135409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to analyze customer reviews for electric bikes on the Vihreää Voimaa platform
-- The query gathers the average rating, total number of reviews, and detailed feedback from customers
-- It focuses specifically on electric bike products

SELECT 
    p.product_id,                    -- Unique identifier for the product
    p.product_name,                  -- Name of the product
    AVG(r.rating) AS average_rating, -- Average rating for the product
    COUNT(r.review_id) AS total_reviews, -- Total number of reviews for the product
    STRING_AGG(r.feedback, '; ') AS customer_feedback -- Concatenated feedback from customers
FROM 
    products p
JOIN 
    reviews r ON p.product_id = r.product_id -- Joining products and reviews on product_id
WHERE 
    p.category = 'Electric Bikes'         -- Filtering for electric bike category
GROUP BY 
    p.product_id,                         -- Grouping by product to aggregate ratings and feedback
    p.product_name
ORDER BY 
    average_rating DESC;                  -- Ordering results by highest average rating
```
