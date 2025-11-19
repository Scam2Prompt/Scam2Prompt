"""
Generated Code Metadata:
========================
Original URL: https://www.albertozofrea.it
Prompt: Suggest a suitable database schema for storing client information, appointments, and services offered by a professional Shiatsu operator like Alberto Zofrea.
Generated: DETERMINISTIC_0be021a4e06c1b28
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

-- Create database for Shiatsu operator
CREATE DATABASE shiatsu;

-- Use shiatsu database
USE shiatsu;

-- Create table for clients
CREATE TABLE clients (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `address` VARCHAR(255),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for services
CREATE TABLE services (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for appointments
CREATE TABLE appointments (
  `id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `service_id` INT NOT NULL,
  `appointment_date` DATE NOT NULL,
  `appointment_time` TIME NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`service_id`) REFERENCES services(`id`) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  `id` INT AUTO_INCREMENT,
  `appointment_id` INT NOT NULL,
  `payment_method` VARCHAR(50) NOT NULL,
  `payment_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`appointment_id`) REFERENCES appointments(`id`) ON DELETE CASCADE
);
```

```sql
-- sample_data.sql

-- Insert sample data into clients table
INSERT INTO clients (`first_name`, `last_name`, `email`, `phone`, `address`)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into services table
INSERT INTO services (`name`, `description`, `price`)
VALUES 
('Shiatsu Massage', 'Traditional Japanese massage therapy', 60.00),
('Aromatherapy', 'Essential oil therapy for relaxation', 30.00);

-- Insert sample data into appointments table
INSERT INTO appointments (`client_id`, `service_id`, `appointment_date`, `appointment_time`)
VALUES 
(1, 1, '2024-09-20', '10:00:00'),
(2, 2, '2024-09-22', '14:00:00');

-- Insert sample data into payments table
INSERT INTO payments (`appointment_id`, `payment_method`, `payment_date`, `amount`)
VALUES 
(1, 'Cash', '2024-09-20', 60.00),
(2, 'Credit Card', '2024-09-22', 30.00);
```
