"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Design a database schema to store information about SOMTU's MBA programs, including program details, course structures, and student records, and provide a simple SQL query to demonstrate its usage.
Generated: DETERMINISTIC_48feebd272893d13
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SOMTU's MBA programs

-- Create a table to store program details
CREATE TABLE MBA_Programs (
    program_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each program
    program_name VARCHAR(100) NOT NULL,         -- Name of the MBA program
    duration INT NOT NULL,                       -- Duration of the program in months
    start_date DATE NOT NULL,                   -- Start date of the program
    end_date DATE NOT NULL                       -- End date of the program
);

-- Create a table to store course structures
CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each course
    program_id INT NOT NULL,                     -- Foreign key referencing MBA_Programs
    course_name VARCHAR(100) NOT NULL,           -- Name of the course
    credits INT NOT NULL,                         -- Number of credits for the course
    FOREIGN KEY (program_id) REFERENCES MBA_Programs(program_id) -- Establishing foreign key relationship
);

-- Create a table to store student records
CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,             -- Student's first name
    last_name VARCHAR(50) NOT NULL,              -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL,          -- Student's email address (must be unique)
    program_id INT NOT NULL,                      -- Foreign key referencing MBA_Programs
    enrollment_date DATE NOT NULL,                -- Date of enrollment
    FOREIGN KEY (program_id) REFERENCES MBA_Programs(program_id) -- Establishing foreign key relationship
);

-- Sample SQL query to demonstrate usage: Retrieve all students enrolled in a specific MBA program
SELECT 
    s.student_id,
    s.first_name,
    s.last_name,
    p.program_name,
    s.enrollment_date
FROM 
    Students s
JOIN 
    MBA_Programs p ON s.program_id = p.program_id
WHERE 
    p.program_name = 'Executive MBA';  -- Replace with the desired program name
```
