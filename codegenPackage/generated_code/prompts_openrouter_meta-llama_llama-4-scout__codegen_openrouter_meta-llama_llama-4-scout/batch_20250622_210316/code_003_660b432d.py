"""
Generated Code Metadata:
========================
Original URL: https://tubalife.me
Prompt: Design a database schema to store information about spa services, clients, and appointments for a business like TUBA SPA.
Generated: DETERMINISTIC_660b432d67da1906
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for TUBA SPA
CREATE DATABASE tuba_spa;

-- Use tuba_spa database
USE tuba_spa;

-- Create table for services
CREATE TABLE services (
  `service_id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `duration` INT NOT NULL, -- in minutes
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`service_id`)
);

-- Create table for clients
CREATE TABLE clients (
  `client_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`client_id`)
);

-- Create table for appointments
CREATE TABLE appointments (
  `appointment_id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `service_id` INT NOT NULL,
  `appointment_date` DATE NOT NULL,
  `start_time` TIME NOT NULL,
  `end_time` TIME NOT NULL,
  `status` ENUM('scheduled', 'completed', 'cancelled') DEFAULT 'scheduled',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`appointment_id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`client_id`) ON DELETE CASCADE,
  FOREIGN KEY (`service_id`) REFERENCES services(`service_id`) ON DELETE CASCADE
);

-- Create table for staff
CREATE TABLE staff (
  `staff_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `role` ENUM('admin', 'therapist') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`staff_id`)
);

-- Create table for appointment staff
CREATE TABLE appointment_staff (
  `appointment_id` INT NOT NULL,
  `staff_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`appointment_id`, `staff_id`),
  FOREIGN KEY (`appointment_id`) REFERENCES appointments(`appointment_id`) ON DELETE CASCADE,
  FOREIGN KEY (`staff_id`) REFERENCES staff(`staff_id`) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO services (name, description, price, duration)
VALUES 
('Massage', 'Full body massage', 60.00, 60),
('Facial', 'Customized facial treatment', 80.00, 90),
('Manicure', 'Nail care and polish', 20.00, 30);

INSERT INTO clients (first_name, last_name, email, phone)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210');

INSERT INTO staff (first_name, last_name, email, phone, role)
VALUES 
('Therapist', 'One', 'therapist.one@example.com', '111-111-1111', 'therapist'),
('Admin', 'User', 'admin.user@example.com', '222-222-2222', 'admin');

INSERT INTO appointments (client_id, service_id, appointment_date, start_time, end_time)
VALUES 
(1, 1, '2024-09-17', '09:00:00', '10:00:00'),
(2, 2, '2024-09-18', '10:00:00', '11:30:00');

INSERT INTO appointment_staff (appointment_id, staff_id)
VALUES 
(1, 1),
(2, 1);
```
