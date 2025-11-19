"""
Generated Code Metadata:
========================
Original URL: https://iedeoccidente.edu.co
Prompt: "Design a database schema for managing student records, including student information, grades, and attendance, for an institution with primary and secondary education sections like IEO."
Generated: DETERMINISTIC_f5bce4d10d6edf8f
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing student records, grades, and attendance
-- This schema is designed for an institution with primary and secondary education sections.

-- Table to store student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Student's gender
    Section ENUM('Primary', 'Secondary') NOT NULL,  -- Education section (Primary or Secondary)
    EnrollmentDate DATE NOT NULL,             -- Date of enrollment
    ContactNumber VARCHAR(15),                -- Contact number (optional)
    Email VARCHAR(100),                       -- Email address (optional)
    Address TEXT                              -- Address (optional)
);

-- Table to store subjects offered by the institution
CREATE TABLE Subjects (
    SubjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subject
    SubjectName VARCHAR(100) NOT NULL,        -- Name of the subject
    Section ENUM('Primary', 'Secondary') NOT NULL -- Section the subject belongs to
);

-- Table to store grades for students
CREATE TABLE Grades (
    GradeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each grade record
    StudentID INT NOT NULL,                  -- Foreign key referencing Students table
    SubjectID INT NOT NULL,                  -- Foreign key referencing Subjects table
    Grade VARCHAR(5) NOT NULL,               -- Grade (e.g., A, B, C, etc.)
    AcademicYear VARCHAR(10) NOT NULL,       -- Academic year (e.g., 2023-2024)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID) ON DELETE CASCADE
);

-- Table to store attendance records for students
CREATE TABLE Attendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    SubjectID INT NOT NULL,                      -- Foreign key referencing Subjects table
    AttendanceDate DATE NOT NULL,                -- Date of attendance
    Status ENUM('Present', 'Absent', 'Late') NOT NULL, -- Attendance status
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID) ON DELETE CASCADE
);

-- Table to store teachers (optional, for future expansion)
CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each teacher
    FirstName VARCHAR(50) NOT NULL,           -- Teacher's first name
    LastName VARCHAR(50) NOT NULL,            -- Teacher's last name
    ContactNumber VARCHAR(15),                -- Contact number (optional)
    Email VARCHAR(100),                       -- Email address (optional)
    Address TEXT                              -- Address (optional)
);

-- Table to store subject-teacher assignments (optional, for future expansion)
CREATE TABLE SubjectTeachers (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    SubjectID INT NOT NULL,                      -- Foreign key referencing Subjects table
    TeacherID INT NOT NULL,                      -- Foreign key referencing Teachers table
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID) ON DELETE CASCADE,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_student_section ON Students(Section);
CREATE INDEX idx_subject_section ON Subjects(Section);
CREATE INDEX idx_grades_academic_year ON Grades(AcademicYear);
CREATE INDEX idx_attendance_date ON Attendance(AttendanceDate);
```
