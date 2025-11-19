"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Create a database schema for storing information about ENAFO's academic programs, including monitorías, modules, and seasonal offerings, along with student enrollment details.
Generated: DETERMINISTIC_af057e70c64c2fc8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- enafo_academic_programs.sql

-- Create database schema for ENAFO's academic programs
CREATE DATABASE enafo_academic_programs;

-- Use the database schema
USE enafo_academic_programs;

-- Create table for monitorías
CREATE TABLE monitorias (
  monitoria_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (monitoria_id)
);

-- Create table for modules
CREATE TABLE modules (
  module_id INT AUTO_INCREMENT,
  code VARCHAR(50) NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  credits INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (module_id)
);

-- Create table for seasonal offerings
CREATE TABLE seasonal_offerings (
  offering_id INT AUTO_INCREMENT,
  module_id INT,
  season VARCHAR(50) NOT NULL,
  year INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (offering_id),
  FOREIGN KEY (module_id) REFERENCES modules(module_id)
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id)
);

-- Create table for student enrollments
CREATE TABLE student_enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT,
  offering_id INT,
  monitoria_id INT,
  enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (offering_id) REFERENCES seasonal_offerings(offering_id),
  FOREIGN KEY (monitoria_id) REFERENCES monitorias(monitoria_id)
);

-- Create index on foreign key columns
CREATE INDEX idx_student_enrollments_student_id ON student_enrollments (student_id);
CREATE INDEX idx_student_enrollments_offering_id ON student_enrollments (offering_id);
CREATE INDEX idx_student_enrollments_monitoria_id ON student_enrollments (monitoria_id);
CREATE INDEX idx_seasonal_offerings_module_id ON seasonal_offerings (module_id);

-- Insert sample data for testing
INSERT INTO monitorias (name, description) 
VALUES 
('Monitoria 1', 'Description for Monitoria 1'),
('Monitoria 2', 'Description for Monitoria 2');

INSERT INTO modules (code, name, description, credits) 
VALUES 
('MOD-001', 'Module 1', 'Description for Module 1', 3),
('MOD-002', 'Module 2', 'Description for Module 2', 4);

INSERT INTO seasonal_offerings (module_id, season, year) 
VALUES 
(1, 'Spring', 2024),
(2, 'Fall', 2024);

INSERT INTO students (first_name, last_name, email) 
VALUES 
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Doe', 'jane.doe@example.com');

INSERT INTO student_enrollments (student_id, offering_id, monitoria_id) 
VALUES 
(1, 1, 1),
(2, 2, 2);
```
