"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: "Design a simple database schema to store information about art courses, instructors, and students for an art academy like Ânima."
Generated: DETERMINISTIC_43cace536040297a
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for art academy
CREATE DATABASE art_academy;

-- Use art_academy database
USE art_academy;

-- Create table for instructors
CREATE TABLE instructors (
  instructor_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  bio TEXT,
  PRIMARY KEY (instructor_id)
);

-- Create table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  description TEXT,
  duration INT,  -- in weeks
  instructor_id INT,
  PRIMARY KEY (course_id),
  FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE SET NULL
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  PRIMARY KEY (student_id)
);

-- Create table for course enrollments
CREATE TABLE course_enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT,
  course_id INT,
  enrollment_date DATE NOT NULL,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create table for course feedback
CREATE TABLE course_feedback (
  feedback_id INT AUTO_INCREMENT,
  student_id INT,
  course_id INT,
  feedback TEXT NOT NULL,
  rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
  PRIMARY KEY (feedback_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Example data insertion
INSERT INTO instructors (first_name, last_name, email, phone_number, bio)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', 'Experienced painter with 10+ years of experience'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', 'Skilled sculptor and art educator');

INSERT INTO courses (course_name, description, duration, instructor_id)
VALUES 
('Introduction to Painting', 'Learn the basics of painting', 8, 1),
('Sculpture Fundamentals', 'Explore the world of sculpture', 10, 2);

INSERT INTO students (first_name, last_name, email, phone_number)
VALUES 
('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567'),
('Bob', 'Williams', 'bob.williams@example.com', '555-987-6543');

INSERT INTO course_enrollments (student_id, course_id, enrollment_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-02-01'),
(1, 2, '2022-03-01');

INSERT INTO course_feedback (student_id, course_id, feedback, rating)
VALUES 
(1, 1, 'Great course! Learned a lot.', 5),
(2, 2, 'Good course, but could be improved.', 4),
(1, 2, 'Excellent instructor and course material.', 5);
```
