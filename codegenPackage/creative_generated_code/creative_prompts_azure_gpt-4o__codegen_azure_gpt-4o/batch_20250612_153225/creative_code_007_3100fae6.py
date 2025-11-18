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
-- Database schema for storing DBT (Dialectical Behavior Therapy) session details

-- Table to store participant details
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each participant
    FirstName VARCHAR(50) NOT NULL,                -- First name of the participant
    LastName VARCHAR(50) NOT NULL,                 -- Last name of the participant
    AgeGroup ENUM('Child', 'Teen', 'Adult', 'Senior') NOT NULL, -- Age group category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of record creation
);

-- Table to store session details (individual and group sessions)
CREATE TABLE Sessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each session
    SessionType ENUM('Individual', 'Group') NOT NULL, -- Type of session
    SessionDate DATE NOT NULL,                     -- Date of the session
    DurationInMinutes INT NOT NULL,               -- Duration of the session in minutes
    TherapistName VARCHAR(100) NOT NULL,          -- Name of the therapist conducting the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table to log attendance of participants in sessions
CREATE TABLE SessionParticipants (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for attendance record
    SessionID INT NOT NULL,                        -- Foreign key referencing Sessions table
    ParticipantID INT NOT NULL,                    -- Foreign key referencing Participants table
    AttendanceStatus ENUM('Present', 'Absent') NOT NULL, -- Status of attendance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store progress milestones for participants
CREATE TABLE Milestones (
    MilestoneID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each milestone
    ParticipantID INT NOT NULL,                    -- Foreign key referencing Participants table
    MilestoneDescription TEXT NOT NULL,            -- Description of the milestone achieved
    AchievedDate DATE NOT NULL,                    -- Date the milestone was achieved
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store therapist details (optional, for tracking therapists separately)
CREATE TABLE Therapists (
    TherapistID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each therapist
    FirstName VARCHAR(50) NOT NULL,                -- First name of the therapist
    LastName VARCHAR(50) NOT NULL,                 -- Last name of the therapist
    Specialization VARCHAR(100),                   -- Area of specialization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of record creation
);

-- Error handling for foreign key violations and cascading deletes is ensured with ON DELETE CASCADE.
-- Ensure proper indexing for foreign keys to optimize query performance.
```
