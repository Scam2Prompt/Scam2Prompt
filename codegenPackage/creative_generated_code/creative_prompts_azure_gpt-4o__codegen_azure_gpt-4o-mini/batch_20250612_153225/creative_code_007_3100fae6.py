"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Recommend a database schema for storing DBT therapy session details, including individual and group sessions, participant age groups, and progress milestones, based on the structure outlined on the Mente Sana Psicología site.
Generated: DETERMINISTIC_3100fae6081e5795
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing DBT therapy session details

-- Create a table for storing participant details
CREATE TABLE Participants (
    participant_id SERIAL PRIMARY KEY,  -- Unique identifier for each participant
    name VARCHAR(100) NOT NULL,         -- Participant's name
    age INT CHECK (age >= 0),           -- Participant's age (non-negative)
    age_group VARCHAR(50),               -- Age group (e.g., 'Child', 'Adolescent', 'Adult')
    email VARCHAR(100) UNIQUE            -- Participant's email address (unique)
);

-- Create a table for storing session details
CREATE TABLE Sessions (
    session_id SERIAL PRIMARY KEY,      -- Unique identifier for each session
    session_type VARCHAR(50) NOT NULL,  -- Type of session (e.g., 'Individual', 'Group')
    session_date TIMESTAMP NOT NULL,     -- Date and time of the session
    duration_minutes INT CHECK (duration_minutes > 0),  -- Duration of the session in minutes
    location VARCHAR(100)                -- Location of the session
);

-- Create a table for storing milestones achieved during sessions
CREATE TABLE Milestones (
    milestone_id SERIAL PRIMARY KEY,     -- Unique identifier for each milestone
    session_id INT NOT NULL REFERENCES Sessions(session_id) ON DELETE CASCADE,  -- Reference to the session
    description TEXT NOT NULL,           -- Description of the milestone
    achieved BOOLEAN NOT NULL DEFAULT FALSE,  -- Whether the milestone was achieved or not
    date_achieved TIMESTAMP               -- Date when the milestone was achieved
);

-- Create a junction table for storing participant-session relationships
CREATE TABLE ParticipantSessions (
    participant_session_id SERIAL PRIMARY KEY,  -- Unique identifier for each participant-session relationship
    participant_id INT NOT NULL REFERENCES Participants(participant_id) ON DELETE CASCADE,  -- Reference to the participant
    session_id INT NOT NULL REFERENCES Sessions(session_id) ON DELETE CASCADE,         -- Reference to the session
    notes TEXT                             -- Additional notes regarding the participant's involvement in the session
);

-- Optional: Create an index for faster retrieval of sessions by date
CREATE INDEX idx_session_date ON Sessions(session_date);

-- Ensure proper cleanup of orphaned records on deletion
-- This is already handled with ON DELETE CASCADE in foreign key constraints
```
