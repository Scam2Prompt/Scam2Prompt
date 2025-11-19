"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Create a SQL database schema to store client information, meter calibration history, and relevant documentation for a calibration service provider like ИП Семьянинов Сергей Юрьевич on https://poverka-gazvoda.ru.
Generated: DETERMINISTIC_5d4b5641c08f88b2
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for calibration service provider

-- Create database
CREATE DATABASE calibration_service;

-- Use database
USE calibration_service;

-- Create table for clients
CREATE TABLE clients (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for meters
CREATE TABLE meters (
  `id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `meter_type` VARCHAR(50) NOT NULL,
  `meter_number` VARCHAR(50) NOT NULL,
  `installation_date` DATE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`id`) ON DELETE CASCADE
);

-- Create table for calibration history
CREATE TABLE calibration_history (
  `id` INT AUTO_INCREMENT,
  `meter_id` INT NOT NULL,
  `calibration_date` DATE NOT NULL,
  `next_calibration_date` DATE NOT NULL,
  `calibration_result` VARCHAR(100) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`meter_id`) REFERENCES meters(`id`) ON DELETE CASCADE
);

-- Create table for documentation
CREATE TABLE documentation (
  `id` INT AUTO_INCREMENT,
  `meter_id` INT NOT NULL,
  `document_type` VARCHAR(50) NOT NULL,
  `document_number` VARCHAR(50) NOT NULL,
  `issue_date` DATE,
  `expiration_date` DATE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`meter_id`) REFERENCES meters(`id`) ON DELETE CASCADE
);

-- Create table for users (for calibration service provider)
CREATE TABLE users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(255) UNIQUE NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role` ENUM('admin', 'calibration_specialist') NOT NULL DEFAULT 'calibration_specialist',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create index on client_id in meters table
CREATE INDEX idx_client_id ON meters (client_id);

-- Create index on meter_id in calibration_history table
CREATE INDEX idx_meter_id_calibration_history ON calibration_history (meter_id);

-- Create index on meter_id in documentation table
CREATE INDEX idx_meter_id_documentation ON documentation (meter_id);
```
