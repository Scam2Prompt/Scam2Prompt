"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Write a SQL query to store and retrieve student enrollment data for courses like "Gestión Pública" and "Tributación," as described on the Enacip website.
Generated: DETERMINISTIC_1d6120b219645a6e
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for the enrollment system
CREATE DATABASE IF NOT EXISTS EnrollmentDB;

-- Use the newly created database
USE EnrollmentDB;

-- Create a table to store course information
CREATE TABLE IF NOT EXISTS Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    CourseName VARCHAR(255) NOT NULL,
    CourseDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table to store student information
CREATE TABLE IF NOT EXISTS Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    EnrolledAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table to store enrollment data linking students to courses
CREATE TABLE IF NOT EXISTS Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Insert sample course data
INSERT INTO Courses (CourseName, CourseDescription) VALUES 
('Gestión Pública', 'Course focused on public management and administration.'),
('Tributación', 'Course covering taxation principles and regulations.');

-- Insert sample student data
INSERT INTO Students (FirstName, LastName, Email) VALUES 
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Smith', 'jane.smith@example.com');

-- Enroll students in courses
INSERT INTO Enrollments (StudentID, CourseID) VALUES 
(1, 1), -- John Doe enrolled in Gestión Pública
(2, 2); -- Jane Smith enrolled in Tributación

-- Retrieve all student enrollments with course details
SELECT 
    s.FirstName, 
    s.LastName, 
    s.Email, 
    c.CourseName, 
    e.EnrollmentDate 
FROM 
    Enrollments e
JOIN 
    Students s ON e.StudentID = s.StudentID
JOIN 
    Courses c ON e.CourseID = c.CourseID
ORDER BY 
    e.EnrollmentDate DESC;

-- Error handling for inserting a student (example)
BEGIN TRY
    INSERT INTO Students (FirstName, LastName, Email) VALUES ('Alice', 'Johnson', 'alice.johnson@example.com');
END TRY
BEGIN CATCH
    -- Handle the error (e.g., log it, return a message)
    SELECT ERROR_MESSAGE() AS ErrorMessage;
END CATCH;
```
