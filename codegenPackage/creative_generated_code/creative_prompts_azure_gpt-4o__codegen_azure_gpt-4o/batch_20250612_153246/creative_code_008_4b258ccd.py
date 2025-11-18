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
-- SQL schema for storing course information
-- This schema is designed to capture course details including name, duration, price, total lessons, and quizzes.

-- Create the database (if not already created)
CREATE DATABASE IF NOT EXISTS CourseManagement;

-- Use the newly created database
USE CourseManagement;

-- Create the courses table to store course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    Duration INT NOT NULL COMMENT 'Duration in days', -- Duration of the course
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the course, with up to 2 decimal places
    TotalLessons INT NOT NULL,               -- Number of lessons in the course
    TotalQuizzes INT NOT NULL,               -- Number of quizzes in the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the course entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Add error handling for invalid input
-- Note: Use constraints and defaults to ensure data integrity.

-- Example constraints:
-- 1. Duration, TotalLessons, and TotalQuizzes must be positive numbers.
-- 2. Price must be non-negative.
ALTER TABLE Courses
ADD CONSTRAINT chk_duration CHECK (Duration > 0),
ADD CONSTRAINT chk_price CHECK (Price >= 0),
ADD CONSTRAINT chk_lessons CHECK (TotalLessons > 0),
ADD CONSTRAINT chk_quizzes CHECK (TotalQuizzes >= 0);
```
