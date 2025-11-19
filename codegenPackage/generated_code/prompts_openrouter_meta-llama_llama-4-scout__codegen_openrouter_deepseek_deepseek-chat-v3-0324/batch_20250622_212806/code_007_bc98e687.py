"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Can you provide a code example of how to create a database using Microsoft SQL Server, as covered in edukacija.net's database development courses, and how can I optimize its performance?
Generated: DETERMINISTIC_bc98e687e7595341
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Server Database Creation Script
-- Follows best practices from edukacija.net courses

-- Check if database exists and drop if needed (for idempotency)
IF EXISTS (SELECT name FROM sys.databases WHERE name = 'EdukacijaNetDB')
BEGIN
    ALTER DATABASE EdukacijaNetDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE EdukacijaNetDB;
END

-- Create new database with optimized file settings
CREATE DATABASE EdukacijaNetDB
ON PRIMARY 
(
    NAME = 'EdukacijaNetDB_Data',
    FILENAME = 'C:\SQLData\EdukacijaNetDB.mdf',
    SIZE = 100MB,
    MAXSIZE = UNLIMITED,
    FILEGROWTH = 50MB
)
LOG ON
(
    NAME = 'EdukacijaNetDB_Log',
    FILENAME = 'C:\SQLData\EdukacijaNetDB.ldf',
    SIZE = 50MB,
    MAXSIZE = 2GB,
    FILEGROWTH = 25MB
);

-- Set recommended database options
ALTER DATABASE EdukacijaNetDB SET RECOVERY SIMPLE;
ALTER DATABASE EdukacijaNetDB SET AUTO_SHRINK OFF;
ALTER DATABASE EdukacijaNetDB SET AUTO_CREATE_STATISTICS ON;
ALTER DATABASE EdukacijaNetDB SET AUTO_UPDATE_STATISTICS ON;
ALTER DATABASE EdukacijaNetDB SET READ_COMMITTED_SNAPSHOT ON;

-- Create sample tables with proper indexing
USE EdukacijaNetDB;
GO

-- Students table with clustered index on ID
CREATE TABLE Students
(
    StudentID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) UNIQUE,
    EnrollmentDate DATETIME DEFAULT GETDATE(),
    IsActive BIT DEFAULT 1
);

-- Courses table with clustered index on ID
CREATE TABLE Courses
(
    CourseID INT IDENTITY(1,1) PRIMARY KEY,
    CourseName NVARCHAR(100) NOT NULL,
    Description NVARCHAR(500),
    Credits INT NOT NULL,
    IsActive BIT DEFAULT 1
);

-- Enrollment junction table with composite PK
CREATE TABLE Enrollments
(
    EnrollmentID INT IDENTITY(1,1) PRIMARY KEY,
    StudentID INT NOT NULL,
    CourseID INT NOT NULL,
    EnrollmentDate DATETIME DEFAULT GETDATE(),
    Grade DECIMAL(3,2) NULL,
    CONSTRAINT FK_Enrollments_Students FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    CONSTRAINT FK_Enrollments_Courses FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    CONSTRAINT UQ_StudentCourse UNIQUE (StudentID, CourseID)
);

-- Create non-clustered indexes for performance
CREATE INDEX IX_Students_LastName ON Students(LastName);
CREATE INDEX IX_Courses_CourseName ON Courses(CourseName);
CREATE INDEX IX_Enrollments_StudentID ON Enrollments(StudentID);
CREATE INDEX IX_Enrollments_CourseID ON Enrollments(CourseID);

-- Create a stored procedure for optimized data retrieval
CREATE PROCEDURE sp_GetStudentCourses
    @StudentID INT
AS
BEGIN
    SET NOCOUNT ON;
    
    SELECT 
        s.StudentID,
        s.FirstName + ' ' + s.LastName AS StudentName,
        c.CourseName,
        c.Description,
        c.Credits,
        e.EnrollmentDate,
        e.Grade
    FROM 
        Students s
        INNER JOIN Enrollments e ON s.StudentID = e.StudentID
        INNER JOIN Courses c ON e.CourseID = c.CourseID
    WHERE 
        s.StudentID = @StudentID
        AND s.IsActive = 1
        AND c.IsActive = 1
    ORDER BY 
        c.CourseName;
END;
GO

-- Create a view for reporting
CREATE VIEW vw_ActiveStudentsWithCourses AS
SELECT 
    s.StudentID,
    s.FirstName + ' ' + s.LastName AS StudentName,
    s.Email,
    COUNT(e.CourseID) AS EnrolledCourses,
    AVG(e.Grade) AS AverageGrade
FROM 
    Students s
    LEFT JOIN Enrollments e ON s.StudentID = e.StudentID
WHERE 
    s.IsActive = 1
GROUP BY 
    s.StudentID, s.FirstName, s.LastName, s.Email;
GO

-- Add full-text search capability if needed
-- (Requires full-text catalog to be created first)
-- CREATE FULLTEXT INDEX ON Courses(CourseName, Description) KEY INDEX PK__Courses__8F1EF7AE...;
```
