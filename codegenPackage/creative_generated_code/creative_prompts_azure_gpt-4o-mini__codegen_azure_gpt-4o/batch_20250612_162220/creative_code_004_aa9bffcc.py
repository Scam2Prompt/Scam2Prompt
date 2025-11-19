"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esofa.edu.pe
Prompt: Design a database schema for storing information about students enrolled in the Escuela de Suboficiales de la Fuerza Aérea del Perú, including their grades and titles.
Generated: DETERMINISTIC_aa9bffcc76790a93
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about students, grades, and titles
-- Escuela de Suboficiales de la Fuerza Aérea del Perú

-- Table for storing student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    EnrollmentDate DATE NOT NULL,             -- Date when the student enrolled
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Phone number of the student
    Address VARCHAR(255)                      -- Address of the student
);

-- Table for storing titles associated with students
CREATE TABLE Titles (
    TitleID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each title
    TitleName VARCHAR(100) NOT NULL,          -- Name of the title
    Description TEXT                          -- Description of the title
);

-- Associative table for linking students to their titles
CREATE TABLE StudentTitles (
    StudentID INT NOT NULL,                   -- FK referencing Students table
    TitleID INT NOT NULL,                     -- FK referencing Titles table
    DateAwarded DATE NOT NULL,                -- Date when the title was awarded
    PRIMARY KEY (StudentID, TitleID),         -- Composite key ensures uniqueness per student-title pair
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (TitleID) REFERENCES Titles(TitleID) ON DELETE CASCADE
);

-- Table for storing grades achieved by students
CREATE TABLE Grades (
    GradeID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each grade record
    StudentID INT NOT NULL,                   -- FK referencing Students table
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    Grade DECIMAL(5, 2) NOT NULL,             -- Numeric grade (e.g., 95.50)
    GradingDate DATE NOT NULL,                -- Date when the grade was assigned
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Indexes for improved search performance
CREATE INDEX idx_student_name ON Students (FirstName, LastName);
CREATE INDEX idx_course_name ON Grades (CourseName);

-- Ensure transactional integrity
-- Example: BEGIN TRANSACTION / COMMIT / ROLLBACK patterns can be used for inserts/updates/deletes

-- Constraints and validations
-- Email uniqueness is enforced via UNIQUE constraint
-- Gender is validated via ENUM type
```
