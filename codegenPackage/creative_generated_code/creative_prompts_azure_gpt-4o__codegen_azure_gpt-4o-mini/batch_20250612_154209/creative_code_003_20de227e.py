"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Develop a SQL database schema to store information about ISIV's course offerings, including fields for course name (e.g., "Negocios Digitales"), duration, and modality (e.g., "Educación a Distancia").
Generated: DETERMINISTIC_20de227e92ddd6be
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Script to create a database schema for ISIV's course offerings

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS ISIV_Courses;

-- Use the created database
USE ISIV_Courses;

-- Drop the Courses table if it exists (for development/testing purposes)
DROP TABLE IF EXISTS Courses;

-- Create the Courses table to store information about course offerings
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course, cannot be null
    Duration INT NOT NULL,                    -- Duration of the course in hours, cannot be null
    Modality ENUM('Educación a Distancia', 'Presencial') NOT NULL, -- Modality of the course, cannot be null
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Insert sample data into the Courses table (optional)
INSERT INTO Courses (CourseName, Duration, Modality) VALUES
('Negocios Digitales', 40, 'Educación a Distancia'),
('Introducción a la Programación', 60, 'Presencial'),
('Marketing Digital', 30, 'Educación a Distancia');

-- Query to retrieve all courses to verify the schema
SELECT * FROM Courses;
```
