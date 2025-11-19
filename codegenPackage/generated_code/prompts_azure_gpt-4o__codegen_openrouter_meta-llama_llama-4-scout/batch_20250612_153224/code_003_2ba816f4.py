"""
Generated Code Metadata:
========================
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Develop a database schema for managing student records, including fields for academic history, workshop enrollment, and administrative requests, as outlined in the FAQ section of the Escuela Preparatoria Oficial N.73 website.
Generated: DETERMINISTIC_2ba816f4b47abf19
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for managing student records
CREATE DATABASE student_records;

-- Use the database
USE student_records;

-- Create a table for students
CREATE TABLE students (
  `student_id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `date_of_birth` DATE NOT NULL,
  `enrollment_date` DATE NOT NULL,
  PRIMARY KEY (`student_id`)
);

-- Create a table for academic history
CREATE TABLE academic_history (
  `academic_history_id` INT AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `semester` INT NOT NULL,
  `year` INT NOT NULL,
  `gpa` DECIMAL(3, 2) NOT NULL,
  `credits_earned` INT NOT NULL,
  PRIMARY KEY (`academic_history_id`),
  FOREIGN KEY (`student_id`) REFERENCES students(`student_id`)
);

-- Create a table for workshops
CREATE TABLE workshops (
  `workshop_id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE NOT NULL,
  PRIMARY KEY (`workshop_id`)
);

-- Create a table for workshop enrollment
CREATE TABLE workshop_enrollment (
  `enrollment_id` INT AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `workshop_id` INT NOT NULL,
  `enrollment_date` DATE NOT NULL,
  PRIMARY KEY (`enrollment_id`),
  FOREIGN KEY (`student_id`) REFERENCES students(`student_id`),
  FOREIGN KEY (`workshop_id`) REFERENCES workshops(`workshop_id`)
);

-- Create a table for administrative requests
CREATE TABLE administrative_requests (
  `request_id` INT AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `request_type` ENUM('transcript', 'diploma', 'other') NOT NULL,
  `request_date` DATE NOT NULL,
  `status` ENUM('pending', 'approved', 'denied') NOT NULL DEFAULT 'pending',
  `comments` TEXT,
  PRIMARY KEY (`request_id`),
  FOREIGN KEY (`student_id`) REFERENCES students(`student_id`)
);

-- Create a table for request updates
CREATE TABLE request_updates (
  `update_id` INT AUTO_INCREMENT,
  `request_id` INT NOT NULL,
  `update_date` DATE NOT NULL,
  `update_by` VARCHAR(255) NOT NULL,
  `update_comments` TEXT NOT NULL,
  PRIMARY KEY (`update_id`),
  FOREIGN KEY (`request_id`) REFERENCES administrative_requests(`request_id`)
);

-- Insert sample data into students table
INSERT INTO students (`name`, `email`, `date_of_birth`, `enrollment_date`)
VALUES 
('John Doe', 'john.doe@example.com', '2000-01-01', '2020-01-01'),
('Jane Doe', 'jane.doe@example.com', '2001-01-01', '2021-01-01');

-- Insert sample data into academic_history table
INSERT INTO academic_history (`student_id`, `semester`, `year`, `gpa`, `credits_earned`)
VALUES 
(1, 1, 2020, 3.5, 30),
(1, 2, 2020, 3.7, 30),
(2, 1, 2021, 3.2, 30);

-- Insert sample data into workshops table
INSERT INTO workshops (`name`, `description`, `start_date`, `end_date`)
VALUES 
('Workshop 1', 'This is workshop 1', '2022-01-01', '2022-01-05'),
('Workshop 2', 'This is workshop 2', '2022-06-01', '2022-06-05');

-- Insert sample data into workshop_enrollment table
INSERT INTO workshop_enrollment (`student_id`, `workshop_id`, `enrollment_date`)
VALUES 
(1, 1, '2021-12-20'),
(2, 1, '2021-12-25'),
(1, 2, '2022-05-20');

-- Insert sample data into administrative_requests table
INSERT INTO administrative_requests (`student_id`, `request_type`, `request_date`, `status`, `comments`)
VALUES 
(1, 'transcript', '2022-01-10', 'pending', 'Please provide transcript for spring 2021'),
(2, 'diploma', '2022-06-15', 'approved', 'Diploma has been mailed');

-- Insert sample data into request_updates table
INSERT INTO request_updates (`request_id`, `update_date`, `update_by`, `update_comments`)
VALUES 
(1, '2022-01-15', 'admin', 'Request received and being processed'),
(1, '2022-01-20', 'admin', 'Transcript has been prepared and is ready for pickup'),
(2, '2022-06-20', 'admin', 'Diploma has been mailed to the student');
```
