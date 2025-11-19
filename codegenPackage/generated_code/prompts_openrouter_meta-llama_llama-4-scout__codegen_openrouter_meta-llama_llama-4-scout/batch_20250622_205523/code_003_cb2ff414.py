"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: "Design a database schema for storing student information, course enrollment, and progress tracking for an educational institution with programs like those offered by Sekolah Quran Indonesia."
Generated: DETERMINISTIC_cb2ff41425dcaae4
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for educational institution

CREATE DATABASE sekolah_quran_indonesia;

USE sekolah_quran_indonesia;

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address TEXT,
  date_of_birth DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id)
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

-- Create table for course enrollment
CREATE TABLE course_enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  enrollment_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE
);

-- Create table for progress tracking
CREATE TABLE progress_tracking (
  progress_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  module_name VARCHAR(255) NOT NULL,
  completion_date DATE,
  score DECIMAL(3, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (progress_id),
  FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE
);

-- Create table for instructors
CREATE TABLE instructors (
  instructor_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (instructor_id)
);

-- Create table for course instructors
CREATE TABLE course_instructors (
  course_id INT NOT NULL,
  instructor_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id, instructor_id),
  FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE,
  FOREIGN KEY (instructor_id) REFERENCES instructors (instructor_id) ON DELETE CASCADE
);

-- Example data insertion
INSERT INTO students (name, email, phone_number, address, date_of_birth)
VALUES 
('John Doe', 'john@example.com', '1234567890', 'Jl. Raya 123', '1990-01-01'),
('Jane Doe', 'jane@example.com', '0987654321', 'Jl. Raya 456', '1995-06-15');

INSERT INTO courses (course_name, course_description)
VALUES 
('Tafsir Quran', 'Understanding the interpretation of Quran'),
('Hadits Nabi', 'Study of the sayings and actions of Prophet Muhammad');

INSERT INTO course_enrollments (student_id, course_id, enrollment_date)
VALUES 
(1, 1, '2022-01-01'),
(1, 2, '2022-02-01'),
(2, 1, '2022-03-01');

INSERT INTO progress_tracking (student_id, course_id, module_name, completion_date, score)
VALUES 
(1, 1, 'Module 1', '2022-01-15', 85.00),
(1, 2, 'Module 2', '2022-02-15', 90.00),
(2, 1, 'Module 3', '2022-03-15', 78.00);

INSERT INTO instructors (name, email, phone_number, address)
VALUES 
('Instructors A', 'instructorA@example.com', '1111111111', 'Jl. Raya 789'),
('Instructors B', 'instructorB@example.com', '2222222222', 'Jl. Raya 321');

INSERT INTO course_instructors (course_id, instructor_id)
VALUES 
(1, 1),
(2, 2);
```
