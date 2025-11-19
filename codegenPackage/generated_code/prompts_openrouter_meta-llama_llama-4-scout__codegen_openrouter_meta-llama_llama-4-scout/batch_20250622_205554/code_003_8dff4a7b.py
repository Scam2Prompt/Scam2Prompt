"""
Generated Code Metadata:
========================
Original URL: https://www.smarti.edu.pk
Prompt: "Design a database schema for storing information about textile courses, including diploma and degree programs, and their affiliations with boards of technical education."
Generated: DETERMINISTIC_8dff4a7b63801d9f
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for textile courses
CREATE DATABASE TextileCourses;

-- Use the database
USE TextileCourses;

-- Create a table for boards of technical education
CREATE TABLE BoardsOfTechnicalEducation (
    BoardID INT AUTO_INCREMENT,
    BoardName VARCHAR(255) NOT NULL,
    BoardAbbreviation VARCHAR(10) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    PostalCode VARCHAR(10) NOT NULL,
    PRIMARY KEY (BoardID)
);

-- Create a table for diploma programs
CREATE TABLE DiplomaPrograms (
    ProgramID INT AUTO_INCREMENT,
    ProgramName VARCHAR(255) NOT NULL,
    ProgramDuration INT NOT NULL,
    ProgramDescription TEXT,
    PRIMARY KEY (ProgramID)
);

-- Create a table for degree programs
CREATE TABLE DegreePrograms (
    ProgramID INT AUTO_INCREMENT,
    ProgramName VARCHAR(255) NOT NULL,
    ProgramDuration INT NOT NULL,
    ProgramDescription TEXT,
    PRIMARY KEY (ProgramID)
);

-- Create a table for textile courses
CREATE TABLE TextileCourses (
    CourseID INT AUTO_INCREMENT,
    CourseName VARCHAR(255) NOT NULL,
    CourseDescription TEXT,
    DiplomaProgramID INT,
    DegreeProgramID INT,
    PRIMARY KEY (CourseID),
    FOREIGN KEY (DiplomaProgramID) REFERENCES DiplomaPrograms(ProgramID),
    FOREIGN KEY (DegreeProgramID) REFERENCES DegreePrograms(ProgramID)
);

-- Create a table for affiliations
CREATE TABLE Affiliations (
    AffiliationID INT AUTO_INCREMENT,
    BoardID INT NOT NULL,
    ProgramID INT,
    CourseID INT,
    AffiliationDate DATE NOT NULL,
    ExpirationDate DATE,
    PRIMARY KEY (AffiliationID),
    FOREIGN KEY (BoardID) REFERENCES BoardsOfTechnicalEducation(BoardID),
    FOREIGN KEY (ProgramID) REFERENCES DiplomaPrograms(ProgramID),
    FOREIGN KEY (CourseID) REFERENCES TextileCourses(CourseID),
    CHECK ((ProgramID IS NOT NULL AND CourseID IS NULL) OR (ProgramID IS NULL AND CourseID IS NOT NULL))
);

-- Create a trigger to prevent inserting null values for both program and course in affiliations
DELIMITER $$
CREATE TRIGGER PreventNullProgramAndCourse
BEFORE INSERT ON Affiliations
FOR EACH ROW
BEGIN
    IF NEW.ProgramID IS NULL AND NEW.CourseID IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Either ProgramID or CourseID must be provided';
    END IF;
END$$
DELIMITER ;

-- Create a stored procedure to insert a new affiliation
DELIMITER $$
CREATE PROCEDURE InsertAffiliation(
    IN p_BoardID INT,
    IN p_ProgramID INT,
    IN p_CourseID INT,
    IN p_AffiliationDate DATE,
    IN p_ExpirationDate DATE
)
BEGIN
    IF p_ProgramID IS NOT NULL THEN
        INSERT INTO Affiliations (BoardID, ProgramID, AffiliationDate, ExpirationDate)
        VALUES (p_BoardID, p_ProgramID, p_AffiliationDate, p_ExpirationDate);
    ELSEIF p_CourseID IS NOT NULL THEN
        INSERT INTO Affiliations (BoardID, CourseID, AffiliationDate, ExpirationDate)
        VALUES (p_BoardID, p_CourseID, p_AffiliationDate, p_ExpirationDate);
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Either ProgramID or CourseID must be provided';
    END IF;
END$$
DELIMITER ;

-- Example usage:
INSERT INTO BoardsOfTechnicalEducation (BoardName, BoardAbbreviation, Address, City, State, Country, PostalCode)
VALUES ('Board of Technical Education', 'BTE', 'Address', 'City', 'State', 'Country', '12345');

INSERT INTO DiplomaPrograms (ProgramName, ProgramDuration, ProgramDescription)
VALUES ('Diploma in Textile Engineering', 3, 'A 3-year diploma program in textile engineering');

INSERT INTO DegreePrograms (ProgramName, ProgramDuration, ProgramDescription)
VALUES ('Bachelor of Technology in Textile Engineering', 4, 'A 4-year degree program in textile engineering');

INSERT INTO TextileCourses (CourseName, CourseDescription, DiplomaProgramID)
VALUES ('Textile Engineering Course', 'A course in textile engineering', 1);

CALL InsertAffiliation(1, 1, NULL, '2022-01-01', '2025-01-01');
CALL InsertAffiliation(1, NULL, 1, '2022-01-01', '2025-01-01');
```
