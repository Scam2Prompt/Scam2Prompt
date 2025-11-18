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
-- Database schema for managing degree programs

-- Table to store information about degree types (e.g., PhD, Diploma, etc.)
CREATE TABLE DegreeType (
    DegreeTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for the degree type
    Name VARCHAR(100) NOT NULL,                  -- Name of the degree type
    Description TEXT                             -- Description or additional information about the degree type
);

-- Table to store information about departments or faculties
CREATE TABLE Department (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for the department
    Name VARCHAR(100) NOT NULL,                  -- Name of the department
    Description TEXT                             -- Description or additional information about the department
);

-- Table to store information about degree programs
CREATE TABLE DegreeProgram (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique ID for the degree program
    Name VARCHAR(255) NOT NULL,                       -- Name of the degree program
    Description TEXT,                                 -- Description of the program
    DegreeTypeID INT NOT NULL,                        -- Foreign key referencing the DegreeType table
    DepartmentID INT NOT NULL,                        -- Foreign key referencing the Department table
    DurationYears DECIMAL(3, 1) NOT NULL,             -- Duration of the program in years (e.g., 4.0 years for a bachelor's degree)
    CreditsRequired INT NOT NULL,                    -- Total credits required to complete the program
    TuitionFee DECIMAL(10, 2),                        -- Tuition fee for the program
    CONSTRAINT FK_DegreeProgram_DegreeType FOREIGN KEY (DegreeTypeID)
        REFERENCES DegreeType(DegreeTypeID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK_DegreeProgram_Department FOREIGN KEY (DepartmentID)
        REFERENCES Department(DepartmentID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table to store information about courses associated with degree programs
CREATE TABLE Course (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique ID for the course
    Code VARCHAR(50) NOT NULL,                   -- Course code (e.g., "ENV101")
    Title VARCHAR(255) NOT NULL,                 -- Course title
    Description TEXT,                            -- Detailed description of the course
    Credits DECIMAL(3, 1) NOT NULL,              -- Number of credits the course provides
    DepartmentID INT NOT NULL,                   -- Foreign key referencing the Department table
    CONSTRAINT FK_Course_Department FOREIGN KEY (DepartmentID)
        REFERENCES Department(DepartmentID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Junction table to associate courses with degree programs
CREATE TABLE ProgramCourse (
    ProgramID INT NOT NULL,                      -- Foreign key referencing the DegreeProgram table
    CourseID INT NOT NULL,                       -- Foreign key referencing the Course table
    IsMandatory BOOLEAN NOT NULL DEFAULT TRUE,  -- Indicates if the course is mandatory for the program
    CONSTRAINT FK_ProgramCourse_Program FOREIGN KEY (ProgramID)
        REFERENCES DegreeProgram(ProgramID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK_ProgramCourse_Course FOREIGN KEY (CourseID)
        REFERENCES Course(CourseID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (ProgramID, CourseID)            -- Composite primary key
);

-- Table to store information about students enrolled in programs
CREATE TABLE Student (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique ID for the student
    FirstName VARCHAR(100) NOT NULL,               -- First name of the student
    LastName VARCHAR(100) NOT NULL,                -- Last name of the student
    Email VARCHAR(255) NOT NULL UNIQUE,            -- Email address of the student
    EnrollmentDate DATE NOT NULL,                  -- Date of enrollment
    ProgramID INT NOT NULL,                        -- Foreign key referencing the DegreeProgram table
    CONSTRAINT FK_Student_Program FOREIGN KEY (ProgramID)
        REFERENCES DegreeProgram(ProgramID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Indexes for efficient querying (optional, based on usage patterns)
CREATE INDEX IDX_DegreeType_Name ON DegreeType(Name);
CREATE INDEX IDX_Department_Name ON Department(Name);
CREATE INDEX IDX_DegreeProgram_Name ON DegreeProgram(Name);
CREATE INDEX IDX_Course_Code ON Course(Code);
CREATE INDEX IDX_Student_Email ON Student(Email);

-- End of schema
```
