"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Design a database schema to store information about students, courses (IELTS, PTE, Spoken English), and study abroad programs (e.g., USA, UK, Canada, Australia, Singapore) for a platform like Red & White International.
Generated: DETERMINISTIC_fcc756fb65f9a569
Batch ID: 20250622_205639
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
CREATE DATABASE red_and_white_international;

-- Use database
USE red_and_white_international;

-- Create table for countries
CREATE TABLE countries (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  iso_code CHAR(2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (iso_code)
);

-- Create table for study abroad programs
CREATE TABLE study_abroad_programs (
  id INT AUTO_INCREMENT,
  country_id INT NOT NULL,
  program_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (country_id) REFERENCES countries(id) ON DELETE CASCADE
);

-- Create table for courses
CREATE TABLE courses (
  id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for students
CREATE TABLE students (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for student courses
CREATE TABLE student_courses (
  id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  enrollment_date DATE,
  completion_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
  UNIQUE KEY (student_id, course_id)
);

-- Create table for student study abroad programs
CREATE TABLE student_programs (
  id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  program_id INT NOT NULL,
  application_date DATE,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  FOREIGN KEY (program_id) REFERENCES study_abroad_programs(id) ON DELETE CASCADE,
  UNIQUE KEY (student_id, program_id)
);

-- Insert sample data
INSERT INTO countries (name, iso_code)
VALUES 
('United States', 'US'),
('United Kingdom', 'GB'),
('Canada', 'CA'),
('Australia', 'AU'),
('Singapore', 'SG');

INSERT INTO study_abroad_programs (country_id, program_name, description)
VALUES 
(1, 'USA Study Abroad', 'Study in the United States'),
(2, 'UK Study Abroad', 'Study in the United Kingdom'),
(3, 'Canada Study Abroad', 'Study in Canada'),
(4, 'Australia Study Abroad', 'Study in Australia'),
(5, 'Singapore Study Abroad', 'Study in Singapore');

INSERT INTO courses (course_name, description)
VALUES 
('IELTS Preparation', 'IELTS preparation course'),
('PTE Preparation', 'PTE preparation course'),
('Spoken English', 'Spoken English course');

INSERT INTO students (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210');

INSERT INTO student_courses (student_id, course_id, enrollment_date)
VALUES 
(1, 1, '2022-01-01'),
(1, 2, '2022-02-01'),
(2, 3, '2022-03-01');

INSERT INTO student_programs (student_id, program_id, application_date)
VALUES 
(1, 1, '2022-01-15'),
(2, 2, '2022-02-15');
```
