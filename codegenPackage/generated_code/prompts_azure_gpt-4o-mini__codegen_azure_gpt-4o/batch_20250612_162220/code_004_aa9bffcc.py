"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Design a database schema for storing information about students enrolled in the Escuela de Suboficiales de la Fuerza Aérea del Perú, including their grades and titles.
Generated: DETERMINISTIC_aa9bffcc76790a93
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about students, their grades, and titles
-- Escuela de Suboficiales de la Fuerza Aérea del Perú

-- Create table for storing student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Gender ENUM('Male', 'Female') NOT NULL,   -- Student's gender
    EnrollmentDate DATE NOT NULL,             -- Date the student enrolled
    Email VARCHAR(100) UNIQUE,                -- Student's email address
    PhoneNumber VARCHAR(15),                  -- Student's phone number
    Address TEXT                              -- Student's address
);

-- Create table for storing titles (e.g., ranks, certifications, etc.)
CREATE TABLE Titles (
    TitleID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each title
    TitleName VARCHAR(100) NOT NULL,          -- Name of the title
    Description TEXT,                         -- Description of the title
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the title was created
);

-- Create table for storing grades
CREATE TABLE Grades (
    GradeID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each grade record
    StudentID INT NOT NULL,                   -- Foreign key referencing Students table
    Subject VARCHAR(100) NOT NULL,            -- Name of the subject
    Grade DECIMAL(5, 2) NOT NULL,             -- Grade received (e.g., 95.50)
    ExamDate DATE NOT NULL,                   -- Date of the exam
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Create table for associating students with titles
CREATE TABLE StudentTitles (
    StudentTitleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    StudentID INT NOT NULL,                        -- Foreign key referencing Students table
    TitleID INT NOT NULL,                          -- Foreign key referencing Titles table
    AwardedDate DATE NOT NULL,                     -- Date the title was awarded
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (TitleID) REFERENCES Titles(TitleID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_student_name ON Students (FirstName, LastName);
CREATE INDEX idx_title_name ON Titles (TitleName);
CREATE INDEX idx_subject ON Grades (Subject);

-- Error handling and constraints
-- Ensure grades are between 0 and 100
ALTER TABLE Grades
ADD CONSTRAINT chk_grade_range CHECK (Grade >= 0 AND Grade <= 100);

-- Ensure gender is valid
ALTER TABLE Students
ADD CONSTRAINT chk_gender_valid CHECK (Gender IN ('Male', 'Female'));
```
