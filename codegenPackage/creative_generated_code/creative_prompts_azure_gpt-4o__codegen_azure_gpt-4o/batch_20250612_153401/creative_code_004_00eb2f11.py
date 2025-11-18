"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Create a database schema to manage courses for admission exam preparation, including categories for secundaria, bachillerato, and licenciatura, as described on Educar Comitán's site.
Generated: DETERMINISTIC_00eb2f1137bcecd7
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Courses for Admission Exam Preparation
-- Categories include Secundaria, Bachillerato, and Licenciatura.

-- Create a database named 'AdmissionPreparation'
CREATE DATABASE IF NOT EXISTS AdmissionPreparation;

-- Switch to the new database
USE AdmissionPreparation;

-- Table to store course categories
CREATE TABLE IF NOT EXISTS CourseCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(50) NOT NULL,         -- Name of the category (e.g., Secundaria, Bachillerato, Licenciatura)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last record update
);

-- Populate the CourseCategories table with predefined categories
INSERT INTO CourseCategories (CategoryName) VALUES 
('Secundaria'),
('Bachillerato'),
('Licenciatura');

-- Table to store individual courses
CREATE TABLE IF NOT EXISTS Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    Description TEXT,                         -- Detailed description of the course
    CategoryID INT NOT NULL,                  -- Foreign key to reference the CourseCategories table
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the course
    DurationWeeks INT NOT NULL,               -- Duration of the course in weeks
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last record update
    FOREIGN KEY (CategoryID) REFERENCES CourseCategories(CategoryID) ON DELETE CASCADE
);

-- Table to manage students
CREATE TABLE IF NOT EXISTS Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the student (must be unique)
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last record update
);

-- Table to manage enrollments of students in courses
CREATE TABLE IF NOT EXISTS Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key to reference the Students table
    CourseID INT NOT NULL,                       -- Foreign key to reference the Courses table
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of enrollment
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Indexes for improving query performance
CREATE INDEX idx_category_name ON CourseCategories (CategoryName);
CREATE INDEX idx_course_name ON Courses (CourseName);
CREATE INDEX idx_student_email ON Students (Email);

-- The database schema is now fully defined and ready for use.
```
