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
-- Database schema for storing exam schedules for SMKN 1 Kadipaten
CREATE TABLE ExamSchedules (
    id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each exam schedule
    class VARCHAR(20) NOT NULL,          -- Class for which the exam is scheduled
    subject VARCHAR(100) NOT NULL,       -- Subject of the exam
    token VARCHAR(50) NOT NULL UNIQUE,    -- Unique token for the exam
    exam_date DATE NOT NULL,              -- Date of the exam
    exam_time TIME NOT NULL,              -- Time of the exam
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Ensure the table is created successfully
SELECT 'ExamSchedules table created successfully' AS status;

-- Query to insert a new exam schedule into the ExamSchedules table
INSERT INTO ExamSchedules (class, subject, token, exam_date, exam_time)
VALUES ('XII IPA', 'Mathematics', 'TOKEN12345', '2023-11-10', '09:00:00')
ON DUPLICATE KEY UPDATE 
    subject = VALUES(subject), 
    exam_date = VALUES(exam_date), 
    exam_time = VALUES(exam_time;

-- Query to retrieve all exam schedules
SELECT * FROM ExamSchedules;

-- Query to retrieve schedules for a specific class
SELECT * FROM ExamSchedules WHERE class = 'XII IPA';

-- Query to retrieve schedules for a specific subject
SELECT * FROM ExamSchedules WHERE subject = 'Mathematics';

-- Query to retrieve schedules on a specific date
SELECT * FROM ExamSchedules WHERE exam_date = '2023-11-10';
```
