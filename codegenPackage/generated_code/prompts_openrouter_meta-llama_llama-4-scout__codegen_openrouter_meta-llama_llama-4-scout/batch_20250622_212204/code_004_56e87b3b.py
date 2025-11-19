"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: "Design a database schema to store information about Chevrolet vehicles, consórcio plans, and customer details, using a relational database management system."
Generated: DETERMINISTIC_56e87b3b08b71215
Batch ID: 20250622_212204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE chevrolet_db;

-- Use database
USE chevrolet_db;

-- Create table for vehicle models
CREATE TABLE vehicle_models (
  `id` INT AUTO_INCREMENT,
  `model_name` VARCHAR(255) NOT NULL,
  `model_year` INT NOT NULL,
  `vehicle_type` ENUM('car', 'truck', 'suv') NOT NULL,
  PRIMARY KEY (`id`)
);

-- Create table for consórcio plans
CREATE TABLE consorcio_plans (
  `id` INT AUTO_INCREMENT,
  `plan_name` VARCHAR(255) NOT NULL,
  `plan_description` TEXT,
  `plan_value` DECIMAL(10, 2) NOT NULL,
  `plan_duration` INT NOT NULL,
  PRIMARY KEY (`id`)
);

-- Create table for customers
CREATE TABLE customers (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `address` TEXT,
  PRIMARY KEY (`id`)
);

-- Create table for customer consórcio plans
CREATE TABLE customer_consorcio_plans (
  `id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `consorcio_plan_id` INT NOT NULL,
  `enrollment_date` DATE NOT NULL,
  `status` ENUM('active', 'inactive', 'pending') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`id`),
  FOREIGN KEY (`consorcio_plan_id`) REFERENCES consorcio_plans(`id`)
);

-- Create table for vehicle purchases
CREATE TABLE vehicle_purchases (
  `id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `vehicle_model_id` INT NOT NULL,
  `purchase_date` DATE NOT NULL,
  `purchase_price` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`id`),
  FOREIGN KEY (`vehicle_model_id`) REFERENCES vehicle_models(`id`)
);

-- Create table for payments
CREATE TABLE payments (
  `id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `consorcio_plan_id` INT NOT NULL,
  `payment_date` DATE NOT NULL,
  `payment_value` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`id`),
  FOREIGN KEY (`consorcio_plan_id`) REFERENCES consorcio_plans(`id`)
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_consorcio_plans_customer_id ON customer_consorcio_plans (customer_id);
CREATE INDEX idx_customer_consorcio_plans_consorcio_plan_id ON customer_consorcio_plans (consorcio_plan_id);
CREATE INDEX idx_vehicle_purchases_customer_id ON vehicle_purchases (customer_id);
CREATE INDEX idx_vehicle_purchases_vehicle_model_id ON vehicle_purchases (vehicle_model_id);
CREATE INDEX idx_payments_customer_id ON payments (customer_id);
CREATE INDEX idx_payments_consorcio_plan_id ON payments (consorcio_plan_id);
```

```sql
-- example_data.sql

-- Insert example data into vehicle models table
INSERT INTO vehicle_models (model_name, model_year, vehicle_type)
VALUES 
('Chevrolet Onix', 2022, 'car'),
('Chevrolet S10', 2020, 'truck'),
('Chevrolet Tracker', 2019, 'suv');

-- Insert example data into consórcio plans table
INSERT INTO consorcio_plans (plan_name, plan_description, plan_value, plan_duration)
VALUES 
('Plan 1', 'Consórcio plan for Chevrolet Onix', 50000.00, 60),
('Plan 2', 'Consórcio plan for Chevrolet S10', 70000.00, 72),
('Plan 3', 'Consórcio plan for Chevrolet Tracker', 60000.00, 60);

-- Insert example data into customers table
INSERT INTO customers (name, email, phone, address)
VALUES 
('John Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
('Jane Doe', 'jane.doe@example.com', '9876543210', '456 Elm St'),
('Bob Smith', 'bob.smith@example.com', '5555555555', '789 Oak St');

-- Insert example data into customer consórcio plans table
INSERT INTO customer_consorcio_plans (customer_id, consorcio_plan_id, enrollment_date, status)
VALUES 
(1, 1, '2022-01-01', 'active'),
(2, 2, '2022-02-01', 'active'),
(3, 3, '2022-03-01', 'pending');

-- Insert example data into vehicle purchases table
INSERT INTO vehicle_purchases (customer_id, vehicle_model_id, purchase_date, purchase_price)
VALUES 
(1, 1, '2022-06-01', 45000.00),
(2, 2, '2022-07-01', 65000.00);

-- Insert example data into payments table
INSERT INTO payments (customer_id, consorcio_plan_id, payment_date, payment_value)
VALUES 
(1, 1, '2022-01-15', 833.33),
(2, 2, '2022-02-15', 972.22),
(3, 3, '2022-03-15', 1000.00);
```
