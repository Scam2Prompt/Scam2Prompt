"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Generate a sample database schema for storing student information, attendance records, and exam results for a school with a similar setup to জি. কে. মাধ্যমিক বিদ্যালয়.
Generated: DETERMINISTIC_4c2aedcaf8646aca
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing student information, attendance records, and exam results

-- Create a database for the school
CREATE DATABASE school_management;

-- Use the created database
USE school_management;

-- Table to store student information
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,            -- Student's first name
    last_name VARCHAR(50) NOT NULL,             -- Student's last name
    date_of_birth DATE NOT NULL,                 -- Student's date of birth
    gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Student's gender
    enrollment_date DATE NOT NULL,               -- Date of enrollment
    class VARCHAR(10) NOT NULL,                  -- Class/grade of the student
    address VARCHAR(255),                         -- Student's address
    phone_number VARCHAR(15)                      -- Student's phone number
);

-- Table to store attendance records
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    student_id INT NOT NULL,                       -- Foreign key referencing students
    attendance_date DATE NOT NULL,                 -- Date of attendance
    status ENUM('Present', 'Absent', 'Late') NOT NULL, -- Attendance status
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store exam results
CREATE TABLE exam_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each exam result
    student_id INT NOT NULL,                       -- Foreign key referencing students
    subject VARCHAR(50) NOT NULL,                  -- Subject of the exam
    exam_date DATE NOT NULL,                       -- Date of the exam
    score DECIMAL(5, 2) NOT NULL,                  -- Score obtained by the student
    max_score DECIMAL(5, 2) NOT NULL,              -- Maximum score for the exam
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for students
INSERT INTO students (first_name, last_name, date_of_birth, gender, enrollment_date, class, address, phone_number)
VALUES 
('John', 'Doe', '2005-05-15', 'Male', '2020-06-01', '10A', '123 Main St, City', '1234567890'),
('Jane', 'Smith', '2006-08-20', 'Female', '2020-06-01', '10B', '456 Elm St, City', '0987654321');

-- Sample data insertion for attendance
INSERT INTO attendance (student_id, attendance_date, status)
VALUES 
(1, '2023-10-01', 'Present'),
(1, '2023-10-02', 'Absent'),
(2, '2023-10-01', 'Late');

-- Sample data insertion for exam results
INSERT INTO exam_results (student_id, subject, exam_date, score, max_score)
VALUES 
(1, 'Mathematics', '2023-09-30', 85.50, 100.00),
(2, 'Science', '2023-09-30', 90.00, 100.00);
```
