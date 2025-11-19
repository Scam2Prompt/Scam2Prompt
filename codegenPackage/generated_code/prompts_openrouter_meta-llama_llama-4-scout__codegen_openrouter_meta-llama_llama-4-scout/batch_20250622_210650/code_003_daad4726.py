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
-- Create database schema
CREATE DATABASE WorldCultureExperience;

-- Use database
USE WorldCultureExperience;

-- Create table for academic programs
CREATE TABLE AcademicPrograms (
    ProgramID INT AUTO_INCREMENT,
    ProgramName VARCHAR(255) NOT NULL,
    Description TEXT,
    Duration VARCHAR(255),
    Eligibility VARCHAR(255),
    PRIMARY KEY (ProgramID)
);

-- Create table for language courses
CREATE TABLE LanguageCourses (
    CourseID INT AUTO_INCREMENT,
    CourseName VARCHAR(255) NOT NULL,
    Language VARCHAR(255) NOT NULL,
    Level VARCHAR(255) NOT NULL,
    Duration VARCHAR(255),
    Fee DECIMAL(10, 2),
    PRIMARY KEY (CourseID)
);

-- Create table for career services
CREATE TABLE CareerServices (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (ServiceID)
);

-- Create table for program courses
CREATE TABLE ProgramCourses (
    ProgramID INT,
    CourseID INT,
    PRIMARY KEY (ProgramID, CourseID),
    FOREIGN KEY (ProgramID) REFERENCES AcademicPrograms(ProgramID),
    FOREIGN KEY (CourseID) REFERENCES LanguageCourses(CourseID)
);

-- Create table for program services
CREATE TABLE ProgramServices (
    ProgramID INT,
    ServiceID INT,
    PRIMARY KEY (ProgramID, ServiceID),
    FOREIGN KEY (ProgramID) REFERENCES AcademicPrograms(ProgramID),
    FOREIGN KEY (ServiceID) REFERENCES CareerServices(ServiceID)
);

-- Populate database with sample data
INSERT INTO AcademicPrograms (ProgramName, Description, Duration, Eligibility)
VALUES 
('International Business', 'Learn about international business practices', '6 months', 'Bachelor\'s degree'),
('Cultural Studies', 'Explore different cultures', '1 year', 'High school diploma'),
('Language and Culture', 'Learn a new language and culture', '3 months', 'High school diploma');

INSERT INTO LanguageCourses (CourseName, Language, Level, Duration, Fee)
VALUES 
('English Beginner', 'English', 'Beginner', '3 months', 1000.00),
('Spanish Intermediate', 'Spanish', 'Intermediate', '6 months', 2000.00),
('Mandarin Advanced', 'Mandarin', 'Advanced', '1 year', 3000.00);

INSERT INTO CareerServices (ServiceName, Description)
VALUES 
('Resume Building', 'Get help building your resume'),
('Interview Preparation', 'Prepare for job interviews'),
('Job Placement', 'Get assistance finding a job');

INSERT INTO ProgramCourses (ProgramID, CourseID)
VALUES 
(1, 1),
(1, 2),
(2, 3);

INSERT INTO ProgramServices (ProgramID, ServiceID)
VALUES 
(1, 1),
(1, 2),
(2, 3),
(3, 1),
(3, 2);
```
