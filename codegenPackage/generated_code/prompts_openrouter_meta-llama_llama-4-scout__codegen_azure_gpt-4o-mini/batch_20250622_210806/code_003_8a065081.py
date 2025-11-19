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
-- Database schema for Fusion Jiu Jitsu School

-- Table to store information about instructors
CREATE TABLE Instructors (
    instructor_id SERIAL PRIMARY KEY, -- Unique identifier for each instructor
    first_name VARCHAR(50) NOT NULL,  -- Instructor's first name
    last_name VARCHAR(50) NOT NULL,   -- Instructor's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Instructor's email address
    phone VARCHAR(15),                 -- Instructor's phone number
    rank VARCHAR(20),                  -- Instructor's rank in Jiu-Jitsu
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about students
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,     -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,   -- Student's first name
    last_name VARCHAR(50) NOT NULL,    -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone VARCHAR(15),                  -- Student's phone number
    rank VARCHAR(20),                   -- Student's rank in Jiu-Jitsu
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about training sessions
CREATE TABLE TrainingSessions (
    session_id SERIAL PRIMARY KEY,      -- Unique identifier for each training session
    instructor_id INT NOT NULL,         -- Foreign key referencing the instructor
    session_date TIMESTAMP NOT NULL,    -- Date and time of the training session
    duration INT NOT NULL,               -- Duration of the session in minutes
    location VARCHAR(100),               -- Location of the training session
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store attendance records for students in training sessions
CREATE TABLE Attendance (
    attendance_id SERIAL PRIMARY KEY,    -- Unique identifier for each attendance record
    session_id INT NOT NULL,             -- Foreign key referencing the training session
    student_id INT NOT NULL,             -- Foreign key referencing the student
    attended BOOLEAN NOT NULL DEFAULT FALSE, -- Attendance status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (session_id) REFERENCES TrainingSessions(session_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_instructor_email ON Instructors(email);
CREATE INDEX idx_student_email ON Students(email);
CREATE INDEX idx_session_date ON TrainingSessions(session_date);
CREATE INDEX idx_attendance_session ON Attendance(session_id);
CREATE INDEX idx_attendance_student ON Attendance(student_id);
```
