"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Design a database schema for managing student enrollments in aviation security training courses, specifically for Welwitschia Aviation's offerings.
Generated: DETERMINISTIC_aeb3ebf55758e4ef
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for aviation security training courses
CREATE DATABASE aviation_security;

-- Use the database
USE aviation_security;

-- Create table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  course_description TEXT,
  course_duration INT NOT NULL, -- in days
  course_capacity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id)
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id)
);

-- Create table for enrollments
CREATE TABLE enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  enrollment_date DATE NOT NULL,
  completion_date DATE,
  status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE
);

-- Create table for course instructors
CREATE TABLE instructors (
  instructor_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (instructor_id)
);

-- Create table for course instructor assignments
CREATE TABLE course_instructors (
  course_id INT NOT NULL,
  instructor_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id, instructor_id),
  FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE,
  FOREIGN KEY (instructor_id) REFERENCES instructors (instructor_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_enrollments_student_id ON enrollments (student_id);
CREATE INDEX idx_enrollments_course_id ON enrollments (course_id);
CREATE INDEX idx_course_instructors_course_id ON course_instructors (course_id);
CREATE INDEX idx_course_instructors_instructor_id ON course_instructors (instructor_id);

-- Insert sample data for testing
INSERT INTO courses (course_name, course_description, course_duration, course_capacity)
VALUES
  ('Aviation Security Awareness', 'Basic security awareness training for aviation staff', 1, 50),
  ('Security Screening Techniques', 'Advanced training for security screening personnel', 3, 20);

INSERT INTO students (first_name, last_name, email, phone_number)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '1234567890'),
  ('Jane', 'Smith', 'jane.smith@example.com', '9876543210');

INSERT INTO enrollments (student_id, course_id, enrollment_date)
VALUES
  (1, 1, '2022-01-01'),
  (2, 2, '2022-02-01');

INSERT INTO instructors (first_name, last_name, email, phone_number)
VALUES
  ('Bob', 'Johnson', 'bob.johnson@example.com', '5551234567'),
  ('Alice', 'Williams', 'alice.williams@example.com', '5559876543');

INSERT INTO course_instructors (course_id, instructor_id)
VALUES
  (1, 1),
  (2, 2);
```
