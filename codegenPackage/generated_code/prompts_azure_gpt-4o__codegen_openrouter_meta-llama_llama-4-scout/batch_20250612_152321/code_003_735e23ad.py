"""
Generated Code Metadata:
========================
Original URL: https://barbudogrowler.cl
Prompt: Write a SQL query to retrieve all products from the "Sour, Gose & otras" category with a discount greater than 20%. Include columns for product name, original price, discounted price, and discount percentage.
Generated: DETERMINISTIC_735e23ad9a09c5b6
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve products from the "Sour, Gose & otras" category with a discount greater than 20%
SELECT 
    p.name AS product_name,
    p.original_price,
    p.discounted_price,
    (1 - p.discounted_price / p.original_price) * 100 AS discount_percentage
FROM 
    products p
INNER JOIN 
    product_categories pc ON p.category_id = pc.id
WHERE 
    pc.name = 'Sour, Gose & otras'
    AND p.discounted_price > 0
    AND (1 - p.discounted_price / p.original_price) * 100 > 20;
```

However, assuming there are separate `products` and `discounts` tables and considering best practices, here is a more normalized version:

```sql
-- Retrieve products from the "Sour, Gose & otras" category with a discount greater than 20%
SELECT 
    p.name AS product_name,
    p.price AS original_price,
    d.discounted_price,
    d.discount_percentage
FROM 
    products p
INNER JOIN 
    product_categories pc ON p.category_id = pc.id
INNER JOIN 
    discounts d ON p.id = d.product_id
WHERE 
    pc.name = 'Sour, Gose & otras'
    AND d.discount_percentage > 20;
```

And if there's a `product_offers` or similar table with offer details:

```sql
-- Retrieve products from the "Sour, Gose & otras" category with a discount greater than 20%
SELECT 
    p.name AS product_name,
    p.price AS original_price,
    po.offer_price AS discounted_price,
    (1 - po.offer_price / p.price) * 100 AS discount_percentage
FROM 
    products p
INNER JOIN 
    product_categories pc ON p.category_id = pc.id
INNER JOIN 
    product_offers po ON p.id = po.product_id
WHERE 
    pc.name = 'Sour, Gose & otras'
    AND po.offer_price > 0
    AND (1 - po.offer_price / p.price) * 100 > 20;
```
