"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Design a database schema to store information about students, teachers, and parents for a school like MercedariasGye, including relationships between entities.
Generated: DETERMINISTIC_f3b295b1b28cf89d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the school management system
CREATE DATABASE MercedariasGye;

-- Use the database
USE MercedariasGye;

-- Create a table for roles
CREATE TABLE Roles (
  RoleID INT AUTO_INCREMENT,
  RoleName VARCHAR(255) NOT NULL,
  Description TEXT,
  PRIMARY KEY (RoleID),
  UNIQUE (RoleName)
);

-- Insert roles
INSERT INTO Roles (RoleName, Description)
VALUES 
('Student', 'A student enrolled in the school'),
('Teacher', 'A teacher working at the school'),
('Parent', 'A parent of a student');

-- Create a table for users
CREATE TABLE Users (
  UserID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  PasswordHash VARCHAR(255) NOT NULL,
  RoleID INT,
  PRIMARY KEY (UserID),
  FOREIGN KEY (RoleID) REFERENCES Roles(RoleID)
);

-- Create a table for students
CREATE TABLE Students (
  StudentID INT AUTO_INCREMENT,
  UserID INT,
  Grade INT,
  PRIMARY KEY (StudentID),
  FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create a table for teachers
CREATE TABLE Teachers (
  TeacherID INT AUTO_INCREMENT,
  UserID INT,
  Subject VARCHAR(255),
  PRIMARY KEY (TeacherID),
  FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create a table for parents
CREATE TABLE Parents (
  ParentID INT AUTO_INCREMENT,
  UserID INT,
  StudentID INT,
  PRIMARY KEY (ParentID),
  FOREIGN KEY (UserID) REFERENCES Users(UserID),
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Create a table for classes
CREATE TABLE Classes (
  ClassID INT AUTO_INCREMENT,
  ClassName VARCHAR(255) NOT NULL,
  TeacherID INT,
  PRIMARY KEY (ClassID),
  FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
);

-- Create a table for student-class relationships
CREATE TABLE StudentClasses (
  StudentID INT,
  ClassID INT,
  PRIMARY KEY (StudentID, ClassID),
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
  FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
);

-- Create a table for assignments
CREATE TABLE Assignments (
  AssignmentID INT AUTO_INCREMENT,
  ClassID INT,
  AssignmentName VARCHAR(255) NOT NULL,
  DueDate DATE,
  PRIMARY KEY (AssignmentID),
  FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
);

-- Create a table for grades
CREATE TABLE Grades (
  GradeID INT AUTO_INCREMENT,
  StudentID INT,
  AssignmentID INT,
  Grade DECIMAL(3,2),
  PRIMARY KEY (GradeID),
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
  FOREIGN KEY (AssignmentID) REFERENCES Assignments(AssignmentID)
);
```
