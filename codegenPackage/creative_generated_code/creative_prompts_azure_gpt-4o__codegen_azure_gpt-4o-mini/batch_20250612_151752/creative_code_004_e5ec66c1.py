"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Write a SQL query to retrieve the most popular brands and products under "لوازم آرایشی صورت" and "کرم ضد آفتاب" from a database similar to chandkala.com.
Generated: DETERMINISTIC_e5ec66c14e5f0dc3
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to retrieve the most popular brands and products under
-- "لوازم آرایشی صورت" (Face Cosmetics) and "کرم ضد آفتاب" (Sunscreen Cream)
-- from a database similar to chandkala.com.

WITH RankedProducts AS (
    SELECT 
        p.product_id,
        p.product_name,
        p.brand_id,
        b.brand_name,
        c.category_name,
        p.popularity_score,
        ROW_NUMBER() OVER (PARTITION BY p.brand_id ORDER BY p.popularity_score DESC) as rank
    FROM 
        products p
    JOIN 
        brands b ON p.brand_id = b.brand_id
    JOIN 
        categories c ON p.category_id = c.category_id
    WHERE 
        c.category_name IN ('لوازم آرایشی صورت', 'کرم ضد آفتاب')
)

SELECT 
    rp.brand_id,
    rp.brand_name,
    rp.product_id,
    rp.product_name,
    rp.popularity_score
FROM 
    RankedProducts rp
WHERE 
    rp.rank = 1
ORDER BY 
    rp.brand_name;

-- This query first creates a Common Table Expression (CTE) named RankedProducts
-- that ranks products by their popularity score for each brand within the specified categories.
-- The final SELECT statement retrieves the top product for each brand.
```
