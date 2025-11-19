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
-- Create database for Ayushman College
CREATE DATABASE AyushmanCollege;

-- Use the database
USE AyushmanCollege;

-- Create table for faculty
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Department VARCHAR(255) NOT NULL,
    Designation VARCHAR(255) NOT NULL,
    PRIMARY KEY (FacultyID)
);

-- Create table for courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT,
    CourseName VARCHAR(255) NOT NULL,
    CourseCode VARCHAR(255) UNIQUE NOT NULL,
    Credits INT NOT NULL,
    Description TEXT,
    PRIMARY KEY (CourseID)
);

-- Create table for students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    AdmissionDate DATE NOT NULL,
    Batch VARCHAR(255) NOT NULL,
    PRIMARY KEY (StudentID)
);

-- Create table for student enrollment
CREATE TABLE StudentEnrollment (
    EnrollmentID INT AUTO_INCREMENT,
    StudentID INT NOT NULL,
    CourseID INT NOT NULL,
    Semester INT NOT NULL,
    AcademicYear INT NOT NULL,
    PRIMARY KEY (EnrollmentID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Create table for faculty teaching assignments
CREATE TABLE FacultyTeachingAssignments (
    AssignmentID INT AUTO_INCREMENT,
    FacultyID INT NOT NULL,
    CourseID INT NOT NULL,
    Semester INT NOT NULL,
    AcademicYear INT NOT NULL,
    PRIMARY KEY (AssignmentID),
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Create table for student results
CREATE TABLE StudentResults (
    ResultID INT AUTO_INCREMENT,
    EnrollmentID INT NOT NULL,
    Marks DECIMAL(5,2) NOT NULL,
    Grade VARCHAR(2) NOT NULL,
    PRIMARY KEY (ResultID),
    FOREIGN KEY (EnrollmentID) REFERENCES StudentEnrollment(EnrollmentID)
);

-- Create table for course prerequisites
CREATE TABLE CoursePrerequisites (
    PrerequisiteID INT AUTO_INCREMENT,
    CourseID INT NOT NULL,
    PrerequisiteCourseID INT NOT NULL,
    PRIMARY KEY (PrerequisiteID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (PrerequisiteCourseID) REFERENCES Courses(CourseID)
);

-- Insert sample data into faculty table
INSERT INTO Faculty (FirstName, LastName, Email, Phone, Department, Designation)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', 'Physiotherapy', 'Professor'),
('Jane', 'Smith', 'jane.smith@example.com', '9876543210', 'Physiotherapy', 'Assistant Professor');

-- Insert sample data into courses table
INSERT INTO Courses (CourseName, CourseCode, Credits, Description)
VALUES 
('Introduction to Physiotherapy', 'PT101', 3, 'Basic principles of physiotherapy'),
('Anatomy and Physiology', 'PT102', 4, 'Human body structure and functions');

-- Insert sample data into students table
INSERT INTO Students (FirstName, LastName, Email, Phone, AdmissionDate, Batch)
VALUES 
('Rahul', 'Kumar', 'rahul.kumar@example.com', '1234567890', '2022-01-01', '2022'),
('Priya', 'Sharma', 'priya.sharma@example.com', '9876543210', '2022-01-01', '2022');

-- Insert sample data into student enrollment table
INSERT INTO StudentEnrollment (StudentID, CourseID, Semester, AcademicYear)
VALUES 
(1, 1, 1, 2022),
(1, 2, 1, 2022),
(2, 1, 1, 2022);

-- Insert sample data into faculty teaching assignments table
INSERT INTO FacultyTeachingAssignments (FacultyID, CourseID, Semester, AcademicYear)
VALUES 
(1, 1, 1, 2022),
(2, 2, 1, 2022);

-- Insert sample data into student results table
INSERT INTO StudentResults (EnrollmentID, Marks, Grade)
VALUES 
(1, 85.00, 'A'),
(2, 90.00, 'A+'),
(3, 78.00, 'B+');

-- Insert sample data into course prerequisites table
INSERT INTO CoursePrerequisites (CourseID, PrerequisiteCourseID)
VALUES 
(2, 1);
```
