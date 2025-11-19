"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Design a database schema to store information about program participants, courses, and training sessions for an organization like SKI Foundation.
Generated: DETERMINISTIC_6c9dcdf68d7ccc34
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about program participants, courses, and training sessions

-- Table to store participant information
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    FirstName VARCHAR(50) NOT NULL,               -- First name of the participant
    LastName VARCHAR(50) NOT NULL,                -- Last name of the participant
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Email address of the participant
    PhoneNumber VARCHAR(15),                      -- Phone number of the participant
    DateOfBirth DATE,                             -- Date of birth of the participant
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date and time of registration
);

-- Table to store course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,             -- Name of the course
    Description TEXT,                             -- Description of the course
    DurationInHours INT NOT NULL,                 -- Duration of the course in hours
    CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date and time the course was created
);

-- Table to store training session information
CREATE TABLE TrainingSessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each training session
    CourseID INT NOT NULL,                        -- Foreign key referencing the Courses table
    SessionDate DATE NOT NULL,                    -- Date of the training session
    StartTime TIME NOT NULL,                      -- Start time of the training session
    EndTime TIME NOT NULL,                        -- End time of the training session
    Location VARCHAR(100),                        -- Location of the training session
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete if course is deleted
);

-- Table to store participant enrollments in training sessions
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each enrollment
    ParticipantID INT NOT NULL,                   -- Foreign key referencing the Participants table
    SessionID INT NOT NULL,                       -- Foreign key referencing the TrainingSessions table
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of enrollment
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE, -- Cascade delete if participant is deleted
    FOREIGN KEY (SessionID) REFERENCES TrainingSessions(SessionID) ON DELETE CASCADE -- Cascade delete if session is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_participant_email ON Participants(Email); -- Index for quick lookup by email
CREATE INDEX idx_course_name ON Courses(CourseName);       -- Index for quick lookup by course name
CREATE INDEX idx_session_date ON TrainingSessions(SessionDate); -- Index for quick lookup by session date
CREATE INDEX idx_enrollment_participant_session ON Enrollments(ParticipantID, SessionID); -- Composite index for participant-session lookup
```
