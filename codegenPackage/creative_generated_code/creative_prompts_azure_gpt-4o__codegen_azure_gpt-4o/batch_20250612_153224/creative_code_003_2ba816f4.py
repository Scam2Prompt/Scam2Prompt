"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Develop a database schema for managing student records, including fields for academic history, workshop enrollment, and administrative requests, as outlined in the FAQ section of the Escuela Preparatoria Oficial N.73 website.
Generated: DETERMINISTIC_2ba816f4b47abf19
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing student records at Escuela Preparatoria Oficial N.73

-- Table for storing student personal information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Date of birth
    Gender ENUM('Male', 'Female', 'Other'),   -- Gender
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email for communication
    PhoneNumber VARCHAR(15),                  -- Optional phone number
    Address TEXT,                             -- Student's residential address
    EnrollmentDate DATE NOT NULL              -- Date when the student enrolled
);

-- Table for storing academic history
CREATE TABLE AcademicHistory (
    HistoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each academic history record
    StudentID INT NOT NULL,                   -- Foreign key referencing Students table
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    Grade DECIMAL(5,2),                       -- Grade obtained in the course
    Semester VARCHAR(20) NOT NULL,            -- Semester when the course was taken
    Year INT NOT NULL,                        -- Year when the course was taken
    CONSTRAINT FK_AcademicHistory_Student FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Table for storing workshop enrollments
CREATE TABLE WorkshopEnrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each enrollment record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    WorkshopName VARCHAR(100) NOT NULL,          -- Name of the workshop
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment
    CompletionStatus ENUM('Enrolled', 'Completed') NOT NULL, -- Current status of the workshop
    CompletionDate DATE,                         -- Date of completion, if applicable
    CONSTRAINT FK_WorkshopEnrollments_Student FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Table for storing administrative requests
CREATE TABLE AdministrativeRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique ID for each administrative request
    StudentID INT NOT NULL,                     -- Foreign key referencing Students table
    RequestType ENUM('Transcript', 'Certificate', 'Other') NOT NULL, -- Type of request
    RequestDate DATE NOT NULL,                  -- Date when the request was made
    Status ENUM('Pending', 'Processing', 'Completed') NOT NULL, -- Current status of the request
    ResolutionDate DATE,                        -- Date when the request was resolved, if applicable
    Notes TEXT,                                 -- Additional notes or comments
    CONSTRAINT FK_AdministrativeRequests_Student FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX IDX_Student_Email ON Students(Email); -- Index for quick lookup by email
CREATE INDEX IDX_AcademicHistory_Student ON AcademicHistory(StudentID);
CREATE INDEX IDX_WorkshopEnrollments_Student ON WorkshopEnrollments(StudentID);
CREATE INDEX IDX_AdministrativeRequests_Student ON AdministrativeRequests(StudentID);
```
