"""
Generated Code Metadata:
========================
Original URL: https://anko-kurzy.sk
Prompt: "Generate a sample database schema for storing information about children's courses, instructors, and attendance records for a platform like AnKo kurzy."
Generated: DETERMINISTIC_2c448157c291d0df
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a children's courses platform

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Detailed description of the course
    AgeGroup VARCHAR(50),                    -- Target age group for the course (e.g., "6-8 years")
    StartDate DATE NOT NULL,                 -- Start date of the course
    EndDate DATE NOT NULL,                   -- End date of the course
    MaxCapacity INT NOT NULL,                -- Maximum number of children allowed in the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about instructors
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instructor
    FirstName VARCHAR(100) NOT NULL,             -- First name of the instructor
    LastName VARCHAR(100) NOT NULL,              -- Last name of the instructor
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the instructor
    PhoneNumber VARCHAR(20),                     -- Contact phone number
    Bio TEXT,                                    -- Short biography of the instructor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the instructor was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about course-instructor relationships
CREATE TABLE CourseInstructors (
    CourseInstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    CourseID INT NOT NULL,                             -- Foreign key referencing Courses table
    InstructorID INT NOT NULL,                         -- Foreign key referencing Instructors table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the instructor was assigned to the course
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE, -- Cascade delete if course is deleted
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE -- Cascade delete if instructor is deleted
);

-- Table to store information about children attending courses
CREATE TABLE Children (
    ChildID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each child
    FirstName VARCHAR(100) NOT NULL,        -- First name of the child
    LastName VARCHAR(100) NOT NULL,         -- Last name of the child
    DateOfBirth DATE NOT NULL,              -- Date of birth of the child
    ParentContact VARCHAR(255),             -- Contact information for the parent/guardian
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the child was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store attendance records
CREATE TABLE AttendanceRecords (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    ChildID INT NOT NULL,                        -- Foreign key referencing Children table
    AttendanceDate DATE NOT NULL,                -- Date of attendance
    Status ENUM('Present', 'Absent') NOT NULL,   -- Attendance status
    Notes TEXT,                                  -- Additional notes about the attendance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE, -- Cascade delete if course is deleted
    FOREIGN KEY (ChildID) REFERENCES Children(ChildID) ON DELETE CASCADE -- Cascade delete if child is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_course_start_end ON Courses (StartDate, EndDate); -- Index for querying courses by date range
CREATE INDEX idx_attendance_date ON AttendanceRecords (AttendanceDate); -- Index for querying attendance by date
```
