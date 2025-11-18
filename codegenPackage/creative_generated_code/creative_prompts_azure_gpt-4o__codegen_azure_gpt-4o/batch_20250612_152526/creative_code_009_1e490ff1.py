"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Create a database schema for tracking student progress in short-term brokerage courses, inspired by Kigali Institute's balance of theoretical and practical training.
Generated: DETERMINISTIC_1e490ff1da6a216d
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking student progress in brokerage courses

-- Create the schema
CREATE SCHEMA BrokerageCourses;

-- Create a table for storing information about students
CREATE TABLE BrokerageCourses.Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,             -- Student's first name
    LastName VARCHAR(50) NOT NULL,              -- Student's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Student's email (must be unique)
    PhoneNumber VARCHAR(15),                    -- Optional: Student's phone number
    EnrollmentDate DATE NOT NULL,               -- Date of student enrollment
    Status ENUM('Active', 'Inactive') DEFAULT 'Active' -- Current status of the student
);

-- Create a table for storing information about courses
CREATE TABLE BrokerageCourses.Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,           -- Name of the course
    Description TEXT,                           -- Optional: Description of the course
    DurationWeeks INT NOT NULL,                 -- Duration of the course in weeks
    PracticalTraining BOOL DEFAULT TRUE,        -- Whether the course includes practical training
    TheoreticalTraining BOOL DEFAULT TRUE,      -- Whether the course includes theoretical training
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Creation timestamp for the course record
);

-- Create a table for storing student enrollments in courses
CREATE TABLE BrokerageCourses.Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the enrollment record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollDate DATE NOT NULL,                    -- Date of enrollment
    ProgressPercent INT DEFAULT 0 CHECK (ProgressPercent BETWEEN 0 AND 100), -- Percentage of course progress
    CompletionStatus ENUM('Incomplete', 'Completed') DEFAULT 'Incomplete', -- Course completion status
    FOREIGN KEY (StudentID) REFERENCES BrokerageCourses.Students(StudentID) 
        ON DELETE CASCADE ON UPDATE CASCADE,     -- Cascade on delete and update
    FOREIGN KEY (CourseID) REFERENCES BrokerageCourses.Courses(CourseID) 
        ON DELETE CASCADE ON UPDATE CASCADE      -- Cascade on delete and update
);

-- Create a table for storing assessments for course progress
CREATE TABLE BrokerageCourses.Assessments (
    AssessmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assessment
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    AssessmentType ENUM('Quiz', 'Assignment', 'Exam') NOT NULL, -- Type of assessment
    MaxScore INT NOT NULL,                       -- Maximum possible score for the assessment
    FOREIGN KEY (CourseID) REFERENCES BrokerageCourses.Courses(CourseID) 
        ON DELETE CASCADE ON UPDATE CASCADE      -- Cascade on delete and update
);

-- Create a table for storing student assessment scores
CREATE TABLE BrokerageCourses.AssessmentScores (
    ScoreID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the score record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    AssessmentID INT NOT NULL,                   -- Foreign key referencing Assessments table
    Score INT NOT NULL CHECK (Score >= 0),       -- Score obtained by the student
    FOREIGN KEY (StudentID) REFERENCES BrokerageCourses.Students(StudentID) 
        ON DELETE CASCADE ON UPDATE CASCADE,     -- Cascade on delete and update
    FOREIGN KEY (AssessmentID) REFERENCES BrokerageCourses.Assessments(AssessmentID) 
        ON DELETE CASCADE ON UPDATE CASCADE      -- Cascade on delete and update
);

-- Create indexes for performance optimization
CREATE INDEX idx_student_email ON BrokerageCourses.Students(Email);
CREATE INDEX idx_course_name ON BrokerageCourses.Courses(CourseName);
CREATE INDEX idx_enrollment_student_course ON BrokerageCourses.Enrollments(StudentID, CourseID);
CREATE INDEX idx_assessment_course ON BrokerageCourses.Assessments(CourseID);
CREATE INDEX idx_score_student_assessment ON BrokerageCourses.AssessmentScores(StudentID, AssessmentID);
```
