"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: "Design a database schema for managing information about students, courses, and certifications at an institution like Trentino Juan Pablo II."
Generated: DETERMINISTIC_d2d10cc4eab4e4b5
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the institution
CREATE DATABASE trentino_juan_pablo_ii;

-- Use the created database
USE trentino_juan_pablo_ii;

-- Create a table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  date_of_birth DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id)
);

-- Create a table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  course_description TEXT,
  credits INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id)
);

-- Create a table for certifications
CREATE TABLE certifications (
  certification_id INT AUTO_INCREMENT,
  certification_name VARCHAR(255) NOT NULL,
  certification_description TEXT,
  issuing_organization VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (certification_id)
);

-- Create a table for student enrollments in courses
CREATE TABLE student_enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  enrollment_date DATE,
  grade DECIMAL(3,2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE
);

-- Create a table for student certifications
CREATE TABLE student_certifications (
  certification_id INT NOT NULL,
  student_id INT NOT NULL,
  issuance_date DATE,
  expiration_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (certification_id, student_id),
  FOREIGN KEY (certification_id) REFERENCES certifications (certification_id) ON DELETE CASCADE,
  FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE
);

-- Create a trigger to prevent inserting a student with an existing email
DELIMITER $$
CREATE TRIGGER prevent_duplicate_email
BEFORE INSERT ON students
FOR EACH ROW
BEGIN
  IF EXISTS (SELECT 1 FROM students WHERE email = NEW.email) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Email already exists';
  END IF;
END$$
DELIMITER ;

-- Create a stored procedure to enroll a student in a course
DELIMITER $$
CREATE PROCEDURE enroll_student_in_course(
  IN p_student_id INT,
  IN p_course_id INT
)
BEGIN
  IF NOT EXISTS (SELECT 1 FROM students WHERE student_id = p_student_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Student does not exist';
  END IF;

  IF NOT EXISTS (SELECT 1 FROM courses WHERE course_id = p_course_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Course does not exist';
  END IF;

  INSERT INTO student_enrollments (student_id, course_id) VALUES (p_student_id, p_course_id);
END$$
DELIMITER ;

-- Create a stored procedure to add a certification to a student
DELIMITER $$
CREATE PROCEDURE add_certification_to_student(
  IN p_certification_id INT,
  IN p_student_id INT,
  IN p_issuance_date DATE,
  IN p_expiration_date DATE
)
BEGIN
  IF NOT EXISTS (SELECT 1 FROM certifications WHERE certification_id = p_certification_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Certification does not exist';
  END IF;

  IF NOT EXISTS (SELECT 1 FROM students WHERE student_id = p_student_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Student does not exist';
  END IF;

  INSERT INTO student_certifications (certification_id, student_id, issuance_date, expiration_date)
  VALUES (p_certification_id, p_student_id, p_issuance_date, p_expiration_date);
END$$
DELIMITER ;
```
