"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beamtoken.org
Prompt: Create a SQL query to extract data on the most popular smart home products from a database that mirrors the Digital Trends product listings.
Generated: DETERMINISTIC_5f2dfdb321db043f
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to extract data on the most popular smart home products
-- Assumes a database schema with relevant tables and columns for product listings

-- Table: products
-- Columns:
--   id (INT) - Unique identifier for the product
--   name (VARCHAR) - Name of the product
--   category (VARCHAR) - Product category
--   views (INT) - Number of views the product has received
--   reviews_count (INT) - Total number of user reviews for the product
--   average_rating (DECIMAL) - Average rating for the product (e.g., 4.5)

-- Extract the top 10 most popular smart home products based on views and rating
-- Criteria: Products within the 'Smart Home' category, ordered by popularity 
--           (views and average_rating), with ties broken by reviews_count.

SELECT 
    id AS product_id, 
    name AS product_name, 
    category AS product_category, 
    views AS product_views, 
    reviews_count AS total_reviews, 
    average_rating AS avg_rating
FROM 
    products
WHERE 
    category = 'Smart Home' -- Filter for smart home products
ORDER BY 
    views DESC,             -- Primary sort by views in descending order
    average_rating DESC,    -- Secondary sort by average rating in descending order
    reviews_count DESC      -- Tertiary sort by total number of reviews in descending order
LIMIT 
    10;                     -- Limit to top 10 products
```
