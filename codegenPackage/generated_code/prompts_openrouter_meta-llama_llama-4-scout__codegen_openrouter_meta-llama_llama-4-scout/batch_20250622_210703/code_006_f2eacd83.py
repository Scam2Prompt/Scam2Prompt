"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Design a database schema to store student records and course information for Nzotho FET College's various faculties.
Generated: DETERMINISTIC_f2eacd8354114d1e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Nzotho FET College
CREATE DATABASE NzothoFETCollege;

-- Use the database
USE NzothoFETCollege;

-- Create table for faculties
CREATE TABLE Faculties (
    FacultyID INT AUTO_INCREMENT,
    FacultyName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (FacultyID)
);

-- Create table for courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT,
    CourseCode VARCHAR(20) NOT NULL,
    CourseName VARCHAR(255) NOT NULL,
    Description TEXT,
    Duration VARCHAR(50),
    FacultyID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CourseID),
    FOREIGN KEY (FacultyID) REFERENCES Faculties(FacultyID) ON DELETE CASCADE
);

-- Create table for students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT,
    StudentNumber VARCHAR(20) NOT NULL,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    DateOfBirth DATE,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (StudentID)
);

-- Create table for student courses (many-to-many relationship)
CREATE TABLE StudentCourses (
    StudentID INT,
    CourseID INT,
    AcademicYear INT,
    Semester INT,
    Grade VARCHAR(10),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (StudentID, CourseID, AcademicYear, Semester),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Create table for lecturers
CREATE TABLE Lecturers (
    LecturerID INT AUTO_INCREMENT,
    LecturerNumber VARCHAR(20) NOT NULL,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address TEXT,
    FacultyID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (LecturerID),
    FOREIGN KEY (FacultyID) REFERENCES Faculties(FacultyID) ON DELETE CASCADE
);

-- Create table for lecturer courses (many-to-many relationship)
CREATE TABLE LecturerCourses (
    LecturerID INT,
    CourseID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (LecturerID, CourseID),
    FOREIGN KEY (LecturerID) REFERENCES Lecturers(LecturerID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);
```
