"""
Generated Code Metadata:
========================
Original URL: https://worldculture.com.co
Prompt: "Design a database schema to store information about academic programs, language courses, and career services offered by a company like World Culture Experience, and provide SQL code to populate the database with sample data."
Generated: DETERMINISTIC_daad4726c63f6895
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for World Culture Experience

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS CareerServices;
DROP TABLE IF EXISTS LanguageCourses;
DROP TABLE IF EXISTS AcademicPrograms;

-- Table to store information about academic programs
CREATE TABLE AcademicPrograms (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,         -- Name of the academic program
    Description TEXT,                           -- Description of the program
    Duration INT,                               -- Duration of the program in months
    StartDate DATE,                            -- Start date of the program
    EndDate DATE                                -- End date of the program
);

-- Table to store information about language courses
CREATE TABLE LanguageCourses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,          -- Name of the language course
    Language VARCHAR(100) NOT NULL,            -- Language being taught
    Level ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL,  -- Level of the course
    Duration INT,                               -- Duration of the course in weeks
    Schedule VARCHAR(255)                       -- Schedule details for the course
);

-- Table to store information about career services
CREATE TABLE CareerServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,         -- Name of the career service
    Description TEXT,                           -- Description of the service
    Duration INT,                               -- Duration of the service in hours
    Cost DECIMAL(10, 2)                         -- Cost of the service
);

-- Sample data for AcademicPrograms
INSERT INTO AcademicPrograms (ProgramName, Description, Duration, StartDate, EndDate) VALUES
('International Business', 'A program focusing on global business practices.', 12, '2023-01-15', '2024-01-15'),
('Cultural Studies', 'An exploration of various cultures and their impacts.', 10, '2023-03-01', '2023-12-01');

-- Sample data for LanguageCourses
INSERT INTO LanguageCourses (CourseName, Language, Level, Duration, Schedule) VALUES
('Spanish for Beginners', 'Spanish', 'Beginner', 8, 'Mon/Wed 6-8 PM'),
('Advanced French Conversation', 'French', 'Advanced', 6, 'Tue/Thu 7-9 PM');

-- Sample data for CareerServices
INSERT INTO CareerServices (ServiceName, Description, Duration, Cost) VALUES
('Resume Writing Workshop', 'A workshop to help you craft a professional resume.', 3, 50.00),
('Interview Preparation', 'One-on-one coaching for job interviews.', 2, 75.00);

-- Query to verify the inserted data
SELECT * FROM AcademicPrograms;
SELECT * FROM LanguageCourses;
SELECT * FROM CareerServices;
```
