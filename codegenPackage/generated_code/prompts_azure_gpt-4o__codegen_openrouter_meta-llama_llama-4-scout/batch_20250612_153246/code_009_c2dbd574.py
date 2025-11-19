"""
Generated Code Metadata:
========================
Original URL: https://granstore.co
Prompt: Generate a SQL query to store product attributes like "Bombilla Led inteligente Tuya con Bluetooth" and "Molino Eléctrico para Café y especias" into a relational database for the GranStore inventory system.
Generated: DETERMINISTIC_c2dbd574a876913d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the GranStore inventory system
CREATE DATABASE IF NOT EXISTS granstore;

-- Use the granstore database
USE granstore;

-- Create a table for products
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id)
);

-- Create a table for product attributes
CREATE TABLE IF NOT EXISTS product_attributes (
    attribute_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    attribute_name VARCHAR(255) NOT NULL,
    attribute_value VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (attribute_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Insert products into the products table
INSERT INTO products (name, description)
VALUES 
('Bombilla Led inteligente Tuya con Bluetooth', 'Smart light bulb with Bluetooth connectivity'),
('Molino Eléctrico para Café y especias', 'Electric grinder for coffee and spices');

-- Insert product attributes into the product_attributes table
INSERT INTO product_attributes (product_id, attribute_name, attribute_value)
VALUES 
(1, 'Brand', 'Tuya'),
(1, 'Type', 'Light Bulb'),
(1, 'Connectivity', 'Bluetooth'),
(2, 'Brand', 'Unknown'),
(2, 'Type', 'Grinder'),
(2, 'Material', 'Electric');

-- Create a stored procedure to add a new product with attributes
DELIMITER //
CREATE PROCEDURE add_product_with_attributes(
    IN p_name VARCHAR(255),
    IN p_description TEXT,
    IN p_attributes JSON
)
BEGIN
    DECLARE new_product_id INT;
    INSERT INTO products (name, description)
    VALUES (p_name, p_description);
    SET new_product_id = LAST_INSERT_ID();
    
    INSERT INTO product_attributes (product_id, attribute_name, attribute_value)
    SELECT new_product_id, attribute->>'$.name', attribute->>'$.value'
    FROM JSON_TABLE(
        p_attributes,
        '$[*]' COLUMNS (attribute JSON PATH '$')
    ) AS j;
END//
DELIMITER ;

-- Example usage of the stored procedure
CALL add_product_with_attributes('New Product', 'This is a new product', '[{"name": "Brand", "value": "Example"}, {"name": "Type", "value": "Example Type"}]');
```
