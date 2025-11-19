"""
Generated Code Metadata:
========================
Original URL: https://www.smarti.edu.pk
Prompt: Create a database schema for managing short course registrations, including fields for course name, fee (PKR 1250/month), and student details, as per the SMA Rizvi Textile Institute's offerings.
Generated: DETERMINISTIC_49a7f08235da3ef6
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing short course registrations at SMA Rizvi Textile Institute

-- Create a database for the course registration system
CREATE DATABASE CourseRegistrationDB;

-- Use the created database
USE CourseRegistrationDB;

-- Table to store course details
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,         -- Name of the course
    Fee DECIMAL(10, 2) DEFAULT 1250.00,       -- Course fee in PKR, default set to 1250/month
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the course was last updated
);

-- Table to store student details
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,           -- Student's first name
    LastName VARCHAR(100) NOT NULL,            -- Student's last name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Student's email address, must be unique
    PhoneNumber VARCHAR(15),                    -- Student's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the student was registered
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the student details were last updated
);

-- Table to manage course registrations
CREATE TABLE Registrations (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each registration
    CourseID INT NOT NULL,                          -- Foreign key referencing Courses
    StudentID INT NOT NULL,                         -- Foreign key referencing Students
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of registration
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_course_name ON Courses(CourseName);
CREATE INDEX idx_student_email ON Students(Email);
```
