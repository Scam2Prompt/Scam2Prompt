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
-- Database schema for managing short course registrations

-- Create a table to store information about short courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,              -- Name of the course
    Fee DECIMAL(10, 2) DEFAULT 1250.00,            -- Monthly fee for the course (PKR 1250 by default)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for course creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,               -- First name of the student
    LastName VARCHAR(100) NOT NULL,                -- Last name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,            -- Email address of the student (must be unique)
    PhoneNumber VARCHAR(15),                       -- Contact number of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for student registration
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store registrations for short courses
CREATE TABLE CourseRegistrations (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each registration
    StudentID INT NOT NULL,                        -- Foreign key referencing the student
    CourseID INT NOT NULL,                         -- Foreign key referencing the course
    RegistrationDate DATE NOT NULL,                -- Date of registration
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Status of the registration
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for registration creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE    -- Ensure referential integrity
);

-- Index optimization for faster lookups
CREATE INDEX IDX_StudentID ON CourseRegistrations(StudentID);
CREATE INDEX IDX_CourseID ON CourseRegistrations(CourseID);
```
