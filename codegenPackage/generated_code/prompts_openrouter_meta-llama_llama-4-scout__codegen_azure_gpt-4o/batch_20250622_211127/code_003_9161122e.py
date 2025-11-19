"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: "Design a database schema for storing student records, faculty information, and course details for an educational institution with multiple centers like Potencia Academy."
Generated: DETERMINISTIC_9161122e4ebcbb71
Batch ID: 20250622_211127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Potencia Academy

-- Table to store information about centers
CREATE TABLE Centers (
    CenterID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each center
    Name VARCHAR(100) NOT NULL,              -- Name of the center
    Address VARCHAR(255),                    -- Address of the center
    City VARCHAR(100),                       -- City where the center is located
    State VARCHAR(100),                      -- State where the center is located
    ZipCode VARCHAR(10),                     -- Zip code of the center
    PhoneNumber VARCHAR(15),                 -- Contact number of the center
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store student records
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- First name of the student
    LastName VARCHAR(100) NOT NULL,           -- Last name of the student
    Email VARCHAR(150) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    DateOfBirth DATE,                         -- Date of birth of the student
    CenterID INT,                             -- Foreign key to the Centers table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CenterID) REFERENCES Centers(CenterID) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Table to store faculty information
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each faculty member
    FirstName VARCHAR(100) NOT NULL,          -- First name of the faculty member
    LastName VARCHAR(100) NOT NULL,           -- Last name of the faculty member
    Email VARCHAR(150) UNIQUE NOT NULL,       -- Email address of the faculty member
    PhoneNumber VARCHAR(15),                  -- Contact number of the faculty member
    Department VARCHAR(100),                  -- Department of the faculty member
    CenterID INT,                             -- Foreign key to the Centers table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CenterID) REFERENCES Centers(CenterID) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Table to store course details
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    Name VARCHAR(100) NOT NULL,              -- Name of the course
    Description TEXT,                        -- Description of the course
    Credits INT NOT NULL,                    -- Number of credits for the course
    CenterID INT,                            -- Foreign key to the Centers table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CenterID) REFERENCES Centers(CenterID) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Table to store enrollment information
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key to the Students table
    CourseID INT NOT NULL,                       -- Foreign key to the Courses table
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment
    Grade VARCHAR(5),                            -- Grade received by the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table to store faculty assignments to courses
CREATE TABLE FacultyAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    FacultyID INT NOT NULL,                      -- Foreign key to the Faculty table
    CourseID INT NOT NULL,                       -- Foreign key to the Courses table
    AssignedDate DATE NOT NULL,                  -- Date of assignment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE ON UPDATE CASCADE
);
```
