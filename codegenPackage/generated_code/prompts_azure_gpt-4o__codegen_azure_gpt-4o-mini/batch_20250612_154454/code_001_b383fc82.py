"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Create a database schema in SQL to store exam schedules for SMKN 1 Kadipaten, including fields for class, subject, token, date, and time. Write the SQL queries to insert and retrieve data.
Generated: DETERMINISTIC_b383fc82efcf2dc1
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing exam schedules for SMKN 1 Kadipaten
CREATE DATABASE IF NOT EXISTS smkn1_kadipaten;

USE smkn1_kadipaten;

-- Create a table to store exam schedules
CREATE TABLE IF NOT EXISTS exam_schedule (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each exam schedule
    class VARCHAR(50) NOT NULL,          -- Class for which the exam is scheduled
    subject VARCHAR(100) NOT NULL,       -- Subject of the exam
    token VARCHAR(50) NOT NULL UNIQUE,   -- Unique token for the exam
    exam_date DATE NOT NULL,             -- Date of the exam
    exam_time TIME NOT NULL,             -- Time of the exam
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Insert sample data into the exam_schedule table
INSERT INTO exam_schedule (class, subject, token, exam_date, exam_time) VALUES
('10A', 'Mathematics', 'TOKEN123', '2023-11-01', '09:00:00'),
('10B', 'Science', 'TOKEN124', '2023-11-02', '10:00:00'),
('11A', 'English', 'TOKEN125', '2023-11-03', '11:00:00');

-- Query to retrieve all exam schedules
SELECT * FROM exam_schedule;

-- Query to retrieve exam schedule by class
SELECT * FROM exam_schedule WHERE class = '10A';

-- Query to retrieve exam schedule by subject
SELECT * FROM exam_schedule WHERE subject = 'Science';

-- Query to retrieve exam schedule by date
SELECT * FROM exam_schedule WHERE exam_date = '2023-11-01';

-- Query to retrieve exam schedule by token
SELECT * FROM exam_schedule WHERE token = 'TOKEN123';
```
