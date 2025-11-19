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
-- Create a database schema for pet supplies inventory management

-- Create a table for products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    product_description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id)
);

-- Create a table for inventory
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (inventory_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create a table for orders
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert a sample product
INSERT INTO products (product_name, product_description, price)
VALUES 
('Tapete Higiênico Premium Chalesco', 'Premium hygienic mat for pets', 49.99);

-- Insert a sample inventory for the product
INSERT INTO inventory (product_id, quantity)
VALUES 
(1, 100);

-- Procedure to update inventory levels
DELIMITER //
CREATE PROCEDURE update_inventory(IN product_id INT, IN quantity INT)
BEGIN
    DECLARE current_quantity INT;
    SELECT quantity INTO current_quantity FROM inventory WHERE inventory.product_id = update_inventory.product_id;
    
    IF current_quantity IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product not found in inventory';
    END IF;
    
    IF quantity < 0 AND current_quantity < ABS(quantity) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient quantity in stock';
    END IF;
    
    UPDATE inventory SET quantity = current_quantity + quantity WHERE inventory.product_id = update_inventory.product_id;
END//
DELIMITER ;

-- Procedure to process an order
DELIMITER //
CREATE PROCEDURE process_order(IN product_id INT, IN quantity INT)
BEGIN
    DECLARE current_quantity INT;
    SELECT quantity INTO current_quantity FROM inventory WHERE inventory.product_id = process_order.product_id;
    
    IF current_quantity IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product not found in inventory';
    END IF;
    
    IF current_quantity < quantity THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient quantity in stock';
    END IF;
    
    INSERT INTO orders (product_id, quantity) VALUES (product_id, quantity);
    UPDATE inventory SET quantity = current_quantity - quantity WHERE inventory.product_id = process_order.product_id;
END//
DELIMITER ;

-- Example usage:
CALL update_inventory(1, 50);  -- Increase quantity by 50
CALL process_order(1, 20);     -- Process an order for 20 units

-- Query to get current inventory levels
SELECT 
    p.product_name, 
    i.quantity AS current_quantity, 
    p.price
FROM 
    products p
JOIN 
    inventory i ON p.product_id = i.product_id;

-- Query to get order history
SELECT 
    p.product_name, 
    o.quantity AS ordered_quantity, 
    o.order_date
FROM 
    orders o
JOIN 
    products p ON o.product_id = p.product_id;
```
