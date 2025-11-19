"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Generate a sample database schema for storing information about cleaning services, customers, and appointments for a company like Maria HouseKeepers.
Generated: DETERMINISTIC_7a9f55422b927d6a
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

-- Create database for Maria HouseKeepers
CREATE DATABASE IF NOT EXISTS maria_housekeepers;

-- Use the database
USE maria_housekeepers;

-- Create table for customers
CREATE TABLE IF NOT EXISTS customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `state` VARCHAR(100) NOT NULL,
  `zip_code` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`customer_id`)
);

-- Create table for cleaning services
CREATE TABLE IF NOT EXISTS services (
  `service_id` INT AUTO_INCREMENT,
  `service_name` VARCHAR(100) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`service_id`)
);

-- Create table for cleaners
CREATE TABLE IF NOT EXISTS cleaners (
  `cleaner_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`cleaner_id`)
);

-- Create table for appointments
CREATE TABLE IF NOT EXISTS appointments (
  `appointment_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `cleaner_id` INT NOT NULL,
  `service_id` INT NOT NULL,
  `appointment_date` DATE NOT NULL,
  `appointment_time` TIME NOT NULL,
  `status` ENUM('scheduled', 'completed', 'cancelled') NOT NULL DEFAULT 'scheduled',
  PRIMARY KEY (`appointment_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`),
  FOREIGN KEY (`cleaner_id`) REFERENCES cleaners(`cleaner_id`),
  FOREIGN KEY (`service_id`) REFERENCES services(`service_id`)
);

-- Create table for payments
CREATE TABLE IF NOT EXISTS payments (
  `payment_id` INT AUTO_INCREMENT,
  `appointment_id` INT NOT NULL,
  `payment_method` VARCHAR(100) NOT NULL,
  `payment_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`payment_id`),
  FOREIGN KEY (`appointment_id`) REFERENCES appointments(`appointment_id`)
);

-- Create indexes for faster queries
CREATE INDEX idx_appointments_customer_id ON appointments (customer_id);
CREATE INDEX idx_appointments_cleaner_id ON appointments (cleaner_id);
CREATE INDEX idx_appointments_service_id ON appointments (service_id);
```

```sql
-- sample_data.sql

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, phone_number, address, city, state, zip_code)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

-- Insert sample data into services table
INSERT INTO services (service_name, description, price)
VALUES
  ('House Cleaning', 'Basic house cleaning services', 50.00),
  ('Deep Cleaning', 'Deep cleaning services for larger homes', 100.00),
  ('Special Event Cleaning', 'Cleaning services for special events', 200.00);

-- Insert sample data into cleaners table
INSERT INTO cleaners (first_name, last_name, email, phone_number)
VALUES
  ('Maria', 'HouseKeeper', 'maria.housekeeper@example.com', '555-123-4567'),
  ('Emily', 'Cleaner', 'emily.cleaner@example.com', '555-987-6543');

-- Insert sample data into appointments table
INSERT INTO appointments (customer_id, cleaner_id, service_id, appointment_date, appointment_time)
VALUES
  (1, 1, 1, '2024-09-17', '09:00:00'),
  (2, 2, 2, '2024-09-18', '10:00:00');

-- Insert sample data into payments table
INSERT INTO payments (appointment_id, payment_method, payment_date, amount)
VALUES
  (1, 'Credit Card', '2024-09-17', 50.00),
  (2, 'Cash', '2024-09-18', 100.00);
```
