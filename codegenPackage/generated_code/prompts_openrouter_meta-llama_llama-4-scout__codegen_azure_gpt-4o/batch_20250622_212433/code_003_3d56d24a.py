"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Design a database schema to manage student information, attendance, and academic records for a school like Param Gyan Niketan.
Generated: DETERMINISTIC_3d56d24af014a78a
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing student information, attendance, and academic records

-- Create a table to store student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Student's gender
    Address TEXT,                             -- Student's address
    ContactNumber VARCHAR(15),                -- Student's contact number
    Email VARCHAR(100),                       -- Student's email address
    EnrollmentDate DATE NOT NULL,             -- Date of enrollment
    Class VARCHAR(20) NOT NULL                -- Class/Grade the student is enrolled in
);

-- Create a table to store attendance records
CREATE TABLE Attendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    AttendanceDate DATE NOT NULL,                -- Date of attendance
    Status ENUM('Present', 'Absent', 'Late') NOT NULL, -- Attendance status
    Remarks TEXT,                                -- Additional remarks (optional)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Create a table to store academic records
CREATE TABLE AcademicRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each academic record
    StudentID INT NOT NULL,                  -- Foreign key referencing Students table
    Subject VARCHAR(50) NOT NULL,            -- Subject name
    ExamDate DATE NOT NULL,                  -- Date of the exam
    MarksObtained DECIMAL(5,2) NOT NULL,     -- Marks obtained by the student
    TotalMarks DECIMAL(5,2) NOT NULL,        -- Total marks for the exam
    Grade VARCHAR(5),                        -- Grade achieved (optional)
    Remarks TEXT,                            -- Additional remarks (optional)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Create a table to store teacher information (optional, for future use)
CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each teacher
    FirstName VARCHAR(50) NOT NULL,           -- Teacher's first name
    LastName VARCHAR(50) NOT NULL,            -- Teacher's last name
    Subject VARCHAR(50) NOT NULL,             -- Subject taught by the teacher
    ContactNumber VARCHAR(15),                -- Teacher's contact number
    Email VARCHAR(100)                        -- Teacher's email address
);

-- Create a table to store class schedules (optional, for future use)
CREATE TABLE ClassSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule
    Class VARCHAR(20) NOT NULL,                -- Class/Grade
    Subject VARCHAR(50) NOT NULL,              -- Subject name
    TeacherID INT NOT NULL,                    -- Foreign key referencing Teachers table
    DayOfWeek ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday') NOT NULL, -- Day of the week
    StartTime TIME NOT NULL,                   -- Start time of the class
    EndTime TIME NOT NULL,                     -- End time of the class
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) ON DELETE SET NULL
);

-- Indexes for optimization
CREATE INDEX idx_student_class ON Students(Class);
CREATE INDEX idx_attendance_date ON Attendance(AttendanceDate);
CREATE INDEX idx_academic_subject ON AcademicRecords(Subject);
CREATE INDEX idx_schedule_class ON ClassSchedules(Class);
```
