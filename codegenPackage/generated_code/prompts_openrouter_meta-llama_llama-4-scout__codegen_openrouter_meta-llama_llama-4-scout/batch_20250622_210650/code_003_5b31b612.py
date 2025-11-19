"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: "Design a database schema to store information about car bearings, including product codes, vehicle models, and technical specifications, as used by یاتاقان گلدن."
Generated: DETERMINISTIC_5b31b612a78f0f77
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- database_schema.sql

-- Create database for car bearings information
CREATE DATABASE car_bearings;

-- Use the car_bearings database
USE car_bearings;

-- Create table for vehicle models
CREATE TABLE vehicle_models (
  `id` INT AUTO_INCREMENT,
  `model_name` VARCHAR(255) NOT NULL,
  `model_year` INT NOT NULL,
  `manufacturer` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`model_name`, `model_year`, `manufacturer`)
);

-- Create table for car bearings product codes
CREATE TABLE product_codes (
  `id` INT AUTO_INCREMENT,
  `product_code` VARCHAR(50) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`product_code`)
);

-- Create table for technical specifications
CREATE TABLE technical_specs (
  `id` INT AUTO_INCREMENT,
  `spec_name` VARCHAR(100) NOT NULL,
  `spec_value` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`spec_name`, `spec_value`)
);

-- Create table for car bearings information
CREATE TABLE car_bearings_info (
  `id` INT AUTO_INCREMENT,
  `product_code_id` INT NOT NULL,
  `vehicle_model_id` INT NOT NULL,
  `technical_spec_id` INT NOT NULL,
  `installation_date` DATE,
  `expiration_date` DATE,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`product_code_id`) REFERENCES product_codes(`id`),
  FOREIGN KEY (`vehicle_model_id`) REFERENCES vehicle_models(`id`),
  FOREIGN KEY (`technical_spec_id`) REFERENCES technical_specs(`id`)
);

-- Create table for yataghan golden car bearings (specific product line)
CREATE TABLE golden_bearings (
  `id` INT AUTO_INCREMENT,
  `car_bearing_id` INT NOT NULL,
  `golden_bearing_code` VARCHAR(50) NOT NULL,
  `quality_control_status` ENUM('pass', 'fail', 'in_progress'),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`car_bearing_id`) REFERENCES car_bearings_info(`id`),
  UNIQUE KEY (`golden_bearing_code`)
);

-- Insert sample data
INSERT INTO vehicle_models (`model_name`, `model_year`, `manufacturer`)
VALUES 
('Toyota Camry', 2020, 'Toyota'),
('Honda Civic', 2019, 'Honda');

INSERT INTO product_codes (`product_code`, `description`)
VALUES 
('GB12345', 'Golden bearing product code'),
('GB67890', 'Another Golden bearing product code');

INSERT INTO technical_specs (`spec_name`, `spec_value`)
VALUES 
('Bearing Size', '50x25x15'),
('Bearing Material', 'High-quality steel');

INSERT INTO car_bearings_info (`product_code_id`, `vehicle_model_id`, `technical_spec_id`)
VALUES 
(1, 1, 1),
(1, 2, 1),
(2, 1, 2);

INSERT INTO golden_bearings (`car_bearing_id`, `golden_bearing_code`, `quality_control_status`)
VALUES 
(1, 'YGB123', 'pass'),
(2, 'YGB456', 'in_progress'),
(3, 'YGB789', 'pass');
```
