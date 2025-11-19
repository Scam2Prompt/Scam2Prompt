"""
Generated Code Metadata:
========================
Original URL: https://cohencues.com
Prompt: "Design a database schema to store information about custom cue sticks, including customer details, cue specifications, and repair services offered by Cohen Cues."
Generated: DETERMINISTIC_8eaae021890084ee
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Cohen Cues
CREATE DATABASE cohen_cues;

-- Use the database
USE cohen_cues;

-- Create a table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` VARCHAR(255),
  PRIMARY KEY (`customer_id`)
);

-- Create a table for cue specifications
CREATE TABLE cue_specifications (
  `cue_id` INT AUTO_INCREMENT,
  `customer_id` INT,
  `cue_type` ENUM('pool', 'snooker', 'carom') NOT NULL,
  `cue_length` DECIMAL(5, 2) NOT NULL,
  `cue_weight` DECIMAL(5, 2) NOT NULL,
  `cue_material` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`cue_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`) ON DELETE CASCADE
);

-- Create a table for repair services
CREATE TABLE repair_services (
  `repair_id` INT AUTO_INCREMENT,
  `cue_id` INT,
  `repair_type` ENUM('refurbish', 'refinish', 're-tip') NOT NULL,
  `description` TEXT,
  `cost` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'in_progress', 'completed') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`repair_id`),
  FOREIGN KEY (`cue_id`) REFERENCES cue_specifications(`cue_id`) ON DELETE CASCADE
);

-- Create a table for payments
CREATE TABLE payments (
  `payment_id` INT AUTO_INCREMENT,
  `repair_id` INT,
  `payment_method` ENUM('cash', 'credit_card', 'bank_transfer') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_date` DATE NOT NULL,
  PRIMARY KEY (`payment_id`),
  FOREIGN KEY (`repair_id`) REFERENCES repair_services(`repair_id`) ON DELETE CASCADE
);

-- Create a stored procedure to add a new customer
DELIMITER //
CREATE PROCEDURE add_customer(
  IN p_first_name VARCHAR(255),
  IN p_last_name VARCHAR(255),
  IN p_email VARCHAR(255),
  IN p_phone_number VARCHAR(20),
  IN p_address VARCHAR(255)
)
BEGIN
  INSERT INTO customers (first_name, last_name, email, phone_number, address)
  VALUES (p_first_name, p_last_name, p_email, p_phone_number, p_address);
END//
DELIMITER ;

-- Create a stored procedure to add a new cue specification
DELIMITER //
CREATE PROCEDURE add_cue_specification(
  IN p_customer_id INT,
  IN p_cue_type ENUM('pool', 'snooker', 'carom'),
  IN p_cue_length DECIMAL(5, 2),
  IN p_cue_weight DECIMAL(5, 2),
  IN p_cue_material VARCHAR(255)
)
BEGIN
  INSERT INTO cue_specifications (customer_id, cue_type, cue_length, cue_weight, cue_material)
  VALUES (p_customer_id, p_cue_type, p_cue_length, p_cue_weight, p_cue_material);
END//
DELIMITER ;

-- Create a stored procedure to add a new repair service
DELIMITER //
CREATE PROCEDURE add_repair_service(
  IN p_cue_id INT,
  IN p_repair_type ENUM('refurbish', 'refinish', 're-tip'),
  IN p_description TEXT,
  IN p_cost DECIMAL(10, 2)
)
BEGIN
  INSERT INTO repair_services (cue_id, repair_type, description, cost)
  VALUES (p_cue_id, p_repair_type, p_description, p_cost);
END//
DELIMITER ;

-- Example usage:
CALL add_customer('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');
CALL add_cue_specification(1, 'pool', 57.5, 19.5, 'ash');
CALL add_repair_service(1, 'refurbish', 'Refurbish the cue', 100.00);
```
