"""
Generated Code Metadata:
========================
Original URL: https://siprosa.org
Prompt: Design a simple database schema to manage information about students, teachers, and classrooms for a school like Siprosa School, with a focus on low student-to-teacher ratio.
Generated: DETERMINISTIC_0efb95d680a98792
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing information about students, teachers, and classrooms

-- Create a database for the school
CREATE DATABASE SiprosaSchool;

-- Use the created database
USE SiprosaSchool;

-- Table to store information about teachers
CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each teacher
    FirstName VARCHAR(50) NOT NULL,            -- Teacher's first name
    LastName VARCHAR(50) NOT NULL,             -- Teacher's last name
    Subject VARCHAR(50) NOT NULL,               -- Subject taught by the teacher
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Teacher's email address
    Phone VARCHAR(15),                         -- Teacher's phone number
    HireDate DATE NOT NULL                      -- Date when the teacher was hired
);

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,             -- Student's first name
    LastName VARCHAR(50) NOT NULL,              -- Student's last name
    DateOfBirth DATE NOT NULL,                  -- Student's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Student's email address
    Phone VARCHAR(15),                          -- Student's phone number
    EnrollmentDate DATE NOT NULL,               -- Date when the student enrolled
    TeacherID INT,                              -- Foreign key referencing the teacher
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) ON DELETE SET NULL -- Relationship with Teachers
);

-- Table to store information about classrooms
CREATE TABLE Classrooms (
    ClassroomID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each classroom
    RoomNumber VARCHAR(10) NOT NULL UNIQUE,      -- Room number of the classroom
    Capacity INT NOT NULL,                        -- Maximum capacity of the classroom
    TeacherID INT,                                -- Foreign key referencing the teacher
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) ON DELETE SET NULL -- Relationship with Teachers
);

-- Table to manage the relationship between students and classrooms
CREATE TABLE StudentClassrooms (
    StudentID INT,                               -- Foreign key referencing the student
    ClassroomID INT,                             -- Foreign key referencing the classroom
    PRIMARY KEY (StudentID, ClassroomID),       -- Composite primary key
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Relationship with Students
    FOREIGN KEY (ClassroomID) REFERENCES Classrooms(ClassroomID) ON DELETE CASCADE -- Relationship with Classrooms
);

-- Sample data insertion (optional)
-- INSERT INTO Teachers (FirstName, LastName, Subject, Email, Phone, HireDate) VALUES ('John', 'Doe', 'Mathematics', 'john.doe@example.com', '1234567890', '2020-01-15');
-- INSERT INTO Students (FirstName, LastName, DateOfBirth, Email, Phone, EnrollmentDate, TeacherID) VALUES ('Jane', 'Smith', '2005-05-20', 'jane.smith@example.com', '0987654321', '2021-09-01', 1);
-- INSERT INTO Classrooms (RoomNumber, Capacity, TeacherID) VALUES ('101', 20, 1);
-- INSERT INTO StudentClassrooms (StudentID, ClassroomID) VALUES (1, 1);
```
