"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Generate a sample database schema for Sakura Dance Studio's management system, including tables for instructors, students, classes, and performance opportunities.
Generated: DETERMINISTIC_f5e9ece430a6141b
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Sakura Dance Studio's management system
CREATE DATABASE sakura_dance_studio;

-- Use the database
USE sakura_dance_studio;

-- Create table for instructors
CREATE TABLE instructors (
  instructor_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  hire_date DATE NOT NULL,
  PRIMARY KEY (instructor_id)
);

-- Create table for classes
CREATE TABLE classes (
  class_id INT AUTO_INCREMENT,
  class_name VARCHAR(100) NOT NULL,
  class_description TEXT,
  class_capacity INT NOT NULL DEFAULT 10,
  class_schedule TIME NOT NULL,
  class_duration INT NOT NULL, -- in minutes
  instructor_id INT,
  PRIMARY KEY (class_id),
  FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE SET NULL
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  join_date DATE NOT NULL,
  PRIMARY KEY (student_id)
);

-- Create table for student-class enrollment
CREATE TABLE student_enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  class_id INT NOT NULL,
  enrollment_date DATE NOT NULL,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
  UNIQUE (student_id, class_id)
);

-- Create table for performance opportunities
CREATE TABLE performance_opportunities (
  opportunity_id INT AUTO_INCREMENT,
  opportunity_name VARCHAR(100) NOT NULL,
  opportunity_date DATE NOT NULL,
  opportunity_description TEXT,
  PRIMARY KEY (opportunity_id)
);

-- Create table for student-performance opportunity participation
CREATE TABLE student_opportunities (
  participation_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  opportunity_id INT NOT NULL,
  participation_date DATE NOT NULL,
  PRIMARY KEY (participation_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (opportunity_id) REFERENCES performance_opportunities(opportunity_id) ON DELETE CASCADE,
  UNIQUE (student_id, opportunity_id)
);

-- Create table for instructor-performance opportunity participation
CREATE TABLE instructor_opportunities (
  instructor_id INT NOT NULL,
  opportunity_id INT NOT NULL,
  PRIMARY KEY (instructor_id, opportunity_id),
  FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE,
  FOREIGN KEY (opportunity_id) REFERENCES performance_opportunities(opportunity_id) ON DELETE CASCADE
);
```
