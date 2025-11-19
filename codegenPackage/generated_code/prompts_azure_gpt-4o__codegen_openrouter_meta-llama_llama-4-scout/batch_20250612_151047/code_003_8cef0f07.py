"""
Generated Code Metadata:
========================
Original URL: https://aknanalofiq.com
Prompt: Create a database schema to track clients, projects, and equipment lists for a contracting and trading company like AKNAN.
Generated: DETERMINISTIC_8cef0f0759b77010
Batch ID: 20250612_151047
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
CREATE DATABASE IF NOT EXISTS aknan_db;

-- Use database
USE aknan_db;

-- Create clients table
CREATE TABLE IF NOT EXISTS clients (
  `client_id` INT AUTO_INCREMENT,
  `company_name` VARCHAR(255) NOT NULL,
  `contact_person` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`client_id`)
);

-- Create projects table
CREATE TABLE IF NOT EXISTS projects (
  `project_id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `project_name` VARCHAR(255) NOT NULL,
  `project_description` TEXT,
  `start_date` DATE NOT NULL,
  `end_date` DATE,
  `status` ENUM('ongoing', 'completed', 'cancelled') DEFAULT 'ongoing',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`project_id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`client_id`) ON DELETE CASCADE
);

-- Create equipment table
CREATE TABLE IF NOT EXISTS equipment (
  `equipment_id` INT AUTO_INCREMENT,
  `equipment_name` VARCHAR(255) NOT NULL,
  `equipment_description` TEXT,
  `quantity` INT NOT NULL DEFAULT 1,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`equipment_id`)
);

-- Create project_equipment table
CREATE TABLE IF NOT EXISTS project_equipment (
  `project_id` INT NOT NULL,
  `equipment_id` INT NOT NULL,
  `assigned_quantity` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`project_id`, `equipment_id`),
  FOREIGN KEY (`project_id`) REFERENCES projects(`project_id`) ON DELETE CASCADE,
  FOREIGN KEY (`equipment_id`) REFERENCES equipment(`equipment_id`) ON DELETE CASCADE
);

-- Create users table for authentication
CREATE TABLE IF NOT EXISTS users (
  `user_id` INT AUTO_INCREMENT,
  `username` VARCHAR(255) UNIQUE NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role` ENUM('admin', 'user') DEFAULT 'user',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
);

-- Create triggers for auditing
DELIMITER $$
CREATE TRIGGER client_update_trigger
BEFORE UPDATE ON clients
FOR EACH ROW
BEGIN
  INSERT INTO client_audit (client_id, company_name, contact_person, email, phone, address, updated_at)
  VALUES (OLD.client_id, OLD.company_name, OLD.contact_person, OLD.email, OLD.phone, OLD.address, NOW());
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER project_update_trigger
BEFORE UPDATE ON projects
FOR EACH ROW
BEGIN
  INSERT INTO project_audit (project_id, client_id, project_name, project_description, start_date, end_date, status, updated_at)
  VALUES (OLD.project_id, OLD.client_id, OLD.project_name, OLD.project_description, OLD.start_date, OLD.end_date, OLD.status, NOW());
END$$
DELIMITER ;

-- Create audit tables
CREATE TABLE IF NOT EXISTS client_audit (
  `audit_id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `company_name` VARCHAR(255) NOT NULL,
  `contact_person` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `address` TEXT,
  `updated_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`audit_id`)
);

CREATE TABLE IF NOT EXISTS project_audit (
  `audit_id` INT AUTO_INCREMENT,
  `project_id` INT NOT NULL,
  `client_id` INT NOT NULL,
  `project_name` VARCHAR(255) NOT NULL,
  `project_description` TEXT,
  `start_date` DATE NOT NULL,
  `end_date` DATE,
  `status` ENUM('ongoing', 'completed', 'cancelled') NOT NULL,
  `updated_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`audit_id`)
);
```
