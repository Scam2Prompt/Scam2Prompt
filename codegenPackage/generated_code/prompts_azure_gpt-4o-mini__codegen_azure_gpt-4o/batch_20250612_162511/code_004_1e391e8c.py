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
-- Database Schema for a School inspired by Param Gyan Niketan

-- Table: Teachers
CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each teacher
    FirstName VARCHAR(50) NOT NULL,           -- First name of the teacher
    LastName VARCHAR(50) NOT NULL,            -- Last name of the teacher
    Subject VARCHAR(100) NOT NULL,            -- Subject taught by the teacher
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the teacher
    PhoneNumber VARCHAR(15),                  -- Contact number of the teacher
    HireDate DATE NOT NULL,                   -- Date the teacher was hired
    Salary DECIMAL(10, 2) NOT NULL            -- Salary of the teacher
);

-- Table: Students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student
    GradeLevel INT NOT NULL,                  -- Grade level of the student
    Email VARCHAR(100) UNIQUE,                -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    EnrollmentDate DATE NOT NULL              -- Date the student was enrolled
);

-- Table: Facilities
CREATE TABLE Facilities (
    FacilityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each facility
    Name VARCHAR(100) NOT NULL,                -- Name of the facility (e.g., Library, Playground)
    Description TEXT,                          -- Description of the facility
    Capacity INT,                              -- Maximum capacity of the facility
    Location VARCHAR(100) NOT NULL,            -- Location of the facility within the school
    MaintenanceDate DATE                       -- Last maintenance date of the facility
);

-- Table: SafetyMeasures
CREATE TABLE SafetyMeasures (
    SafetyMeasureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each safety measure
    Name VARCHAR(100) NOT NULL,                     -- Name of the safety measure (e.g., Fire Extinguisher, CCTV)
    Description TEXT,                               -- Description of the safety measure
    InstallationDate DATE NOT NULL,                 -- Date the safety measure was installed
    LastInspectionDate DATE,                        -- Date of the last inspection
    Status ENUM('Active', 'Inactive') NOT NULL      -- Current status of the safety measure
);

-- Relationships and Foreign Keys
-- Assuming teachers and students may be associated with facilities (e.g., classrooms)

-- Table: TeacherFacilityMapping
CREATE TABLE TeacherFacilityMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the mapping
    TeacherID INT NOT NULL,                   -- Foreign key referencing Teachers table
    FacilityID INT NOT NULL,                  -- Foreign key referencing Facilities table
    AssignmentDate DATE NOT NULL,             -- Date the teacher was assigned to the facility
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) ON DELETE CASCADE,
    FOREIGN KEY (FacilityID) REFERENCES Facilities(FacilityID) ON DELETE CASCADE
);

-- Table: StudentFacilityMapping
CREATE TABLE StudentFacilityMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the mapping
    StudentID INT NOT NULL,                   -- Foreign key referencing Students table
    FacilityID INT NOT NULL,                  -- Foreign key referencing Facilities table
    AssignmentDate DATE NOT NULL,             -- Date the student was assigned to the facility
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (FacilityID) REFERENCES Facilities(FacilityID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_teacher_email ON Teachers(Email);
CREATE INDEX idx_student_email ON Students(Email);
CREATE INDEX idx_facility_name ON Facilities(Name);
CREATE INDEX idx_safety_measure_name ON SafetyMeasures(Name);
```
