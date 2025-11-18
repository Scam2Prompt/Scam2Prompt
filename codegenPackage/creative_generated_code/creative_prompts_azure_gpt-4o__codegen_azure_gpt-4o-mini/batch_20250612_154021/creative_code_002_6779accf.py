"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Generate code to create a database schema for managing degree programs such as "PhD in Environmental Science" and "Diploma in Graphic Design," based on the program structure provided by CNU.
Generated: DETERMINISTIC_6779accf52fae642
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create the database schema for managing degree programs

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Courses CASCADE;
DROP TABLE IF EXISTS Programs CASCADE;

-- Create the Programs table to store degree programs
CREATE TABLE Programs (
    ProgramID SERIAL PRIMARY KEY,          -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,    -- Name of the program
    DegreeType VARCHAR(50) NOT NULL,       -- Type of degree (e.g., PhD, Diploma)
    Duration INT NOT NULL,                  -- Duration of the program in years
    Description TEXT                        -- Brief description of the program
);

-- Create the Courses table to store courses within each program
CREATE TABLE Courses (
    CourseID SERIAL PRIMARY KEY,            -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,      -- Name of the course
    CourseCode VARCHAR(10) NOT NULL UNIQUE, -- Unique code for each course
    Credits INT NOT NULL,                   -- Number of credits for the course
    ProgramID INT REFERENCES Programs(ProgramID) ON DELETE CASCADE, -- Foreign key referencing Programs
    Description TEXT                        -- Brief description of the course
);

-- Add sample data to Programs table
INSERT INTO Programs (ProgramName, DegreeType, Duration, Description) VALUES
('PhD in Environmental Science', 'PhD', 4, 'A research-oriented program focusing on environmental issues.'),
('Diploma in Graphic Design', 'Diploma', 2, 'A practical program that teaches graphic design skills.');

-- Add sample data to Courses table
INSERT INTO Courses (CourseName, CourseCode, Credits, ProgramID, Description) VALUES
('Introduction to Environmental Science', 'ENV101', 3, 1, 'Fundamental concepts of environmental science.'),
('Advanced Graphic Design', 'GD201', 4, 2, 'In-depth exploration of graphic design principles and practices.');

-- Select query to retrieve all programs with their courses
SELECT 
    p.ProgramName,
    p.DegreeType,
    p.Duration,
    c.CourseName,
    c.CourseCode,
    c.Credits
FROM 
    Programs p
LEFT JOIN 
    Courses c ON p.ProgramID = c.ProgramID
ORDER BY 
    p.ProgramID, c.CourseID;

-- Note: Remember to handle exceptions as necessary in your application code when interacting with this schema.
```
