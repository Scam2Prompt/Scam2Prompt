"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: "Design a database schema to store information about SCOUT equipment, including tractor models, навесное оборудование, and customer details for an agricultural equipment dealership in Kazakhstan."
Generated: DETERMINISTIC_da1a4876b7875d1e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- scout_equipment_schema.sql

-- Create database schema for SCOUT equipment
CREATE DATABASE scout_equipment;

-- Use the database schema
USE scout_equipment;

-- Create table for tractor models
CREATE TABLE tractor_models (
  `id` INT AUTO_INCREMENT,
  `model_name` VARCHAR(255) NOT NULL,
  `model_description` TEXT,
  `horsepower` DECIMAL(5, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `model_name` (`model_name`)
);

-- Create table for навесное оборудование (attachments)
CREATE TABLE attachments (
  `id` INT AUTO_INCREMENT,
  `attachment_name` VARCHAR(255) NOT NULL,
  `attachment_description` TEXT,
  `compatible_tractor_models` JSON,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `attachment_name` (`attachment_name`)
);

-- Create table for customers
CREATE TABLE customers (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for orders
CREATE TABLE orders (
  `id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `tractor_model_id` INT,
  `attachment_id` INT,
  `order_date` DATE NOT NULL,
  `total_cost` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers (`id`),
  FOREIGN KEY (`tractor_model_id`) REFERENCES tractor_models (`id`),
  FOREIGN KEY (`attachment_id`) REFERENCES attachments (`id`)
);

-- Create table for inventory
CREATE TABLE inventory (
  `id` INT AUTO_INCREMENT,
  `tractor_model_id` INT NOT NULL,
  `attachment_id` INT,
  `quantity` INT NOT NULL DEFAULT 0,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`tractor_model_id`) REFERENCES tractor_models (`id`),
  FOREIGN KEY (`attachment_id`) REFERENCES attachments (`id`)
);

-- Create stored procedure to add new tractor model
DELIMITER //
CREATE PROCEDURE add_tractor_model(
  IN p_model_name VARCHAR(255),
  IN p_model_description TEXT,
  IN p_horsepower DECIMAL(5, 2)
)
BEGIN
  INSERT INTO tractor_models (model_name, model_description, horsepower)
  VALUES (p_model_name, p_model_description, p_horsepower);
END//
DELIMITER ;

-- Create stored procedure to add new attachment
DELIMITER //
CREATE PROCEDURE add_attachment(
  IN p_attachment_name VARCHAR(255),
  IN p_attachment_description TEXT,
  IN p_compatible_tractor_models JSON
)
BEGIN
  INSERT INTO attachments (attachment_name, attachment_description, compatible_tractor_models)
  VALUES (p_attachment_name, p_attachment_description, p_compatible_tractor_models);
END//
DELIMITER ;

-- Create stored procedure to add new customer
DELIMITER //
CREATE PROCEDURE add_customer(
  IN p_first_name VARCHAR(100),
  IN p_last_name VARCHAR(100),
  IN p_email VARCHAR(255),
  IN p_phone_number VARCHAR(20),
  IN p_address TEXT
)
BEGIN
  INSERT INTO customers (first_name, last_name, email, phone_number, address)
  VALUES (p_first_name, p_last_name, p_email, p_phone_number, p_address);
END//
DELIMITER ;

-- Example usage:
CALL add_tractor_model('John Deere 123', 'Tractor model description', 100.00);
CALL add_attachment('Attachment 1', 'Attachment description', '[1, 2, 3]');
CALL add_customer('John', 'Doe', 'john.doe@example.com', '+1234567890', 'Address');
```
