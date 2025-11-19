"""
Generated Code Metadata:
========================
Original URL: https://firstcrackcoffeeroasters.com
Prompt: Create a SQL query to retrieve a list of best-selling coffee products from a database, considering factors like product sales and customer reviews.
Generated: DETERMINISTIC_e420abf2f4505b47
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve best-selling coffee products based on sales and reviews
SELECT 
    p.product_id,
    p.product_name,
    p.description,
    p.price,
    SUM(oi.quantity) AS total_units_sold,
    COUNT(r.review_id) AS review_count,
    AVG(r.rating) AS average_rating,
    -- Weighted score calculation (60% sales, 40% reviews)
    (SUM(oi.quantity) * 0.6 + AVG(r.rating) * COUNT(r.review_id) * 0.4) AS popularity_score
FROM 
    products p
LEFT JOIN 
    order_items oi ON p.product_id = oi.product_id
LEFT JOIN 
    orders o ON oi.order_id = o.order_id AND o.order_status = 'completed'
LEFT JOIN 
    reviews r ON p.product_id = r.product_id
WHERE 
    p.category = 'coffee'
    AND p.is_active = TRUE
GROUP BY 
    p.product_id, p.product_name, p.description, p.price
HAVING 
    COUNT(r.review_id) >= 5  -- Only include products with at least 5 reviews
    AND AVG(r.rating) >= 3.0  -- Minimum average rating threshold
ORDER BY 
    popularity_score DESC,
    total_units_sold DESC,
    average_rating DESC
LIMIT 10;  -- Return top 10 best-selling coffee products
```
