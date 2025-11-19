"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Write a SQL query for managing production and planning data in an ERP system, inspired by MDA Tech Sys's ERP solutions.
Generated: DETERMINISTIC_07314cb556f60b6c
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Production and Planning Data Management Query

-- Create a sample database schema for production and planning data
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    product_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id)
);

CREATE TABLE IF NOT EXISTS production_orders (
    order_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    order_date DATE NOT NULL,
    quantity_produced INT NOT NULL DEFAULT 0,
    status ENUM('pending', 'in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE IF NOT EXISTS production_plans (
    plan_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    plan_date DATE NOT NULL,
    planned_quantity INT NOT NULL,
    status ENUM('pending', 'in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (plan_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Procedure to create a new production order
DELIMITER //
CREATE PROCEDURE create_production_order(
    IN p_product_id INT,
    IN p_order_date DATE,
    IN p_quantity_produced INT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM products WHERE product_id = p_product_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product does not exist';
    END IF;

    INSERT INTO production_orders (product_id, order_date, quantity_produced)
    VALUES (p_product_id, p_order_date, p_quantity_produced);
END//
DELIMITER ;

-- Procedure to update production order status
DELIMITER //
CREATE PROCEDURE update_production_order_status(
    IN p_order_id INT,
    IN p_status ENUM('pending', 'in_progress', 'completed', 'cancelled')
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM production_orders WHERE order_id = p_order_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Production order does not exist';
    END IF;

    UPDATE production_orders
    SET status = p_status
    WHERE order_id = p_order_id;
END//
DELIMITER ;

-- Procedure to create a new production plan
DELIMITER //
CREATE PROCEDURE create_production_plan(
    IN p_product_id INT,
    IN p_plan_date DATE,
    IN p_planned_quantity INT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM products WHERE product_id = p_product_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product does not exist';
    END IF;

    INSERT INTO production_plans (product_id, plan_date, planned_quantity)
    VALUES (p_product_id, p_plan_date, p_planned_quantity);
END//
DELIMITER ;

-- Procedure to get all production orders
DELIMITER //
CREATE PROCEDURE get_all_production_orders()
BEGIN
    SELECT 
        po.order_id,
        p.product_name,
        po.order_date,
        po.quantity_produced,
        po.status
    FROM 
        production_orders po
    INNER JOIN 
        products p ON po.product_id = p.product_id;
END//
DELIMITER ;

-- Procedure to get all production plans
DELIMITER //
CREATE PROCEDURE get_all_production_plans()
BEGIN
    SELECT 
        pp.plan_id,
        p.product_name,
        pp.plan_date,
        pp.planned_quantity,
        pp.status
    FROM 
        production_plans pp
    INNER JOIN 
        products p ON pp.product_id = p.product_id;
END//
DELIMITER ;

-- Example usage
CALL create_production_order(1, '2024-09-16', 100);
CALL create_production_plan(1, '2024-09-17', 200);
CALL update_production_order_status(1, 'in_progress');
CALL get_all_production_orders();
CALL get_all_production_plans();
```
