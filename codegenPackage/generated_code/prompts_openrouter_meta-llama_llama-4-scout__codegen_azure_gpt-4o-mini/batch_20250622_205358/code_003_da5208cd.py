"""
Generated Code Metadata:
========================
Original URL: https://munshihr.com
Prompt: Design a database schema for an HR training and skill development platform that tracks employee training programs and skill assessments.
Generated: DETERMINISTIC_da5208cd72abb276
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an HR training and skill development platform

-- Create a table to store employee information
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,             -- Employee's first name
    LastName VARCHAR(50) NOT NULL,               -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Employee's email address
    HireDate DATE NOT NULL,                       -- Date the employee was hired
    Department VARCHAR(50) NOT NULL              -- Department the employee belongs to
);

-- Create a table to store training programs
CREATE TABLE TrainingPrograms (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each training program
    ProgramName VARCHAR(100) NOT NULL,           -- Name of the training program
    Description TEXT,                             -- Description of the training program
    StartDate DATE NOT NULL,                      -- Start date of the training program
    EndDate DATE NOT NULL,                        -- End date of the training program
    MaxParticipants INT NOT NULL                  -- Maximum number of participants allowed
);

-- Create a table to store employee training enrollments
CREATE TABLE EmployeeTrainingEnrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each enrollment
    EmployeeID INT NOT NULL,                      -- Foreign key referencing Employees
    ProgramID INT NOT NULL,                       -- Foreign key referencing TrainingPrograms
    EnrollmentDate DATE NOT NULL,                 -- Date the employee enrolled in the program
    Status ENUM('Enrolled', 'Completed', 'Cancelled') NOT NULL,  -- Status of the enrollment
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE
);

-- Create a table to store skill assessments
CREATE TABLE SkillAssessments (
    AssessmentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each assessment
    EmployeeID INT NOT NULL,                       -- Foreign key referencing Employees
    SkillName VARCHAR(100) NOT NULL,              -- Name of the skill being assessed
    AssessmentDate DATE NOT NULL,                  -- Date of the assessment
    Score INT CHECK (Score >= 0 AND Score <= 100), -- Score received in the assessment
    Comments TEXT,                                 -- Additional comments about the assessment
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Create a table to store skills associated with training programs
CREATE TABLE ProgramSkills (
    ProgramSkillID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each program-skill association
    ProgramID INT NOT NULL,                        -- Foreign key referencing TrainingPrograms
    SkillName VARCHAR(100) NOT NULL,              -- Name of the skill associated with the program
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE
);
```
