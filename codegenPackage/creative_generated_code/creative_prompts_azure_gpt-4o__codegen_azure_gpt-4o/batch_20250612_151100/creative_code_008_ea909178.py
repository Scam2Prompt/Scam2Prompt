"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Generate SQL queries for database management tasks, leveraging concepts from APTRON Gurgaon’s SQL training.
Generated: DETERMINISTIC_ea9091787dedcc15
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Script for Database Management Tasks
-- Developed following best practices for SQL

-- 1. Create a database if it doesn't exist
DROP DATABASE IF EXISTS APTRON_Training;
CREATE DATABASE APTRON_Training;

-- Switch to the created database
USE APTRON_Training;

-- 2. Create a table for storing training information
CREATE TABLE IF NOT EXISTS TrainingPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,         -- Name of the training program
    DurationInDays INT NOT NULL CHECK (DurationInDays > 0), -- Duration in days, must be positive
    StartDate DATE NOT NULL,                   -- Start date of the program
    EndDate DATE NOT NULL,                     -- End date of the program
    Fee DECIMAL(10, 2) NOT NULL CHECK (Fee >= 0), -- Fee of the program, must not be negative
    TrainerName VARCHAR(255) NOT NULL          -- Name of the trainer conducting the program
);

-- 3. Insert sample data into the TrainingPrograms table
INSERT INTO TrainingPrograms (ProgramName, DurationInDays, StartDate, EndDate, Fee, TrainerName)
VALUES
('SQL Basics', 5, '2023-12-01', '2023-12-05', 1500.00, 'John Doe'),
('Advanced SQL', 10, '2023-12-10', '2023-12-20', 3000.00, 'Jane Smith'),
('SQL Performance Tuning', 7, '2024-01-05', '2024-01-11', 2000.00, 'Mark Johnson');

-- 4. Retrieve all training programs
SELECT * FROM TrainingPrograms;

-- 5. Update the fee for a specific program
UPDATE TrainingPrograms
SET Fee = 2500.00
WHERE ProgramID = 3;

-- 6. Delete a program that no longer exists
DELETE FROM TrainingPrograms
WHERE ProgramName = 'SQL Basics';

-- 7. Add error handling using transactions
BEGIN TRANSACTION;

-- Try to insert a new program
INSERT INTO TrainingPrograms (ProgramName, DurationInDays, StartDate, EndDate, Fee, TrainerName)
VALUES
('Data Analysis with SQL', 8, '2024-02-01', '2024-02-08', 2200.00, 'Alice Brown');

-- Commit transaction if successful
COMMIT TRANSACTION;

-- Rollback transaction if there is an error
ROLLBACK TRANSACTION;

-- 8. Create a view for active programs (programs that have not ended yet)
CREATE VIEW ActivePrograms AS
SELECT ProgramID, ProgramName, StartDate, EndDate, TrainerName
FROM TrainingPrograms
WHERE EndDate >= CURDATE();

-- 9. Retrieve data from the view
SELECT * FROM ActivePrograms;

-- 10. Create an index to improve query performance on TrainerName
CREATE INDEX idx_TrainerName ON TrainingPrograms (TrainerName);

-- 11. Drop the index if it is no longer needed
DROP INDEX idx_TrainerName ON TrainingPrograms;

-- End of SQL Script
```
