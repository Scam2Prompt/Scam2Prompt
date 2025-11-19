"""
Generated Code Metadata:
========================
Original URL: https://openmindsinstituto.com.br
Prompt: Create a database schema for storing participant information and session details for study groups focused on respiratory disorders and neonatal dysphagia, as described on Open Minds Instituto's website.
Generated: DETERMINISTIC_a19f62d085bd4859
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing participant information and session details
-- for study groups focused on respiratory disorders and neonatal dysphagia.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Participants;
DROP TABLE IF EXISTS Sessions;
DROP TABLE IF EXISTS StudyGroups;

-- Table to store participant information
CREATE TABLE Participants (
    participant_id SERIAL PRIMARY KEY, -- Unique identifier for each participant
    first_name VARCHAR(50) NOT NULL,   -- Participant's first name
    last_name VARCHAR(50) NOT NULL,    -- Participant's last name
    date_of_birth DATE NOT NULL,        -- Participant's date of birth
    email VARCHAR(100) UNIQUE NOT NULL, -- Participant's email address
    phone_number VARCHAR(15),           -- Participant's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store study group session details
CREATE TABLE Sessions (
    session_id SERIAL PRIMARY KEY,      -- Unique identifier for each session
    session_date DATE NOT NULL,         -- Date of the session
    session_time TIME NOT NULL,         -- Time of the session
    duration INT NOT NULL,              -- Duration of the session in minutes
    location VARCHAR(100) NOT NULL,     -- Location of the session
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to link participants to study groups and sessions
CREATE TABLE StudyGroups (
    group_id SERIAL PRIMARY KEY,         -- Unique identifier for each study group
    participant_id INT NOT NULL,         -- Foreign key referencing Participants
    session_id INT NOT NULL,             -- Foreign key referencing Sessions
    group_role VARCHAR(50),              -- Role of the participant in the group (e.g., 'attendee', 'facilitator')
    feedback TEXT,                       -- Feedback provided by the participant after the session
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (session_id) REFERENCES Sessions(session_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_participant_email ON Participants(email);
CREATE INDEX idx_session_date ON Sessions(session_date);
CREATE INDEX idx_group_participant ON StudyGroups(participant_id);
CREATE INDEX idx_group_session ON StudyGroups(session_id);
```
