"""
Generated Code Metadata:
========================
Original URL: https://colatraining.com
Prompt: Design a database schema to store information about training courses, instructors, and students for a company like CoLa Training Services that offers classroom-based and online training programs.
Generated: DETERMINISTIC_0a7a86bde4b98bfc
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for CoLa Training Services

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Detailed description of the course
    Mode ENUM('Classroom', 'Online') NOT NULL, -- Mode of delivery: Classroom or Online
    DurationInHours INT NOT NULL,            -- Duration of the course in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about instructors
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instructor
    FirstName VARCHAR(100) NOT NULL,             -- First name of the instructor
    LastName VARCHAR(100) NOT NULL,              -- Last name of the instructor
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the instructor
    PhoneNumber VARCHAR(15),                     -- Contact number of the instructor
    Bio TEXT,                                    -- Short biography of the instructor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the instructor was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- First name of the student
    LastName VARCHAR(100) NOT NULL,           -- Last name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the student was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store course enrollments
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment
    CompletionStatus ENUM('Enrolled', 'Completed', 'Dropped') DEFAULT 'Enrolled', -- Status of the enrollment
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete if student is removed
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete if course is removed
);

-- Table to store course assignments for instructors
CREATE TABLE CourseAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    InstructorID INT NOT NULL,                   -- Foreign key referencing Instructors table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    AssignedDate DATE NOT NULL,                  -- Date when the instructor was assigned to the course
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE, -- Cascade delete if instructor is removed
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete if course is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_course_name ON Courses(CourseName);
CREATE INDEX idx_instructor_email ON Instructors(Email);
CREATE INDEX idx_student_email ON Students(Email);
CREATE INDEX idx_enrollment_status ON Enrollments(CompletionStatus);
```
