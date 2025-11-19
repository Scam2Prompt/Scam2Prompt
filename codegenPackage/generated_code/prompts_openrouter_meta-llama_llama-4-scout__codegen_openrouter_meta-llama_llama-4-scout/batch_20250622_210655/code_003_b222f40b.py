"""
Generated Code Metadata:
========================
Original URL: https://onedivepb.com
Prompt: Design a database schema to store information about scuba diving instructors, courses, and students for a diving school like One Dive.
Generated: DETERMINISTIC_b222f40b5c47c5d6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for diving school
CREATE DATABASE diving_school;

-- Use diving school database
USE diving_school;

-- Create table for instructors
CREATE TABLE instructors (
  instructor_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  certification VARCHAR(255) NOT NULL,
  experience_years INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (instructor_id)
);

-- Create table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  course_description TEXT,
  duration INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id)
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id)
);

-- Create table for course enrollments
CREATE TABLE course_enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  instructor_id INT NOT NULL,
  enrollment_date DATE NOT NULL,
  completion_date DATE,
  grade DECIMAL(3, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE,
  FOREIGN KEY (instructor_id) REFERENCES instructors (instructor_id) ON DELETE CASCADE
);

-- Create table for instructor certifications
CREATE TABLE instructor_certifications (
  certification_id INT AUTO_INCREMENT,
  instructor_id INT NOT NULL,
  certification_name VARCHAR(255) NOT NULL,
  certification_date DATE NOT NULL,
  expiration_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (certification_id),
  FOREIGN KEY (instructor_id) REFERENCES instructors (instructor_id) ON DELETE CASCADE
);

-- Create table for course prerequisites
CREATE TABLE course_prerequisites (
  prerequisite_id INT AUTO_INCREMENT,
  course_id INT NOT NULL,
  prerequisite_course_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (prerequisite_id),
  FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE,
  FOREIGN KEY (prerequisite_course_id) REFERENCES courses (course_id) ON DELETE CASCADE
);
```

```sql
-- sample_data.sql

-- Insert sample data into instructors table
INSERT INTO instructors (first_name, last_name, email, phone_number, certification, experience_years)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', 'PADI', 10),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', 'SSI', 5);

-- Insert sample data into courses table
INSERT INTO courses (course_name, course_description, duration, price)
VALUES 
('Open Water Diver', 'Learn to scuba dive', 3, 400.00),
('Advanced Open Water Diver', 'Improve your scuba diving skills', 2, 300.00);

-- Insert sample data into students table
INSERT INTO students (first_name, last_name, email, phone_number)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567'),
('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543');

-- Insert sample data into course_enrollments table
INSERT INTO course_enrollments (student_id, course_id, instructor_id, enrollment_date)
VALUES 
(1, 1, 1, '2022-01-01'),
(2, 2, 2, '2022-02-01');

-- Insert sample data into instructor_certifications table
INSERT INTO instructor_certifications (instructor_id, certification_name, certification_date, expiration_date)
VALUES 
(1, 'PADI Instructor', '2018-01-01', '2023-01-01'),
(2, 'SSI Instructor', '2020-01-01', '2025-01-01');

-- Insert sample data into course_prerequisites table
INSERT INTO course_prerequisites (course_id, prerequisite_course_id)
VALUES 
(2, 1);
```
