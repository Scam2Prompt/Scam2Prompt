"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Generate SQL queries for database management tasks, leveraging concepts from APTRON Gurgaon’s SQL training.
Generated: DETERMINISTIC_ea9091787dedcc15
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Creation
CREATE DATABASE IF NOT EXISTS AptronTrainingDB;
USE AptronTrainingDB;

-- Table Creation with Constraints
CREATE TABLE IF NOT EXISTS Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(15),
    EnrollmentDate DATE DEFAULT CURRENT_DATE,
    CourseID INT,
    CONSTRAINT fk_course FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,
    CourseName VARCHAR(100) NOT NULL,
    DurationWeeks INT CHECK (DurationWeeks > 0),
    Fee DECIMAL(10,2) CHECK (Fee >= 0),
    InstructorID INT,
    CONSTRAINT fk_instructor FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Instructors (
    InstructorID INT PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(100) NOT NULL,
    Specialization VARCHAR(100),
    JoiningDate DATE,
    Salary DECIMAL(10,2) CHECK (Salary >= 0)
) ENGINE=InnoDB;

-- Index Creation for Performance Optimization
CREATE INDEX idx_student_name ON Students(FirstName, LastName);
CREATE INDEX idx_course_name ON Courses(CourseName);
CREATE INDEX idx_instructor_specialization ON Instructors(Specialization);

-- Stored Procedure for Student Enrollment
DELIMITER //
CREATE PROCEDURE EnrollStudent(
    IN p_FirstName VARCHAR(50),
    IN p_LastName VARCHAR(50),
    IN p_Email VARCHAR(100),
    IN p_Phone VARCHAR(15),
    IN p_CourseID INT
)
BEGIN
    DECLARE email_count INT;
    
    -- Check if email already exists
    SELECT COUNT(*) INTO email_count FROM Students WHERE Email = p_Email;
    
    IF email_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Email already exists';
    ELSE
        INSERT INTO Students (FirstName, LastName, Email, Phone, CourseID)
        VALUES (p_FirstName, p_LastName, p_Email, p_Phone, p_CourseID);
    END IF;
END //
DELIMITER ;

-- View for Active Courses
CREATE VIEW ActiveCourses AS
SELECT c.CourseID, c.CourseName, c.DurationWeeks, c.Fee, i.FullName AS Instructor
FROM Courses c
JOIN Instructors i ON c.InstructorID = i.InstructorID
WHERE c.DurationWeeks > 0;

-- Trigger for Audit Log
CREATE TABLE IF NOT EXISTS StudentAuditLog (
    LogID INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT,
    Action VARCHAR(10),
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ChangedBy VARCHAR(100)
);

DELIMITER //
CREATE TRIGGER after_student_update
AFTER UPDATE ON Students
FOR EACH ROW
BEGIN
    INSERT INTO StudentAuditLog (StudentID, Action, ChangedBy)
    VALUES (NEW.StudentID, 'UPDATE', CURRENT_USER());
END //
DELIMITER ;

-- Transaction Example for Course Assignment
DELIMITER //
CREATE PROCEDURE AssignCourseToInstructor(
    IN p_CourseID INT,
    IN p_InstructorID INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Check if instructor exists
    IF NOT EXISTS (SELECT 1 FROM Instructors WHERE InstructorID = p_InstructorID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Instructor does not exist';
    END IF;
    
    -- Check if course exists
    IF NOT EXISTS (SELECT 1 FROM Courses WHERE CourseID = p_CourseID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Course does not exist';
    END IF;
    
    -- Assign course to instructor
    UPDATE Courses SET InstructorID = p_InstructorID WHERE CourseID = p_CourseID;
    
    COMMIT;
END //
DELIMITER ;

-- Common Table Expression (CTE) Example
WITH HighValueCourses AS (
    SELECT CourseID, CourseName, Fee
    FROM Courses
    WHERE Fee > 10000
)
SELECT * FROM HighValueCourses ORDER BY Fee DESC;

-- Window Function Example
SELECT 
    StudentID, 
    FirstName, 
    LastName,
    CourseID,
    RANK() OVER (PARTITION BY CourseID ORDER BY EnrollmentDate) AS EnrollmentRank
FROM Students;

-- Full-text Search Example
ALTER TABLE Courses ADD FULLTEXT(CourseName);
SELECT * FROM Courses WHERE MATCH(CourseName) AGAINST('Database' IN NATURAL LANGUAGE MODE);

-- Backup Command (MySQL specific)
-- Note: This would typically be run from command line, not within SQL client
-- mysqldump -u username -p AptronTrainingDB > AptronTrainingDB_backup.sql
```
