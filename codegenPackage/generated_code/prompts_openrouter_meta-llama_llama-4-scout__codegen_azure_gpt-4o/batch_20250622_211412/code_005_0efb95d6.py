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
-- Focused on maintaining a low student-to-teacher ratio

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    ClassroomID INT,                          -- Foreign key to associate the student with a classroom
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClassroomID) REFERENCES Classrooms(ClassroomID) -- Ensures valid classroom association
);

-- Table to store information about teachers
CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each teacher
    FirstName VARCHAR(50) NOT NULL,           -- First name of the teacher
    LastName VARCHAR(50) NOT NULL,            -- Last name of the teacher
    Subject VARCHAR(100) NOT NULL,            -- Subject taught by the teacher
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the teacher
    PhoneNumber VARCHAR(15),                  -- Contact number of the teacher
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about classrooms
CREATE TABLE Classrooms (
    ClassroomID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each classroom
    RoomNumber VARCHAR(10) NOT NULL,            -- Room number or identifier
    Capacity INT NOT NULL,                      -- Maximum number of students the classroom can hold
    TeacherID INT,                              -- Foreign key to associate the classroom with a teacher
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) -- Ensures valid teacher association
);

-- Table to manage student-teacher relationships for low student-to-teacher ratio
CREATE TABLE StudentTeacherMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each mapping
    StudentID INT NOT NULL,                    -- Foreign key to associate a student
    TeacherID INT NOT NULL,                    -- Foreign key to associate a teacher
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID), -- Ensures valid student association
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) -- Ensures valid teacher association
);

-- Indexes for optimizing queries
CREATE INDEX idx_student_classroom ON Students(ClassroomID);
CREATE INDEX idx_teacher_classroom ON Classrooms(TeacherID);
CREATE INDEX idx_student_teacher ON StudentTeacherMapping(StudentID, TeacherID);

-- Constraints to ensure low student-to-teacher ratio
-- Example: Ensure no teacher is assigned more than 10 students
-- This can be enforced programmatically in application logic or via triggers if needed.
```
