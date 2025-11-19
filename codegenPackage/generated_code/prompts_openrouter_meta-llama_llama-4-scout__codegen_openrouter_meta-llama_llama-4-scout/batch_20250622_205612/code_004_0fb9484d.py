"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: "Create a basic structure for a school management system using a database, including tables for students, teachers, and courses, reflecting the bilingual education system of Del Sol Montessori."
Generated: DETERMINISTIC_0fb9484d0fad6b09
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for school management system
CREATE DATABASE del_sol_montessori;

-- Use the database
USE del_sol_montessori;

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id)
);

-- Create table for teachers
CREATE TABLE teachers (
  teacher_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (teacher_id)
);

-- Create table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  course_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id)
);

-- Create table for bilingual courses
CREATE TABLE bilingual_courses (
  bilingual_course_id INT AUTO_INCREMENT,
  course_id INT NOT NULL,
  language VARCHAR(50) NOT NULL CHECK (language IN ('English', 'Spanish')),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (bilingual_course_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Create table for student enrollments
CREATE TABLE student_enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  enrollment_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Create table for teacher assignments
CREATE TABLE teacher_assignments (
  assignment_id INT AUTO_INCREMENT,
  teacher_id INT NOT NULL,
  course_id INT NOT NULL,
  assignment_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Example insert statements
INSERT INTO students (first_name, last_name, date_of_birth, email, phone_number, address)
VALUES 
('John', 'Doe', '2000-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO teachers (first_name, last_name, email, phone_number, address)
VALUES 
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO courses (course_name, course_description)
VALUES 
('Math', 'Basic math course'),
('Science', 'Basic science course');

INSERT INTO bilingual_courses (course_id, language)
VALUES 
(1, 'English'),
(1, 'Spanish'),
(2, 'English'),
(2, 'Spanish');

INSERT INTO student_enrollments (student_id, course_id, enrollment_date)
VALUES 
(1, 1, '2022-01-01'),
(1, 2, '2022-01-15');

INSERT INTO teacher_assignments (teacher_id, course_id, assignment_date)
VALUES 
(1, 1, '2022-01-01'),
(1, 2, '2022-01-15');
```
