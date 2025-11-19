"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Design a database schema to store information about underprivileged children and their education progress, similar to Indological India's education empowerment programs.
Generated: DETERMINISTIC_b21d644357eec457
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about underprivileged children and their education progress

-- Table to store information about children
CREATE TABLE Children (
    ChildID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each child
    FirstName VARCHAR(50) NOT NULL,         -- First name of the child
    LastName VARCHAR(50) NOT NULL,          -- Last name of the child
    DateOfBirth DATE NOT NULL,              -- Date of birth of the child
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the child
    Address TEXT,                           -- Address of the child
    GuardianName VARCHAR(100),              -- Name of the child's guardian
    ContactNumber VARCHAR(15),              -- Contact number of the guardian
    RegistrationDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of registration
    Notes TEXT                              -- Additional notes about the child
);

-- Table to store information about education programs
CREATE TABLE EducationPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL,        -- Name of the education program
    Description TEXT,                         -- Description of the program
    StartDate DATE NOT NULL,                  -- Start date of the program
    EndDate DATE,                             -- End date of the program (nullable for ongoing programs)
    Status ENUM('Active', 'Completed', 'Inactive') NOT NULL DEFAULT 'Active' -- Status of the program
);

-- Table to store enrollment information (linking children to education programs)
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    ChildID INT NOT NULL,                        -- Foreign key referencing Children table
    ProgramID INT NOT NULL,                      -- Foreign key referencing EducationPrograms table
    EnrollmentDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of enrollment
    ProgressPercentage DECIMAL(5, 2) DEFAULT 0.00, -- Progress percentage in the program
    CompletionStatus ENUM('Not Started', 'In Progress', 'Completed') NOT NULL DEFAULT 'Not Started', -- Status of completion
    Feedback TEXT,                               -- Feedback or remarks about the child's progress
    FOREIGN KEY (ChildID) REFERENCES Children(ChildID) ON DELETE CASCADE, -- Cascade delete if child is removed
    FOREIGN KEY (ProgramID) REFERENCES EducationPrograms(ProgramID) ON DELETE CASCADE -- Cascade delete if program is removed
);

-- Table to store attendance records for children in programs
CREATE TABLE Attendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    ChildID INT NOT NULL,                        -- Foreign key referencing Children table
    ProgramID INT NOT NULL,                      -- Foreign key referencing EducationPrograms table
    AttendanceDate DATE NOT NULL,                -- Date of attendance
    Status ENUM('Present', 'Absent') NOT NULL,   -- Attendance status
    Remarks TEXT,                                -- Additional remarks about attendance
    FOREIGN KEY (ChildID) REFERENCES Children(ChildID) ON DELETE CASCADE, -- Cascade delete if child is removed
    FOREIGN KEY (ProgramID) REFERENCES EducationPrograms(ProgramID) ON DELETE CASCADE -- Cascade delete if program is removed
);

-- Table to store performance metrics for children
CREATE TABLE PerformanceMetrics (
    MetricID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each performance metric
    ChildID INT NOT NULL,                    -- Foreign key referencing Children table
    ProgramID INT NOT NULL,                  -- Foreign key referencing EducationPrograms table
    MetricName VARCHAR(100) NOT NULL,        -- Name of the performance metric (e.g., "Math Score", "Reading Level")
    MetricValue DECIMAL(10, 2) NOT NULL,     -- Value of the performance metric
    RecordedDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date the metric was recorded
    FOREIGN KEY (ChildID) REFERENCES Children(ChildID) ON DELETE CASCADE, -- Cascade delete if child is removed
    FOREIGN KEY (ProgramID) REFERENCES EducationPrograms(ProgramID) ON DELETE CASCADE -- Cascade delete if program is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_child_program ON Enrollments (ChildID, ProgramID);
CREATE INDEX idx_attendance_date ON Attendance (AttendanceDate);
CREATE INDEX idx_metric_date ON PerformanceMetrics (RecordedDate);
```
