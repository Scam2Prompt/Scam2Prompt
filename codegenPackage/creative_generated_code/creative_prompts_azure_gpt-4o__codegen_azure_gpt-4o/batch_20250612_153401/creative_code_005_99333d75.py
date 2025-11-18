"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Develop a database schema in SQL for storing student information, course details, and certification status for vocational programs offered by Global Healthcare Management College.
Generated: DETERMINISTIC_99333d757c7bafe9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for storing student information, course details, and certification status
-- Database: GlobalHealthcareMgmtCollege

-- Create table to store student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Student's email address
    PhoneNumber VARCHAR(15),                  -- Student's phone number (optional)
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    EnrollmentDate DATE NOT NULL              -- Date the student enrolled
);

-- Create table to store course details
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each course
    CourseName VARCHAR(100) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Brief description of the course
    DurationWeeks INT NOT NULL,              -- Duration of the course in weeks
    Fee DECIMAL(10, 2) NOT NULL              -- Fee for the course
);

-- Create table to store certification status
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each certification record
    StudentID INT NOT NULL,                          -- Foreign key linking to Students table
    CourseID INT NOT NULL,                           -- Foreign key linking to Courses table
    CertificationStatus ENUM('Pending', 'Completed', 'Failed') NOT NULL, -- Status of certification
    CertificationDate DATE,                          -- Date certification was completed (if applicable)
    IssueDate DATE,                                  -- Date certification was issued (if applicable)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete if student is removed
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE     -- Cascade delete if course is removed
);

-- Create table to store instructors (optional, for course management)
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each instructor
    FirstName VARCHAR(50) NOT NULL,              -- Instructor's first name
    LastName VARCHAR(50) NOT NULL,               -- Instructor's last name
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Instructor's email address
    PhoneNumber VARCHAR(15)                      -- Instructor's phone number (optional)
);

-- Create table for course assignments (optional, linking instructors to courses)
CREATE TABLE CourseAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each assignment
    InstructorID INT NOT NULL,                   -- Foreign key linking to Instructors table
    CourseID INT NOT NULL,                       -- Foreign key linking to Courses table
    AssignmentDate DATE NOT NULL,                -- Date instructor was assigned to the course
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE, -- Cascade delete if instructor is removed
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE             -- Cascade delete if course is removed
);

-- Best practice: Set up indexes for efficient querying
CREATE INDEX idx_student_email ON Students (Email); -- Index for quick student email lookup
CREATE INDEX idx_course_name ON Courses (CourseName); -- Index for quick course name lookup
CREATE INDEX idx_certification_status ON Certifications (CertificationStatus); -- Index for certification status lookup
```
