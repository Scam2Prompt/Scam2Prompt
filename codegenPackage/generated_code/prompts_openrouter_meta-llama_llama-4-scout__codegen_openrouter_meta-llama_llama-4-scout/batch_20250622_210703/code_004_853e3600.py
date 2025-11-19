"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Design a database schema to store information about ENEM preparation courses, including details about professors, lessons, and student progress, inspired by the Maratona do ENEM platform."
Generated: DETERMINISTIC_853e3600f2a64e74
Batch ID: 20250622_210703
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/math-material.pdf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/science-material.pdf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- Create database schema for ENEM preparation courses
CREATE DATABASE enem_courses;

-- Use the database schema
USE enem_courses;

-- Create table for professors
CREATE TABLE professors (
  professor_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (professor_id)
);

-- Create table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  professor_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id),
  FOREIGN KEY (professor_id) REFERENCES professors(professor_id)
);

-- Create table for lessons
CREATE TABLE lessons (
  lesson_id INT AUTO_INCREMENT,
  course_id INT,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (lesson_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id)
);

-- Create table for student courses
CREATE TABLE student_courses (
  student_id INT,
  course_id INT,
  enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Create table for lesson progress
CREATE TABLE lesson_progress (
  student_id INT,
  lesson_id INT,
  completed BOOLEAN DEFAULT FALSE,
  score DECIMAL(3, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id, lesson_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id)
);

-- Create table for course materials
CREATE TABLE course_materials (
  material_id INT AUTO_INCREMENT,
  course_id INT,
  title VARCHAR(255) NOT NULL,
  file_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (material_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Example data insertion
INSERT INTO professors (name, email, phone_number)
VALUES 
('John Doe', 'john.doe@example.com', '1234567890'),
('Jane Doe', 'jane.doe@example.com', '9876543210');

INSERT INTO courses (title, description, professor_id)
VALUES 
('ENEM Math', 'ENEM math preparation course', 1),
('ENEM Science', 'ENEM science preparation course', 2);

INSERT INTO lessons (course_id, title, content)
VALUES 
(1, 'Math Lesson 1', 'This is the content of math lesson 1'),
(1, 'Math Lesson 2', 'This is the content of math lesson 2'),
(2, 'Science Lesson 1', 'This is the content of science lesson 1');

INSERT INTO students (name, email, phone_number)
VALUES 
('Student 1', 'student1@example.com', '1234567890'),
('Student 2', 'student2@example.com', '9876543210');

INSERT INTO student_courses (student_id, course_id)
VALUES 
(1, 1),
(2, 2);

INSERT INTO lesson_progress (student_id, lesson_id, completed, score)
VALUES 
(1, 1, TRUE, 0.8),
(1, 2, FALSE, NULL),
(2, 3, TRUE, 0.9);

INSERT INTO course_materials (course_id, title, file_url)
VALUES 
(1, 'Math Course Material', 'https://example.com/math-material.pdf'),
(2, 'Science Course Material', 'https://example.com/science-material.pdf');
```
