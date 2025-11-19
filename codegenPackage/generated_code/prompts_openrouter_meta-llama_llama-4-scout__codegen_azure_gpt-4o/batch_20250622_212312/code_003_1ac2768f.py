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
-- Database schema for storing student information, academic subjects, and co-curricular activities

-- Create a table for storing student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    Address TEXT,                             -- Address of the student
    ContactNumber VARCHAR(15),                -- Contact number of the student
    Email VARCHAR(100),                       -- Email address of the student
    EnrollmentDate DATE NOT NULL              -- Date of enrollment in the school
);

-- Create a table for storing academic subjects
CREATE TABLE Subjects (
    SubjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subject
    SubjectName VARCHAR(100) NOT NULL,        -- Name of the subject
    SubjectCode VARCHAR(10) NOT NULL UNIQUE,  -- Unique code for the subject
    Description TEXT                          -- Description of the subject
);

-- Create a table for storing co-curricular activities
CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each activity
    ActivityName VARCHAR(100) NOT NULL,        -- Name of the activity
    Description TEXT,                          -- Description of the activity
    ActivityType ENUM('Sports', 'Arts', 'Music', 'Other') NOT NULL -- Type of activity
);

-- Create a table for mapping students to subjects (many-to-many relationship)
CREATE TABLE StudentSubjects (
    StudentID INT NOT NULL,                    -- Foreign key referencing Students table
    SubjectID INT NOT NULL,                    -- Foreign key referencing Subjects table
    PRIMARY KEY (StudentID, SubjectID),        -- Composite primary key
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID) ON DELETE CASCADE
);

-- Create a table for mapping students to activities (many-to-many relationship)
CREATE TABLE StudentActivities (
    StudentID INT NOT NULL,                    -- Foreign key referencing Students table
    ActivityID INT NOT NULL,                   -- Foreign key referencing Activities table
    PRIMARY KEY (StudentID, ActivityID),       -- Composite primary key
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE
);

-- Create indexes for faster lookups
CREATE INDEX idx_student_name ON Students (FirstName, LastName);
CREATE INDEX idx_subject_name ON Subjects (SubjectName);
CREATE INDEX idx_activity_name ON Activities (ActivityName);
```
