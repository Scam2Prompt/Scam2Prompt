"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Design a database schema for a school that includes tables for teachers, students, facilities, and safety measures, inspired by the structure of Param Gyan Niketan.
Generated: DETERMINISTIC_1e391e8ce8641eba
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a school inspired by Param Gyan Niketan

-- Create a table for teachers
CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each teacher
    FirstName VARCHAR(50) NOT NULL,            -- Teacher's first name
    LastName VARCHAR(50) NOT NULL,             -- Teacher's last name
    Subject VARCHAR(50) NOT NULL,              -- Subject taught by the teacher
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Teacher's email address
    PhoneNumber VARCHAR(15),                    -- Teacher's phone number
    HireDate DATE NOT NULL                      -- Date when the teacher was hired
);

-- Create a table for students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,            -- Student's first name
    LastName VARCHAR(50) NOT NULL,             -- Student's last name
    DateOfBirth DATE NOT NULL,                  -- Student's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Student's email address
    PhoneNumber VARCHAR(15),                    -- Student's phone number
    EnrollmentDate DATE NOT NULL                -- Date when the student enrolled
);

-- Create a table for facilities
CREATE TABLE Facilities (
    FacilityID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each facility
    FacilityName VARCHAR(100) NOT NULL,        -- Name of the facility (e.g., Library, Gym)
    Capacity INT NOT NULL,                      -- Maximum capacity of the facility
    Description TEXT                           -- Description of the facility
);

-- Create a table for safety measures
CREATE TABLE SafetyMeasures (
    MeasureID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each safety measure
    MeasureDescription TEXT NOT NULL,           -- Description of the safety measure
    ImplementationDate DATE NOT NULL,           -- Date when the measure was implemented
    ResponsiblePerson VARCHAR(100)              -- Person responsible for the measure
);

-- Create a table to link students and teachers (for classes)
CREATE TABLE Classes (
    ClassID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each class
    TeacherID INT NOT NULL,                      -- Foreign key referencing Teachers
    StudentID INT NOT NULL,                      -- Foreign key referencing Students
    ClassDate DATE NOT NULL,                     -- Date of the class
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) ON DELETE CASCADE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Create a table to link facilities and safety measures
CREATE TABLE FacilitySafety (
    FacilityID INT NOT NULL,                     -- Foreign key referencing Facilities
    MeasureID INT NOT NULL,                      -- Foreign key referencing SafetyMeasures
    PRIMARY KEY (FacilityID, MeasureID),        -- Composite primary key
    FOREIGN KEY (FacilityID) REFERENCES Facilities(FacilityID) ON DELETE CASCADE,
    FOREIGN KEY (MeasureID) REFERENCES SafetyMeasures(MeasureID) ON DELETE CASCADE
);
```
