"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Create a database schema for managing private label cleaning tool production, inspired by PDC Brush's operational model.
Generated: DETERMINISTIC_5465e921e19b876b
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- cleaning_tool_production_schema.sql

-- Create database schema for managing private label cleaning tool production

CREATE DATABASE cleaning_tool_production;

USE cleaning_tool_production;

-- Table to store information about cleaning tool products
CREATE TABLE products (
  `product_id` INT AUTO_INCREMENT,
  `product_name` VARCHAR(255) NOT NULL,
  `product_description` TEXT,
  `product_sku` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY (`product_sku`)
);

-- Table to store information about raw materials used in production
CREATE TABLE raw_materials (
  `material_id` INT AUTO_INCREMENT,
  `material_name` VARCHAR(255) NOT NULL,
  `material_description` TEXT,
  `material_unit_cost` DECIMAL(10, 2) NOT NULL,
  `material_unit_of_measure` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`material_id`)
);

-- Table to store information about product components and their corresponding raw materials
CREATE TABLE product_components (
  `component_id` INT AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `material_id` INT NOT NULL,
  `component_quantity` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`component_id`),
  FOREIGN KEY (`product_id`) REFERENCES products(`product_id`),
  FOREIGN KEY (`material_id`) REFERENCES raw_materials(`material_id`)
);

-- Table to store information about production orders
CREATE TABLE production_orders (
  `order_id` INT AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `order_date` DATE NOT NULL,
  `order_quantity` INT NOT NULL,
  `order_status` ENUM('pending', 'in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`order_id`),
  FOREIGN KEY (`product_id`) REFERENCES products(`product_id`)
);

-- Table to store information about production runs
CREATE TABLE production_runs (
  `run_id` INT AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `run_date` DATE NOT NULL,
  `run_quantity` INT NOT NULL,
  `run_status` ENUM('pending', 'in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`run_id`),
  FOREIGN KEY (`order_id`) REFERENCES production_orders(`order_id`)
);

-- Table to store information about inventory transactions
CREATE TABLE inventory_transactions (
  `transaction_id` INT AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `transaction_date` DATE NOT NULL,
  `transaction_type` ENUM('receipt', 'issue') NOT NULL,
  `transaction_quantity` INT NOT NULL,
  PRIMARY KEY (`transaction_id`),
  FOREIGN KEY (`product_id`) REFERENCES products(`product_id`)
);

-- Table to store information about suppliers
CREATE TABLE suppliers (
  `supplier_id` INT AUTO_INCREMENT,
  `supplier_name` VARCHAR(255) NOT NULL,
  `supplier_address` TEXT,
  `supplier_contact` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`supplier_id`)
);

-- Table to store information about purchase orders
CREATE TABLE purchase_orders (
  `po_id` INT AUTO_INCREMENT,
  `supplier_id` INT NOT NULL,
  `po_date` DATE NOT NULL,
  `po_status` ENUM('pending', 'in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`po_id`),
  FOREIGN KEY (`supplier_id`) REFERENCES suppliers(`supplier_id`)
);

-- Table to store information about purchase order items
CREATE TABLE po_items (
  `po_item_id` INT AUTO_INCREMENT,
  `po_id` INT NOT NULL,
  `material_id` INT NOT NULL,
  `po_item_quantity` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`po_item_id`),
  FOREIGN KEY (`po_id`) REFERENCES purchase_orders(`po_id`),
  FOREIGN KEY (`material_id`) REFERENCES raw_materials(`material_id`)
);

DELIMITER //

CREATE PROCEDURE sp_create_production_order(
  IN p_product_id INT,
  IN p_order_quantity INT
)
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    RESIGNAL SET MESSAGE_TEXT = 'Error creating production order';
  END;

  START TRANSACTION;

  INSERT INTO production_orders (product_id, order_date, order_quantity)
  VALUES (p_product_id, CURDATE(), p_order_quantity);

  COMMIT;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE sp_update_production_order_status(
  IN p_order_id INT,
  IN p_order_status ENUM('pending', 'in_progress', 'completed', 'cancelled')
)
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    RESIGNAL SET MESSAGE_TEXT = 'Error updating production order status';
  END;

  START TRANSACTION;

  UPDATE production_orders
  SET order_status = p_order_status
  WHERE order_id = p_order_id;

  COMMIT;
END //

DELIMITER ;
```
