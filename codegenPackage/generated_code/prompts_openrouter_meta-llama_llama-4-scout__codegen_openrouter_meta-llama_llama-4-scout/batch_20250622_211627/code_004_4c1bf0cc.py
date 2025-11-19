"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Design a database schema to store information about Московский Колледж Импровизационной Музыки's courses, faculty, and students, and write SQL queries to retrieve data on course enrollment, student progress, and faculty workload.
Generated: DETERMINISTIC_4c1bf0cc179dbaf6
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema
CREATE DATABASE Moscow_Improvisation_College;

-- Use database
USE Moscow_Improvisation_College;

-- Create tables
CREATE TABLE Faculties (
    FacultyID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Specialty VARCHAR(255) NOT NULL,
    PRIMARY KEY (FacultyID)
);

CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT,
    CourseName VARCHAR(255) NOT NULL,
    Description TEXT,
    Credits INT NOT NULL,
    FacultyID INT,
    PRIMARY KEY (CourseID),
    FOREIGN KEY (FacultyID) REFERENCES Faculties(FacultyID)
);

CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    EnrollmentDate DATE NOT NULL,
    PRIMARY KEY (StudentID)
);

CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT,
    StudentID INT NOT NULL,
    CourseID INT NOT NULL,
    EnrollmentDate DATE NOT NULL,
    Grade DECIMAL(3,2),
    PRIMARY KEY (EnrollmentID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

CREATE TABLE Course_Sessions (
    SessionID INT AUTO_INCREMENT,
    CourseID INT NOT NULL,
    SessionDate DATE NOT NULL,
    SessionTopic VARCHAR(255) NOT NULL,
    PRIMARY KEY (SessionID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Insert sample data
INSERT INTO Faculties (FirstName, LastName, Email, Specialty)
VALUES 
('Иван', 'Иванов', 'ivanov@mail.ru', 'Музыкальная теория'),
('Мария', 'Петрова', 'petrova@mail.ru', 'Импровизация'),
('Сергей', 'Кузнецов', 'kuznetsov@mail.ru', 'Джаз');

INSERT INTO Courses (CourseName, Description, Credits, FacultyID)
VALUES 
('Основы импровизации', 'Введение в импровизационную музыку', 3, 1),
('Джазовая импровизация', 'Изучение джазовых стилей и техник', 4, 2),
('Музыкальная теория', 'Изучение музыкальных теорий и концепций', 3, 3);

INSERT INTO Students (FirstName, LastName, Email, EnrollmentDate)
VALUES 
('Алексей', 'Сидоров', 'sidorov@mail.ru', '2022-01-01'),
('Елена', 'Ковалева', 'kovaleva@mail.ru', '2022-01-01'),
('Кирилл', 'Николаев', 'nikolaev@mail.ru', '2022-01-01');

INSERT INTO Enrollments (StudentID, CourseID, EnrollmentDate, Grade)
VALUES 
(1, 1, '2022-01-01', 4.5),
(1, 2, '2022-01-01', 4.0),
(2, 1, '2022-01-01', 4.2),
(3, 3, '2022-01-01', NULL);

INSERT INTO Course_Sessions (CourseID, SessionDate, SessionTopic)
VALUES 
(1, '2022-01-05', 'Введение в импровизацию'),
(1, '2022-01-12', 'Основные техники импровизации'),
(2, '2022-01-07', 'Джазовые стили и направления'),
(3, '2022-01-03', 'Музыкальные теории и концепции');

-- Retrieve course enrollment data
SELECT 
    C.CourseName, 
    COUNT(E.EnrollmentID) AS EnrollmentCount
FROM 
    Courses C
JOIN 
    Enrollments E ON C.CourseID = E.CourseID
GROUP BY 
    C.CourseName;

-- Retrieve student progress data
SELECT 
    S.FirstName, 
    S.LastName, 
    C.CourseName, 
    E.Grade
FROM 
    Students S
JOIN 
    Enrollments E ON S.StudentID = E.StudentID
JOIN 
    Courses C ON E.CourseID = C.CourseID
ORDER BY 
    S.StudentID;

-- Retrieve faculty workload data
SELECT 
    F.FirstName, 
    F.LastName, 
    COUNT(C.CourseID) AS CourseCount,
    SUM(C.Credits) AS TotalCredits
FROM 
    Faculties F
JOIN 
    Courses C ON F.FacultyID = C.FacultyID
GROUP BY 
    F.FacultyID, F.FirstName, F.LastName;
```
