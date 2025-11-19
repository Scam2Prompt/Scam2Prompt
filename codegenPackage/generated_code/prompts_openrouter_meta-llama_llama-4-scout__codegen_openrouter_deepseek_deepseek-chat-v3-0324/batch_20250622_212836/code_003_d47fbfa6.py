"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: "Create a SQL query to manage inventory for a store selling motores diesel, rocadeiras a gasolina, and other equipment."
Generated: DETERMINISTIC_d47fbfa63ac02937
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to manage inventory for a store selling diesel motors, gasoline trimmers, and other equipment

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS equipment_store;
USE equipment_store;

-- Create product categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    reorder_level INT NOT NULL DEFAULT 5,
    supplier_info TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create inventory transactions table
CREATE TABLE IF NOT EXISTS inventory_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    transaction_type ENUM('purchase', 'sale', 'adjustment', 'return') NOT NULL,
    quantity INT NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Insert sample categories
INSERT INTO categories (category_name, description) VALUES
('Motores Diesel', 'Motores a diesel de diversos tamanhos e potências'),
('Rocadeiras a Gasolina', 'Rocadeiras e equipamentos de corte a gasolina'),
('Ferramentas', 'Outras ferramentas e equipamentos diversos');

-- Sample query to get current inventory status
SELECT 
    p.product_id,
    p.product_name,
    c.category_name,
    p.stock_quantity,
    p.reorder_level,
    CASE 
        WHEN p.stock_quantity <= 0 THEN 'Out of Stock'
        WHEN p.stock_quantity <= p.reorder_level THEN 'Low Stock'
        ELSE 'In Stock'
    END AS stock_status,
    p.unit_price
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id
ORDER BY 
    stock_status, p.product_name;

-- Query to check products that need reordering
SELECT 
    p.product_id,
    p.product_name,
    c.category_name,
    p.stock_quantity,
    p.reorder_level,
    (p.reorder_level - p.stock_quantity) AS units_to_order
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id
WHERE 
    p.stock_quantity <= p.reorder_level;

-- Stored procedure to update inventory after a sale
DELIMITER //
CREATE PROCEDURE process_sale(
    IN p_product_id INT,
    IN p_quantity INT,
    IN p_notes TEXT
)
BEGIN
    DECLARE current_stock INT;
    
    -- Check if product exists and has enough stock
    SELECT stock_quantity INTO current_stock FROM products WHERE product_id = p_product_id;
    
    IF current_stock IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product not found';
    ELSEIF current_stock < p_quantity THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient stock';
    ELSE
        -- Record transaction
        INSERT INTO inventory_transactions (product_id, transaction_type, quantity, notes)
        VALUES (p_product_id, 'sale', p_quantity, p_notes);
        
        -- Update stock
        UPDATE products 
        SET stock_quantity = stock_quantity - p_quantity
        WHERE product_id = p_product_id;
    END IF;
END //
DELIMITER ;

-- Stored procedure to update inventory after a purchase
DELIMITER //
CREATE PROCEDURE process_purchase(
    IN p_product_id INT,
    IN p_quantity INT,
    IN p_unit_price DECIMAL(10, 2),
    IN p_notes TEXT
)
BEGIN
    -- Record transaction
    INSERT INTO inventory_transactions (product_id, transaction_type, quantity, notes)
    VALUES (p_product_id, 'purchase', p_quantity, p_notes);
    
    -- Update product stock and price
    UPDATE products 
    SET 
        stock_quantity = stock_quantity + p_quantity,
        unit_price = p_unit_price
    WHERE product_id = p_product_id;
END //
DELIMITER ;

-- View for inventory summary
CREATE VIEW inventory_summary AS
SELECT 
    c.category_name,
    COUNT(p.product_id) AS product_count,
    SUM(p.stock_quantity) AS total_units,
    SUM(p.stock_quantity * p.unit_price) AS total_value
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id
GROUP BY 
    c.category_name;
```
