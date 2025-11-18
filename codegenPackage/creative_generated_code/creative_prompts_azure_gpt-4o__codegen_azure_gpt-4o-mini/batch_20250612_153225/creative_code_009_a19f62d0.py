"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmindsinstituto.com.br
Prompt: Create a database schema for storing participant information and session details for study groups focused on respiratory disorders and neonatal dysphagia, as described on Open Minds Instituto's website.
Generated: DETERMINISTIC_a19f62d085bd4859
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing participant information and session details
-- for study groups focused on respiratory disorders and neonatal dysphagia.

CREATE DATABASE IF NOT EXISTS StudyGroupsDB;
USE StudyGroupsDB;

-- Table to store participant information
CREATE TABLE IF NOT EXISTS Participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    contact_number VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about each study session
CREATE TABLE IF NOT EXISTS Sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    session_date DATETIME NOT NULL,
    location VARCHAR(255) NOT NULL,
    topic VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store the relationship between participants and sessions
CREATE TABLE IF NOT EXISTS ParticipantSessions (
    participant_session_id INT AUTO_INCREMENT PRIMARY KEY,
    participant_id INT NOT NULL,
    session_id INT NOT NULL,
    attendance_status ENUM('Attended', 'Missed', 'Cancelled') NOT NULL DEFAULT 'Attended',
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id)
        ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES Sessions(session_id)
        ON DELETE CASCADE
);

-- Indexes to improve query performance
CREATE INDEX idx_participant_email ON Participants(email);
CREATE INDEX idx_session_date ON Sessions(session_date);
CREATE INDEX idx_participant_session ON ParticipantSessions(participant_id, session_id);
```
