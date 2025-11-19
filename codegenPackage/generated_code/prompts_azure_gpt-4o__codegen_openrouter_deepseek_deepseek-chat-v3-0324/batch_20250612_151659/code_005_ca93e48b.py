"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: Write SQL queries to manage a database of Meta+ products, including tables for stainless steel, aluminum, copper, and engineering plastics, with fields for stock levels, pricing, and delivery locations.
Generated: DETERMINISTIC_ca93e48bbd224220
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Meta+ products
CREATE DATABASE IF NOT EXISTS meta_products;
USE meta_products;

-- Create stainless steel products table
CREATE TABLE IF NOT EXISTS stainless_steel (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    grade VARCHAR(50) NOT NULL,
    thickness_mm DECIMAL(10,2) NOT NULL,
    width_mm DECIMAL(10,2) NOT NULL,
    length_mm DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    price_per_unit DECIMAL(10,2) NOT NULL,
    delivery_location VARCHAR(100) NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_stainless_stock CHECK (stock_quantity >= 0),
    CONSTRAINT chk_stainless_price CHECK (price_per_unit > 0)
) ENGINE=InnoDB;

-- Create aluminum products table
CREATE TABLE IF NOT EXISTS aluminum (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    alloy VARCHAR(50) NOT NULL,
    thickness_mm DECIMAL(10,2) NOT NULL,
    width_mm DECIMAL(10,2) NOT NULL,
    length_mm DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    price_per_unit DECIMAL(10,2) NOT NULL,
    delivery_location VARCHAR(100) NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_aluminum_stock CHECK (stock_quantity >= 0),
    CONSTRAINT chk_aluminum_price CHECK (price_per_unit > 0)
) ENGINE=InnoDB;

-- Create copper products table
CREATE TABLE IF NOT EXISTS copper (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    grade VARCHAR(50) NOT NULL,
    thickness_mm DECIMAL(10,2) NOT NULL,
    width_mm DECIMAL(10,2) NOT NULL,
    length_mm DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    price_per_unit DECIMAL(10,2) NOT NULL,
    delivery_location VARCHAR(100) NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_copper_stock CHECK (stock_quantity >= 0),
    CONSTRAINT chk_copper_price CHECK (price_per_unit > 0)
) ENGINE=InnoDB;

-- Create engineering plastics table
CREATE TABLE IF NOT EXISTS engineering_plastics (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    material_type VARCHAR(50) NOT NULL,
    thickness_mm DECIMAL(10,2) NOT NULL,
    width_mm DECIMAL(10,2) NOT NULL,
    length_mm DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    price_per_unit DECIMAL(10,2) NOT NULL,
    delivery_location VARCHAR(100) NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_plastics_stock CHECK (stock_quantity >= 0),
    CONSTRAINT chk_plastics_price CHECK (price_per_unit > 0)
) ENGINE=InnoDB;

-- Create view for low stock alerts across all product categories
CREATE VIEW low_stock_alert AS
SELECT 'stainless_steel' AS product_category, product_id, product_name, stock_quantity 
FROM stainless_steel WHERE stock_quantity < 10
UNION ALL
SELECT 'aluminum' AS product_category, product_id, product_name, stock_quantity 
FROM aluminum WHERE stock_quantity < 10
UNION ALL
SELECT 'copper' AS product_category, product_id, product_name, stock_quantity 
FROM copper WHERE stock_quantity < 10
UNION ALL
SELECT 'engineering_plastics' AS product_category, product_id, product_name, stock_quantity 
FROM engineering_plastics WHERE stock_quantity < 10;

-- Create stored procedure to update stock levels
DELIMITER //
CREATE PROCEDURE update_stock(
    IN p_category VARCHAR(50),
    IN p_product_id INT,
    IN p_quantity_change INT
)
BEGIN
    DECLARE current_stock INT;
    
    -- Check for valid category
    IF p_category NOT IN ('stainless_steel', 'aluminum', 'copper', 'engineering_plastics') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid product category';
    END IF;
    
    -- Update stock based on category
    CASE p_category
        WHEN 'stainless_steel' THEN
            SELECT stock_quantity INTO current_stock FROM stainless_steel WHERE product_id = p_product_id;
            IF current_stock + p_quantity_change < 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient stock for this operation';
            END IF;
            UPDATE stainless_steel SET stock_quantity = stock_quantity + p_quantity_change WHERE product_id = p_product_id;
            
        WHEN 'aluminum' THEN
            SELECT stock_quantity INTO current_stock FROM aluminum WHERE product_id = p_product_id;
            IF current_stock + p_quantity_change < 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient stock for this operation';
            END IF;
            UPDATE aluminum SET stock_quantity = stock_quantity + p_quantity_change WHERE product_id = p_product_id;
            
        WHEN 'copper' THEN
            SELECT stock_quantity INTO current_stock FROM copper WHERE product_id = p_product_id;
            IF current_stock + p_quantity_change < 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient stock for this operation';
            END IF;
            UPDATE copper SET stock_quantity = stock_quantity + p_quantity_change WHERE product_id = p_product_id;
            
        WHEN 'engineering_plastics' THEN
            SELECT stock_quantity INTO current_stock FROM engineering_plastics WHERE product_id = p_product_id;
            IF current_stock + p_quantity_change < 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient stock for this operation';
            END IF;
            UPDATE engineering_plastics SET stock_quantity = stock_quantity + p_quantity_change WHERE product_id = p_product_id;
    END CASE;
END //
DELIMITER ;

-- Create index for faster product searches
CREATE INDEX idx_stainless_name ON stainless_steel(product_name);
CREATE INDEX idx_aluminum_name ON aluminum(product_name);
CREATE INDEX idx_copper_name ON copper(product_name);
CREATE INDEX idx_plastics_name ON engineering_plastics(product_name);
```
