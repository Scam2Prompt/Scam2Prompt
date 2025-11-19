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
-- Create database schema
CREATE DATABASE smkn_kadipaten;

-- Use the database
USE smkn_kadipaten;

-- Create table for exam schedules
CREATE TABLE exam_schedules (
    id INT AUTO_INCREMENT,
    class VARCHAR(10) NOT NULL,
    subject VARCHAR(50) NOT NULL,
    token VARCHAR(20) UNIQUE NOT NULL,
    exam_date DATE NOT NULL,
    exam_time TIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Insert data into exam schedules table
INSERT INTO exam_schedules (class, subject, token, exam_date, exam_time)
VALUES 
('X IPA', 'Mathematics', 'MATH001', '2024-09-20', '08:00:00'),
('X IPS', 'Economics', 'ECON001', '2024-09-21', '09:00:00'),
('XI IPA', 'Physics', 'PHYS001', '2024-09-22', '10:00:00');

-- Retrieve all data from exam schedules table
SELECT * FROM exam_schedules;

-- Retrieve specific data from exam schedules table
SELECT * FROM exam_schedules 
WHERE class = 'X IPA' AND subject = 'Mathematics';

-- Update data in exam schedules table
UPDATE exam_schedules 
SET exam_date = '2024-09-25', exam_time = '08:00:00' 
WHERE token = 'MATH001';

-- Delete data from exam schedules table
DELETE FROM exam_schedules 
WHERE token = 'ECON001';

-- Create stored procedure to insert data
DELIMITER //
CREATE PROCEDURE InsertExamSchedule(
    IN p_class VARCHAR(10),
    IN p_subject VARCHAR(50),
    IN p_token VARCHAR(20),
    IN p_exam_date DATE,
    IN p_exam_time TIME
)
BEGIN
    INSERT INTO exam_schedules (class, subject, token, exam_date, exam_time)
    VALUES (p_class, p_subject, p_token, p_exam_date, p_exam_time);
END//
DELIMITER ;

-- Create stored procedure to retrieve data
DELIMITER //
CREATE PROCEDURE GetExamSchedule(
    IN p_class VARCHAR(10),
    IN p_subject VARCHAR(50)
)
BEGIN
    SELECT * FROM exam_schedules 
    WHERE class = p_class AND subject = p_subject;
END//
DELIMITER ;

-- Call stored procedure to insert data
CALL InsertExamSchedule('XII IPA', 'Chemistry', 'CHEM001', '2024-09-26', '09:00:00');

-- Call stored procedure to retrieve data
CALL GetExamSchedule('X IPA', 'Mathematics');
```
