"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Create a database schema for a coaching center like Retina that tracks student enrollment, course progress, exam results, and mentor assignments.
Generated: DETERMINISTIC_eb0683cafdfa8295
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a coaching center "Retina"

-- Drop existing tables if they exist (useful for development)
DROP TABLE IF EXISTS Mentors CASCADE;
DROP TABLE IF EXISTS Students CASCADE;
DROP TABLE IF EXISTS Courses CASCADE;
DROP TABLE IF EXISTS Enrollments CASCADE;
DROP TABLE IF EXISTS ExamResults CASCADE;

-- Table to store information about mentors
CREATE TABLE Mentors (
    MentorID SERIAL PRIMARY KEY,            -- Unique identifier for each mentor
    Name VARCHAR(100) NOT NULL,            -- Mentor's name
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Mentor's email (unique)
    Phone VARCHAR(15),                      -- Mentor's phone number
    Specialty VARCHAR(100),                 -- Area of expertise
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table to store information about students
CREATE TABLE Students (
    StudentID SERIAL PRIMARY KEY,           -- Unique identifier for each student
    Name VARCHAR(100) NOT NULL,             -- Student's name
    Email VARCHAR(100) UNIQUE NOT NULL,     -- Student's email (unique)
    Phone VARCHAR(15),                      -- Student's phone number
    EnrolledAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of enrollment
);

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID SERIAL PRIMARY KEY,            -- Unique identifier for each course
    Title VARCHAR(100) NOT NULL,            -- Course title
    Description TEXT,                       -- Course description
    Duration INT NOT NULL,                  -- Duration in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of course creation
);

-- Table to track student enrollments in courses
CREATE TABLE Enrollments (
    EnrollmentID SERIAL PRIMARY KEY,        -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                 -- Foreign key to Students
    CourseID INT NOT NULL,                  -- Foreign key to Courses
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of enrollment
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE,
    UNIQUE(StudentID, CourseID)             -- Ensure a student can enroll in a course only once
);

-- Table to track exam results for students
CREATE TABLE ExamResults (
    ResultID SERIAL PRIMARY KEY,            -- Unique identifier for each result
    EnrollmentID INT NOT NULL,              -- Foreign key to Enrollments
    Score DECIMAL(5, 2) CHECK (Score >= 0 AND Score <= 100), -- Score out of 100
    ExamDate TIMESTAMP NOT NULL,            -- Date of the exam
    FOREIGN KEY (EnrollmentID) REFERENCES Enrollments(EnrollmentID) ON DELETE CASCADE
);

-- Table to assign mentors to students
CREATE TABLE MentorAssignments (
    AssignmentID SERIAL PRIMARY KEY,        -- Unique identifier for each assignment
    MentorID INT NOT NULL,                  -- Foreign key to Mentors
    StudentID INT NOT NULL,                 -- Foreign key to Students
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of assignment
    FOREIGN KEY (MentorID) REFERENCES Mentors(MentorID) ON DELETE CASCADE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    UNIQUE(MentorID, StudentID)             -- Ensure a mentor can be assigned to a student only once
);

-- Indexes for efficient querying
CREATE INDEX idx_student_email ON Students(Email);
CREATE INDEX idx_course_title ON Courses(Title);
CREATE INDEX idx_mentor_specialty ON Mentors(Specialty);
```
