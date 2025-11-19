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
-- SQL Query to analyze customer reviews and ratings for a frozen yogurt business
-- focusing on aspects like service, flavor variety, and overall experience.

-- Assuming we have a table named `customer_reviews` with the following columns:
-- - review_id (INT): Unique identifier for each review
-- - customer_id (INT): Unique identifier for the customer
-- - service_rating (INT): Rating for service (1-5 scale)
-- - flavor_variety_rating (INT): Rating for flavor variety (1-5 scale)
-- - overall_experience_rating (INT): Rating for overall experience (1-5 scale)
-- - review_text (TEXT): Text of the customer review
-- - review_date (DATE): Date the review was submitted

-- This query calculates average ratings for each aspect, identifies the number of reviews,
-- and highlights reviews with low ratings for further analysis.

WITH RatingsSummary AS (
    SELECT
        AVG(service_rating) AS avg_service_rating,          -- Average service rating
        AVG(flavor_variety_rating) AS avg_flavor_variety_rating, -- Average flavor variety rating
        AVG(overall_experience_rating) AS avg_overall_experience_rating, -- Average overall experience rating
        COUNT(*) AS total_reviews                          -- Total number of reviews
    FROM
        customer_reviews
),
LowRatingReviews AS (
    SELECT
        review_id,
        customer_id,
        service_rating,
        flavor_variety_rating,
        overall_experience_rating,
        review_text,
        review_date
    FROM
        customer_reviews
    WHERE
        service_rating <= 2 OR                             -- Identify reviews with low service rating
        flavor_variety_rating <= 2 OR                     -- Identify reviews with low flavor variety rating
        overall_experience_rating <= 2                    -- Identify reviews with low overall experience rating
)
SELECT
    rs.avg_service_rating,
    rs.avg_flavor_variety_rating,
    rs.avg_overall_experience_rating,
    rs.total_reviews,
    lr.review_id,
    lr.customer_id,
    lr.service_rating,
    lr.flavor_variety_rating,
    lr.overall_experience_rating,
    lr.review_text,
    lr.review_date
FROM
    RatingsSummary rs
LEFT JOIN
    LowRatingReviews lr ON TRUE; -- Combine summary data with low-rating reviews for analysis
```
