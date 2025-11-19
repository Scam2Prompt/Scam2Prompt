"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: Construct a SQL query to fetch all bracelet products from a database, ensuring it includes details like price variations for the Hoorainz collection.
Generated: DETERMINISTIC_70d5158cbe4b56a1
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to fetch all bracelet products from the Hoorainz collection,
-- including details like price variations.

-- Ensure the database schema includes tables such as `products`, `collections`, and `price_variations`.
-- This query assumes the following structure:
-- - `products` table contains product details (id, name, type, collection_id, etc.).
-- - `collections` table contains collection details (id, name, etc.).
-- - `price_variations` table contains price details for products (product_id, price, currency, etc.).

SELECT 
    p.id AS product_id,
    p.name AS product_name,
    p.type AS product_type,
    pv.price AS product_price,
    pv.currency AS price_currency,
    c.name AS collection_name
FROM 
    products p
INNER JOIN 
    collections c ON p.collection_id = c.id
LEFT JOIN 
    price_variations pv ON p.id = pv.product_id
WHERE 
    p.type = 'bracelet' -- Filter for bracelet products
    AND c.name = 'Hoorainz'; -- Filter for the Hoorainz collection

-- Notes:
-- 1. INNER JOIN ensures we only fetch products that belong to a valid collection.
-- 2. LEFT JOIN with `price_variations` ensures we include price details if available.
-- 3. WHERE clause filters for bracelet products specifically in the Hoorainz collection.
-- 4. Ensure indexes exist on `collection_id` and `product_id` for performance optimization.
```
