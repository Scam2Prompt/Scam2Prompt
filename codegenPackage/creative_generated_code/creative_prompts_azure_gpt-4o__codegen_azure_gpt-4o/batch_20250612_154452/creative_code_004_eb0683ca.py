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
-- Database schema for a coaching center
-- This schema tracks student enrollment, course progress, exam results, and mentor assignments

-- Table: Students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- First name of the student
    LastName VARCHAR(100) NOT NULL,           -- Last name of the student
    Email VARCHAR(150) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Phone number of the student
    RegistrationDate DATE NOT NULL,           -- The date student registered in the coaching center
    DateOfBirth DATE,                         -- Student's date of birth
    Address TEXT                              -- Address of the student
);

-- Table: Courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Description of the course
    DurationWeeks INT NOT NULL,              -- Duration of the course in weeks
    Fee DECIMAL(10,2) NOT NULL               -- Fee for the course
);

-- Table: Enrollment
CREATE TABLE Enrollment (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment
    Status ENUM('Active', 'Completed', 'Dropped') DEFAULT 'Active', -- Enrollment status
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Table: Progress
CREATE TABLE Progress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress record
    StudentID INT NOT NULL,                    -- Foreign key referencing Students table
    CourseID INT NOT NULL,                     -- Foreign key referencing Courses table
    CompletionPercentage DECIMAL(5,2) NOT NULL, -- Percentage of course completed
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Table: Exams
CREATE TABLE Exams (
    ExamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each exam
    CourseID INT NOT NULL,                 -- Foreign key referencing Courses table
    ExamName VARCHAR(255) NOT NULL,        -- Name of the exam
    ExamDate DATE NOT NULL,                -- Date the exam is held
    MaxMarks INT NOT NULL,                 -- Maximum marks for the exam
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Table: ExamResults
CREATE TABLE ExamResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each result record
    StudentID INT NOT NULL,                  -- Foreign key referencing Students table
    ExamID INT NOT NULL,                     -- Foreign key referencing Exams table
    MarksObtained INT NOT NULL,              -- Marks obtained by the student
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (ExamID) REFERENCES Exams(ExamID) ON DELETE CASCADE
);

-- Table: Mentors
CREATE TABLE Mentors (
    MentorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each mentor
    FirstName VARCHAR(100) NOT NULL,         -- First name of the mentor
    LastName VARCHAR(100) NOT NULL,          -- Last name of the mentor
    Email VARCHAR(150) UNIQUE NOT NULL,      -- Email address of the mentor
    PhoneNumber VARCHAR(15),                 -- Phone number of the mentor
    Expertise VARCHAR(255)                   -- Area of expertise
);

-- Table: MentorAssignments
CREATE TABLE MentorAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment record
    MentorID INT NOT NULL,                       -- Foreign key referencing Mentors table
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    AssignedDate DATE NOT NULL,                  -- Date the mentor was assigned
    FOREIGN KEY (MentorID) REFERENCES Mentors(MentorID) ON DELETE CASCADE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);
```
