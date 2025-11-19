"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: "Design a simple database schema to store information about security guards, their training, and deployment for a company like Mando Security."
Generated: DETERMINISTIC_914fe72fc33a9d1a
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Mando Security
CREATE DATABASE mando_security;

-- Use mando_security database
USE mando_security;

-- Create table for security guards
CREATE TABLE guards (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  `date_of_birth` DATE,
  `hire_date` DATE NOT NULL,
  `guard_status` ENUM('active', 'inactive') DEFAULT 'active',
  PRIMARY KEY (`id`)
);

-- Create table for training types
CREATE TABLE training_types (
  `id` INT AUTO_INCREMENT,
  `training_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`)
);

-- Create table for guard training
CREATE TABLE guard_training (
  `id` INT AUTO_INCREMENT,
  `guard_id` INT NOT NULL,
  `training_id` INT NOT NULL,
  `training_date` DATE NOT NULL,
  `expiry_date` DATE,
  `certification_number` VARCHAR(255),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`guard_id`) REFERENCES guards(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`training_id`) REFERENCES training_types(`id`) ON DELETE CASCADE
);

-- Create table for deployment locations
CREATE TABLE locations (
  `id` INT AUTO_INCREMENT,
  `location_name` VARCHAR(255) NOT NULL,
  `address` TEXT NOT NULL,
  PRIMARY KEY (`id`)
);

-- Create table for guard deployment
CREATE TABLE guard_deployment (
  `id` INT AUTO_INCREMENT,
  `guard_id` INT NOT NULL,
  `location_id` INT NOT NULL,
  `deployment_date` DATE NOT NULL,
  `end_date` DATE,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`guard_id`) REFERENCES guards(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`location_id`) REFERENCES locations(`id`) ON DELETE CASCADE
);

-- Create table for incident reports
CREATE TABLE incident_reports (
  `id` INT AUTO_INCREMENT,
  `guard_id` INT NOT NULL,
  `location_id` INT NOT NULL,
  `incident_date` DATE NOT NULL,
  `incident_description` TEXT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`guard_id`) REFERENCES guards(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`location_id`) REFERENCES locations(`id`) ON DELETE CASCADE
);
```

```sql
-- sample_data.sql

-- Insert sample data into guards table
INSERT INTO guards (`first_name`, `last_name`, `email`, `phone_number`, `address`, `date_of_birth`, `hire_date`)
VALUES 
('John', 'Doe', 'john.doe@mando.com', '1234567890', '123 Main St', '1990-01-01', '2020-01-01'),
('Jane', 'Doe', 'jane.doe@mando.com', '9876543210', '456 Elm St', '1995-06-01', '2022-06-01');

-- Insert sample data into training_types table
INSERT INTO training_types (`training_name`, `description`)
VALUES 
('Basic Security Training', 'Basic security procedures and protocols'),
('Fire Safety Training', 'Fire safety and emergency procedures');

-- Insert sample data into guard_training table
INSERT INTO guard_training (`guard_id`, `training_id`, `training_date`, `expiry_date`, `certification_number`)
VALUES 
(1, 1, '2020-01-15', '2025-01-15', 'BST-12345'),
(1, 2, '2020-06-01', '2027-06-01', 'FST-67890'),
(2, 1, '2022-06-15', '2027-06-15', 'BST-34567');

-- Insert sample data into locations table
INSERT INTO locations (`location_name`, `address`)
VALUES 
('Downtown Office', '789 Oak St'),
('Uptown Mall', '321 Maple St');

-- Insert sample data into guard_deployment table
INSERT INTO guard_deployment (`guard_id`, `location_id`, `deployment_date`, `end_date`)
VALUES 
(1, 1, '2020-01-01', NULL),
(2, 2, '2022-06-01', NULL);

-- Insert sample data into incident_reports table
INSERT INTO incident_reports (`guard_id`, `location_id`, `incident_date`, `incident_description`)
VALUES 
(1, 1, '2022-01-01', 'Reported suspicious activity'),
(2, 2, '2023-03-01', 'Responded to medical emergency');
```
