"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Create a sample database schema for a staffing agency that specializes in placing healthcare professionals, referencing the unique roles mentioned on Amazing Grace Medical Recruitment's site.
Generated: DETERMINISTIC_07c26b594a1daeef
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for staffing agency
CREATE DATABASE healthcare_staffing;

-- Use the database
USE healthcare_staffing;

-- Create table for healthcare professionals
CREATE TABLE healthcare_professionals (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  `city` VARCHAR(100),
  `state` VARCHAR(100),
  `zip` VARCHAR(20),
  `country` VARCHAR(100),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for job openings
CREATE TABLE job_openings (
  `id` INT AUTO_INCREMENT,
  `job_title` VARCHAR(255) NOT NULL,
  `job_description` TEXT NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  `job_type` ENUM('full-time', 'part-time', 'contract') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for job specialties
CREATE TABLE job_specialties (
  `id` INT AUTO_INCREMENT,
  `specialty_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Create table for healthcare professional certifications
CREATE TABLE healthcare_professional_certifications (
  `id` INT AUTO_INCREMENT,
  `healthcare_professional_id` INT NOT NULL,
  `certification_name` VARCHAR(255) NOT NULL,
  `certification_number` VARCHAR(255) NOT NULL,
  `expiration_date` DATE,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`healthcare_professional_id`) REFERENCES healthcare_professionals(`id`) ON DELETE CASCADE
);

-- Create table for healthcare professional experience
CREATE TABLE healthcare_professional_experience (
  `id` INT AUTO_INCREMENT,
  `healthcare_professional_id` INT NOT NULL,
  `job_title` VARCHAR(255) NOT NULL,
  `employer` VARCHAR(255) NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`healthcare_professional_id`) REFERENCES healthcare_professionals(`id`) ON DELETE CASCADE
);

-- Create table for job applications
CREATE TABLE job_applications (
  `id` INT AUTO_INCREMENT,
  `job_opening_id` INT NOT NULL,
  `healthcare_professional_id` INT NOT NULL,
  `application_date` DATE NOT NULL,
  `status` ENUM('pending', 'interviewing', 'placed', 'rejected') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`job_opening_id`) REFERENCES job_openings(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`healthcare_professional_id`) REFERENCES healthcare_professionals(`id`) ON DELETE CASCADE
);

-- Create table for job openings specialties
CREATE TABLE job_opening_specialties (
  `id` INT AUTO_INCREMENT,
  `job_opening_id` INT NOT NULL,
  `job_specialty_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`job_opening_id`) REFERENCES job_openings(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`job_specialty_id`) REFERENCES job_specialties(`id`) ON DELETE CASCADE,
  UNIQUE KEY (`job_opening_id`, `job_specialty_id`)
);

-- Insert sample job specialties
INSERT INTO job_specialties (specialty_name)
VALUES 
('Cardiology'),
('Oncology'),
('Neurology'),
('Pediatrics'),
('Emergency Medicine');

-- Insert sample job openings
INSERT INTO job_openings (job_title, job_description, location, job_type)
VALUES 
('Cardiothoracic Surgeon', 'Seeking a skilled cardiothoracic surgeon for a full-time position.', 'New York, NY', 'full-time'),
('Pediatric Nurse Practitioner', 'Seeking a pediatric nurse practitioner for a part-time position.', 'Chicago, IL', 'part-time'),
('Neurosurgeon', 'Seeking a skilled neurosurgeon for a full-time position.', 'Los Angeles, CA', 'full-time');

-- Insert sample healthcare professionals
INSERT INTO healthcare_professionals (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

-- Insert sample healthcare professional certifications
INSERT INTO healthcare_professional_certifications (healthcare_professional_id, certification_name, certification_number)
VALUES 
(1, 'Board Certified Cardiologist', '123456'),
(2, 'Board Certified Pediatrician', '789012');

-- Insert sample healthcare professional experience
INSERT INTO healthcare_professional_experience (healthcare_professional_id, job_title, employer, start_date, end_date)
VALUES 
(1, 'Cardiologist', 'ABC Hospital', '2010-01-01', NULL),
(2, 'Pediatrician', 'DEF Clinic', '2015-06-01', NULL);

-- Insert sample job applications
INSERT INTO job_applications (job_opening_id, healthcare_professional_id, application_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-06-01');
```
