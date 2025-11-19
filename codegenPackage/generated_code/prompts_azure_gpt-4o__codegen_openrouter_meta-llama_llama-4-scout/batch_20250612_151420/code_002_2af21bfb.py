"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: Generate code to create a database schema for managing physiotherapy student records, including fields for course enrollment (e.g., MPT, BPTh.), clinical training schedules, and academic achievements, as described by Ayushman College.
Generated: DETERMINISTIC_2af21bfb04036deb
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for physiotherapy student records
CREATE DATABASE PhysiotherapyStudentRecords;

-- Use the created database
USE PhysiotherapyStudentRecords;

-- Create table for students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    Course VARCHAR(50) NOT NULL CHECK (Course IN ('MPT', 'BPTh.')),
    EnrollmentDate DATE NOT NULL,
    PRIMARY KEY (StudentID)
);

-- Create table for clinical training schedules
CREATE TABLE ClinicalTrainingSchedules (
    ScheduleID INT AUTO_INCREMENT,
    StudentID INT NOT NULL,
    TrainingDate DATE NOT NULL,
    TrainingTime TIME NOT NULL,
    Location VARCHAR(255) NOT NULL,
    Supervisor VARCHAR(255) NOT NULL,
    PRIMARY KEY (ScheduleID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Create table for academic achievements
CREATE TABLE AcademicAchievements (
    AchievementID INT AUTO_INCREMENT,
    StudentID INT NOT NULL,
    AchievementType VARCHAR(100) NOT NULL CHECK (AchievementType IN ('Assignment', 'Exam', 'Project')),
    AchievementDate DATE NOT NULL,
    Score DECIMAL(3,2) NOT NULL,
    Grade VARCHAR(10),
    Description VARCHAR(255),
    PRIMARY KEY (AchievementID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Create table for course enrollment
CREATE TABLE CourseEnrollment (
    EnrollmentID INT AUTO_INCREMENT,
    StudentID INT NOT NULL,
    CourseName VARCHAR(100) NOT NULL,
    Semester INT NOT NULL,
    EnrollmentDate DATE NOT NULL,
    PRIMARY KEY (EnrollmentID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_StudentID ON ClinicalTrainingSchedules (StudentID);
CREATE INDEX idx_StudentID ON AcademicAchievements (StudentID);
CREATE INDEX idx_StudentID ON CourseEnrollment (StudentID);

-- Example data insertion
INSERT INTO Students (FirstName, LastName, DateOfBirth, Email, Phone, Address, Course, EnrollmentDate)
VALUES 
('John', 'Doe', '2000-01-01', 'john.doe@example.com', '1234567890', '123 Main St', 'MPT', '2020-01-01'),
('Jane', 'Doe', '2001-01-01', 'jane.doe@example.com', '9876543210', '456 Elm St', 'BPTh.', '2020-01-01');

INSERT INTO ClinicalTrainingSchedules (StudentID, TrainingDate, TrainingTime, Location, Supervisor)
VALUES 
(1, '2022-01-01', '09:00:00', 'Hospital A', 'Dr. Smith'),
(2, '2022-01-02', '10:00:00', 'Hospital B', 'Dr. Johnson');

INSERT INTO AcademicAchievements (StudentID, AchievementType, AchievementDate, Score, Grade, Description)
VALUES 
(1, 'Assignment', '2022-01-01', 85.00, 'B+', 'Completed assignment on time'),
(2, 'Exam', '2022-01-02', 90.00, 'A-', 'Scored high on exam');

INSERT INTO CourseEnrollment (StudentID, CourseName, Semester, EnrollmentDate)
VALUES 
(1, 'MPT - Semester 1', 1, '2020-01-01'),
(2, 'BPTh. - Semester 2', 2, '2020-01-01');
```
