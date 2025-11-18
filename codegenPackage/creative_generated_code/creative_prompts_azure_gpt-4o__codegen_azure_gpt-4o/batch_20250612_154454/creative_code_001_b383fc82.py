"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Create a database schema in SQL to store exam schedules for SMKN 1 Kadipaten, including fields for class, subject, token, date, and time. Write the SQL queries to insert and retrieve data.
Generated: DETERMINISTIC_b383fc82efcf2dc1
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema to store exam schedules for SMKN 1 Kadipaten

-- Step 1: Create the table to store exam schedules
CREATE TABLE ExamSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each schedule
    Class VARCHAR(50) NOT NULL,                 -- Class name/identifier (e.g., "Class 10A")
    Subject VARCHAR(100) NOT NULL,              -- Subject name (e.g., "Mathematics")
    Token VARCHAR(50) NOT NULL,                 -- Token for exam authentication
    ExamDate DATE NOT NULL,                     -- Date of the exam
    ExamTime TIME NOT NULL                      -- Time of the exam
);

-- Step 2: Insert sample data into the ExamSchedules table
INSERT INTO ExamSchedules (Class, Subject, Token, ExamDate, ExamTime)
VALUES 
    ('Class 10A', 'Mathematics', 'MTX1234', '2023-10-15', '09:00:00'),
    ('Class 10B', 'Physics', 'PHX5678', '2023-10-16', '10:00:00'),
    ('Class 11A', 'Chemistry', 'CHX9101', '2023-10-17', '08:30:00'),
    ('Class 12B', 'History', 'HTX1121', '2023-10-18', '13:00:00');

-- Step 3: Query to retrieve all exam schedules
SELECT * FROM ExamSchedules;

-- Step 4: Query to retrieve exam schedules for a specific class (example: "Class 10A")
SELECT * FROM ExamSchedules
WHERE Class = 'Class 10A';

-- Step 5: Query to retrieve exam schedules for a specific date (example: "2023-10-15")
SELECT * FROM ExamSchedules
WHERE ExamDate = '2023-10-15';
```
