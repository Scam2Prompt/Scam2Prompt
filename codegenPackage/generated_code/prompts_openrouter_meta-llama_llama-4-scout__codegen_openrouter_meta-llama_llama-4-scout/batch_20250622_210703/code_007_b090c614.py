"""
Generated Code Metadata:
========================
Original URL: https://yury.lt
Prompt: Design a database schema to store information about hair services, products, and client appointments for a beauty salon management system.
Generated: DETERMINISTIC_b090c6143f9b728d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for beauty salon management system
CREATE DATABASE beauty_salon;

-- Use the database
USE beauty_salon;

-- Create table for services
CREATE TABLE services (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for products
CREATE TABLE products (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `quantity` INT NOT NULL DEFAULT 0,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for clients
CREATE TABLE clients (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for appointments
CREATE TABLE appointments (
  `id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `service_id` INT,
  `appointment_date` DATE NOT NULL,
  `appointment_time` TIME NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`id`),
  FOREIGN KEY (`service_id`) REFERENCES services(`id`)
);

-- Create table for appointment products
CREATE TABLE appointment_products (
  `id` INT AUTO_INCREMENT,
  `appointment_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `quantity` INT NOT NULL DEFAULT 1,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`appointment_id`) REFERENCES appointments(`id`),
  FOREIGN KEY (`product_id`) REFERENCES products(`id`)
);

-- Create table for payments
CREATE TABLE payments (
  `id` INT AUTO_INCREMENT,
  `appointment_id` INT NOT NULL,
  `payment_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`appointment_id`) REFERENCES appointments(`id`)
);
```

```sql
-- sample_data.sql

-- Insert sample data into services table
INSERT INTO services (name, description, price)
VALUES 
('Haircut', 'Basic haircut', 20.00),
('Coloring', 'Hair coloring service', 50.00),
('Styling', 'Hair styling service', 30.00);

-- Insert sample data into products table
INSERT INTO products (name, description, price, quantity)
VALUES 
('Shampoo', 'Basic shampoo', 10.00, 100),
('Conditioner', 'Basic conditioner', 15.00, 50),
('Hair Mask', 'Hair mask treatment', 20.00, 20);

-- Insert sample data into clients table
INSERT INTO clients (first_name, last_name, email, phone)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210');

-- Insert sample data into appointments table
INSERT INTO appointments (client_id, service_id, appointment_date, appointment_time)
VALUES 
(1, 1, '2024-09-16', '10:00:00'),
(2, 2, '2024-09-17', '11:00:00');

-- Insert sample data into appointment products table
INSERT INTO appointment_products (appointment_id, product_id, quantity)
VALUES 
(1, 1, 1),
(2, 2, 2);

-- Insert sample data into payments table
INSERT INTO payments (appointment_id, payment_date, amount)
VALUES 
(1, '2024-09-16', 20.00),
(2, '2024-09-17', 100.00);
```
