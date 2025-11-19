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
-- Database schema for SMKN 1 Kadipaten exam schedules
CREATE TABLE exam_schedules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    class VARCHAR(20) NOT NULL COMMENT 'Class name (e.g., X-RPL-1, XI-TKJ-2)',
    subject VARCHAR(100) NOT NULL COMMENT 'Exam subject name',
    token VARCHAR(20) NOT NULL COMMENT 'Unique exam token/identifier',
    exam_date DATE NOT NULL COMMENT 'Date of the exam (YYYY-MM-DD)',
    start_time TIME NOT NULL COMMENT 'Start time of exam (HH:MM:SS)',
    end_time TIME NOT NULL COMMENT 'End time of exam (HH:MM:SS)',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Record creation timestamp',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Record update timestamp',
    CONSTRAINT unique_exam_token UNIQUE (token)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Stores exam schedules for SMKN 1 Kadipaten';

-- Create an index for faster class-based queries
CREATE INDEX idx_class ON exam_schedules (class);

-- Create an index for faster date-based queries
CREATE INDEX idx_exam_date ON exam_schedules (exam_date);

-- Insert a new exam schedule
INSERT INTO exam_schedules (
    class, 
    subject, 
    token, 
    exam_date, 
    start_time, 
    end_time
) VALUES (
    'X-RPL-1', 
    'Pemrograman Dasar', 
    'EXAM2023PD001', 
    '2023-11-15', 
    '08:00:00', 
    '10:00:00'
);

-- Retrieve all exam schedules
SELECT 
    id,
    class,
    subject,
    token,
    DATE_FORMAT(exam_date, '%Y-%m-%d') AS exam_date,
    TIME_FORMAT(start_time, '%H:%i') AS start_time,
    TIME_FORMAT(end_time, '%H:%i') AS end_time
FROM 
    exam_schedules
ORDER BY 
    exam_date, 
    start_time;

-- Retrieve exam schedules for a specific class
SELECT 
    id,
    class,
    subject,
    token,
    DATE_FORMAT(exam_date, '%Y-%m-%d') AS exam_date,
    TIME_FORMAT(start_time, '%H:%i') AS start_time,
    TIME_FORMAT(end_time, '%H:%i') AS end_time
FROM 
    exam_schedules
WHERE 
    class = 'X-RPL-1'
ORDER BY 
    exam_date, 
    start_time;

-- Retrieve exam schedules for a specific date range
SELECT 
    id,
    class,
    subject,
    token,
    DATE_FORMAT(exam_date, '%Y-%m-%d') AS exam_date,
    TIME_FORMAT(start_time, '%H:%i') AS start_time,
    TIME_FORMAT(end_time, '%H:%i') AS end_time
FROM 
    exam_schedules
WHERE 
    exam_date BETWEEN '2023-11-01' AND '2023-11-30'
ORDER BY 
    exam_date, 
    start_time;

-- Retrieve a specific exam schedule by token
SELECT 
    id,
    class,
    subject,
    token,
    DATE_FORMAT(exam_date, '%Y-%m-%d') AS exam_date,
    TIME_FORMAT(start_time, '%H:%i') AS start_time,
    TIME_FORMAT(end_time, '%H:%i') AS end_time
FROM 
    exam_schedules
WHERE 
    token = 'EXAM2023PD001';
```
