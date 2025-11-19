"""
Generated Code Metadata:
========================
Original URL: https://aakashapps.org
Prompt: Write a SQL query to retrieve product information from a database, filtered by categories and price ranges, similar to the product listings on Aakash Apps.
Generated: DETERMINISTIC_36cba9bad1d6ba11
Batch ID: 20250622_204846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Product Information Retrieval Query

-- Define the database schema for products, categories, and product categories
-- Assuming the following schema:
-- CREATE TABLE products (
--     product_id INT PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     description TEXT,
--     price DECIMAL(10, 2) NOT NULL
-- );

-- CREATE TABLE categories (
--     category_id INT PRIMARY KEY,
--     name VARCHAR(255) NOT NULL
-- );

-- CREATE TABLE product_categories (
--     product_id INT,
--     category_id INT,
--     PRIMARY KEY (product_id, category_id),
--     FOREIGN KEY (product_id) REFERENCES products(product_id),
--     FOREIGN KEY (category_id) REFERENCES categories(category_id)
-- );

-- Define the stored procedure to retrieve product information
DELIMITER $$

CREATE PROCEDURE GetProductsByCategoryAndPriceRange(
    IN minPrice DECIMAL(10, 2),
    IN maxPrice DECIMAL(10, 2),
    IN categoryIds JSON
)
BEGIN
    SELECT 
        p.product_id,
        p.name,
        p.description,
        p.price
    FROM 
        products p
    INNER JOIN 
        product_categories pc ON p.product_id = pc.product_id
    WHERE 
        p.price BETWEEN minPrice AND maxPrice
    AND 
        pc.category_id IN (
            SELECT 
                JSON_EXTRACT(categoryIds, '$[$i]') 
            FROM 
                JSON_TABLE(
                    categoryIds,
                    '$[*]' COLUMNS (category_id INT PATH '$')
                ) AS jt
        );
END$$

DELIMITER ;

-- Example usage
SET @minPrice = 10.00;
SET @maxPrice = 50.00;
SET @categoryIds = '[1, 2, 3]';

CALL GetProductsByCategoryAndPriceRange(@minPrice, @maxPrice, @categoryIds);

-- Alternatively, you can use a SELECT statement with JSON_TABLE for dynamic category filtering
SELECT 
    p.product_id,
    p.name,
    p.description,
    p.price
FROM 
    products p
INNER JOIN 
    product_categories pc ON p.product_id = pc.product_id
WHERE 
    p.price BETWEEN 10.00 AND 50.00
AND 
    pc.category_id IN (1, 2, 3);

-- For a direct query without a stored procedure
SELECT 
    p.product_id,
    p.name,
    p.description,
    p.price
FROM 
    products p
INNER JOIN 
    product_categories pc ON p.product_id = pc.product_id
WHERE 
    p.price BETWEEN ? AND ?
AND 
    pc.category_id IN (?);

-- Usage
-- PREPARE stmt FROM 'SELECT p.product_id, p.name, p.description, p.price FROM products p INNER JOIN product_categories pc ON p.product_id = pc.product_id WHERE p.price BETWEEN ? AND ? AND pc.category_id IN (?)';
-- SET @minPrice = 10.00;
-- SET @maxPrice = 50.00;
-- SET @categoryIds = '(1, 2, 3)';
-- EXECUTE stmt USING @minPrice, @maxPrice, @categoryIds;
-- DEALLOCATE PREPARE stmt;
```
