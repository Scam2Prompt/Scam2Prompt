"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: "Design a database schema to store information about students, courses, and programs at an online university like CNU."
Generated: DETERMINISTIC_bcbdbf25ccc9143a
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the online university
CREATE DATABASE online_university;

-- Use the database
USE online_university;

-- Create a table to store information about programs
CREATE TABLE programs (
  program_id INT AUTO_INCREMENT,
  program_name VARCHAR(255) NOT NULL,
  program_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (program_id)
);

-- Create a table to store information about courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  course_description TEXT,
  course_credits INT,
  program_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
);

-- Create a table to store information about students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  program_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE SET NULL
);

-- Create a table to store information about course enrollments
CREATE TABLE course_enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT,
  course_id INT,
  enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
  UNIQUE KEY (student_id, course_id)
);

-- Create a table to store information about course grades
CREATE TABLE course_grades (
  grade_id INT AUTO_INCREMENT,
  enrollment_id INT,
  grade DECIMAL(3, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (grade_id),
  FOREIGN KEY (enrollment_id) REFERENCES course_enrollments(enrollment_id) ON DELETE CASCADE
);

-- Example data for testing
INSERT INTO programs (program_name, program_description)
VALUES
  ('Computer Science', 'A program in computer science'),
  ('Mathematics', 'A program in mathematics');

INSERT INTO courses (course_name, course_description, course_credits, program_id)
VALUES
  ('Introduction to Programming', 'An introduction to programming', 3, 1),
  ('Data Structures', 'A course on data structures', 4, 1),
  ('Calculus I', 'A course on calculus', 4, 2);

INSERT INTO students (first_name, last_name, email, password_hash, program_id)
VALUES
  ('John', 'Doe', 'john.doe@example.com', 'password_hash', 1),
  ('Jane', 'Doe', 'jane.doe@example.com', 'password_hash', 2);

INSERT INTO course_enrollments (student_id, course_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 3);

INSERT INTO course_grades (enrollment_id, grade)
VALUES
  (1, 3.50),
  (2, 3.75),
  (3, 3.25);
```
