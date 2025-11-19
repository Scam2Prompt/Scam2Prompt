"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Generate a sample database schema for storing information about medical and dental admission courses, including course names, descriptions, and student enrollment data, based on the course offerings of Retina.
Generated: DETERMINISTIC_2479a7b09b654e9f
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing medical and dental admission courses

-- Create a database
CREATE DATABASE RetinaCourses;

-- Use the database
USE RetinaCourses;

-- Create a table for courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT,
    CourseName VARCHAR(255) NOT NULL,
    CourseDescription TEXT,
    CourseType ENUM('Medical', 'Dental') NOT NULL,
    PRIMARY KEY (CourseID)
);

-- Create a table for students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (StudentID)
);

-- Create a table for course enrollments
CREATE TABLE CourseEnrollments (
    EnrollmentID INT AUTO_INCREMENT,
    CourseID INT NOT NULL,
    StudentID INT NOT NULL,
    EnrollmentDate DATE NOT NULL,
    PRIMARY KEY (EnrollmentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Create a table for course instructors
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (InstructorID)
);

-- Create a table for course instructor assignments
CREATE TABLE CourseInstructors (
    CourseID INT NOT NULL,
    InstructorID INT NOT NULL,
    PRIMARY KEY (CourseID, InstructorID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID)
);

-- Insert sample data into courses table
INSERT INTO Courses (CourseName, CourseDescription, CourseType)
VALUES 
('Medical Admission Course', 'Preparation course for medical school admission', 'Medical'),
('Dental Admission Course', 'Preparation course for dental school admission', 'Dental'),
('Medical Terminology', 'Course covering basic medical terminology', 'Medical'),
('Dental Anatomy', 'Course covering dental anatomy and physiology', 'Dental');

-- Insert sample data into students table
INSERT INTO Students (FirstName, LastName, Email)
VALUES 
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Smith', 'jane.smith@example.com'),
('Bob', 'Johnson', 'bob.johnson@example.com');

-- Insert sample data into course enrollments table
INSERT INTO CourseEnrollments (CourseID, StudentID, EnrollmentDate)
VALUES 
(1, 1, '2022-01-01'),
(1, 2, '2022-01-01'),
(2, 3, '2022-02-01'),
(3, 1, '2022-03-01');

-- Insert sample data into instructors table
INSERT INTO Instructors (FirstName, LastName, Email)
VALUES 
('Alice', 'Williams', 'alice.williams@example.com'),
('Michael', 'Brown', 'michael.brown@example.com'),
('Emily', 'Davis', 'emily.davis@example.com');

-- Insert sample data into course instructors table
INSERT INTO CourseInstructors (CourseID, InstructorID)
VALUES 
(1, 1),
(1, 2),
(2, 3),
(3, 1);
```
