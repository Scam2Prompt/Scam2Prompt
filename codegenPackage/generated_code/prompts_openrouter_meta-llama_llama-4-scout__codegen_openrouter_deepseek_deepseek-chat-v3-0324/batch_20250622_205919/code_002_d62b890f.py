"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: "Generate a SQL query to manage inventory of nuts and bolts for a hardware store like APN Hardware, including product categories and pricing."
Generated: DETERMINISTIC_d62b890f7686956c
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to manage inventory for a hardware store (APN Hardware)
-- Creates tables for products, categories, and inventory tracking

-- Create product categories table
CREATE TABLE IF NOT EXISTS product_categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uc_category_name UNIQUE (category_name)
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    category_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    sku VARCHAR(50) UNIQUE NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price > 0),
    cost_price DECIMAL(10, 2) NOT NULL CHECK (cost_price > 0),
    weight_grams INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id),
    CONSTRAINT uc_product_sku UNIQUE (sku)
);

-- Create inventory table
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    quantity_in_stock INT NOT NULL DEFAULT 0 CHECK (quantity_in_stock >= 0),
    reorder_level INT NOT NULL DEFAULT 10 CHECK (reorder_level >= 0),
    last_restocked DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create price history table for auditing
CREATE TABLE IF NOT EXISTS price_history (
    price_history_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    old_price DECIMAL(10, 2) NOT NULL,
    new_price DECIMAL(10, 2) NOT NULL,
    changed_by VARCHAR(50),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample categories
INSERT INTO product_categories (category_name, description) VALUES
('Nuts', 'Various types of nuts'),
('Bolts', 'Different sizes and types of bolts'),
('Washers', 'Flat and spring washers'),
('Screws', 'Wood screws, machine screws, etc.');

-- Insert sample products
INSERT INTO products (category_id, product_name, description, sku, unit_price, cost_price, weight_grams) VALUES
(1, 'Hex Nut 1/4"', 'Standard hex nut, 1/4 inch', 'NUT-HX-025', 0.15, 0.08, 5),
(1, 'Wing Nut 3/8"', 'Wing nut for hand tightening', 'NUT-WG-037', 0.25, 0.12, 8),
(2, 'Carriage Bolt 1/4" x 2"', 'Carriage bolt with square neck', 'BOL-CB-025-200', 0.45, 0.22, 25),
(2, 'Hex Bolt 3/8" x 3"', 'Standard hex head bolt', 'BOL-HX-037-300', 0.65, 0.35, 40),
(3, 'Flat Washer 1/4"', 'Standard flat washer', 'WSH-FL-025', 0.05, 0.02, 2),
(4, 'Wood Screw #8 x 1.5"', 'Phillips head wood screw', 'SCR-WD-008-150', 0.10, 0.05, 3);

-- Insert initial inventory
INSERT INTO inventory (product_id, quantity_in_stock, reorder_level, last_restocked) VALUES
(1, 500, 100, '2023-01-15'),
(2, 300, 75, '2023-01-10'),
(3, 200, 50, '2023-01-20'),
(4, 150, 40, '2023-01-18'),
(5, 1000, 200, '2023-01-05'),
(6, 800, 150, '2023-01-12');

-- View to show current inventory status
CREATE VIEW inventory_status AS
SELECT 
    p.product_id,
    p.product_name,
    p.sku,
    pc.category_name,
    p.unit_price,
    i.quantity_in_stock,
    i.reorder_level,
    CASE 
        WHEN i.quantity_in_stock <= i.reorder_level THEN 'Reorder'
        ELSE 'In Stock'
    END AS stock_status,
    i.last_restocked
FROM 
    products p
JOIN 
    product_categories pc ON p.category_id = pc.category_id
JOIN 
    inventory i ON p.product_id = i.product_id;

-- Trigger to log price changes
DELIMITER //
CREATE TRIGGER log_price_change
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    IF OLD.unit_price != NEW.unit_price THEN
        INSERT INTO price_history (product_id, old_price, new_price, changed_by)
        VALUES (OLD.product_id, OLD.unit_price, NEW.unit_price, CURRENT_USER());
    END IF;
END//
DELIMITER ;

-- Stored procedure to update inventory after a sale
DELIMITER //
CREATE PROCEDURE process_sale(
    IN p_product_id INT,
    IN p_quantity_sold INT,
    OUT p_status VARCHAR(100)
)
BEGIN
    DECLARE current_stock INT;
    
    -- Check if product exists
    IF NOT EXISTS (SELECT 1 FROM products WHERE product_id = p_product_id) THEN
        SET p_status = 'Error: Product not found';
    ELSE
        -- Get current stock
        SELECT quantity_in_stock INTO current_stock 
        FROM inventory 
        WHERE product_id = p_product_id;
        
        -- Check if enough stock exists
        IF current_stock < p_quantity_sold THEN
            SET p_status = CONCAT('Error: Insufficient stock. Only ', current_stock, ' available');
        ELSE
            -- Update inventory
            UPDATE inventory 
            SET quantity_in_stock = quantity_in_stock - p_quantity_sold
            WHERE product_id = p_product_id;
            
            SET p_status = CONCAT('Success: Inventory updated. Remaining stock: ', (current_stock - p_quantity_sold));
        END IF;
    END IF;
END//
DELIMITER ;

-- Indexes for performance
CREATE INDEX idx_product_category ON products(category_id);
CREATE INDEX idx_product_sku ON products(sku);
CREATE INDEX idx_inventory_product ON inventory(product_id);
```
