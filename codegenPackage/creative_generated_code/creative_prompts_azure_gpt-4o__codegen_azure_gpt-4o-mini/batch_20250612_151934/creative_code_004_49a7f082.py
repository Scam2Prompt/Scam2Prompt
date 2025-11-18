"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Create a database schema for managing short course registrations, including fields for course name, fee (PKR 1250/month), and student details, as per the SMA Rizvi Textile Institute's offerings.
Generated: DETERMINISTIC_49a7f08235da3ef6
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Script to create a database schema for managing short course registrations

-- Create a database for the SMA Rizvi Textile Institute
CREATE DATABASE IF NOT EXISTS ShortCourseRegistration;

-- Use the newly created database
USE ShortCourseRegistration;

-- Table to store course details
CREATE TABLE IF NOT EXISTS Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,         -- Name of the course
    CourseFee DECIMAL(10, 2) DEFAULT 1250.00, -- Course fee in PKR, defaulted to 1250 PKR/month
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for course creation
);

-- Table to store student details
CREATE TABLE IF NOT EXISTS Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,           -- First name of the student
    LastName VARCHAR(100) NOT NULL,            -- Last name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the student, must be unique
    PhoneNumber VARCHAR(15),                    -- Contact number of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for student registration
);

-- Table to manage registrations of students for courses
CREATE TABLE IF NOT EXISTS Registrations (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each registration
    StudentID INT NOT NULL,                         -- Foreign key referencing Students
    CourseID INT NOT NULL,                          -- Foreign key referencing Courses
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of registration
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Enforce referential integrity
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE        -- Enforce referential integrity
);

-- Indexes for faster queries
CREATE INDEX idx_student_email ON Students(Email);
CREATE INDEX idx_course_name ON Courses(CourseName);
CREATE INDEX idx_registration_date ON Registrations(RegistrationDate);

-- Sample insert statements for testing
INSERT INTO Courses (CourseName) VALUES ('Textile Design');
INSERT INTO Courses (CourseName) VALUES ('Fashion Technology');

INSERT INTO Students (FirstName, LastName, Email, PhoneNumber) VALUES ('John', 'Doe', 'john.doe@example.com', '1234567890');
INSERT INTO Students (FirstName, LastName, Email, PhoneNumber) VALUES ('Jane', 'Smith', 'jane.smith@example.com', '0987654321');

-- Sample registration
INSERT INTO Registrations (StudentID, CourseID) VALUES (1, 1);
INSERT INTO Registrations (StudentID, CourseID) VALUES (2, 2);
```
