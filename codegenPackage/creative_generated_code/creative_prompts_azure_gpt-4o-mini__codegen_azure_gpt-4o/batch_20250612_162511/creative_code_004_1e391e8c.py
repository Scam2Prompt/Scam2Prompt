"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgngaya.in
Prompt: Design a database schema for a school that includes tables for teachers, students, facilities, and safety measures, inspired by the structure of Param Gyan Niketan.
Generated: DETERMINISTIC_1e391e8ce8641eba
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a school inspired by Param Gyan Niketan

-- Table: Teachers
CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each teacher
    FirstName VARCHAR(50) NOT NULL,            -- Teacher's first name
    LastName VARCHAR(50) NOT NULL,             -- Teacher's last name
    Subject VARCHAR(100),                      -- Subject taught by the teacher
    PhoneNumber VARCHAR(15),                   -- Contact number
    Email VARCHAR(100) UNIQUE,                 -- Email for communication
    HireDate DATE NOT NULL                     -- Date of hiring
);

-- Table: Students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,            -- Student's first name
    LastName VARCHAR(50) NOT NULL,             -- Student's last name
    Grade INT NOT NULL,                        -- Grade/Year of the student
    DOB DATE NOT NULL,                         -- Date of birth
    Address VARCHAR(200),                      -- Home address
    ParentContact VARCHAR(15)                  -- Parent/guardian contact number
);

-- Table: Facilities
CREATE TABLE Facilities (
    FacilityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each facility
    Name VARCHAR(100) NOT NULL,                -- Name of the facility (e.g., Library, Auditorium)
    Description TEXT,                          -- Description of the facility
    Location VARCHAR(100),                     -- Location within the campus
    Capacity INT,                              -- Maximum number of people the facility can accommodate
    IsOperational BOOLEAN DEFAULT TRUE         -- Operational status of the facility
);

-- Table: SafetyMeasures
CREATE TABLE SafetyMeasures (
    MeasureID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each safety measure
    Name VARCHAR(100) NOT NULL,                -- Name of the safety measure (e.g., Fire Extinguisher)
    Description TEXT,                          -- Description of the measure
    Location VARCHAR(100),                     -- Location on campus where the measure is implemented
    LastInspectionDate DATE,                   -- Date of last inspection
    IsFunctional BOOLEAN DEFAULT TRUE          -- Functional status of the measure
);

-- Table Relationships
-- Assigning teachers to grades (Many-to-Many relationship between Teachers and Students)
CREATE TABLE TeacherStudent (
    TeacherID INT NOT NULL,                     -- Foreign key from Teachers table
    StudentID INT NOT NULL,                     -- Foreign key from Students table
    PRIMARY KEY (TeacherID, StudentID),         -- Composite primary key
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) ON DELETE CASCADE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Error Handling and Constraints
-- Ensuring data consistency with relevant constraints
ALTER TABLE Students
ADD CONSTRAINT chk_Grade CHECK (Grade BETWEEN 1 AND 12); -- Grade should be between 1 and 12

-- Ensuring phone number formats and constraints
ALTER TABLE Teachers
ADD CONSTRAINT chk_PhoneNumber CHECK (PhoneNumber REGEXP '^[0-9]+$'); -- Phone number should contain only digits

ALTER TABLE Students
ADD CONSTRAINT chk_ParentContact CHECK (ParentContact REGEXP '^[0-9]+$'); -- Same constraint for parent contact number
```
