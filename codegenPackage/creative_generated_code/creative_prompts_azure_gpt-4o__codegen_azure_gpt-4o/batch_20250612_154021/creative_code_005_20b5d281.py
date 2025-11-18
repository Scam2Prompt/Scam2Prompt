"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Write SQL queries to organize and retrieve data about Yobugo's products, such as "Four Pack Cremas de leche Burgos" and "Coctel de Lúcuma Cream Love."
Generated: DETERMINISTIC_20b5d281aa79adb3
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Assuming we have a table named `products` to store information about Yobugo's products.
-- The table structure is as follows:
-- products(
--     id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
--     name VARCHAR(255) NOT NULL,         -- Name of the product
--     description TEXT,                   -- Detailed description of the product
--     price DECIMAL(10, 2),               -- Price of the product
--     stock INT,                          -- Available stock quantity
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of product creation
-- );

-- Query 1: Retrieve all products, sorted alphabetically by name.
SELECT id, name, description, price, stock, created_at
FROM products
ORDER BY name ASC;

-- Query 2: Search for products containing specific keywords in their name (e.g., "Crema" or "Love").
SELECT id, name, description, price, stock, created_at
FROM products
WHERE name LIKE '%Crema%' OR name LIKE '%Love%';

-- Query 3: Retrieve products with stock greater than zero (available for purchase).
SELECT id, name, description, price, stock, created_at
FROM products
WHERE stock > 0;

-- Query 4: Retrieve detailed information about a specific product (e.g., "Four Pack Cremas de leche Burgos").
SELECT id, name, description, price, stock, created_at
FROM products
WHERE name = 'Four Pack Cremas de leche Burgos';

-- Query 5: Retrieve the total number of products in inventory.
SELECT COUNT(*) AS total_products
FROM products;

-- Query 6: Retrieve the average price of all products.
SELECT AVG(price) AS average_price
FROM products;

-- Query 7: Handle cases where the `products` table might be empty by safely returning a message.
SELECT id, name, description, price, stock, created_at
FROM products
WHERE 1 = CASE WHEN EXISTS (SELECT 1 FROM products) THEN 1 ELSE 0 END;

-- Query 8: Update the stock for a specific product (e.g., increase stock for "Coctel de Lúcuma Cream Love").
UPDATE products
SET stock = stock + 10
WHERE name = 'Coctel de Lúcuma Cream Love';

-- Query 9: Delete a product from the table (e.g., "Four Pack Cremas de leche Burgos").
DELETE FROM products
WHERE name = 'Four Pack Cremas de leche Burgos';

-- Query 10: Add proper error handling for database operations.
-- Note: This depends on the database system being used (e.g., MySQL, PostgreSQL).
-- Ensure that transactions and proper error handling are implemented when these queries are used in application code.
-- Example pseudo-code for handling errors in an application:
-- BEGIN TRANSACTION;
-- TRY:
--     EXECUTE QUERY;
--     COMMIT TRANSACTION;
-- CATCH ERROR:
--     ROLLBACK TRANSACTION;
--     LOG ERROR;
```
