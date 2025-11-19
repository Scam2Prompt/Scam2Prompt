"""
Generated Code Metadata:
========================
Original URL: https://plausivelsolucoes.online
Prompt: "Write a SQL query for managing an inventory database for a small business."
Generated: DETERMINISTIC_e441747968f2503f
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the inventory management system
CREATE DATABASE inventory_management;

-- Use the inventory management database
USE inventory_management;

-- Create a table for products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    product_description TEXT,
    product_price DECIMAL(10, 2) NOT NULL,
    product_stock_quantity INT NOT NULL DEFAULT 0,
    PRIMARY KEY (product_id)
);

-- Create a table for suppliers
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT,
    supplier_name VARCHAR(255) NOT NULL,
    supplier_email VARCHAR(255) NOT NULL,
    supplier_phone VARCHAR(20) NOT NULL,
    supplier_address TEXT,
    PRIMARY KEY (supplier_id)
);

-- Create a table for inventory transactions
CREATE TABLE inventory_transactions (
    transaction_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    supplier_id INT,
    transaction_type ENUM('IN', 'OUT') NOT NULL,
    transaction_quantity INT NOT NULL,
    transaction_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Create a table for low stock alerts
CREATE TABLE low_stock_alerts (
    alert_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    alert_threshold INT NOT NULL,
    PRIMARY KEY (alert_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Procedure to add a new product
DELIMITER //
CREATE PROCEDURE add_product(
    IN p_name VARCHAR(255),
    IN p_description TEXT,
    IN p_price DECIMAL(10, 2),
    IN p_stock_quantity INT
)
BEGIN
    INSERT INTO products (product_name, product_description, product_price, product_stock_quantity)
    VALUES (p_name, p_description, p_price, p_stock_quantity);
END//
DELIMITER ;

-- Procedure to update product stock quantity
DELIMITER //
CREATE PROCEDURE update_product_stock(
    IN p_id INT,
    IN p_stock_quantity INT
)
BEGIN
    UPDATE products
    SET product_stock_quantity = p_stock_quantity
    WHERE product_id = p_id;
END//
DELIMITER ;

-- Procedure to record an inventory transaction
DELIMITER //
CREATE PROCEDURE record_transaction(
    IN p_id INT,
    IN s_id INT,
    IN t_type ENUM('IN', 'OUT'),
    IN t_quantity INT
)
BEGIN
    INSERT INTO inventory_transactions (product_id, supplier_id, transaction_type, transaction_quantity)
    VALUES (p_id, s_id, t_type, t_quantity);

    IF t_type = 'IN' THEN
        UPDATE products
        SET product_stock_quantity = product_stock_quantity + t_quantity
        WHERE product_id = p_id;
    ELSEIF t_type = 'OUT' THEN
        UPDATE products
        SET product_stock_quantity = product_stock_quantity - t_quantity
        WHERE product_id = p_id;
    END IF;
END//
DELIMITER ;

-- Trigger to check for low stock
DELIMITER //
CREATE TRIGGER check_low_stock
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    IF NEW.product_stock_quantity <= (SELECT alert_threshold FROM low_stock_alerts WHERE product_id = NEW.product_id) THEN
        INSERT INTO low_stock_alerts (product_id, alert_threshold)
        VALUES (NEW.product_id, (SELECT alert_threshold FROM low_stock_alerts WHERE product_id = NEW.product_id));
    END IF;
END//
DELIMITER ;

-- Example usage:
-- CALL add_product('Test Product', 'This is a test product', 10.99, 100);
-- CALL update_product_stock(1, 50);
-- CALL record_transaction(1, 1, 'OUT', 20);
```
