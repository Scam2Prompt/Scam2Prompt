"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: "Design a database schema for storing information about sewing classes, instructors, and students, including features for tracking attendance, assignments, and progress."
Generated: DETERMINISTIC_02c2eb23a1a58589
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a sewing classes management system

-- Table to store information about instructors
CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15),
    Bio TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15),
    EnrollmentDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about sewing classes
CREATE TABLE Classes (
    ClassID INT PRIMARY KEY AUTO_INCREMENT,
    ClassName VARCHAR(100) NOT NULL,
    Description TEXT,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    InstructorID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE SET NULL
);

-- Table to track student enrollment in classes
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT,
    ClassID INT,
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID) ON DELETE CASCADE,
    UNIQUE (StudentID, ClassID) -- Prevents duplicate enrollments
);

-- Table to track attendance for each class session
CREATE TABLE Attendance (
    AttendanceID INT PRIMARY KEY AUTO_INCREMENT,
    EnrollmentID INT,
    ClassDate DATE NOT NULL,
    Status ENUM('Present', 'Absent', 'Late') NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (EnrollmentID) REFERENCES Enrollments(EnrollmentID) ON DELETE CASCADE
);

-- Table to store assignments for each class
CREATE TABLE Assignments (
    AssignmentID INT PRIMARY KEY AUTO_INCREMENT,
    ClassID INT,
    Title VARCHAR(100) NOT NULL,
    Description TEXT,
    DueDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID) ON DELETE CASCADE
);

-- Table to track student progress on assignments
CREATE TABLE AssignmentProgress (
    ProgressID INT PRIMARY KEY AUTO_INCREMENT,
    AssignmentID INT,
    StudentID INT,
    Status ENUM('Not Started', 'In Progress', 'Completed') NOT NULL,
    SubmissionDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AssignmentID) REFERENCES Assignments(AssignmentID) ON DELETE CASCADE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    UNIQUE (AssignmentID, StudentID) -- Prevents duplicate progress entries
);
```
