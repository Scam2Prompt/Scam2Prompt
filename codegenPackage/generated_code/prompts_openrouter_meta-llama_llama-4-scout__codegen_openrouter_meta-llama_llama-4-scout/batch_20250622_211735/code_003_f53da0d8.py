"""
Generated Code Metadata:
========================
Original URL: https://wufis.com
Prompt: Design a database schema for storing caregiver profiles, pet information, and reservation details for a pet sitting service like WUFIS.
Generated: DETERMINISTIC_f53da0d8d7279c9a
Batch ID: 20250622_211735
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for pet sitting service
CREATE DATABASE wufis;

-- Use the database
USE wufis;

-- Create table for caregiver profiles
CREATE TABLE caregivers (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `state` VARCHAR(100) NOT NULL,
  `zip_code` VARCHAR(10) NOT NULL,
  `bio` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for pet information
CREATE TABLE pets (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `type` ENUM('dog', 'cat', 'other') NOT NULL,
  `breed` VARCHAR(100),
  `age` INT NOT NULL,
  `weight` DECIMAL(5, 2) NOT NULL,
  `health_conditions` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for reservation details
CREATE TABLE reservations (
  `id` INT AUTO_INCREMENT,
  `caregiver_id` INT NOT NULL,
  `pet_id` INT NOT NULL,
  `reservation_date` DATE NOT NULL,
  `start_time` TIME NOT NULL,
  `end_time` TIME NOT NULL,
  `service_type` ENUM('sitting', 'walking', 'overnight') NOT NULL,
  `price` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'confirmed', 'cancelled') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`caregiver_id`) REFERENCES caregivers(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`pet_id`) REFERENCES pets(`id`) ON DELETE CASCADE
);

-- Create table for client information
CREATE TABLE clients (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `state` VARCHAR(100) NOT NULL,
  `zip_code` VARCHAR(10) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for client reservations
CREATE TABLE client_reservations (
  `id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `reservation_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`reservation_id`) REFERENCES reservations(`id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_caregiver_id ON reservations (caregiver_id);
CREATE INDEX idx_pet_id ON reservations (pet_id);
CREATE INDEX idx_client_id ON client_reservations (client_id);
CREATE INDEX idx_reservation_id ON client_reservations (reservation_id);
```

```sql
-- sample_data.sql

-- Insert sample data into caregivers table
INSERT INTO caregivers (first_name, last_name, email, phone_number, address, city, state, zip_code, bio)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345', 'Experienced pet caregiver'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890', 'Pet lover and caregiver');

-- Insert sample data into pets table
INSERT INTO pets (name, type, breed, age, weight, health_conditions)
VALUES 
('Fido', 'dog', 'Golden Retriever', 3, 50.00, 'None'),
('Whiskers', 'cat', 'Siamese', 5, 10.00, 'Hyperthyroidism');

-- Insert sample data into clients table
INSERT INTO clients (first_name, last_name, email, phone_number, address, city, state, zip_code)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567', '789 Oak St', 'Anytown', 'CA', '12345'),
('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543', '321 Maple St', 'Othertown', 'NY', '67890');

-- Insert sample data into reservations table
INSERT INTO reservations (caregiver_id, pet_id, reservation_date, start_time, end_time, service_type, price, status)
VALUES 
(1, 1, '2024-09-17', '09:00:00', '17:00:00', 'sitting', 50.00, 'confirmed'),
(1, 2, '2024-09-18', '10:00:00', '18:00:00', 'walking', 30.00, 'pending'),
(2, 1, '2024-09-19', '11:00:00', '19:00:00', 'overnight', 100.00, 'confirmed');

-- Insert sample data into client_reservations table
INSERT INTO client_reservations (client_id, reservation_id)
VALUES 
(1, 1),
(1, 2),
(2, 3);
```
