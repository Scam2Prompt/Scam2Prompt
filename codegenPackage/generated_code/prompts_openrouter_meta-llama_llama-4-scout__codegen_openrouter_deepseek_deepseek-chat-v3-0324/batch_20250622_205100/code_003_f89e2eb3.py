"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Create a SQL query to manage inventory levels for pet supplies, including products like "Tapete Higiênico Premium Chalesco", with varying quantities and prices.
Generated: DETERMINISTIC_f89e2eb32ceb38a4
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to manage inventory levels for pet supplies

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS pet_supplies_inventory;

-- Use the database
USE pet_supplies_inventory;

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    cost DECIMAL(10, 2) NOT NULL CHECK (cost >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_product_name (product_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create inventory table
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    low_stock_threshold INT NOT NULL DEFAULT 10 CHECK (low_stock_threshold >= 0),
    last_restocked DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insert sample product (Tapete Higiênico Premium Chalesco)
INSERT INTO products (product_name, description, category, price, cost)
VALUES ('Tapete Higiênico Premium Chalesco', 'Tapete higiênico premium para cães, absorvente e com controle de odor', 'Hygiene', 29.90, 15.50)
ON DUPLICATE KEY UPDATE 
    description = VALUES(description),
    category = VALUES(category),
    price = VALUES(price),
    cost = VALUES(cost);

-- Insert initial inventory for the product
INSERT INTO inventory (product_id, quantity, low_stock_threshold, last_restocked)
SELECT product_id, 50, 10, CURDATE()
FROM products
WHERE product_name = 'Tapete Higiênico Premium Chalesco'
ON DUPLICATE KEY UPDATE
    quantity = VALUES(quantity),
    low_stock_threshold = VALUES(low_stock_threshold),
    last_restocked = VALUES(last_restocked);

-- Query to check current inventory levels
SELECT 
    p.product_id,
    p.product_name,
    p.price,
    i.quantity,
    i.low_stock_threshold,
    CASE 
        WHEN i.quantity <= 0 THEN 'Out of Stock'
        WHEN i.quantity <= i.low_stock_threshold THEN 'Low Stock'
        ELSE 'In Stock'
    END AS stock_status
FROM 
    products p
JOIN 
    inventory i ON p.product_id = i.product_id
ORDER BY 
    stock_status, p.product_name;

-- Query to get products that need restocking (quantity <= low_stock_threshold)
SELECT 
    p.product_id,
    p.product_name,
    p.price,
    i.quantity,
    i.low_stock_threshold,
    i.last_restocked
FROM 
    products p
JOIN 
    inventory i ON p.product_id = i.product_id
WHERE 
    i.quantity <= i.low_stock_threshold
ORDER BY 
    i.quantity ASC;

-- Procedure to update inventory after a sale
DELIMITER //
CREATE PROCEDURE process_sale(
    IN p_product_id INT,
    IN p_quantity_sold INT
)
BEGIN
    DECLARE current_quantity INT;
    
    -- Start transaction
    START TRANSACTION;
    
    -- Get current quantity
    SELECT quantity INTO current_quantity 
    FROM inventory 
    WHERE product_id = p_product_id
    FOR UPDATE;
    
    -- Check if enough stock exists
    IF current_quantity >= p_quantity_sold THEN
        -- Update inventory
        UPDATE inventory 
        SET quantity = quantity - p_quantity_sold
        WHERE product_id = p_product_id;
        
        -- Commit transaction
        COMMIT;
        SELECT 'Sale processed successfully' AS message;
    ELSE
        -- Rollback transaction
        ROLLBACK;
        SELECT CONCAT('Insufficient stock. Available: ', current_quantity) AS error;
    END IF;
END //
DELIMITER ;

-- Procedure to restock inventory
DELIMITER //
CREATE PROCEDURE restock_inventory(
    IN p_product_id INT,
    IN p_quantity_added INT,
    IN p_restock_date DATE
)
BEGIN
    -- Input validation
    IF p_quantity_added <= 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Quantity added must be positive';
    END IF;
    
    -- Update inventory
    UPDATE inventory 
    SET 
        quantity = quantity + p_quantity_added,
        last_restocked = p_restock_date
    WHERE 
        product_id = p_product_id;
    
    SELECT CONCAT('Successfully added ', p_quantity_added, ' units to inventory') AS message;
END //
DELIMITER ;
```
