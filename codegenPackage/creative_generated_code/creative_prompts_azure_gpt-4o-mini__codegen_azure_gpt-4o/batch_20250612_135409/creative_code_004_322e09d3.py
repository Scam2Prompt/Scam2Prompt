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
-- This SQL query analyzes customer reviews for electric bikes on the Vihreää Voimaa platform
-- focusing on ratings and feedback. Ensure your database structure matches the table and column names.

-- Query assumes a table schema like:
-- Table: customer_reviews
-- Columns:
--   - review_id (INT): Unique identifier for each review
--   - product_id (INT): Unique identifier for the electric bike
--   - customer_id (INT): Unique identifier for the customer
--   - rating (INT): Rating provided by the customer (e.g., 1-5 scale)
--   - feedback (TEXT): Written feedback from the customer
--   - review_date (DATE): Date the review was submitted

-- This query aggregates reviews for electric bikes and provides insights into ratings and feedback.

SELECT 
    product_id,
    COUNT(review_id) AS total_reviews,                     -- Total number of reviews per product
    AVG(rating) AS average_rating,                        -- Average rating per product
    MIN(rating) AS lowest_rating,                         -- Lowest rating per product
    MAX(rating) AS highest_rating,                        -- Highest rating per product
    GROUP_CONCAT(feedback SEPARATOR '; ') AS feedback_snippets -- Concatenated customer feedback
FROM 
    customer_reviews
WHERE 
    product_id IN (
        SELECT product_id 
        FROM products 
        WHERE category = 'Electric Bikes'                  -- Analyzing only electric bikes
    )
    AND review_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 YEAR) -- Reviews from the last year only
GROUP BY 
    product_id
ORDER BY 
    average_rating DESC;                                   -- Order by highest average rating
```
