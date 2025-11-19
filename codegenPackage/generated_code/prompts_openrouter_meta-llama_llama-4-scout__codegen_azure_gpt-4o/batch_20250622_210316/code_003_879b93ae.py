"""
Generated Code Metadata:
========================
Original URL: https://araform.org
Prompt: "Design a database schema to store information about courses, instructors, and students for a vocational training agency like Araform, incorporating details from their course offerings."
Generated: DETERMINISTIC_879b93ae06e47721
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a vocational training agency

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Detailed description of the course
    DurationWeeks INT NOT NULL,              -- Duration of the course in weeks
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the course was created
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
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the instructor was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- First name of the student
    LastName VARCHAR(100) NOT NULL,           -- Last name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    DateOfBirth DATE,                         -- Date of birth of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the student was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store the relationship between courses and instructors
CREATE TABLE CourseInstructors (
    CourseInstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    CourseID INT NOT NULL,                             -- Foreign key referencing Courses table
    InstructorID INT NOT NULL,                         -- Foreign key referencing Instructors table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the instructor was assigned to the course
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE, -- Cascade delete if course is deleted
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE -- Cascade delete if instructor is deleted
);

-- Table to store the relationship between courses and students
CREATE TABLE CourseEnrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the enrollment
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the student enrolled
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE, -- Cascade delete if course is deleted
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE -- Cascade delete if student is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_course_name ON Courses(CourseName); -- Index for quick search by course name
CREATE INDEX idx_instructor_email ON Instructors(Email); -- Index for quick search by instructor email
CREATE INDEX idx_student_email ON Students(Email); -- Index for quick search by student email
```
