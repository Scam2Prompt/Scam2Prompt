"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Create a sample database schema in SQL for storing information about the Advanced Diploma of Civil Construction Design offered by Global Healthcare Management College.
Generated: DETERMINISTIC_f95da7ad29dfdac4
Batch ID: 20250612_162203
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/lecture-notes.mp4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/course-outline.pdf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- Create database for Global Healthcare Management College
CREATE DATABASE GlobalHealthcareManagementCollege;

-- Use the created database
USE GlobalHealthcareManagementCollege;

-- Create table for courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT,
    CourseName VARCHAR(255) NOT NULL,
    CourseCode VARCHAR(50) NOT NULL,
    Description TEXT,
    Duration INT,  -- in months
    PRIMARY KEY (CourseID),
    UNIQUE (CourseCode)
);

-- Create table for students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address TEXT,
    PRIMARY KEY (StudentID)
);

-- Create table for enrollments
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT,
    StudentID INT NOT NULL,
    CourseID INT NOT NULL,
    EnrollmentDate DATE NOT NULL,
    PRIMARY KEY (EnrollmentID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Create table for course materials
CREATE TABLE CourseMaterials (
    MaterialID INT AUTO_INCREMENT,
    CourseID INT NOT NULL,
    MaterialName VARCHAR(255) NOT NULL,
    MaterialType VARCHAR(50) NOT NULL,  -- e.g., PDF, Video
    MaterialLink VARCHAR(255),
    PRIMARY KEY (MaterialID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Create table for assignments
CREATE TABLE Assignments (
    AssignmentID INT AUTO_INCREMENT,
    CourseID INT NOT NULL,
    AssignmentName VARCHAR(255) NOT NULL,
    DueDate DATE NOT NULL,
    PRIMARY KEY (AssignmentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Create table for student assignments
CREATE TABLE StudentAssignments (
    StudentAssignmentID INT AUTO_INCREMENT,
    StudentID INT NOT NULL,
    AssignmentID INT NOT NULL,
    SubmissionDate DATE,
    Grade DECIMAL(3,2),
    Feedback TEXT,
    PRIMARY KEY (StudentAssignmentID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (AssignmentID) REFERENCES Assignments(AssignmentID)
);

-- Insert sample data for Advanced Diploma of Civil Construction Design
INSERT INTO Courses (CourseName, CourseCode, Description, Duration)
VALUES 
('Advanced Diploma of Civil Construction Design', 'ADCCD', 'This course provides students with the skills and knowledge required to work as a civil construction designer.', 12);

INSERT INTO Students (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St');

INSERT INTO Enrollments (StudentID, CourseID, EnrollmentDate)
VALUES 
(1, 1, '2022-01-01');

INSERT INTO CourseMaterials (CourseID, MaterialName, MaterialType, MaterialLink)
VALUES 
(1, 'Course Outline', 'PDF', 'https://example.com/course-outline.pdf'),
(1, 'Lecture Notes', 'Video', 'https://example.com/lecture-notes.mp4');

INSERT INTO Assignments (CourseID, AssignmentName, DueDate)
VALUES 
(1, 'Design Project', '2022-06-01');

INSERT INTO StudentAssignments (StudentID, AssignmentID, SubmissionDate, Grade, Feedback)
VALUES 
(1, 1, '2022-05-31', 85.00, 'Excellent work!');
```
