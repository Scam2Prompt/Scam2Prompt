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
-- SQL query to analyze customer reviews and ratings for a used electronics buyback service
-- Focuses on identifying positive/negative sentiment and service quality keywords

WITH review_analysis AS (
    SELECT 
        review_id,
        customer_id,
        rating,
        review_text,
        review_date,
        -- Extract common positive sentiment keywords
        CASE 
            WHEN LOWER(review_text) LIKE '%excellent%' THEN 1
            WHEN LOWER(review_text) LIKE '%great%' THEN 1
            WHEN LOWER(review_text) LIKE '%awesome%' THEN 1
            WHEN LOWER(review_text) LIKE '%fast%' THEN 1
            WHEN LOWER(review_text) LIKE '%easy%' THEN 1
            WHEN LOWER(review_text) LIKE '%happy%' THEN 1
            WHEN LOWER(review_text) LIKE '%satisfied%' THEN 1
            ELSE 0
        END AS positive_keywords,
        -- Extract common negative sentiment keywords
        CASE 
            WHEN LOWER(review_text) LIKE '%poor%' THEN 1
            WHEN LOWER(review_text) LIKE '%bad%' THEN 1
            WHEN LOWER(review_text) LIKE '%slow%' THEN 1
            WHEN LOWER(review_text) LIKE '%difficult%' THEN 1
            WHEN LOWER(review_text) LIKE '%unhappy%' THEN 1
            WHEN LOWER(review_text) LIKE '%disappointed%' THEN 1
            WHEN LOWER(review_text) LIKE '%problem%' THEN 1
            ELSE 0
        END AS negative_keywords,
        -- Extract service quality keywords
        CASE 
            WHEN LOWER(review_text) LIKE '%service%' THEN 1
            WHEN LOWER(review_text) LIKE '%support%' THEN 1
            WHEN LOWER(review_text) LIKE '%process%' THEN 1
            WHEN LOWER(review_text) LIKE '%communication%' THEN 1
            WHEN LOWER(review_text) LIKE '%price%' THEN 1
            WHEN LOWER(review_text) LIKE '%offer%' THEN 1
            WHEN LOWER(review_text) LIKE '%condition%' THEN 1
            ELSE 0
        END AS service_keywords
    FROM customer_reviews
    WHERE review_date >= DATEADD(month, -6, GETDATE())  -- Last 6 months of reviews
)

SELECT 
    rating,
    COUNT(*) AS total_reviews,
    AVG(CAST(positive_keywords AS FLOAT)) * 100 AS percent_positive_keywords,
    AVG(CAST(negative_keywords AS FLOAT)) * 100 AS percent_negative_keywords,
    AVG(CAST(service_keywords AS FLOAT)) * 100 AS percent_service_keywords,
    SUM(CASE WHEN positive_keywords = 1 THEN 1 ELSE 0 END) AS positive_reviews,
    SUM(CASE WHEN negative_keywords = 1 THEN 1 ELSE 0 END) AS negative_reviews,
    -- Calculate sentiment score (positive - negative keywords)
    AVG(CAST(positive_keywords AS FLOAT) - CAST(negative_keywords AS FLOAT)) AS sentiment_score
FROM review_analysis
GROUP BY rating
ORDER BY rating DESC;
```
