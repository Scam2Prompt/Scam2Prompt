"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Design a database schema for Uni4Kashmir's student information system, including fields for student demographics, academic records, and course enrollment.
Generated: DETERMINISTIC_4731481b8cc54b68
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Uni4Kashmir's student information system
CREATE DATABASE uni4kashmir_sis;

-- Use the database
USE uni4kashmir_sis;

-- Create a table for student demographics
CREATE TABLE students (
  `student_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `date_of_birth` DATE NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` VARCHAR(255),
  `city` VARCHAR(100),
  `state` VARCHAR(100),
  `country` VARCHAR(100),
  `postal_code` VARCHAR(10),
  PRIMARY KEY (`student_id`)
);

-- Create a table for academic records
CREATE TABLE academic_records (
  `record_id` INT AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `semester` INT NOT NULL,
  `academic_year` INT NOT NULL,
  `gpa` DECIMAL(3, 2),
  `cgpa` DECIMAL(3, 2),
  PRIMARY KEY (`record_id`),
  FOREIGN KEY (`student_id`) REFERENCES students(`student_id`)
);

-- Create a table for courses
CREATE TABLE courses (
  `course_id` INT AUTO_INCREMENT,
  `course_code` VARCHAR(20) UNIQUE NOT NULL,
  `course_name` VARCHAR(100) NOT NULL,
  `credits` INT NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`course_id`)
);

-- Create a table for course enrollment
CREATE TABLE course_enrollments (
  `enrollment_id` INT AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  `semester` INT NOT NULL,
  `academic_year` INT NOT NULL,
  `grade` VARCHAR(2),
  PRIMARY KEY (`enrollment_id`),
  FOREIGN KEY (`student_id`) REFERENCES students(`student_id`),
  FOREIGN KEY (`course_id`) REFERENCES courses(`course_id`)
);

-- Create a table for faculty members
CREATE TABLE faculty_members (
  `faculty_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  PRIMARY KEY (`faculty_id`)
);

-- Create a table for course instructors
CREATE TABLE course_instructors (
  `course_id` INT NOT NULL,
  `faculty_id` INT NOT NULL,
  PRIMARY KEY (`course_id`, `faculty_id`),
  FOREIGN KEY (`course_id`) REFERENCES courses(`course_id`),
  FOREIGN KEY (`faculty_id`) REFERENCES faculty_members(`faculty_id`)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_academic_records_student_id ON academic_records (`student_id`);
CREATE INDEX idx_course_enrollments_student_id ON course_enrollments (`student_id`);
CREATE INDEX idx_course_enrollments_course_id ON course_enrollments (`course_id`);
CREATE INDEX idx_course_instructors_course_id ON course_instructors (`course_id`);
CREATE INDEX idx_course_instructors_faculty_id ON course_instructors (`faculty_id`);

-- Insert sample data
INSERT INTO students (`first_name`, `last_name`, `date_of_birth`, `email`, `phone_number`, `address`, `city`, `state`, `country`, `postal_code`)
VALUES 
('John', 'Doe', '1995-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', 'USA', '12345'),
('Jane', 'Smith', '1997-06-01', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', 'USA', '67890');

INSERT INTO academic_records (`student_id`, `semester`, `academic_year`, `gpa`, `cgpa`)
VALUES 
(1, 1, 2020, 3.5, 3.5),
(1, 2, 2021, 3.7, 3.6),
(2, 1, 2020, 3.2, 3.2);

INSERT INTO courses (`course_code`, `course_name`, `credits`, `description`)
VALUES 
('CS101', 'Introduction to Computer Science', 3, 'Basic concepts of computer science'),
('MATH202', 'Calculus II', 4, 'Multivariable calculus');

INSERT INTO course_enrollments (`student_id`, `course_id`, `semester`, `academic_year`, `grade`)
VALUES 
(1, 1, 1, 2020, 'A-'),
(1, 2, 2, 2021, 'B+'),
(2, 1, 1, 2020, 'B-');

INSERT INTO faculty_members (`first_name`, `last_name`, `email`, `phone_number`)
VALUES 
('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567'),
('Bob', 'Williams', 'bob.williams@example.com', '555-987-6543');

INSERT INTO course_instructors (`course_id`, `faculty_id`)
VALUES 
(1, 1),
(2, 2);
```
