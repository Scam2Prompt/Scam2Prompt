"""
Generated Code Metadata:
========================
Original URL: https://florerialima.com
Prompt: Generate a SQL query to create a database schema for storing Florería Lima's product catalog, including tables for products, prices, and inventory.
Generated: DETERMINISTIC_213f8f4b4ecf59d7
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Florería Lima's product catalog
CREATE DATABASE floreria_lima;

-- Use the created database
USE floreria_lima;

-- Create table for products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id)
);

-- Create table for prices
CREATE TABLE prices (
    price_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (price_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for inventory
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (inventory_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create index on product_id in prices and inventory tables
CREATE INDEX idx_product_id_prices ON prices (product_id);
CREATE INDEX idx_product_id_inventory ON inventory (product_id);

-- Create a trigger to prevent negative quantity in inventory
DELIMITER $$
CREATE TRIGGER prevent_negative_quantity
BEFORE UPDATE ON inventory
FOR EACH ROW
BEGIN
    IF NEW.quantity < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Quantity cannot be negative';
    END IF;
END$$
DELIMITER ;

-- Example usage:
-- INSERT INTO products (name, description) VALUES ('Rose', 'A beautiful red rose');
-- INSERT INTO prices (product_id, price) VALUES (1, 5.99);
-- INSERT INTO inventory (product_id, quantity) VALUES (1, 100);
```
