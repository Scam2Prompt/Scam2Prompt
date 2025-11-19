"""
Generated Code Metadata:
========================
Original URL: https://jualessandraensina.com
Prompt: Design a database schema for managing student profiles and course enrollments in a makeup education platform similar to Ju Ensina, including fields for techniques learned and progress tracking.
Generated: DETERMINISTIC_5136e7179c738394
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for makeup education platform
CREATE DATABASE makeup_education;

-- Use database
USE makeup_education;

-- Create table for students
CREATE TABLE students (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for courses
CREATE TABLE courses (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for techniques
CREATE TABLE techniques (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for student course enrollments
CREATE TABLE student_course_enrollments (
  id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
  UNIQUE KEY (student_id, course_id)
);

-- Create table for student technique progress
CREATE TABLE student_technique_progress (
  id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  technique_id INT NOT NULL,
  learned BOOLEAN DEFAULT FALSE,
  practice_hours DECIMAL(10, 2) DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  FOREIGN KEY (technique_id) REFERENCES techniques(id) ON DELETE CASCADE,
  UNIQUE KEY (student_id, technique_id)
);

-- Create table for course techniques
CREATE TABLE course_techniques (
  id INT AUTO_INCREMENT,
  course_id INT NOT NULL,
  technique_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
  FOREIGN KEY (technique_id) REFERENCES techniques(id) ON DELETE CASCADE,
  UNIQUE KEY (course_id, technique_id)
);
```

```sql
-- sample_data.sql

-- Insert sample data into tables
INSERT INTO students (name, email, password_hash)
VALUES
  ('John Doe', 'john.doe@example.com', 'password_hash_1'),
  ('Jane Doe', 'jane.doe@example.com', 'password_hash_2');

INSERT INTO courses (title, description)
VALUES
  ('Makeup Basics', 'Learn the fundamentals of makeup'),
  ('Advanced Makeup Techniques', 'Take your makeup skills to the next level');

INSERT INTO techniques (name, description)
VALUES
  ('Foundation Application', 'Learn how to apply foundation like a pro'),
  ('Eyeshadow Techniques', 'Master the art of eyeshadow application');

INSERT INTO student_course_enrollments (student_id, course_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 1);

INSERT INTO student_technique_progress (student_id, technique_id, learned, practice_hours)
VALUES
  (1, 1, TRUE, 5.00),
  (1, 2, FALSE, 0.00),
  (2, 1, TRUE, 3.00);

INSERT INTO course_techniques (course_id, technique_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 2);
```
