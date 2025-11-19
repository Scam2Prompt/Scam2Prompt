"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Design a database schema to store information about underprivileged children and their education progress, similar to Indological India's education empowerment programs.
Generated: DETERMINISTIC_b21d644357eec457
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for education empowerment programs
CREATE DATABASE education_empowerment;

-- Use the database
USE education_empowerment;

-- Create table for underprivileged children
CREATE TABLE children (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `date_of_birth` DATE NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `contact_number` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for schools/educational institutions
CREATE TABLE schools (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `contact_number` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for teachers/educators
CREATE TABLE teachers (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `date_of_birth` DATE NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `contact_number` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for education programs
CREATE TABLE programs (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for child education progress
CREATE TABLE child_progress (
  `id` INT AUTO_INCREMENT,
  `child_id` INT NOT NULL,
  `program_id` INT NOT NULL,
  `school_id` INT,
  `teacher_id` INT,
  `current_level` VARCHAR(255),
  `last_updated` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`child_id`) REFERENCES children(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`program_id`) REFERENCES programs(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`school_id`) REFERENCES schools(`id`) ON DELETE SET NULL,
  FOREIGN KEY (`teacher_id`) REFERENCES teachers(`id`) ON DELETE SET NULL
);

-- Create table for assessments/evaluations
CREATE TABLE assessments (
  `id` INT AUTO_INCREMENT,
  `child_id` INT NOT NULL,
  `program_id` INT NOT NULL,
  `assessment_date` DATE NOT NULL,
  `score` DECIMAL(3,2),
  `comments` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`child_id`) REFERENCES children(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`program_id`) REFERENCES programs(`id`) ON DELETE CASCADE
);

-- Create table for donations
CREATE TABLE donations (
  `id` INT AUTO_INCREMENT,
  `donor_name` VARCHAR(255) NOT NULL,
  `donation_date` DATE NOT NULL,
  `amount` DECIMAL(10,2) NOT NULL,
  `program_id` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`program_id`) REFERENCES programs(`id`) ON DELETE SET NULL
);
```

```sql
-- sample_data.sql

-- Insert sample data into children table
INSERT INTO children (name, date_of_birth, address, contact_number)
VALUES 
('John Doe', '2010-01-01', '123 Main St', '1234567890'),
('Jane Doe', '2012-06-01', '456 Elm St', '9876543210');

-- Insert sample data into schools table
INSERT INTO schools (name, address, contact_number)
VALUES 
('Springfield Elementary', '789 Oak St', '5551234567'),
('Lincoln High School', '321 Maple St', '5559012345');

-- Insert sample data into teachers table
INSERT INTO teachers (name, date_of_birth, address, contact_number)
VALUES 
('Ms. Smith', '1980-03-01', '901 Broadway', '1112223333'),
('Mr. Johnson', '1975-09-01', '456 Cedar St', '4445556666');

-- Insert sample data into programs table
INSERT INTO programs (name, description)
VALUES 
('Literacy Program', 'Program to improve reading and writing skills'),
('Math Tutoring', 'Program to improve math skills');

-- Insert sample data into child_progress table
INSERT INTO child_progress (child_id, program_id, school_id, teacher_id, current_level)
VALUES 
(1, 1, 1, 1, 'Grade 5'),
(2, 2, 2, 2, 'Grade 3');

-- Insert sample data into assessments table
INSERT INTO assessments (child_id, program_id, assessment_date, score, comments)
VALUES 
(1, 1, '2022-06-01', 85.00, 'Good progress'),
(2, 2, '2022-12-01', 90.00, 'Excellent progress');

-- Insert sample data into donations table
INSERT INTO donations (donor_name, donation_date, amount, program_id)
VALUES 
('Anonymous', '2022-01-01', 1000.00, 1),
('John Q Public', '2022-06-01', 500.00, 2);
```
