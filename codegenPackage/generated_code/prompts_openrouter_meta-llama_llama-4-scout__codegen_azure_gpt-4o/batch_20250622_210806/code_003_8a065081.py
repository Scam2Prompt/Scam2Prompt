"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: "Design a database schema to store information about Jiu-Jitsu instructors, students, and training sessions for a school like Fusion Jiu Jitsu School."
Generated: DETERMINISTIC_8a065081ec51c719
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Jiu-Jitsu school to store information about instructors, students, and training sessions.

-- Table to store information about instructors
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instructor
    FirstName VARCHAR(50) NOT NULL,              -- First name of the instructor
    LastName VARCHAR(50) NOT NULL,               -- Last name of the instructor
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Email address of the instructor
    PhoneNumber VARCHAR(15),                     -- Phone number of the instructor
    Rank VARCHAR(50) NOT NULL,                   -- Rank of the instructor (e.g., Black Belt)
    DateJoined DATE NOT NULL,                    -- Date the instructor joined the school
    IsActive BOOLEAN DEFAULT TRUE                -- Whether the instructor is currently active
);

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,              -- First name of the student
    LastName VARCHAR(50) NOT NULL,               -- Last name of the student
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Email address of the student
    PhoneNumber VARCHAR(15),                     -- Phone number of the student
    Rank VARCHAR(50),                            -- Rank of the student (e.g., White Belt, Blue Belt)
    DateJoined DATE NOT NULL,                    -- Date the student joined the school
    IsActive BOOLEAN DEFAULT TRUE                -- Whether the student is currently active
);

-- Table to store information about training sessions
CREATE TABLE TrainingSessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each training session
    SessionDate DATE NOT NULL,                   -- Date of the training session
    StartTime TIME NOT NULL,                     -- Start time of the training session
    EndTime TIME NOT NULL,                       -- End time of the training session
    InstructorID INT NOT NULL,                   -- ID of the instructor leading the session
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE,
    MaxParticipants INT NOT NULL,                -- Maximum number of participants allowed
    SessionType VARCHAR(50) NOT NULL             -- Type of session (e.g., Gi, No-Gi, Open Mat)
);

-- Table to store attendance for training sessions
CREATE TABLE SessionAttendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    SessionID INT NOT NULL,                      -- ID of the training session
    StudentID INT NOT NULL,                      -- ID of the student attending the session
    FOREIGN KEY (SessionID) REFERENCES TrainingSessions(SessionID) ON DELETE CASCADE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    AttendanceDate DATE NOT NULL                 -- Date the student attended the session
);

-- Indexes for optimizing queries
CREATE INDEX idx_instructor_email ON Instructors(Email);
CREATE INDEX idx_student_email ON Students(Email);
CREATE INDEX idx_session_date ON TrainingSessions(SessionDate);
CREATE INDEX idx_attendance_session_student ON SessionAttendance(SessionID, StudentID);
```
