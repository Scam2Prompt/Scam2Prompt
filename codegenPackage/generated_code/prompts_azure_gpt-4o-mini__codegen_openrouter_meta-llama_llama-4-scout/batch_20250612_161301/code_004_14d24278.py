"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Design a database schema in SQL for managing the administrative services of I.E Politécnico Municipal Cali, including tables for student information, academic programs, and faculty members.
Generated: DETERMINISTIC_14d24278b8d4f154
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for I.E Politécnico Municipal Cali administrative services
CREATE DATABASE iep_municipal_cali;

-- Use the created database
USE iep_municipal_cali;

-- Create table for academic programs
CREATE TABLE academic_programs (
    program_id INT AUTO_INCREMENT,
    program_name VARCHAR(255) NOT NULL,
    program_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (program_id)
);

-- Create table for faculty members
CREATE TABLE faculty_members (
    faculty_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (faculty_id)
);

-- Create table for student information
CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    date_of_birth DATE,
    address TEXT,
    program_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id),
    FOREIGN KEY (program_id) REFERENCES academic_programs(program_id) ON DELETE SET NULL
);

-- Create table for student enrollment
CREATE TABLE student_enrollments (
    enrollment_id INT AUTO_INCREMENT,
    student_id INT,
    program_id INT,
    enrollment_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES academic_programs(program_id) ON DELETE CASCADE,
    UNIQUE KEY (student_id, program_id)
);

-- Create table for faculty assignments
CREATE TABLE faculty_assignments (
    assignment_id INT AUTO_INCREMENT,
    faculty_id INT,
    program_id INT,
    assignment_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (assignment_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty_members(faculty_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES academic_programs(program_id) ON DELETE CASCADE,
    UNIQUE KEY (faculty_id, program_id)
);

-- Create table for student grades
CREATE TABLE student_grades (
    grade_id INT AUTO_INCREMENT,
    student_id INT,
    program_id INT,
    grade DECIMAL(3, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (grade_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES academic_programs(program_id) ON DELETE CASCADE,
    UNIQUE KEY (student_id, program_id)
);

-- Insert some sample data for testing
INSERT INTO academic_programs (program_name, program_description)
VALUES 
('Computer Science', 'Bachelor of Science in Computer Science'),
('Electrical Engineering', 'Bachelor of Science in Electrical Engineering'),
('Mathematics', 'Bachelor of Science in Mathematics');

INSERT INTO faculty_members (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210'),
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567');

INSERT INTO students (first_name, last_name, email, phone_number, date_of_birth, address, program_id)
VALUES 
('Alice', 'Williams', 'alice.williams@example.com', '111-222-3333', '2000-01-01', '123 Main St', 1),
('Mike', 'Brown', 'mike.brown@example.com', '444-555-6666', '1999-06-01', '456 Elm St', 2),
('Emily', 'Davis', 'emily.davis@example.com', '777-888-9999', '1998-03-01', '789 Oak St', 3);

INSERT INTO student_enrollments (student_id, program_id, enrollment_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-06-01'),
(3, 3, '2022-03-01');

INSERT INTO faculty_assignments (faculty_id, program_id, assignment_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-06-01'),
(3, 3, '2022-03-01');

INSERT INTO student_grades (student_id, program_id, grade)
VALUES 
(1, 1, 85.00),
(2, 2, 90.00),
(3, 3, 78.00);
```
