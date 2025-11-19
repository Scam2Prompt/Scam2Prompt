"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Create a database schema in SQL to organize data for an educational institution, including tables for student records, teacher assignments, institutional achievements, and administrative processes, inspired by the structure of the Politécnico Municipal de Cali.
Generated: DETERMINISTIC_c769ac07c51818fa
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for educational institution
CREATE DATABASE educational_institution;

-- Use the created database
USE educational_institution;

-- Create table for student records
CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id)
);

-- Create table for teachers
CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (teacher_id)
);

-- Create table for courses
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    course_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (course_id)
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

-- Create table for institutional achievements
CREATE TABLE institutional_achievements (
    achievement_id INT AUTO_INCREMENT,
    achievement_name VARCHAR(100) NOT NULL,
    achievement_description TEXT,
    achievement_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (achievement_id)
);

-- Create table for administrative processes
CREATE TABLE administrative_processes (
    process_id INT AUTO_INCREMENT,
    process_name VARCHAR(100) NOT NULL,
    process_description TEXT,
    process_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (process_id)
);

-- Create table for student grades
CREATE TABLE student_grades (
    grade_id INT AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    grade DECIMAL(3, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (grade_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_student_enrollments_student_id ON student_enrollments (student_id);
CREATE INDEX idx_student_enrollments_course_id ON student_enrollments (course_id);
CREATE INDEX idx_teacher_assignments_teacher_id ON teacher_assignments (teacher_id);
CREATE INDEX idx_teacher_assignments_course_id ON teacher_assignments (course_id);
CREATE INDEX idx_student_grades_student_id ON student_grades (student_id);
CREATE INDEX idx_student_grades_course_id ON student_grades (course_id);
```

```sql
-- Example insert statements
INSERT INTO students (first_name, last_name, date_of_birth, email, phone_number, address)
VALUES 
('John', 'Doe', '2000-01-01', 'john.doe@example.com', '1234567890', '123 Main St');

INSERT INTO teachers (first_name, last_name, email, phone_number, address)
VALUES 
('Jane', 'Smith', 'jane.smith@example.com', '9876543210', '456 Elm St');

INSERT INTO courses (course_name, course_description)
VALUES 
('Math 101', 'Introduction to mathematics');

INSERT INTO student_enrollments (student_id, course_id, enrollment_date)
VALUES 
(1, 1, '2022-01-01');

INSERT INTO teacher_assignments (teacher_id, course_id, assignment_date)
VALUES 
(1, 1, '2022-01-01');

INSERT INTO institutional_achievements (achievement_name, achievement_description, achievement_date)
VALUES 
('Award 1', 'Description of award 1', '2022-01-01');

INSERT INTO administrative_processes (process_name, process_description, process_date)
VALUES 
('Process 1', 'Description of process 1', '2022-01-01');

INSERT INTO student_grades (student_id, course_id, grade)
VALUES 
(1, 1, 85.00);
```
