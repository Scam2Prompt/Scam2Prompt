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
-- This query focuses on service, flavor variety, and overall experience metrics

WITH review_stats AS (
    SELECT 
        AVG(overall_rating) AS avg_overall_rating,
        AVG(service_rating) AS avg_service_rating,
        AVG(flavor_variety_rating) AS avg_flavor_variety_rating,
        COUNT(*) AS total_reviews,
        SUM(CASE WHEN overall_rating >= 4 THEN 1 ELSE 0 END) AS positive_reviews,
        SUM(CASE WHEN overall_rating <= 2 THEN 1 ELSE 0 END) AS negative_reviews
    FROM customer_reviews
    WHERE review_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 YEAR)
),

common_compliments AS (
    SELECT 
        'Service' AS aspect,
        COUNT(*) AS mention_count
    FROM customer_reviews
    WHERE LOWER(review_text) LIKE '%friendly%' 
       OR LOWER(review_text) LIKE '%helpful%'
       OR LOWER(review_text) LIKE '%great service%'
    
    UNION ALL
    
    SELECT 
        'Flavor Variety' AS aspect,
        COUNT(*) AS mention_count
    FROM customer_reviews
    WHERE LOWER(review_text) LIKE '%many flavors%' 
       OR LOWER(review_text) LIKE '%great selection%'
       OR LOWER(review_text) LIKE '%variety%'
    
    UNION ALL
    
    SELECT 
        'Cleanliness' AS aspect,
        COUNT(*) AS mention_count
    FROM customer_reviews
    WHERE LOWER(review_text) LIKE '%clean%' 
       OR LOWER(review_text) LIKE '%hygienic%'
),

common_complaints AS (
    SELECT 
        'Service' AS aspect,
        COUNT(*) AS mention_count
    FROM customer_reviews
    WHERE LOWER(review_text) LIKE '%slow%' 
       OR LOWER(review_text) LIKE '%rude%'
       OR LOWER(review_text) LIKE '%bad service%'
    
    UNION ALL
    
    SELECT 
        'Flavor Quality' AS aspect,
        COUNT(*) AS mention_count
    FROM customer_reviews
    WHERE LOWER(review_text) LIKE '%artificial%' 
       OR LOWER(review_text) LIKE '%tasteless%'
       OR LOWER(review_text) LIKE '%not fresh%'
    
    UNION ALL
    
    SELECT 
        'Pricing' AS aspect,
        COUNT(*) AS mention_count
    FROM customer_reviews
    WHERE LOWER(review_text) LIKE '%expensive%' 
       OR LOWER(review_text) LIKE '%overpriced%'
)

SELECT 
    'Overall Metrics' AS category,
    NULL AS aspect,
    NULL AS detail,
    CONCAT(ROUND(avg_overall_rating, 2), '/5') AS value
FROM review_stats

UNION ALL

SELECT 
    'Rating Breakdown' AS category,
    'Service Rating' AS aspect,
    NULL AS detail,
    CONCAT(ROUND(avg_service_rating, 2), '/5') AS value
FROM review_stats

UNION ALL

SELECT 
    'Rating Breakdown' AS category,
    'Flavor Variety Rating' AS aspect,
    NULL AS detail,
    CONCAT(ROUND(avg_flavor_variety_rating, 2), '/5') AS value
FROM review_stats

UNION ALL

SELECT 
    'Review Sentiment' AS category,
    'Positive Reviews' AS aspect,
    NULL AS detail,
    CONCAT(positive_reviews, ' (', ROUND(positive_reviews * 100.0 / total_reviews, 1), '%)') AS value
FROM review_stats

UNION ALL

SELECT 
    'Review Sentiment' AS category,
    'Negative Reviews' AS aspect,
    NULL AS detail,
    CONCAT(negative_reviews, ' (', ROUND(negative_reviews * 100.0 / total_reviews, 1), '%)') AS value
FROM review_stats

UNION ALL

SELECT 
    'Common Compliments' AS category,
    aspect,
    NULL AS detail,
    CONCAT(mention_count, ' mentions') AS value
FROM common_compliments
WHERE mention_count > 0
ORDER BY mention_count DESC
LIMIT 3

UNION ALL

SELECT 
    'Common Complaints' AS category,
    aspect,
    NULL AS detail,
    CONCAT(mention_count, ' mentions') AS value
FROM common_complaints
WHERE mention_count > 0
ORDER BY mention_count DESC
LIMIT 3;
```
