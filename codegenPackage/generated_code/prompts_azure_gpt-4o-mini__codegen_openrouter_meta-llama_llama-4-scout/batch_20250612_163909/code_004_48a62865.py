"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Construct a SQL query to extract all items related to construction civil tools from a product database, including mixers and hand tools.
Generated: DETERMINISTIC_48a628650ee26e62
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Construction Civil Tools Query

-- Define the query to extract construction civil tools
SELECT 
    p.product_id,
    p.product_name,
    p.description,
    p.price,
    p.category
FROM 
    products p
INNER JOIN 
    product_categories pc ON p.category_id = pc.category_id
WHERE 
    pc.category_name IN ('Construction Tools', 'Civil Engineering Tools', 'Mixers', 'Hand Tools')
    OR p.product_name LIKE '%Mixer%'
    OR p.product_name LIKE '%Drill%'
    OR p.product_name LIKE '%Saw%'
    OR p.product_name LIKE '%Shovel%'
    OR p.product_name LIKE '%Trowel%';

-- Define a stored procedure for executing the query
DELIMITER //
CREATE PROCEDURE GetConstructionCivilTools()
BEGIN
    SELECT 
        p.product_id,
        p.product_name,
        p.description,
        p.price,
        p.category
    FROM 
        products p
    INNER JOIN 
        product_categories pc ON p.category_id = pc.category_id
    WHERE 
        pc.category_name IN ('Construction Tools', 'Civil Engineering Tools', 'Mixers', 'Hand Tools')
        OR p.product_name LIKE '%Mixer%'
        OR p.product_name LIKE '%Drill%'
        OR p.product_name LIKE '%Saw%'
        OR p.product_name LIKE '%Shovel%'
        OR p.product_name LIKE '%Trowel%';
END//
DELIMITER ;

-- Example usage:
-- CALL GetConstructionCivilTools();

-- Create a function to handle errors
DELIMITER //
CREATE FUNCTION HandleError(error_message VARCHAR(255))
RETURNS VARCHAR(255)
BEGIN
    DECLARE error_text VARCHAR(255);
    SET error_text = CONCAT('Error: ', error_message);
    RETURN error_text;
END//
DELIMITER ;

-- Create a table for products
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    category_id INT,
    PRIMARY KEY (product_id)
);

-- Create a table for product categories
CREATE TABLE IF NOT EXISTS product_categories (
    category_id INT AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (category_id)
);

-- Insert sample data
INSERT INTO product_categories (category_id, category_name)
VALUES 
(1, 'Construction Tools'),
(2, 'Civil Engineering Tools'),
(3, 'Mixers'),
(4, 'Hand Tools');

INSERT INTO products (product_id, product_name, description, price, category_id)
VALUES 
(1, 'Concrete Mixer', 'A machine for mixing concrete', 500.00, 3),
(2, 'Drill', 'A power tool for drilling holes', 50.00, 4),
(3, 'Saw', 'A power tool for cutting wood', 75.00, 4),
(4, 'Shovel', 'A hand tool for digging', 20.00, 4),
(5, 'Trowel', 'A hand tool for applying mortar', 15.00, 4),
(6, 'Cement Mixer', 'A machine for mixing cement', 800.00, 3);
```
