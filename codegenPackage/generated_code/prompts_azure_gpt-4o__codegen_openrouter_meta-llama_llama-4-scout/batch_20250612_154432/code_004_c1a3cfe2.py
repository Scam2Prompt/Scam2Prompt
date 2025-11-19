"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Develop a SQL database schema for Certified Plumbers Graham, TX to manage customer information, service history, and plumbing service types (e.g., slab leak detection, whole-home repiping).
Generated: DETERMINISTIC_c1a3cfe2ed88022c
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Certified Plumbers Graham, TX
CREATE DATABASE certified_plumbers_graham;

-- Use the database
USE certified_plumbers_graham;

-- Create table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `state` VARCHAR(50) NOT NULL,
  `zip` VARCHAR(10) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`customer_id`)
);

-- Create table for service types
CREATE TABLE service_types (
  `service_type_id` INT AUTO_INCREMENT,
  `service_type_name` VARCHAR(100) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`service_type_id`)
);

-- Create table for services
CREATE TABLE services (
  `service_id` INT AUTO_INCREMENT,
  `service_type_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `service_date` DATE NOT NULL,
  `description` TEXT,
  `cost` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`service_id`),
  FOREIGN KEY (`service_type_id`) REFERENCES service_types(`service_type_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`)
);

-- Create table for technicians
CREATE TABLE technicians (
  `technician_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`technician_id`)
);

-- Create table for service technicians
CREATE TABLE service_technicians (
  `service_id` INT NOT NULL,
  `technician_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`service_id`, `technician_id`),
  FOREIGN KEY (`service_id`) REFERENCES services(`service_id`),
  FOREIGN KEY (`technician_id`) REFERENCES technicians(`technician_id`)
);

-- Insert sample data for service types
INSERT INTO service_types (service_type_name, description)
VALUES
  ('Slab Leak Detection', 'Detection of leaks under concrete slabs'),
  ('Whole-Home Repiping', 'Replacement of old pipes in entire home'),
  ('Drain Cleaning', 'Clearing of clogged drains'),
  ('Toilet Installation', 'Installation of new toilets');

-- Insert sample data for customers
INSERT INTO customers (first_name, last_name, email, phone, address, city, state, zip)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Graham', 'TX', '76444'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Graham', 'TX', '76444');

-- Insert sample data for technicians
INSERT INTO technicians (first_name, last_name, email, phone)
VALUES
  ('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567'),
  ('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543');

-- Insert sample data for services
INSERT INTO services (service_type_id, customer_id, service_date, description, cost)
VALUES
  (1, 1, '2022-01-01', 'Detected slab leak', 100.00),
  (2, 2, '2022-06-01', 'Replaced pipes in entire home', 5000.00);

-- Insert sample data for service technicians
INSERT INTO service_technicians (service_id, technician_id)
VALUES
  (1, 1),
  (2, 2);
```
