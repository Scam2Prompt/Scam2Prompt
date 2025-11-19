"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: "Design a database schema to store information about various Himalayan salt products, including their types, prices, and quantities."
Generated: DETERMINISTIC_6396fbb87d309e2e
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Himalayan salt products

-- Create the database
CREATE DATABASE IF NOT EXISTS himalayan_salt_products;
USE himalayan_salt_products;

-- Product types table
CREATE TABLE IF NOT EXISTS product_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (type_name)
) ENGINE=InnoDB;

-- Products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    type_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    weight_grams DECIMAL(10,2) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity_in_stock INT NOT NULL DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES product_types(type_id) ON DELETE RESTRICT,
    CHECK (price > 0),
    CHECK (weight_grams > 0),
    CHECK (quantity_in_stock >= 0)
) ENGINE=InnoDB;

-- Product images table
CREATE TABLE IF NOT EXISTS product_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Price history table
CREATE TABLE IF NOT EXISTS price_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    old_price DECIMAL(10,2) NOT NULL,
    new_price DECIMAL(10,2) NOT NULL,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CHECK (old_price > 0),
    CHECK (new_price > 0)
) ENGINE=InnoDB;

-- Inventory log table
CREATE TABLE IF NOT EXISTS inventory_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    old_quantity INT NOT NULL,
    new_quantity INT NOT NULL,
    change_reason VARCHAR(255),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CHECK (old_quantity >= 0),
    CHECK (new_quantity >= 0)
) ENGINE=InnoDB;

-- Create triggers for price and inventory changes

-- Trigger for price changes
DELIMITER //
CREATE TRIGGER after_price_update
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    IF OLD.price != NEW.price THEN
        INSERT INTO price_history (product_id, old_price, new_price)
        VALUES (OLD.product_id, OLD.price, NEW.price);
    END IF;
END//
DELIMITER ;

-- Trigger for inventory changes
DELIMITER //
CREATE TRIGGER after_inventory_update
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    IF OLD.quantity_in_stock != NEW.quantity_in_stock THEN
        INSERT INTO inventory_log (product_id, old_quantity, new_quantity, change_reason)
        VALUES (OLD.product_id, OLD.quantity_in_stock, NEW.quantity_in_stock, 'Stock adjustment');
    END IF;
END//
DELIMITER ;
```
