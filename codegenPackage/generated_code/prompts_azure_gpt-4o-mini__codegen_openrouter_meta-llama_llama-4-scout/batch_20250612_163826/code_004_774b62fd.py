"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Design a database schema in SQL for managing student records and course enrollments at a music school, including tables for instruments, faculty, and student information.
Generated: DETERMINISTIC_774b62fd0ba65a03
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the music school
CREATE DATABASE MusicSchool;

-- Use the MusicSchool database
USE MusicSchool;

-- Create a table for instruments
CREATE TABLE Instruments (
    InstrumentID INT AUTO_INCREMENT,
    InstrumentName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (InstrumentID)
);

-- Create a table for faculty members
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    InstrumentID INT,
    PRIMARY KEY (FacultyID),
    FOREIGN KEY (InstrumentID) REFERENCES Instruments(InstrumentID)
);

-- Create a table for students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    DateOfBirth DATE,
    PRIMARY KEY (StudentID)
);

-- Create a table for courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT,
    CourseName VARCHAR(255) NOT NULL,
    Description TEXT,
    FacultyID INT,
    PRIMARY KEY (CourseID),
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID)
);

-- Create a table for course enrollments
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE NOT NULL,
    PRIMARY KEY (EnrollmentID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    UNIQUE (StudentID, CourseID)
);

-- Create a table for student instruments
CREATE TABLE StudentInstruments (
    StudentID INT,
    InstrumentID INT,
    PRIMARY KEY (StudentID, InstrumentID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (InstrumentID) REFERENCES Instruments(InstrumentID)
);

-- Insert some sample data
INSERT INTO Instruments (InstrumentName, Description)
VALUES 
('Piano', 'A keyboard instrument'),
('Guitar', 'A stringed instrument'),
('Violin', 'A stringed instrument');

INSERT INTO Faculty (FirstName, LastName, Email, InstrumentID)
VALUES 
('John', 'Doe', 'john.doe@example.com', 1),
('Jane', 'Smith', 'jane.smith@example.com', 2);

INSERT INTO Students (FirstName, LastName, Email, DateOfBirth)
VALUES 
('Alice', 'Johnson', 'alice.johnson@example.com', '2000-01-01'),
('Bob', 'Williams', 'bob.williams@example.com', '2001-01-01');

INSERT INTO Courses (CourseName, Description, FacultyID)
VALUES 
('Piano Lessons', 'Learn to play the piano', 1),
('Guitar Class', 'Learn to play the guitar', 2);

INSERT INTO Enrollments (StudentID, CourseID, EnrollmentDate)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-01-15');

INSERT INTO StudentInstruments (StudentID, InstrumentID)
VALUES 
(1, 1),
(2, 2);
```
