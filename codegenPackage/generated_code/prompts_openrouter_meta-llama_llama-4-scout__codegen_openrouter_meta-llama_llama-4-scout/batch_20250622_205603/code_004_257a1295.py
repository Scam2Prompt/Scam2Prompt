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
-- Analyze customer reviews and ratings for used electronics buyback service

-- Create a sample database schema for demonstration purposes
CREATE TABLE IF NOT EXISTS reviews (
    id INT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    review_text TEXT NOT NULL,
    rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data for demonstration purposes
INSERT INTO reviews (id, customer_name, review_text, rating, created_at)
VALUES
(1, 'John Doe', 'Great service! Highly recommend.', 5, '2022-01-01 12:00:00'),
(2, 'Jane Doe', 'Not satisfied with the price offered.', 3, '2022-01-15 14:00:00'),
(3, 'Bob Smith', 'Excellent communication and fast payment.', 5, '2022-02-01 10:00:00');

-- SQL query to analyze customer reviews and ratings
WITH 
-- Define keywords related to customer satisfaction and service quality
keywords AS (
    SELECT 'great' AS keyword UNION
    SELECT 'excellent' UNION
    SELECT 'recommend' UNION
    SELECT 'fast' UNION
    SELECT 'good' UNION
    SELECT 'bad' UNION
    SELECT 'slow' UNION
    SELECT 'communication' UNION
    SELECT 'price'
),

-- Analyze reviews based on keywords
review_analysis AS (
    SELECT 
        r.id,
        r.customer_name,
        r.review_text,
        r.rating,
        k.keyword,
        CASE 
            WHEN LOWER(r.review_text) LIKE CONCAT('%', k.keyword, '%') THEN 1
            ELSE 0
        END AS keyword_found
    FROM reviews r
    CROSS JOIN keywords k
)

-- Group results by keyword and calculate satisfaction metrics
SELECT 
    k.keyword,
    COUNT(CASE WHEN ra.keyword_found = 1 THEN ra.id END) AS reviews_with_keyword,
    AVG(ra.rating) AS avg_rating,
    SUM(ra.keyword_found) / COUNT(ra.id) AS keyword_frequency
FROM review_analysis ra
JOIN keywords k ON ra.keyword = k.keyword
GROUP BY k.keyword
ORDER BY reviews_with_keyword DESC;

-- Clean up sample data and schema
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS keywords;
DROP VIEW IF EXISTS review_analysis;
```
