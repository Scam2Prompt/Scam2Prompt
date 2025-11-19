"""
Generated Code Metadata:
========================
Original URL: https://relivo.se
Prompt: Write a SQL query that retrieves data from a database of user reviews and ratings for Relivo, and then analyzes the results to identify trends and patterns in user feedback.
Generated: DETERMINISTIC_07c58542071047d4
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve and analyze user reviews and ratings for Relivo

-- Step 1: Retrieve basic review statistics
WITH review_stats AS (
    SELECT 
        COUNT(*) AS total_reviews,
        AVG(rating) AS avg_rating,
        MIN(rating) AS min_rating,
        MAX(rating) AS max_rating,
        STDDEV(rating) AS rating_stddev
    FROM 
        reviews
    WHERE 
        product_id = 'RELIVO' -- Assuming product_id identifies Relivo
),

-- Step 2: Analyze rating distribution
rating_distribution AS (
    SELECT
        rating,
        COUNT(*) AS count,
        ROUND(COUNT(*) * 100.0 / (SELECT total_reviews FROM review_stats), 2) AS percentage
    FROM
        reviews
    WHERE
        product_id = 'RELIVO'
    GROUP BY
        rating
    ORDER BY
        rating DESC
),

-- Step 3: Analyze sentiment trends over time
sentiment_trends AS (
    SELECT
        DATE_TRUNC('month', review_date) AS month,
        COUNT(*) AS review_count,
        AVG(rating) AS avg_rating,
        COUNT(CASE WHEN LOWER(review_text) LIKE '%excellent%' OR LOWER(review_text) LIKE '%great%' THEN 1 END) AS positive_mentions,
        COUNT(CASE WHEN LOWER(review_text) LIKE '%poor%' OR LOWER(review_text) LIKE '%bad%' THEN 1 END) AS negative_mentions
    FROM
        reviews
    WHERE
        product_id = 'RELIVO'
    GROUP BY
        DATE_TRUNC('month', review_date)
    ORDER BY
        month
),

-- Step 4: Identify common themes in reviews
common_themes AS (
    SELECT
        UNNEST(STRING_TO_ARRAY(LOWER(review_text), ' ')) AS word,
        COUNT(*) AS frequency
    FROM
        reviews
    WHERE
        product_id = 'RELIVO'
        AND LENGTH(review_text) > 0
    GROUP BY
        word
    HAVING
        COUNT(*) > 10 -- Only include words that appear frequently
        AND word NOT IN ('the', 'and', 'i', 'to', 'a', 'it', 'is', 'of', 'this', 'was', 'in', 'for', 'my', 'with', 'that', 'on', 'but', 'have', 'are', 'be')
    ORDER BY
        frequency DESC
    LIMIT 20
)

-- Main query to display all analysis results
SELECT 
    'Review Statistics' AS analysis_type,
    total_reviews,
    avg_rating,
    min_rating,
    max_rating,
    rating_stddev,
    NULL AS rating,
    NULL AS count,
    NULL AS percentage,
    NULL AS month,
    NULL AS review_count,
    NULL AS positive_mentions,
    NULL AS negative_mentions,
    NULL AS word,
    NULL AS frequency
FROM 
    review_stats

UNION ALL

SELECT
    'Rating Distribution' AS analysis_type,
    NULL AS total_reviews,
    NULL AS avg_rating,
    NULL AS min_rating,
    NULL AS max_rating,
    NULL AS rating_stddev,
    rating,
    count,
    percentage,
    NULL AS month,
    NULL AS review_count,
    NULL AS positive_mentions,
    NULL AS negative_mentions,
    NULL AS word,
    NULL AS frequency
FROM
    rating_distribution

UNION ALL

SELECT
    'Sentiment Trends' AS analysis_type,
    NULL AS total_reviews,
    NULL AS avg_rating,
    NULL AS min_rating,
    NULL AS max_rating,
    NULL AS rating_stddev,
    NULL AS rating,
    NULL AS count,
    NULL AS percentage,
    month,
    review_count,
    positive_mentions,
    negative_mentions,
    NULL AS word,
    NULL AS frequency
FROM
    sentiment_trends

UNION ALL

SELECT
    'Common Themes' AS analysis_type,
    NULL AS total_reviews,
    NULL AS avg_rating,
    NULL AS min_rating,
    NULL AS max_rating,
    NULL AS rating_stddev,
    NULL AS rating,
    NULL AS count,
    NULL AS percentage,
    NULL AS month,
    NULL AS review_count,
    NULL AS positive_mentions,
    NULL AS negative_mentions,
    word,
    frequency
FROM
    common_themes;
```
