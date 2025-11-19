"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Design a database schema for storing information about SMKN 1 Kadipaten's students, teachers, and staff, including details about their roles and responsibilities like the deputy leader Abdul Madjid, S.Pd., M.Pd.
Generated: DETERMINISTIC_1fe698e256a35b03
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SMKN 1 Kadipaten

-- Create a database
CREATE DATABASE SMKN1Kadipaten;

-- Use the database
USE SMKN1Kadipaten;

-- Table for storing general user information (students, teachers, staff)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(100) NOT NULL,        -- Full name of the user
    Email VARCHAR(100) UNIQUE,             -- Email address (optional, unique)
    PhoneNumber VARCHAR(15),               -- Contact number (optional)
    Address TEXT,                          -- Address of the user
    Role ENUM('Student', 'Teacher', 'Staff') NOT NULL, -- Role of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for storing student-specific information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    Class VARCHAR(50) NOT NULL,               -- Class the student belongs to
    Major VARCHAR(50),                        -- Major/field of study
    EnrollmentDate DATE NOT NULL,             -- Date of enrollment
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete
);

-- Table for storing teacher-specific information
CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each teacher
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    Subject VARCHAR(100) NOT NULL,            -- Subject taught by the teacher
    Position VARCHAR(100),                    -- Position (e.g., Deputy Leader)
    HireDate DATE NOT NULL,                   -- Date of hire
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete
);

-- Table for storing staff-specific information
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each staff member
    UserID INT NOT NULL,                    -- Foreign key referencing Users table
    Department VARCHAR(100) NOT NULL,       -- Department the staff member belongs to
    Position VARCHAR(100),                  -- Position (e.g., Administrative Assistant)
    HireDate DATE NOT NULL,                 -- Date of hire
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete
);

-- Insert example data for the deputy leader Abdul Madjid, S.Pd., M.Pd.
INSERT INTO Users (FullName, Email, PhoneNumber, Address, Role)
VALUES ('Abdul Madjid, S.Pd., M.Pd.', 'abdul.madjid@smkn1kadipaten.sch.id', '081234567890', 'Kadipaten, Indonesia', 'Teacher');

INSERT INTO Teachers (UserID, Subject, Position, HireDate)
VALUES (LAST_INSERT_ID(), 'Leadership and Education', 'Deputy Leader', '2010-07-15');
```
