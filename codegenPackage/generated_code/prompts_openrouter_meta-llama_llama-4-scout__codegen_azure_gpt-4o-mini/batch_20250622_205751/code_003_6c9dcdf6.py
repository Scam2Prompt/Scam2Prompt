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
-- Database schema for SKI Foundation to store information about program participants, courses, and training sessions

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Participants;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS TrainingSessions;

-- Table to store information about participants
CREATE TABLE Participants (
    participant_id SERIAL PRIMARY KEY, -- Unique identifier for each participant
    first_name VARCHAR(50) NOT NULL,   -- First name of the participant
    last_name VARCHAR(50) NOT NULL,    -- Last name of the participant
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address of the participant
    phone VARCHAR(15),                  -- Phone number of the participant
    date_of_birth DATE NOT NULL,        -- Date of birth of the participant
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about courses
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,       -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,  -- Name of the course
    description TEXT,                   -- Description of the course
    duration INT NOT NULL,              -- Duration of the course in hours
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about training sessions
CREATE TABLE TrainingSessions (
    session_id SERIAL PRIMARY KEY,      -- Unique identifier for each training session
    course_id INT NOT NULL,             -- Foreign key referencing Courses
    session_date DATE NOT NULL,         -- Date of the training session
    start_time TIME NOT NULL,           -- Start time of the training session
    end_time TIME NOT NULL,             -- End time of the training session
    location VARCHAR(100),              -- Location of the training session
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to associate participants with training sessions
CREATE TABLE ParticipantSessions (
    participant_session_id SERIAL PRIMARY KEY, -- Unique identifier for each participant-session association
    participant_id INT NOT NULL,                -- Foreign key referencing Participants
    session_id INT NOT NULL,                    -- Foreign key referencing TrainingSessions
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Registration timestamp
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (session_id) REFERENCES TrainingSessions(session_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster lookups
CREATE INDEX idx_participant_email ON Participants(email);
CREATE INDEX idx_course_name ON Courses(course_name);
CREATE INDEX idx_session_date ON TrainingSessions(session_date);
```
