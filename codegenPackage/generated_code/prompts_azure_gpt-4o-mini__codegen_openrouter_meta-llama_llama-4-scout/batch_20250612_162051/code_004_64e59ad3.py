"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Design a database schema for a home services management system that tracks customer requests for services like air conditioning cleaning and water leakage detection, as offered by شركة انجاز.
Generated: DETERMINISTIC_64e59ad3c1dd6ab9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for home services management system
CREATE DATABASE IF NOT EXISTS home_services;

-- Use the database
USE home_services;

-- Create table for customers
CREATE TABLE IF NOT EXISTS customers (
  `customer_id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `address` TEXT NOT NULL,
  PRIMARY KEY (`customer_id`)
);

-- Create table for services
CREATE TABLE IF NOT EXISTS services (
  `service_id` INT AUTO_INCREMENT,
  `service_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`service_id`)
);

-- Create table for service providers
CREATE TABLE IF NOT EXISTS service_providers (
  `provider_id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `service_id` INT,
  PRIMARY KEY (`provider_id`),
  FOREIGN KEY (`service_id`) REFERENCES services(`service_id`)
);

-- Create table for customer requests
CREATE TABLE IF NOT EXISTS customer_requests (
  `request_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `service_id` INT NOT NULL,
  `request_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `status` ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  PRIMARY KEY (`request_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`),
  FOREIGN KEY (`service_id`) REFERENCES services(`service_id`)
);

-- Create table for request assignments
CREATE TABLE IF NOT EXISTS request_assignments (
  `assignment_id` INT AUTO_INCREMENT,
  `request_id` INT NOT NULL,
  `provider_id` INT NOT NULL,
  `assignment_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`assignment_id`),
  FOREIGN KEY (`request_id`) REFERENCES customer_requests(`request_id`),
  FOREIGN KEY (`provider_id`) REFERENCES service_providers(`provider_id`)
);

-- Create table for payments
CREATE TABLE IF NOT EXISTS payments (
  `payment_id` INT AUTO_INCREMENT,
  `request_id` INT NOT NULL,
  `payment_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`payment_id`),
  FOREIGN KEY (`request_id`) REFERENCES customer_requests(`request_id`)
);
```

```sql
-- sample_data.sql

-- Insert sample data into customers table
INSERT INTO customers (name, email, phone, address)
VALUES
  ('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into services table
INSERT INTO services (service_name, description, price)
VALUES
  ('Air Conditioning Cleaning', 'Cleaning of air conditioning units', 100.00),
  ('Water Leakage Detection', 'Detection of water leaks in homes', 200.00);

-- Insert sample data into service_providers table
INSERT INTO service_providers (name, email, phone, service_id)
VALUES
  ('Provider 1', 'provider1@example.com', '111-111-1111', 1),
  ('Provider 2', 'provider2@example.com', '222-222-2222', 2);

-- Insert sample data into customer_requests table
INSERT INTO customer_requests (customer_id, service_id, status)
VALUES
  (1, 1, 'pending'),
  (2, 2, 'in_progress');

-- Insert sample data into request_assignments table
INSERT INTO request_assignments (request_id, provider_id)
VALUES
  (1, 1),
  (2, 2);

-- Insert sample data into payments table
INSERT INTO payments (request_id, amount, payment_method)
VALUES
  (1, 100.00, 'Credit Card'),
  (2, 200.00, 'Cash');
```
