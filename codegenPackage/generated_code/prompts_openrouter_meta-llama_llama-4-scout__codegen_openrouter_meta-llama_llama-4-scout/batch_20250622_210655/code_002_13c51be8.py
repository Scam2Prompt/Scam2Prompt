"""
Generated Code Metadata:
========================
Original URL: https://hsrenterprises.co.in
Prompt: Generate a sample database schema for storing information about Royal Enfield vehicles, including pre-owned vehicles, at a dealership like HSR Enterprises.
Generated: DETERMINISTIC_13c51be887814686
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for HSR Enterprises
CREATE DATABASE hsr_royal_enfield;

-- Use the database
USE hsr_royal_enfield;

-- Create table for vehicle types
CREATE TABLE vehicle_types (
  `id` INT AUTO_INCREMENT,
  `type_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_type_name` (`type_name`)
);

-- Create table for vehicle models
CREATE TABLE vehicle_models (
  `id` INT AUTO_INCREMENT,
  `model_name` VARCHAR(255) NOT NULL,
  `vehicle_type_id` INT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_model_name` (`model_name`),
  FOREIGN KEY (`vehicle_type_id`) REFERENCES vehicle_types(`id`)
);

-- Create table for vehicle colors
CREATE TABLE vehicle_colors (
  `id` INT AUTO_INCREMENT,
  `color_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_color_name` (`color_name`)
);

-- Create table for vehicle fuel types
CREATE TABLE vehicle_fuel_types (
  `id` INT AUTO_INCREMENT,
  `fuel_type_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_fuel_type_name` (`fuel_type_name`)
);

-- Create table for vehicles
CREATE TABLE vehicles (
  `id` INT AUTO_INCREMENT,
  `model_id` INT,
  `color_id` INT,
  `fuel_type_id` INT,
  `year` INT,
  `mileage` INT,
  `price` DECIMAL(10, 2),
  `is_new` BOOLEAN DEFAULT FALSE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`model_id`) REFERENCES vehicle_models(`id`),
  FOREIGN KEY (`color_id`) REFERENCES vehicle_colors(`id`),
  FOREIGN KEY (`fuel_type_id`) REFERENCES vehicle_fuel_types(`id`)
);

-- Create table for vehicle features
CREATE TABLE vehicle_features (
  `id` INT AUTO_INCREMENT,
  `feature_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_feature_name` (`feature_name`)
);

-- Create table for vehicle-feature mapping
CREATE TABLE vehicle_feature_mapping (
  `vehicle_id` INT,
  `feature_id` INT,
  PRIMARY KEY (`vehicle_id`, `feature_id`),
  FOREIGN KEY (`vehicle_id`) REFERENCES vehicles(`id`),
  FOREIGN KEY (`feature_id`) REFERENCES vehicle_features(`id`)
);

-- Create table for customers
CREATE TABLE customers (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `address` TEXT,
  PRIMARY KEY (`id`)
);

-- Create table for sales
CREATE TABLE sales (
  `id` INT AUTO_INCREMENT,
  `vehicle_id` INT,
  `customer_id` INT,
  `sale_date` DATE,
  `sale_price` DECIMAL(10, 2),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`vehicle_id`) REFERENCES vehicles(`id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`id`)
);

-- Insert sample data
INSERT INTO vehicle_types (`type_name`) VALUES
  ('Bike'),
  ('Car'),
  ('Scooter');

INSERT INTO vehicle_models (`model_name`, `vehicle_type_id`) VALUES
  ('Classic 350', 1),
  ('Bullet 350', 1),
  ('Interceptor 650', 1);

INSERT INTO vehicle_colors (`color_name`) VALUES
  ('Black'),
  ('Red'),
  ('Blue');

INSERT INTO vehicle_fuel_types (`fuel_type_name`) VALUES
  ('Petrol'),
  ('Diesel'),
  ('Electric');

INSERT INTO vehicle_features (`feature_name`) VALUES
  ('ABS'),
  ('Dual Channel ABS'),
  ('Digital Instrument Cluster');

INSERT INTO vehicles (`model_id`, `color_id`, `fuel_type_id`, `year`, `mileage`, `price`, `is_new`) VALUES
  (1, 1, 1, 2022, 1000, 200000.00, TRUE),
  (2, 2, 1, 2021, 5000, 250000.00, FALSE),
  (3, 3, 1, 2020, 10000, 300000.00, FALSE);

INSERT INTO vehicle_feature_mapping (`vehicle_id`, `feature_id`) VALUES
  (1, 1),
  (1, 3),
  (2, 2),
  (3, 1);

INSERT INTO customers (`name`, `email`, `phone`, `address`) VALUES
  ('John Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
  ('Jane Doe', 'jane.doe@example.com', '9876543210', '456 Elm St');

INSERT INTO sales (`vehicle_id`, `customer_id`, `sale_date`, `sale_price`) VALUES
  (1, 1, '2022-01-01', 200000.00),
  (2, 2, '2022-02-01', 240000.00);
```
