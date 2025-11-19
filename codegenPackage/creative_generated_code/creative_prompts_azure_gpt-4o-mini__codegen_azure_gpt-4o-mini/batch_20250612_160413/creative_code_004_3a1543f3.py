"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myflowfoundationke.org
Prompt: Design a data model in SQL to manage the records of girls impacted by menstrual health initiatives, similar to the tracking done by My Flow Foundation.
Generated: DETERMINISTIC_3a1543f3ceb01dfb
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database: menstrual_health_initiatives
CREATE DATABASE menstrual_health_initiatives;

-- Use the created database
USE menstrual_health_initiatives;

-- Table to store information about participants
CREATE TABLE participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each participant
    name VARCHAR(100) NOT NULL,                     -- Participant's name
    age INT CHECK (age >= 10 AND age <= 50),        -- Age of the participant (between 10 and 50)
    email VARCHAR(100) UNIQUE,                       -- Email address of the participant (unique)
    phone_number VARCHAR(15),                        -- Phone number of the participant
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store menstrual health education sessions
CREATE TABLE education_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each session
    session_title VARCHAR(150) NOT NULL,             -- Title of the education session
    session_date DATE NOT NULL,                       -- Date of the education session
    duration INT CHECK (duration > 0),               -- Duration of the session in minutes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP    -- Record creation timestamp
);

-- Table to track attendance of participants in sessions
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for attendance record
    participant_id INT NOT NULL,                       -- Foreign key referencing participants
    session_id INT NOT NULL,                           -- Foreign key referencing education sessions
    attended BOOLEAN DEFAULT FALSE,                    -- Attendance status (TRUE if attended, FALSE otherwise)
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE, -- Foreign key relationship
    FOREIGN KEY (session_id) REFERENCES education_sessions(session_id) ON DELETE CASCADE,   -- Foreign key relationship
    UNIQUE (participant_id, session_id)               -- Ensure a participant can only record attendance for a session once
);

-- Table to store feedback from participants about the sessions
CREATE TABLE feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for feedback record
    participant_id INT NOT NULL,                       -- Foreign key referencing participants
    session_id INT NOT NULL,                           -- Foreign key referencing education sessions
    rating INT CHECK (rating >= 1 AND rating <= 5),   -- Rating given by the participant (1 to 5 scale)
    comments TEXT,                                     -- Optional comments provided by the participant
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE, -- Foreign key relationship
    FOREIGN KEY (session_id) REFERENCES education_sessions(session_id) ON DELETE CASCADE   -- Foreign key relationship
);

-- Sample query to find all participants who attended a specific session
-- SELECT p.name, a.attended
-- FROM participants p
-- JOIN attendance a ON p.participant_id = a.participant_id
-- WHERE a.session_id = ?; -- Replace ? with the session_id you want to query
```
