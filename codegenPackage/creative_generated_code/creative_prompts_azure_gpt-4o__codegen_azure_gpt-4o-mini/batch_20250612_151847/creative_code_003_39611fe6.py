"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sekolahquranindonesia.com
Prompt: Create a database schema using SQL for managing student data at Sekolah Quran Indonesia, including tables for personal details, program enrollment, payment history, and attendance.
Generated: DETERMINISTIC_39611fe6d1f71edb
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script for creating a database schema to manage student data at Sekolah Quran Indonesia

-- Create a new database
CREATE DATABASE SekolahQuranIndonesia;

-- Use the newly created database
USE SekolahQuranIndonesia;

-- Table to store personal details of students
CREATE TABLE Student (
    student_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    full_name VARCHAR(100) NOT NULL,           -- Full name of the student
    date_of_birth DATE NOT NULL,                -- Date of birth of the student
    gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    contact_number VARCHAR(15),                 -- Contact number of the student
    email VARCHAR(100),                         -- Email address of the student
    address TEXT,                               -- Residential address of the student
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store program enrollment details
CREATE TABLE ProgramEnrollment (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL,                     -- Foreign key referencing Student table
    program_name VARCHAR(100) NOT NULL,          -- Name of the program the student is enrolled in
    enrollment_date DATE NOT NULL,               -- Date of enrollment
    status ENUM('Active', 'Completed', 'Dropped') NOT NULL, -- Enrollment status
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store payment history
CREATE TABLE PaymentHistory (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each payment
    student_id INT NOT NULL,                     -- Foreign key referencing Student table
    payment_date DATE NOT NULL,                   -- Date of payment
    amount DECIMAL(10, 2) NOT NULL,              -- Amount paid
    payment_method ENUM('Cash', 'Bank Transfer', 'Credit Card') NOT NULL, -- Payment method
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store attendance records
CREATE TABLE Attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    student_id INT NOT NULL,                      -- Foreign key referencing Student table
    attendance_date DATE NOT NULL,                -- Date of attendance
    status ENUM('Present', 'Absent', 'Late') NOT NULL, -- Attendance status
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Ensure proper indexing for faster queries
CREATE INDEX idx_student_email ON Student (email);
CREATE INDEX idx_enrollment_student ON ProgramEnrollment (student_id);
CREATE INDEX idx_payment_student ON PaymentHistory (student_id);
CREATE INDEX idx_attendance_student ON Attendance (student_id);
```
