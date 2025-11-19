"""
Generated Code Metadata:
========================
Original URL: https://iedeoccidente.edu.co
Prompt: "Design a database schema for managing student records, including student information, grades, and attendance, for an institution with primary and secondary education sections like IEO."
Generated: DETERMINISTIC_f5bce4d10d6edf8f
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for managing student records
CREATE DATABASE ieo_education;

-- Use the created database
USE ieo_education;

-- Create table for education sections
CREATE TABLE education_sections (
  `section_id` INT AUTO_INCREMENT,
  `section_name` VARCHAR(255) NOT NULL,
  `section_type` ENUM('primary', 'secondary') NOT NULL,
  PRIMARY KEY (`section_id`),
  UNIQUE KEY (`section_name`)
);

-- Create table for student information
CREATE TABLE students (
  `student_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `date_of_birth` DATE NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  `section_id` INT NOT NULL,
  PRIMARY KEY (`student_id`),
  FOREIGN KEY (`section_id`) REFERENCES education_sections(`section_id`)
);

-- Create table for teachers
CREATE TABLE teachers (
  `teacher_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  PRIMARY KEY (`teacher_id`)
);

-- Create table for classes
CREATE TABLE classes (
  `class_id` INT AUTO_INCREMENT,
  `class_name` VARCHAR(255) NOT NULL,
  `section_id` INT NOT NULL,
  `teacher_id` INT NOT NULL,
  PRIMARY KEY (`class_id`),
  FOREIGN KEY (`section_id`) REFERENCES education_sections(`section_id`),
  FOREIGN KEY (`teacher_id`) REFERENCES teachers(`teacher_id`)
);

-- Create table for student classes
CREATE TABLE student_classes (
  `student_id` INT NOT NULL,
  `class_id` INT NOT NULL,
  PRIMARY KEY (`student_id`, `class_id`),
  FOREIGN KEY (`student_id`) REFERENCES students(`student_id`),
  FOREIGN KEY (`class_id`) REFERENCES classes(`class_id`)
);

-- Create table for grades
CREATE TABLE grades (
  `grade_id` INT AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `class_id` INT NOT NULL,
  `subject` VARCHAR(255) NOT NULL,
  `grade` DECIMAL(3, 2) NOT NULL,
  PRIMARY KEY (`grade_id`),
  FOREIGN KEY (`student_id`) REFERENCES students(`student_id`),
  FOREIGN KEY (`class_id`) REFERENCES classes(`class_id`)
);

-- Create table for attendance
CREATE TABLE attendance (
  `attendance_id` INT AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `class_id` INT NOT NULL,
  `attendance_date` DATE NOT NULL,
  `is_present` BOOLEAN NOT NULL DEFAULT 0,
  PRIMARY KEY (`attendance_id`),
  FOREIGN KEY (`student_id`) REFERENCES students(`student_id`),
  FOREIGN KEY (`class_id`) REFERENCES classes(`class_id`)
);

-- Insert sample data into education sections
INSERT INTO education_sections (`section_name`, `section_type`)
VALUES 
('Primary Section', 'primary'),
('Secondary Section', 'secondary');

-- Insert sample data into teachers
INSERT INTO teachers (`first_name`, `last_name`, `email`, `phone_number`, `address`)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210', '456 Elm St');

-- Insert sample data into classes
INSERT INTO classes (`class_name`, `section_id`, `teacher_id`)
VALUES 
('Class 1', 1, 1),
('Class 2', 2, 2);

-- Insert sample data into students
INSERT INTO students (`first_name`, `last_name`, `date_of_birth`, `email`, `phone_number`, `address`, `section_id`)
VALUES 
('Student1', 'Lastname1', '2000-01-01', 'student1@example.com', '1234567890', '123 Main St', 1),
('Student2', 'Lastname2', '2001-01-01', 'student2@example.com', '9876543210', '456 Elm St', 2);

-- Insert sample data into student classes
INSERT INTO student_classes (`student_id`, `class_id`)
VALUES 
(1, 1),
(2, 2);

-- Insert sample data into grades
INSERT INTO grades (`student_id`, `class_id`, `subject`, `grade`)
VALUES 
(1, 1, 'Math', 85.00),
(2, 2, 'English', 90.00);

-- Insert sample data into attendance
INSERT INTO attendance (`student_id`, `class_id`, `attendance_date`, `is_present`)
VALUES 
(1, 1, '2022-01-01', 1),
(2, 2, '2022-01-01', 0);
```
