"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upjobsead.com.br
Prompt: Create a SQL database schema to store course information, including course name, duration, price, total lessons, and quizzes, as seen on the website.
Generated: DETERMINISTIC_4b258ccdf079542f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing course information

-- Create a new database for the courses
CREATE DATABASE CourseManagement;

-- Use the created database
USE CourseManagement;

-- Create a table to store course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course (cannot be null)
    Duration INT NOT NULL,                    -- Duration of the course in hours (cannot be null)
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the course (cannot be null)
    TotalLessons INT NOT NULL,                -- Total number of lessons in the course (cannot be null)
    Quizzes INT DEFAULT 0,                    -- Number of quizzes in the course (default is 0)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create an index for the CourseName to improve search performance
CREATE INDEX idx_course_name ON Courses (CourseName);

-- Insert sample data into the Courses table for testing
INSERT INTO Courses (CourseName, Duration, Price, TotalLessons, Quizzes) 
VALUES 
('Introduction to Programming', 40, 199.99, 20, 5),
('Advanced Database Management', 60, 299.99, 30, 10),
('Web Development Bootcamp', 80, 399.99, 40, 15);

-- Query to retrieve all courses
SELECT * FROM Courses;

-- Ensure foreign key constraints and data integrity in future expansions
-- (For demonstration purposes, actual foreign keys are not defined here, but they can be added as needed)
```
