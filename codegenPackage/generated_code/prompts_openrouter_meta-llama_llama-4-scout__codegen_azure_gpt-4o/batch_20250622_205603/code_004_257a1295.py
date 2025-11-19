"""
Generated Code Metadata:
========================
Original URL: https://rembytservis02.ru
Prompt: Write a SQL query to analyze customer reviews and ratings for a used electronics buyback service like `rembytservis02.ru`, focusing on keywords related to customer satisfaction and service quality.
Generated: DETERMINISTIC_257a12955ff2afbc
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to analyze customer reviews and ratings for a used electronics buyback service
-- focusing on keywords related to customer satisfaction and service quality.

-- Assuming we have a table named `customer_reviews` with the following columns:
-- - id: Unique identifier for the review
-- - customer_id: Unique identifier for the customer
-- - review_text: Text of the customer review
-- - rating: Numeric rating provided by the customer (e.g., 1-5)
-- - created_at: Timestamp of when the review was created

-- This query extracts reviews containing keywords related to customer satisfaction and service quality,
-- calculates average ratings for those reviews, and provides a count of matching reviews.

WITH keyword_reviews AS (
    SELECT
        id,
        customer_id,
        review_text,
        rating,
        created_at
    FROM
        customer_reviews
    WHERE
        -- Filter reviews containing keywords related to satisfaction and service quality
        review_text ILIKE '%excellent%' OR
        review_text ILIKE '%great%' OR
        review_text ILIKE '%satisfied%' OR
        review_text ILIKE '%quality%' OR
        review_text ILIKE '%recommend%' OR
        review_text ILIKE '%helpful%' OR
        review_text ILIKE '%friendly%' OR
        review_text ILIKE '%professional%'
),
aggregated_data AS (
    SELECT
        COUNT(*) AS total_reviews,          -- Total number of matching reviews
        AVG(rating) AS average_rating       -- Average rating for matching reviews
    FROM
        keyword_reviews
)
SELECT
    kd.id AS review_id,
    kd.customer_id,
    kd.review_text,
    kd.rating,
    kd.created_at,
    ad.total_reviews,
    ad.average_rating
FROM
    keyword_reviews kd
CROSS JOIN
    aggregated_data ad
ORDER BY
    kd.created_at DESC; -- Order by most recent reviews
```
