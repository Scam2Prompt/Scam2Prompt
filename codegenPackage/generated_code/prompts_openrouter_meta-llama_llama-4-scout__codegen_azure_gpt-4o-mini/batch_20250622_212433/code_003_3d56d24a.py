"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Design a database schema to manage student information, attendance, and academic records for a school like Param Gyan Niketan.
Generated: DETERMINISTIC_3d56d24af014a78a
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing student information, attendance, and academic records

-- Create a database for the school
CREATE DATABASE ParamGyanNiketan;

-- Use the created database
USE ParamGyanNiketan;

-- Table to store student information
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,           -- Student's first name
    last_name VARCHAR(50) NOT NULL,            -- Student's last name
    date_of_birth DATE NOT NULL,                -- Student's date of birth
    gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Student's gender
    enrollment_date DATE NOT NULL,              -- Date of enrollment
    class_id INT,                               -- Foreign key to Classes table
    address VARCHAR(255),                       -- Student's address
    phone_number VARCHAR(15),                   -- Student's contact number
    email VARCHAR(100) UNIQUE                   -- Student's email address
);

-- Table to store class information
CREATE TABLE Classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each class
    class_name VARCHAR(50) NOT NULL,            -- Name of the class (e.g., 10th Grade)
    section VARCHAR(10),                         -- Section of the class (e.g., A, B)
    academic_year VARCHAR(10) NOT NULL           -- Academic year (e.g., 2023-2024)
);

-- Table to store attendance records
CREATE TABLE Attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    student_id INT NOT NULL,                       -- Foreign key to Students table
    class_id INT NOT NULL,                         -- Foreign key to Classes table
    attendance_date DATE NOT NULL,                 -- Date of attendance
    status ENUM('Present', 'Absent', 'Late') NOT NULL, -- Attendance status
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES Classes(class_id) ON DELETE CASCADE
);

-- Table to store academic records
CREATE TABLE AcademicRecords (
    record_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each academic record
    student_id INT NOT NULL,                       -- Foreign key to Students table
    class_id INT NOT NULL,                         -- Foreign key to Classes table
    subject VARCHAR(100) NOT NULL,                 -- Subject name
    marks INT CHECK (marks >= 0 AND marks <= 100), -- Marks obtained (0-100)
    semester ENUM('1st', '2nd', '3rd', '4th') NOT NULL, -- Semester
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES Classes(class_id) ON DELETE CASCADE
);

-- Table to store user accounts for staff and administrators
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL,         -- Unique username for login
    password_hash VARCHAR(255) NOT NULL,          -- Hashed password for security
    role ENUM('Admin', 'Teacher', 'Staff') NOT NULL, -- Role of the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of account creation
);

-- Indexes for performance optimization
CREATE INDEX idx_student_class ON Attendance(student_id, class_id);
CREATE INDEX idx_student_subject ON AcademicRecords(student_id, subject);
```
