"""
Generated Code Metadata:
========================
Original URL: https://jualessandraensina.com
Prompt: Design a database schema for managing student profiles and course enrollments in a makeup education platform similar to Ju Ensina, including fields for techniques learned and progress tracking.
Generated: DETERMINISTIC_5136e7179c738394
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing student profiles and course enrollments
-- in a makeup education platform.

-- Table to store student profiles
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Student's email address (must be unique)
    PhoneNumber VARCHAR(15),                  -- Student's phone number
    DateOfBirth DATE,                         -- Student's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the profile was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store courses offered by the platform
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    Description TEXT,                         -- Detailed description of the course
    DurationInHours INT NOT NULL,             -- Duration of the course in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store techniques taught in each course
CREATE TABLE Techniques (
    TechniqueID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each technique
    CourseID INT NOT NULL,                      -- Foreign key referencing Courses table
    TechniqueName VARCHAR(100) NOT NULL,        -- Name of the technique
    Description TEXT,                           -- Detailed description of the technique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the technique was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete if course is removed
);

-- Table to store student enrollments in courses
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate DATE NOT NULL,                -- Date when the student enrolled in the course
    ProgressPercentage DECIMAL(5, 2) DEFAULT 0,  -- Progress tracking (percentage completed)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete if student is removed
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete if course is removed
);

-- Table to track techniques learned by students
CREATE TABLE TechniquesLearned (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each record
    StudentID INT NOT NULL,                     -- Foreign key referencing Students table
    TechniqueID INT NOT NULL,                   -- Foreign key referencing Techniques table
    LearnedDate DATE NOT NULL,                  -- Date when the technique was learned
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete if student is removed
    FOREIGN KEY (TechniqueID) REFERENCES Techniques(TechniqueID) ON DELETE CASCADE -- Cascade delete if technique is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_student_email ON Students(Email); -- Index for quick lookup by email
CREATE INDEX idx_course_name ON Courses(CourseName); -- Index for quick lookup by course name
CREATE INDEX idx_technique_name ON Techniques(TechniqueName); -- Index for quick lookup by technique name
CREATE INDEX idx_enrollment_student_course ON Enrollments(StudentID, CourseID); -- Composite index for enrollment lookups
CREATE INDEX idx_techniques_learned_student ON TechniquesLearned(StudentID); -- Index for tracking techniques learned by students
```
