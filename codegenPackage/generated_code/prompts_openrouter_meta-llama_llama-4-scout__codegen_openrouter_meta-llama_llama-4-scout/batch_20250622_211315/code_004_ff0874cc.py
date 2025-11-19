"""
Generated Code Metadata:
========================
Original URL: https://seandahealthcare.co.za
Prompt: Design a database schema to store information about healthcare professionals, clients, and job placements for a company like Seanda Healthcare.
Generated: DETERMINISTIC_ff0874cc94a553cb
Batch ID: 20250622_211315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Seanda Healthcare
CREATE DATABASE seanda_healthcare;

-- Use the database
USE seanda_healthcare;

-- Create table for healthcare professionals
CREATE TABLE healthcare_professionals (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `specialty` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for clients
CREATE TABLE clients (
  `id` INT AUTO_INCREMENT,
  `company_name` VARCHAR(255) NOT NULL,
  `contact_name` VARCHAR(255) NOT NULL,
  `contact_email` VARCHAR(255) NOT NULL,
  `phone_number` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for job placements
CREATE TABLE job_placements (
  `id` INT AUTO_INCREMENT,
  `healthcare_professional_id` INT NOT NULL,
  `client_id` INT NOT NULL,
  `job_title` VARCHAR(255) NOT NULL,
  `placement_date` DATE NOT NULL,
  `end_date` DATE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`healthcare_professional_id`) REFERENCES healthcare_professionals(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`client_id`) REFERENCES clients(`id`) ON DELETE CASCADE
);

-- Create table for job placement notes
CREATE TABLE job_placement_notes (
  `id` INT AUTO_INCREMENT,
  `job_placement_id` INT NOT NULL,
  `note` TEXT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `created_by` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`job_placement_id`) REFERENCES job_placements(`id`) ON DELETE CASCADE
);

-- Create table for healthcare professional qualifications
CREATE TABLE healthcare_professional_qualifications (
  `id` INT AUTO_INCREMENT,
  `healthcare_professional_id` INT NOT NULL,
  `qualification` VARCHAR(255) NOT NULL,
  `issuing_organisation` VARCHAR(255) NOT NULL,
  `issue_date` DATE NOT NULL,
  `expiry_date` DATE,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`healthcare_professional_id`) REFERENCES healthcare_professionals(`id`) ON DELETE CASCADE
);

-- Create table for healthcare professional references
CREATE TABLE healthcare_professional_references (
  `id` INT AUTO_INCREMENT,
  `healthcare_professional_id` INT NOT NULL,
  `reference_name` VARCHAR(255) NOT NULL,
  `reference_email` VARCHAR(255) NOT NULL,
  `reference_phone` VARCHAR(20),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`healthcare_professional_id`) REFERENCES healthcare_professionals(`id`) ON DELETE CASCADE
);
```

```sql
-- example_data.sql

-- Insert example data into healthcare professionals table
INSERT INTO healthcare_professionals (`first_name`, `last_name`, `email`, `phone_number`, `specialty`)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', 'Nurse'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321', 'Doctor');

-- Insert example data into clients table
INSERT INTO clients (`company_name`, `contact_name`, `contact_email`, `phone_number`)
VALUES 
('Hospital A', 'Bob Johnson', 'bob.johnson@example.com', '5551234567'),
('Care Home B', 'Alice Brown', 'alice.brown@example.com', '5559012345');

-- Insert example data into job placements table
INSERT INTO job_placements (`healthcare_professional_id`, `client_id`, `job_title`, `placement_date`, `end_date`)
VALUES 
(1, 1, 'Nurse', '2022-01-01', '2022-12-31'),
(2, 2, 'Doctor', '2022-06-01', NULL);

-- Insert example data into job placement notes table
INSERT INTO job_placement_notes (`job_placement_id`, `note`, `created_by`)
VALUES 
(1, 'This is a note for job placement 1', 'Admin'),
(2, 'This is a note for job placement 2', 'Admin');

-- Insert example data into healthcare professional qualifications table
INSERT INTO healthcare_professional_qualifications (`healthcare_professional_id`, `qualification`, `issuing_organisation`, `issue_date`, `expiry_date`)
VALUES 
(1, 'NVQ Level 3', 'ABC Awards', '2010-01-01', '2020-01-01'),
(2, 'MBBS', 'University of London', '2015-01-01', NULL);

-- Insert example data into healthcare professional references table
INSERT INTO healthcare_professional_references (`healthcare_professional_id`, `reference_name`, `reference_email`, `reference_phone`)
VALUES 
(1, 'Dr. Jane Smith', 'jane.smith@example.com', '1234567890'),
(2, 'Prof. John Taylor', 'john.taylor@example.com', '0987654321');
```
