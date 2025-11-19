"""
Generated Code Metadata:
========================
Original URL: https://ezway.com.br
Prompt: Design a database schema for storing information about English courses, instructors, and students for an institution like EZ Way.
Generated: DETERMINISTIC_2adcae5cdf0398b5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about English courses, instructors, and students

-- Table to store information about instructors
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instructor
    FirstName VARCHAR(50) NOT NULL,              -- First name of the instructor
    LastName VARCHAR(50) NOT NULL,               -- Last name of the instructor
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Email address of the instructor
    PhoneNumber VARCHAR(15),                     -- Contact number of the instructor
    HireDate DATE NOT NULL,                      -- Date the instructor was hired
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,            -- Name of the course
    Description TEXT,                            -- Description of the course
    StartDate DATE NOT NULL,                     -- Start date of the course
    EndDate DATE NOT NULL,                       -- End date of the course
    InstructorID INT NOT NULL,                   -- Foreign key referencing the instructor teaching the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,              -- First name of the student
    LastName VARCHAR(50) NOT NULL,               -- Last name of the student
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Email address of the student
    PhoneNumber VARCHAR(15),                     -- Contact number of the student
    EnrollmentDate DATE NOT NULL,                -- Date the student enrolled
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store the relationship between students and courses (many-to-many)
CREATE TABLE StudentCourses (
    StudentCourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    StudentID INT NOT NULL,                         -- Foreign key referencing the student
    CourseID INT NOT NULL,                          -- Foreign key referencing the course
    EnrollmentDate DATE NOT NULL,                   -- Date the student enrolled in the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE,    -- Ensures referential integrity
    UNIQUE(StudentID, CourseID)                     -- Ensures a student cannot enroll in the same course multiple times
);
```
