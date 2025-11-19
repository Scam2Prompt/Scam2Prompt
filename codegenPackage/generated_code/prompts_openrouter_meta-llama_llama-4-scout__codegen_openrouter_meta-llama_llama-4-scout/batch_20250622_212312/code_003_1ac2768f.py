"""
Generated Code Metadata:
========================
Original URL: https://jhpsgaya.com
Prompt: Design a database schema for storing student information, academic subjects, and co-curricular activities for a school like JHPS Gaya.
Generated: DETERMINISTIC_1ac2768f9ca51940
Batch ID: 20250622_212312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the school
CREATE DATABASE JHPS_Gaya;

-- Use the database
USE JHPS_Gaya;

-- Create a table for students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (StudentID)
);

-- Create a table for academic subjects
CREATE TABLE Subjects (
    SubjectID INT AUTO_INCREMENT,
    SubjectName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SubjectID)
);

-- Create a table for co-curricular activities
CREATE TABLE CoCurricularActivities (
    ActivityID INT AUTO_INCREMENT,
    ActivityName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ActivityID)
);

-- Create a table for student subjects (many-to-many relationship)
CREATE TABLE StudentSubjects (
    StudentID INT NOT NULL,
    SubjectID INT NOT NULL,
    Grade DECIMAL(3,2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (StudentID, SubjectID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID) ON DELETE CASCADE
);

-- Create a table for student co-curricular activities (many-to-many relationship)
CREATE TABLE StudentActivities (
    StudentID INT NOT NULL,
    ActivityID INT NOT NULL,
    ParticipationStatus VARCHAR(50),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (StudentID, ActivityID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (ActivityID) REFERENCES CoCurricularActivities(ActivityID) ON DELETE CASCADE
);

-- Create a table for teachers (optional, but could be useful for future expansion)
CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    SubjectID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TeacherID),
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID)
);

-- Create a table for classes (optional, but could be useful for future expansion)
CREATE TABLE Classes (
    ClassID INT AUTO_INCREMENT,
    ClassName VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClassID)
);

-- Create a table for student classes (many-to-many relationship, optional)
CREATE TABLE StudentClasses (
    StudentID INT NOT NULL,
    ClassID INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (StudentID, ClassID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID) ON DELETE CASCADE
);
```
