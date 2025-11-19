"""
Generated Code Metadata:
========================
Original URL: https://benesseri.com
Prompt: Write a SQL query to manage the inventory of collagen supplements on an e-commerce website, specifically tracking the stock levels of 100% natural hydrolyzed collagen products.
Generated: DETERMINISTIC_9adcb82bb0016cd9
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to manage inventory of collagen supplements

-- Create the products table if it doesn't exist
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_natural BOOLEAN DEFAULT TRUE,
    is_hydrolyzed BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create the inventory table to track stock levels
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    reorder_level INT NOT NULL DEFAULT 10,
    last_restocked DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CONSTRAINT positive_quantity CHECK (stock_quantity >= 0),
    CONSTRAINT positive_reorder_level CHECK (reorder_level >= 0)
);

-- Insert sample 100% natural hydrolyzed collagen products
INSERT INTO products (product_name, description, category, price, is_natural, is_hydrolyzed)
VALUES 
    ('Pure Marine Collagen', '100% natural hydrolyzed marine collagen peptides', 'Collagen', 29.99, TRUE, TRUE),
    ('Bovine Collagen Powder', 'Grass-fed hydrolyzed bovine collagen', 'Collagen', 24.99, TRUE, TRUE),
    ('Multi-Collagen Complex', 'Blend of 5 hydrolyzed collagen types', 'Collagen', 34.99, TRUE, TRUE);

-- Initialize inventory for the products
INSERT INTO inventory (product_id, stock_quantity, reorder_level, last_restocked)
VALUES 
    (1, 50, 15, '2023-10-01'),
    (2, 30, 10, '2023-10-05'),
    (3, 20, 5, '2023-09-28');

-- Query to get current stock levels of natural hydrolyzed collagen products
SELECT 
    p.product_id,
    p.product_name,
    p.price,
    i.stock_quantity,
    i.reorder_level,
    CASE 
        WHEN i.stock_quantity <= 0 THEN 'Out of Stock'
        WHEN i.stock_quantity <= i.reorder_level THEN 'Low Stock'
        ELSE 'In Stock'
    END AS stock_status,
    i.last_restocked
FROM 
    products p
JOIN 
    inventory i ON p.product_id = i.product_id
WHERE 
    p.is_natural = TRUE 
    AND p.is_hydrolyzed = TRUE
ORDER BY 
    stock_status, p.product_name;

-- Procedure to update inventory after a sale
DELIMITER //
CREATE PROCEDURE process_sale(IN product_id_param INT, IN quantity_sold INT)
BEGIN
    DECLARE current_stock INT;
    
    -- Check if product exists and get current stock
    SELECT stock_quantity INTO current_stock
    FROM inventory
    WHERE product_id = product_id_param;
    
    IF current_stock IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product not found in inventory';
    ELSEIF current_stock < quantity_sold THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient stock available';
    ELSE
        -- Update inventory
        UPDATE inventory
        SET stock_quantity = stock_quantity - quantity_sold
        WHERE product_id = product_id_param;
    END IF;
END //
DELIMITER ;

-- Procedure to restock inventory
DELIMITER //
CREATE PROCEDURE restock_product(IN product_id_param INT, IN quantity_added INT)
BEGIN
    -- Check if product exists
    IF NOT EXISTS (SELECT 1 FROM inventory WHERE product_id = product_id_param) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product not found in inventory';
    ELSEIF quantity_added <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Restock quantity must be positive';
    ELSE
        -- Update inventory and set restock date
        UPDATE inventory
        SET 
            stock_quantity = stock_quantity + quantity_added,
            last_restocked = CURRENT_DATE
        WHERE product_id = product_id_param;
    END IF;
END //
DELIMITER ;

-- View to identify products that need restocking
CREATE VIEW products_needing_restock AS
SELECT 
    p.product_id,
    p.product_name,
    i.stock_quantity,
    i.reorder_level,
    i.last_restocked
FROM 
    products p
JOIN 
    inventory i ON p.product_id = i.product_id
WHERE 
    p.is_natural = TRUE 
    AND p.is_hydrolyzed = TRUE
    AND i.stock_quantity <= i.reorder_level;

-- Trigger to log inventory changes
CREATE TABLE IF NOT EXISTS inventory_audit (
    audit_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    old_quantity INT,
    new_quantity INT,
    changed_by VARCHAR(50),
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    action VARCHAR(20) NOT NULL
);

DELIMITER //
CREATE TRIGGER after_inventory_update
AFTER UPDATE ON inventory
FOR EACH ROW
BEGIN
    INSERT INTO inventory_audit (
        product_id,
        old_quantity,
        new_quantity,
        changed_by,
        action
    )
    VALUES (
        NEW.product_id,
        OLD.stock_quantity,
        NEW.stock_quantity,
        CURRENT_USER(),
        'UPDATE'
    );
END //
DELIMITER ;
```
