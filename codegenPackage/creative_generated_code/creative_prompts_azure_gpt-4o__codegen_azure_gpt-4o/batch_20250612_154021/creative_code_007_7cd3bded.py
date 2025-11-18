"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Write SQL queries to retrieve information about students enrolled in programs like "Bachelor’s in Psychology" and "Master’s in Education Leadership," referencing the program details from CNU.
Generated: DETERMINISTIC_7cd3bdedd55a9181
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Queries to retrieve student information for specific programs

-- Step 1: Create a table for the students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,          -- Unique identifier for each student
    FirstName VARCHAR(50),              -- First name of the student
    LastName VARCHAR(50),               -- Last name of the student
    ProgramID INT                       -- Foreign key referencing the Programs table
);

-- Step 2: Create a table for the programs
CREATE TABLE Programs (
    ProgramID INT PRIMARY KEY,          -- Unique identifier for each program
    ProgramName VARCHAR(100),           -- Name of the program
    InstitutionName VARCHAR(100)        -- Name of the institution offering the program
);

-- Step 3: Insert sample data into the Programs table
INSERT INTO Programs (ProgramID, ProgramName, InstitutionName) VALUES
(1, 'Bachelor’s in Psychology', 'CNU'),
(2, 'Master’s in Education Leadership', 'CNU'),
(3, 'Bachelor’s in Computer Science', 'CNU'); -- Additional program for variety

-- Step 4: Insert sample data into the Students table
INSERT INTO Students (StudentID, FirstName, LastName, ProgramID) VALUES
(101, 'Alice', 'Smith', 1),
(102, 'Bob', 'Johnson', 2),
(103, 'Charlie', 'Williams', 3);

-- Step 5: Query to retrieve students enrolled in "Bachelor’s in Psychology" or "Master’s in Education Leadership"
SELECT 
    S.StudentID,
    S.FirstName,
    S.LastName,
    P.ProgramName,
    P.InstitutionName
FROM 
    Students S
INNER JOIN 
    Programs P
ON 
    S.ProgramID = P.ProgramID
WHERE 
    P.ProgramName IN ('Bachelor’s in Psychology', 'Master’s in Education Leadership')
    AND P.InstitutionName = 'CNU'; -- Ensuring the institution matches "CNU"

-- The above query joins the Students and Programs tables, filters for the specified programs, and institution.
```
