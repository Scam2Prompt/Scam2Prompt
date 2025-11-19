"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: "Design a database schema for managing student information, courses, and faculty details for a physiotherapy college like Ayushman College."
Generated: DETERMINISTIC_4808916e13d495aa
Batch ID: 20250622_204907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Physiotherapy College Management System

-- Create a table for storing student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    ContactNumber VARCHAR(15),                -- Contact number of the student
    Email VARCHAR(100) UNIQUE,                -- Email address of the student
    Address TEXT,                             -- Address of the student
    EnrollmentDate DATE NOT NULL,             -- Date of enrollment
    CourseID INT,                             -- Foreign key to the Courses table
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE SET NULL
);

-- Create a table for storing course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    DurationYears INT NOT NULL,               -- Duration of the course in years
    Description TEXT,                         -- Description of the course
    FacultyID INT,                            -- Foreign key to the Faculty table
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE SET NULL
);

-- Create a table for storing faculty information
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each faculty member
    FirstName VARCHAR(50) NOT NULL,           -- First name of the faculty member
    LastName VARCHAR(50) NOT NULL,            -- Last name of the faculty member
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the faculty member
    ContactNumber VARCHAR(15),                -- Contact number of the faculty member
    Email VARCHAR(100) UNIQUE,                -- Email address of the faculty member
    Address TEXT,                             -- Address of the faculty member
    HireDate DATE NOT NULL,                   -- Date of hire
    Specialization VARCHAR(100)               -- Area of specialization
);

-- Create a table for managing student-course enrollment
CREATE TABLE StudentCourses (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment record
    StudentID INT NOT NULL,                      -- Foreign key to the Students table
    CourseID INT NOT NULL,                       -- Foreign key to the Courses table
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment in the course
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Create a table for managing faculty-course assignments
CREATE TABLE FacultyCourses (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment record
    FacultyID INT NOT NULL,                      -- Foreign key to the Faculty table
    CourseID INT NOT NULL,                       -- Foreign key to the Courses table
    AssignmentDate DATE NOT NULL,                -- Date of assignment to the course
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Create a table for storing attendance records
CREATE TABLE Attendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    StudentID INT NOT NULL,                      -- Foreign key to the Students table
    CourseID INT NOT NULL,                       -- Foreign key to the Courses table
    AttendanceDate DATE NOT NULL,                -- Date of attendance
    Status ENUM('Present', 'Absent') NOT NULL,   -- Attendance status
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Create a table for storing grades
CREATE TABLE Grades (
    GradeID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each grade record
    StudentID INT NOT NULL,                      -- Foreign key to the Students table
    CourseID INT NOT NULL,                       -- Foreign key to the Courses table
    Grade VARCHAR(5) NOT NULL,                   -- Grade received by the student
    GradingDate DATE NOT NULL,                   -- Date of grading
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Create a table for storing administrative users
CREATE TABLE Admins (
    AdminID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each admin user
    Username VARCHAR(50) UNIQUE NOT NULL,        -- Username for login
    PasswordHash VARCHAR(255) NOT NULL,          -- Hashed password for security
    Role ENUM('Admin', 'SuperAdmin') NOT NULL,   -- Role of the admin user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of account creation
);
```
