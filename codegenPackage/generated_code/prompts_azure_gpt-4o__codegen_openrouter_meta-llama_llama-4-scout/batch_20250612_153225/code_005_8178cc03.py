"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Create a database schema for managing cleaning service plans (weekly, biweekly, monthly) and tracking customer preferences for specific cleaning details.
Generated: DETERMINISTIC_8178cc03e562e8b9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- cleaning_service_schema.sql

-- Create database schema for cleaning service plans
CREATE DATABASE cleaning_service;

-- Use the cleaning_service database
USE cleaning_service;

-- Create table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`customer_id`)
);

-- Create table for cleaning plans
CREATE TABLE cleaning_plans (
  `plan_id` INT AUTO_INCREMENT,
  `plan_name` ENUM('weekly', 'biweekly', 'monthly') NOT NULL,
  `plan_description` TEXT,
  `plan_price` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`plan_id`)
);

-- Create table for cleaning services
CREATE TABLE cleaning_services (
  `service_id` INT AUTO_INCREMENT,
  `service_name` VARCHAR(100) NOT NULL,
  `service_description` TEXT,
  PRIMARY KEY (`service_id`)
);

-- Create table for customer preferences
CREATE TABLE customer_preferences (
  `preference_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `service_id` INT NOT NULL,
  `frequency` ENUM('daily', 'weekly', 'monthly'),
  `special_requests` TEXT,
  PRIMARY KEY (`preference_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`),
  FOREIGN KEY (`service_id`) REFERENCES cleaning_services(`service_id`)
);

-- Create table for customer plans
CREATE TABLE customer_plans (
  `customer_plan_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `plan_id` INT NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE,
  PRIMARY KEY (`customer_plan_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`),
  FOREIGN KEY (`plan_id`) REFERENCES cleaning_plans(`plan_id`)
);

-- Create table for cleaning schedules
CREATE TABLE cleaning_schedules (
  `schedule_id` INT AUTO_INCREMENT,
  `customer_plan_id` INT NOT NULL,
  `schedule_date` DATE NOT NULL,
  `schedule_time` TIME NOT NULL,
  `status` ENUM('pending', 'in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`schedule_id`),
  FOREIGN KEY (`customer_plan_id`) REFERENCES customer_plans(`customer_plan_id`)
);

-- Insert sample data into cleaning_plans table
INSERT INTO cleaning_plans (plan_name, plan_description, plan_price)
VALUES
('weekly', 'Weekly cleaning service', 100.00),
('biweekly', 'Biweekly cleaning service', 150.00),
('monthly', 'Monthly cleaning service', 200.00);

-- Insert sample data into cleaning_services table
INSERT INTO cleaning_services (service_name, service_description)
VALUES
('dusting', 'Dusting of all surfaces'),
('vacuuming', 'Vacuuming of all floors'),
('mopping', 'Mopping of all floors'),
('bathroom cleaning', 'Cleaning of bathroom');

-- Example usage:
-- Insert a new customer
INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

-- Insert a new customer plan
INSERT INTO customer_plans (customer_id, plan_id, start_date)
VALUES (1, 1, '2024-09-01');

-- Insert a new customer preference
INSERT INTO customer_preferences (customer_id, service_id, frequency, special_requests)
VALUES (1, 1, 'weekly', 'Please use eco-friendly products');

-- Retrieve all customer plans
SELECT * FROM customer_plans;

-- Retrieve all customer preferences
SELECT * FROM customer_preferences;
```
