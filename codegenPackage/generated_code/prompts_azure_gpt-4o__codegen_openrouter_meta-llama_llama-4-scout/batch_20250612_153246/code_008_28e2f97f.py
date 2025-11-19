"""
Generated Code Metadata:
========================
Original URL: https://simho.in
Prompt: Create a database schema to store HR service details, including permanent staffing, temporary staffing, and training, based on the structure provided by SIMHO.
Generated: DETERMINISTIC_28e2f97f063c76b1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for HR services
CREATE DATABASE hr_services;

-- Use the hr_services database
USE hr_services;

-- Create table for permanent staffing
CREATE TABLE permanent_staffing (
  `id` INT AUTO_INCREMENT,
  `employee_id` INT NOT NULL,
  `job_title` VARCHAR(255) NOT NULL,
  `department` VARCHAR(255) NOT NULL,
  `hire_date` DATE NOT NULL,
  `salary` DECIMAL(10, 2) NOT NULL,
  `benefits` VARCHAR(255),
  PRIMARY KEY (`id`),
  UNIQUE KEY `employee_id` (`employee_id`)
);

-- Create table for temporary staffing
CREATE TABLE temporary_staffing (
  `id` INT AUTO_INCREMENT,
  `temp_employee_id` INT NOT NULL,
  `job_title` VARCHAR(255) NOT NULL,
  `department` VARCHAR(255) NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE,
  `hourly_rate` DECIMAL(10, 2) NOT NULL,
  `hours_worked` DECIMAL(10, 2),
  PRIMARY KEY (`id`),
  UNIQUE KEY `temp_employee_id` (`temp_employee_id`)
);

-- Create table for training
CREATE TABLE training (
  `id` INT AUTO_INCREMENT,
  `training_title` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `start_date` DATE NOT NULL,
  `end_date` DATE,
  `trainer` VARCHAR(255) NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Create table for employee training
CREATE TABLE employee_training (
  `id` INT AUTO_INCREMENT,
  `employee_id` INT NOT NULL,
  `training_id` INT NOT NULL,
  `completion_date` DATE,
  `evaluation` VARCHAR(255),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`employee_id`) REFERENCES permanent_staffing(`employee_id`),
  FOREIGN KEY (`training_id`) REFERENCES training(`id`)
);

-- Create table for training sessions
CREATE TABLE training_sessions (
  `id` INT AUTO_INCREMENT,
  `training_id` INT NOT NULL,
  `session_date` DATE NOT NULL,
  `start_time` TIME NOT NULL,
  `end_time` TIME NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`training_id`) REFERENCES training(`id`)
);

-- Create table for trainers
CREATE TABLE trainers (
  `id` INT AUTO_INCREMENT,
  `trainer_name` VARCHAR(255) NOT NULL,
  `expertise` VARCHAR(255) NOT NULL,
  `contact_info` VARCHAR(255),
  PRIMARY KEY (`id`)
);

-- Update training table to include foreign key to trainers
ALTER TABLE training
ADD COLUMN `trainer_id` INT,
ADD FOREIGN KEY (`trainer_id`) REFERENCES trainers(`id`);

-- Drop trainer column from training table
ALTER TABLE training
DROP COLUMN `trainer`;

-- Create indexes on foreign key columns
CREATE INDEX idx_permanent_staffing_employee_id ON permanent_staffing (employee_id);
CREATE INDEX idx_temporary_staffing_temp_employee_id ON temporary_staffing (temp_employee_id);
CREATE INDEX idx_employee_training_employee_id ON employee_training (employee_id);
CREATE INDEX idx_employee_training_training_id ON employee_training (training_id);
CREATE INDEX idx_training_sessions_training_id ON training_sessions (training_id);
CREATE INDEX idx_training_trainer_id ON training (trainer_id);
```
