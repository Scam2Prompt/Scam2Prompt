"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Generate a sample database schema for storing information about vocational education and training programs, including courses like the Graduate Diploma of Management (Learning) (BSB80120) and Diploma of Community Services (CHC52021).
Generated: DETERMINISTIC_341ff88c935e4eb9
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- vocational_education_database.sql

-- Create database
CREATE DATABASE vocational_education;

-- Use database
USE vocational_education;

-- Create table for training programs
CREATE TABLE training_programs (
  program_id INT AUTO_INCREMENT,
  program_code VARCHAR(255) NOT NULL,
  program_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (program_id),
  UNIQUE KEY (program_code)
);

-- Create table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  course_code VARCHAR(255) NOT NULL,
  course_name VARCHAR(255) NOT NULL,
  program_id INT,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id),
  UNIQUE KEY (course_code),
  FOREIGN KEY (program_id) REFERENCES training_programs(program_id) ON DELETE SET NULL
);

-- Create table for course units
CREATE TABLE course_units (
  unit_id INT AUTO_INCREMENT,
  unit_code VARCHAR(255) NOT NULL,
  unit_name VARCHAR(255) NOT NULL,
  course_id INT,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (unit_id),
  UNIQUE KEY (unit_code),
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE SET NULL
);

-- Create table for training providers
CREATE TABLE training_providers (
  provider_id INT AUTO_INCREMENT,
  provider_name VARCHAR(255) NOT NULL,
  provider_code VARCHAR(255) NOT NULL,
  address VARCHAR(255),
  phone VARCHAR(20),
  email VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (provider_id),
  UNIQUE KEY (provider_code)
);

-- Create table for course offerings
CREATE TABLE course_offerings (
  offering_id INT AUTO_INCREMENT,
  course_id INT,
  provider_id INT,
  start_date DATE,
  end_date DATE,
  location VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (offering_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE SET NULL,
  FOREIGN KEY (provider_id) REFERENCES training_providers(provider_id) ON DELETE SET NULL
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  phone VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id),
  UNIQUE KEY (email)
);

-- Create table for student enrollments
CREATE TABLE student_enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT,
  offering_id INT,
  enrollment_date DATE,
  completion_date DATE,
  status VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE SET NULL,
  FOREIGN KEY (offering_id) REFERENCES course_offerings(offering_id) ON DELETE SET NULL
);

-- Insert sample data
INSERT INTO training_programs (program_code, program_name, description)
VALUES 
('BSB80120', 'Graduate Diploma of Management (Learning)', 'A graduate diploma program for management professionals'),
('CHC52021', 'Diploma of Community Services', 'A diploma program for community services professionals');

INSERT INTO courses (course_code, course_name, program_id, description)
VALUES 
('BSB80120', 'Graduate Diploma of Management (Learning)', 1, 'A graduate diploma course'),
('CHC52021', 'Diploma of Community Services', 2, 'A diploma course');

INSERT INTO course_units (unit_code, unit_name, course_id, description)
VALUES 
('BSBMGT801', 'Manage personal and professional development', 1, 'A unit of study'),
('CHCCOM002', 'Engage in community work', 2, 'A unit of study');

INSERT INTO training_providers (provider_name, provider_code, address, phone, email)
VALUES 
('ABC Training', 'ABCT', '123 Main St', '1234567890', 'info@abct.com.au'),
('XYZ Institute', 'XYZI', '456 Elm St', '9876543210', 'info@xyzi.edu.au');

INSERT INTO course_offerings (course_id, provider_id, start_date, end_date, location)
VALUES 
(1, 1, '2022-01-01', '2022-06-30', 'Sydney'),
(2, 2, '2022-07-01', '2022-12-31', 'Melbourne');

INSERT INTO students (first_name, last_name, email, phone, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
('Jane', 'Smith', 'jane.smith@example.com', '9876543210', '456 Elm St');

INSERT INTO student_enrollments (student_id, offering_id, enrollment_date, status)
VALUES 
(1, 1, '2022-01-01', 'Completed'),
(2, 2, '2022-07-01', 'In Progress');
```
