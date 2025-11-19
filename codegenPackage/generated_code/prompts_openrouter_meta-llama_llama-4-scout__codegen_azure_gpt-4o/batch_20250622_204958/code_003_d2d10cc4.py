"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: "Design a database schema for managing information about students, courses, and certifications at an institution like Trentino Juan Pablo II."
Generated: DETERMINISTIC_d2d10cc4eab4e4b5
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Managing Students, Courses, and Certifications

-- Create a table for storing student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    EnrollmentDate DATE NOT NULL,             -- Date the student enrolled
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    Description TEXT,                         -- Description of the course
    Credits INT NOT NULL,                     -- Number of credits for the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    CertificationName VARCHAR(100) NOT NULL,        -- Name of the certification
    IssuingOrganization VARCHAR(100) NOT NULL,      -- Organization issuing the certification
    ValidityPeriod INT,                             -- Validity period in months (NULL if indefinite)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for managing student-course enrollments
CREATE TABLE StudentCourses (
    StudentCourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment record
    StudentID INT NOT NULL,                         -- Foreign key referencing Students table
    CourseID INT NOT NULL,                          -- Foreign key referencing Courses table
    EnrollmentDate DATE NOT NULL,                   -- Date the student enrolled in the course
    Grade DECIMAL(5, 2),                            -- Grade received by the student (NULL if not graded yet)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE     -- Cascade delete
);

-- Create a table for managing student certifications
CREATE TABLE StudentCertifications (
    StudentCertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification record
    StudentID INT NOT NULL,                                -- Foreign key referencing Students table
    CertificationID INT NOT NULL,                         -- Foreign key referencing Certifications table
    DateIssued DATE NOT NULL,                             -- Date the certification was issued
    ExpirationDate DATE,                                  -- Expiration date of the certification (NULL if indefinite)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,        -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_students_email ON Students(Email); -- Index for quick lookup by email
CREATE INDEX idx_courses_name ON Courses(CourseName); -- Index for quick lookup by course name
CREATE INDEX idx_certifications_name ON Certifications(CertificationName); -- Index for quick lookup by certification name
```
