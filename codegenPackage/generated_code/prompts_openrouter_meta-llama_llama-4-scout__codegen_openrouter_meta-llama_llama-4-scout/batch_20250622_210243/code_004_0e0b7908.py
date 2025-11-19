"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: "Design a database schema to store information about printing services, including customer details, order history, and material specifications, for a company like Detalj Reklam & Tryckeri."
Generated: DETERMINISTIC_0e0b7908de6ef795
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for printing services
CREATE DATABASE printing_services;

-- Use the database schema
USE printing_services;

-- Create table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `company_name` VARCHAR(255) NOT NULL,
  `contact_name` VARCHAR(255) NOT NULL,
  `contact_email` VARCHAR(255) UNIQUE NOT NULL,
  `contact_phone` VARCHAR(20) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `postal_code` VARCHAR(20) NOT NULL,
  `country` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`customer_id`)
);

-- Create table for materials
CREATE TABLE materials (
  `material_id` INT AUTO_INCREMENT,
  `material_name` VARCHAR(255) NOT NULL,
  `material_description` TEXT,
  `material_type` ENUM('paper', 'cardboard', 'vinyl', 'other') NOT NULL,
  PRIMARY KEY (`material_id`)
);

-- Create table for orders
CREATE TABLE orders (
  `order_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `order_date` DATE NOT NULL,
  `delivery_date` DATE,
  `total_cost` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'in_progress', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`order_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`)
);

-- Create table for order items
CREATE TABLE order_items (
  `order_item_id` INT AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `material_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  `unit_price` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`order_item_id`),
  FOREIGN KEY (`order_id`) REFERENCES orders(`order_id`),
  FOREIGN KEY (`material_id`) REFERENCES materials(`material_id`)
);

-- Create table for printing services
CREATE TABLE printing_services (
  `service_id` INT AUTO_INCREMENT,
  `service_name` VARCHAR(255) NOT NULL,
  `service_description` TEXT,
  `service_price` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`service_id`)
);

-- Create table for order services
CREATE TABLE order_services (
  `order_service_id` INT AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `service_id` INT NOT NULL,
  PRIMARY KEY (`order_service_id`),
  FOREIGN KEY (`order_id`) REFERENCES orders(`order_id`),
  FOREIGN KEY (`service_id`) REFERENCES printing_services(`service_id`)
);

-- Insert sample data into customers table
INSERT INTO customers (company_name, contact_name, contact_email, contact_phone, address, city, postal_code, country)
VALUES 
('Detalj Reklam & Tryckeri', 'John Doe', 'john.doe@example.com', '+46 123 456 789', 'Main Street 1', 'Stockholm', '12345', 'Sweden'),
('ABC Company', 'Jane Smith', 'jane.smith@example.com', '+46 987 654 321', 'Park Avenue 2', 'Gothenburg', '67890', 'Sweden');

-- Insert sample data into materials table
INSERT INTO materials (material_name, material_description, material_type)
VALUES 
('Glossy Paper', 'High-quality glossy paper', 'paper'),
('Cardboard', 'Thick and sturdy cardboard', 'cardboard'),
('Vinyl', 'Flexible and waterproof vinyl', 'vinyl');

-- Insert sample data into orders table
INSERT INTO orders (customer_id, order_date, delivery_date, total_cost)
VALUES 
(1, '2022-01-01', '2022-01-15', 1000.00),
(2, '2022-02-01', '2022-02-15', 500.00);

-- Insert sample data into order items table
INSERT INTO order_items (order_id, material_id, quantity, unit_price)
VALUES 
(1, 1, 100, 5.00),
(1, 2, 50, 10.00),
(2, 3, 200, 3.00);

-- Insert sample data into printing services table
INSERT INTO printing_services (service_name, service_description, service_price)
VALUES 
('Digital Printing', 'High-quality digital printing', 500.00),
('Offset Printing', 'Large-scale offset printing', 2000.00);

-- Insert sample data into order services table
INSERT INTO order_services (order_id, service_id)
VALUES 
(1, 1),
(2, 2);
```
