"""
Generated Code Metadata:
========================
Original URL: https://colatraining.com
Prompt: Design a database schema to store information about training courses, instructors, and students for a company like CoLa Training Services that offers classroom-based and online training programs.
Generated: DETERMINISTIC_0a7a86bde4b98bfc
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for CoLa Training Services
CREATE DATABASE cola_training_services;

-- Use the database
USE cola_training_services;

-- Create table for instructors
CREATE TABLE instructors (
  instructor_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (instructor_id)
);

-- Create table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  description TEXT,
  course_type ENUM('classroom', 'online') NOT NULL,
  duration INT, -- in hours
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id)
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id)
);

-- Create table for course instructors
CREATE TABLE course_instructors (
  course_id INT NOT NULL,
  instructor_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id, instructor_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
  FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE
);

-- Create table for course enrollments
CREATE TABLE course_enrollments (
  course_id INT NOT NULL,
  student_id INT NOT NULL,
  enrollment_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id, student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- Create table for course sessions
CREATE TABLE course_sessions (
  session_id INT AUTO_INCREMENT,
  course_id INT NOT NULL,
  session_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  location VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (session_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create table for attendance
CREATE TABLE attendance (
  session_id INT NOT NULL,
  student_id INT NOT NULL,
  attended BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (session_id, student_id),
  FOREIGN KEY (session_id) REFERENCES course_sessions(session_id) ON DELETE CASCADE,
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);
```

```sql
-- example usage
DELIMITER //

CREATE PROCEDURE insert_instructor(
  IN p_first_name VARCHAR(50),
  IN p_last_name VARCHAR(50),
  IN p_email VARCHAR(100)
)
BEGIN
  INSERT INTO instructors (first_name, last_name, email)
  VALUES (p_first_name, p_last_name, p_email);
END //

DELIMITER ;

CALL insert_instructor('John', 'Doe', 'john.doe@example.com');

DELIMITER //

CREATE PROCEDURE insert_course(
  IN p_title VARCHAR(100),
  IN p_description TEXT,
  IN p_course_type ENUM('classroom', 'online'),
  IN p_duration INT
)
BEGIN
  INSERT INTO courses (title, description, course_type, duration)
  VALUES (p_title, p_description, p_course_type, p_duration);
END //

DELIMITER ;

CALL insert_course('Introduction to Python', 'Learn the basics of Python programming', 'online', 40);

DELIMITER //

CREATE PROCEDURE enroll_student_in_course(
  IN p_course_id INT,
  IN p_student_id INT
)
BEGIN
  INSERT INTO course_enrollments (course_id, student_id, enrollment_date)
  VALUES (p_course_id, p_student_id, CURDATE());
END //

DELIMITER ;

CALL enroll_student_in_course(1, 1);
```
