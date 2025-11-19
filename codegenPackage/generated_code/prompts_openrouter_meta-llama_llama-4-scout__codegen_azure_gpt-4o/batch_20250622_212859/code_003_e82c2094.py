"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: "Design a data model for tracking employee progress and engagement in a company-wide training program, similar to Virtual5's solutions for organizational development, and provide a sample SQL schema."
Generated: DETERMINISTIC_e82c2094c4de1e26
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for tracking employee progress and engagement in a company-wide training program

-- Table to store information about employees
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,            -- Employee's first name
    LastName VARCHAR(50) NOT NULL,             -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Employee's email address
    Department VARCHAR(50),                    -- Department the employee belongs to
    DateJoined DATE NOT NULL,                  -- Date the employee joined the company
    IsActive BOOLEAN DEFAULT TRUE              -- Indicates if the employee is currently active
);

-- Table to store information about training programs
CREATE TABLE TrainingPrograms (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each training program
    ProgramName VARCHAR(100) NOT NULL,         -- Name of the training program
    Description TEXT,                          -- Description of the training program
    StartDate DATE NOT NULL,                   -- Start date of the training program
    EndDate DATE NOT NULL,                     -- End date of the training program
    IsMandatory BOOLEAN DEFAULT FALSE          -- Indicates if the program is mandatory
);

-- Table to track employee enrollment in training programs
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each enrollment record
    EmployeeID INT NOT NULL,                     -- Foreign key referencing Employees table
    ProgramID INT NOT NULL,                      -- Foreign key referencing TrainingPrograms table
    EnrollmentDate DATE NOT NULL,                -- Date the employee enrolled in the program
    CompletionDate DATE,                         -- Date the employee completed the program (NULL if not completed)
    ProgressPercentage INT DEFAULT 0,            -- Progress percentage (0-100)
    EngagementScore INT DEFAULT 0,               -- Engagement score (e.g., based on participation, feedback, etc.)
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE
);

-- Table to store feedback provided by employees for training programs
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each feedback record
    EmployeeID INT NOT NULL,                   -- Foreign key referencing Employees table
    ProgramID INT NOT NULL,                    -- Foreign key referencing TrainingPrograms table
    FeedbackText TEXT NOT NULL,                -- Feedback provided by the employee
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating provided by the employee (1-5 scale)
    FeedbackDate DATE NOT NULL,                -- Date the feedback was submitted
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE
);

-- Table to store training program facilitators
CREATE TABLE Facilitators (
    FacilitatorID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each facilitator
    ProgramID INT NOT NULL,                       -- Foreign key referencing TrainingPrograms table
    FacilitatorName VARCHAR(100) NOT NULL,        -- Name of the facilitator
    ContactEmail VARCHAR(100) UNIQUE NOT NULL,    -- Contact email of the facilitator
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_employee_email ON Employees(Email);
CREATE INDEX idx_program_name ON TrainingPrograms(ProgramName);
CREATE INDEX idx_enrollment_employee_program ON Enrollments(EmployeeID, ProgramID);
CREATE INDEX idx_feedback_employee_program ON Feedback(EmployeeID, ProgramID);
```
