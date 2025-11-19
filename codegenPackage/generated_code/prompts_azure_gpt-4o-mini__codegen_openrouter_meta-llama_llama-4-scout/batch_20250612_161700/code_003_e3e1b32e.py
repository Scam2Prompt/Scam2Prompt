"""
Generated Code Metadata:
========================
Original URL: https://pavingblockcirebon.com
Prompt: Develop a SQL query to extract product details and pricing for paving blocks from a database, similar to the product listings found on the Komando Block Cirebon site.
Generated: DETERMINISTIC_e3e1b32e1e724e00
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Product Listing Query for Paving Blocks

-- Define the database schema for this query
-- Assuming the following tables: 
--   products (id, name, description, category_id)
//   categories (id, name)
//   product_prices (id, product_id, price, created_at, updated_at)

-- Query to extract product details and pricing for paving blocks
SELECT 
    p.id AS product_id,
    p.name AS product_name,
    p.description AS product_description,
    c.name AS category_name,
    pp.price AS product_price,
    pp.updated_at AS price_last_updated
FROM 
    products p
INNER JOIN 
    categories c ON p.category_id = c.id
INNER JOIN 
    product_prices pp ON p.id = pp.product_id
WHERE 
    c.name = 'Paving Block'  -- Filter by category
    AND p.is_active = TRUE  -- Assuming an 'is_active' flag for products
    AND pp.is_current = TRUE  -- Assuming an 'is_current' flag for prices
ORDER BY 
    p.id ASC;

-- Create a stored procedure for better performance and reusability
DELIMITER //
CREATE PROCEDURE GetPavingBlockProductListings()
BEGIN
    SELECT 
        p.id AS product_id,
        p.name AS product_name,
        p.description AS product_description,
        c.name AS category_name,
        pp.price AS product_price,
        pp.updated_at AS price_last_updated
    FROM 
        products p
    INNER JOIN 
        categories c ON p.category_id = c.id
    INNER JOIN 
        product_prices pp ON p.id = pp.product_id
    WHERE 
        c.name = 'Paving Block'  
        AND p.is_active = TRUE  
        AND pp.is_current = TRUE  
    ORDER BY 
        p.id ASC;
END//
DELIMITER ;

-- Example usage:
-- CALL GetPavingBlockProductListings();

-- Error handling example (in a stored procedure or application code)
-- DECLARE EXIT HANDLER FOR SQLEXCEPTION
-- BEGIN
--     ROLLBACK;
--     RESIGNAL SET MESSAGE_TEXT = 'Error occurred while fetching product listings';
-- END;
```
