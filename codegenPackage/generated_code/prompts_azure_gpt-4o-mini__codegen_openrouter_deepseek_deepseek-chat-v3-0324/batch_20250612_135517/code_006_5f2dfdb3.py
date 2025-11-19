"""
Generated Code Metadata:
========================
Original URL: https://beamtoken.org
Prompt: Create a SQL query to extract data on the most popular smart home products from a database that mirrors the Digital Trends product listings.
Generated: DETERMINISTIC_5f2dfdb321db043f
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to extract the most popular smart home products from a Digital Trends-like database
SELECT 
    p.product_id,
    p.product_name,
    p.brand,
    p.category,
    p.price,
    p.release_date,
    AVG(r.rating) AS average_rating,
    COUNT(r.review_id) AS review_count,
    COUNT(f.favorite_id) AS favorite_count,
    (COUNT(r.review_id) * 0.5) + (AVG(r.rating) * 20) + (COUNT(f.favorite_id) * 0.3) AS popularity_score
FROM 
    products p
LEFT JOIN 
    reviews r ON p.product_id = r.product_id
LEFT JOIN 
    favorites f ON p.product_id = f.product_id
WHERE 
    p.category = 'Smart Home'
    AND p.is_active = TRUE
GROUP BY 
    p.product_id, p.product_name, p.brand, p.category, p.price, p.release_date
HAVING 
    COUNT(r.review_id) >= 5  -- Only include products with at least 5 reviews
ORDER BY 
    popularity_score DESC,
    average_rating DESC,
    review_count DESC
LIMIT 50;  -- Return top 50 most popular products
```
