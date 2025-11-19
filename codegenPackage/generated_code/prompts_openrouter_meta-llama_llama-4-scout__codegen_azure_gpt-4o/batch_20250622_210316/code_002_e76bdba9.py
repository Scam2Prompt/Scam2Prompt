"""
Generated Code Metadata:
========================
Original URL: https://fotopoint.com.ar
Prompt: "Generate a SQL query to retrieve product information from a database schema similar to Fotopoint's, filtering by 'Tarjetas de Memoria' and 'Cámaras de Seguridad'."
Generated: DETERMINISTIC_e76bdba97f42cd95
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve product information filtered by specific categories
-- Assumes a database schema with tables: `products` and `categories`
-- `products` table contains columns: id, name, description, price, category_id
-- `categories` table contains columns: id, name

-- Using a JOIN to link products with their categories
SELECT 
    p.id AS product_id,
    p.name AS product_name,
    p.description AS product_description,
    p.price AS product_price,
    c.name AS category_name
FROM 
    products p
INNER JOIN 
    categories c
ON 
    p.category_id = c.id
WHERE 
    c.name IN ('Tarjetas de Memoria', 'Cámaras de Seguridad') -- Filter by specific categories
ORDER BY 
    p.name ASC; -- Sort products alphabetically by name
```
