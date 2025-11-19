"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: Create a SQL database schema to store course information, including course name, duration, price, total lessons, and quizzes, as seen on the website.
Generated: DETERMINISTIC_4b258ccdf079542f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing course information

-- Create a new database for the course management system
CREATE DATABASE CourseManagement;

-- Use the newly created database
USE CourseManagement;

-- Create a table to store course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,         -- Name of the course
    Duration INT NOT NULL,                     -- Duration of the course in hours
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the course
    TotalLessons INT NOT NULL,                 -- Total number of lessons in the course
    Quizzes INT NOT NULL,                      -- Number of quizzes associated with the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create an index on CourseName for faster search queries
CREATE INDEX idx_course_name ON Courses (CourseName);

-- Example of inserting a course into the Courses table
-- INSERT INTO Courses (CourseName, Duration, Price, TotalLessons, Quizzes)
-- VALUES ('Introduction to Programming', 40, 199.99, 20, 5);

-- Note: Uncomment the above INSERT statement to add a sample course
```
