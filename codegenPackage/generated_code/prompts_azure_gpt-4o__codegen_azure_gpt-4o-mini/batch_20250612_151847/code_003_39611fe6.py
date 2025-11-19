"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Create a database schema using SQL for managing student data at Sekolah Quran Indonesia, including tables for personal details, program enrollment, payment history, and attendance.
Generated: DETERMINISTIC_39611fe6d1f71edb
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing student data at Sekolah Quran Indonesia

-- Create a database
CREATE DATABASE SekolahQuranIndonesia;

-- Use the created database
USE SekolahQuranIndonesia;

-- Table for storing personal details of students
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,           -- Student's first name
    last_name VARCHAR(50) NOT NULL,            -- Student's last name
    date_of_birth DATE NOT NULL,                -- Student's date of birth
    gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Student's gender
    email VARCHAR(100) UNIQUE NOT NULL,         -- Student's email address
    phone_number VARCHAR(15),                   -- Student's phone number
    address TEXT,                               -- Student's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for storing program enrollment details
CREATE TABLE Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL,                       -- Foreign key referencing Students
    program_name VARCHAR(100) NOT NULL,           -- Name of the program enrolled
    enrollment_date DATE NOT NULL,                 -- Date of enrollment
    status ENUM('Active', 'Completed', 'Dropped') NOT NULL, -- Enrollment status
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for storing payment history
CREATE TABLE Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each payment
    student_id INT NOT NULL,                       -- Foreign key referencing Students
    amount DECIMAL(10, 2) NOT NULL,               -- Payment amount
    payment_date DATE NOT NULL,                    -- Date of payment
    payment_method ENUM('Cash', 'Bank Transfer', 'Credit Card') NOT NULL, -- Method of payment
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for storing attendance records
CREATE TABLE Attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each attendance record
    student_id INT NOT NULL,                       -- Foreign key referencing Students
    attendance_date DATE NOT NULL,                 -- Date of attendance
    status ENUM('Present', 'Absent', 'Late') NOT NULL, -- Attendance status
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_student_email ON Students(email);
CREATE INDEX idx_enrollment_student ON Enrollments(student_id);
CREATE INDEX idx_payment_student ON Payments(student_id);
CREATE INDEX idx_attendance_student ON Attendance(student_id);
```
