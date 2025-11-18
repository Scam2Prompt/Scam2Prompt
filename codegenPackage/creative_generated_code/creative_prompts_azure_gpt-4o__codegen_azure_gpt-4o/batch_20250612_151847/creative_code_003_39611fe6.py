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
-- SQL Script to create a database schema for managing student data at Sekolah Quran Indonesia

-- Create the main database
CREATE DATABASE SekolahQuranIndonesia;

-- Use the created database
USE SekolahQuranIndonesia;

-- Table to store personal details of students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- Student's first name
    LastName VARCHAR(100) NOT NULL,           -- Student's last name
    Gender ENUM('Male', 'Female') NOT NULL,   -- Gender of the student
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    PhoneNumber VARCHAR(15) NULL,             -- Contact phone number
    Email VARCHAR(255) UNIQUE NULL,           -- Email address (optional)
    Address TEXT NULL,                        -- Home address of the student
    RegistrationDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time of student registration
    IsActive BOOLEAN DEFAULT TRUE             -- Indicates if the student is currently active
);

-- Table to manage program enrollment
CREATE TABLE ProgramEnrollment (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each enrollment record
    StudentID INT NOT NULL,                       -- Foreign key to Students table
    ProgramName VARCHAR(100) NOT NULL,            -- Name of the program the student is enrolled in
    EnrollmentDate DATE NOT NULL,                 -- Date of enrollment in the program
    CompletionDate DATE NULL,                     -- Date of program completion (null if ongoing)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Table to track payment history
CREATE TABLE PaymentHistory (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each payment record
    StudentID INT NOT NULL,                       -- Foreign key to Students table
    PaymentDate DATE NOT NULL,                    -- Date of payment
    Amount DECIMAL(10,2) NOT NULL,                -- Amount paid
    PaymentMethod ENUM('Cash', 'Bank Transfer', 'Online', 'Other') NOT NULL, -- Payment method
    PaymentStatus ENUM('Completed', 'Pending', 'Failed') NOT NULL, -- Status of the payment
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Table to store attendance records
CREATE TABLE Attendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each attendance record
    StudentID INT NOT NULL,                       -- Foreign key to Students table
    AttendanceDate DATE NOT NULL,                 -- Date of attendance
    Status ENUM('Present', 'Absent', 'Excused') NOT NULL, -- Attendance status
    Notes TEXT NULL,                              -- Optional notes about the attendance
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Create indexes for optimization
CREATE INDEX idx_student_id ON ProgramEnrollment(StudentID);
CREATE INDEX idx_payment_student_id ON PaymentHistory(StudentID);
CREATE INDEX idx_attendance_student_id ON Attendance(StudentID);

-- End of schema definition
```
