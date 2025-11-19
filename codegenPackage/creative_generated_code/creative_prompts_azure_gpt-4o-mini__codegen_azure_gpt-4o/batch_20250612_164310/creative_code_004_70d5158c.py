"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoorainz.com
Prompt: Construct a SQL query to fetch all bracelet products from a database, ensuring it includes details like price variations for the Hoorainz collection.
Generated: DETERMINISTIC_70d5158cbe4b56a1
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to fetch all bracelet products from the database, including price variations,
-- specifically for the "Hoorainz" collection.

-- Assumes the following schema:
-- - products table: contains product details (id, name, type, collection_id, etc.)
-- - collections table: contains collection details (id, name, etc.)
-- - price_variations table: contains price variations for products (id, product_id, variation_details, price, etc.)

-- Fetch bracelet products with their price variations for the "Hoorainz" collection
SELECT 
    p.id AS product_id, 
    p.name AS product_name, 
    p.type AS product_type, 
    pv.variation_details AS price_variation_details, 
    pv.price AS price,
    c.name AS collection_name
FROM 
    products AS p
INNER JOIN 
    collections AS c ON p.collection_id = c.id
LEFT JOIN 
    price_variations AS pv ON p.id = pv.product_id
WHERE 
    p.type = 'bracelet'                        -- Filter for bracelets only
    AND c.name = 'Hoorainz';                   -- Filter for "Hoorainz" collection
```
