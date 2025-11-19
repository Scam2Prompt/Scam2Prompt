"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Create a database schema for a coaching center like Retina that tracks student enrollment, course progress, exam results, and mentor assignments.
Generated: DETERMINISTIC_eb0683cafdfa8295
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a coaching center

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Mentors;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS ExamResults;

-- Table to store mentor information
CREATE TABLE Mentors (
    MentorID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each mentor
    Name VARCHAR(100) NOT NULL,               -- Mentor's name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Mentor's email (must be unique)
    Phone VARCHAR(15),                        -- Mentor's phone number
    Specialization VARCHAR(100),               -- Area of expertise
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store student information
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each student
    Name VARCHAR(100) NOT NULL,                -- Student's name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Student's email (must be unique)
    Phone VARCHAR(15),                         -- Student's phone number
    EnrollmentDate DATE NOT NULL,              -- Date of enrollment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store course information
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each course
    Title VARCHAR(100) NOT NULL,                -- Course title
    Description TEXT,                           -- Course description
    Duration INT NOT NULL,                      -- Duration of the course in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to track student enrollments in courses
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment in the course
    Status ENUM('Active', 'Completed', 'Dropped') DEFAULT 'Active', -- Enrollment status
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store exam results for students
CREATE TABLE ExamResults (
    ResultID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each exam result
    StudentID INT NOT NULL,                      -- Foreign key referencing Students
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses
    Score DECIMAL(5,2) NOT NULL,                -- Score obtained in the exam
    ExamDate DATE NOT NULL,                      -- Date of the exam
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to assign mentors to courses
CREATE TABLE CourseMentors (
    CourseMentorID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each course-mentor assignment
    CourseID INT NOT NULL,                          -- Foreign key referencing Courses
    MentorID INT NOT NULL,                          -- Foreign key referencing Mentors
    AssignedDate DATE NOT NULL,                     -- Date when the mentor was assigned
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (MentorID) REFERENCES Mentors(MentorID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_student_email ON Students(Email);
CREATE INDEX idx_course_title ON Courses(Title);
CREATE INDEX idx_enrollment_status ON Enrollments(Status);
CREATE INDEX idx_exam_date ON ExamResults(ExamDate);
```
