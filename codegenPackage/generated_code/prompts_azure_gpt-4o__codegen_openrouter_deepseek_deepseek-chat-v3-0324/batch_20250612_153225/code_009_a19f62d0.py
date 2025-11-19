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
-- Database schema for Open Minds Instituto study groups
-- Tables for participant information and session details

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing study group types
CREATE TABLE IF NOT EXISTS study_group_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE, -- e.g., "Respiratory Disorders", "Neonatal Dysphagia"
    description TEXT
);

-- Table for storing participant information
CREATE TABLE IF NOT EXISTS participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    profession TEXT,
    institution TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    special_notes TEXT,
    CHECK (email LIKE '%@%.%')
);

-- Table for storing session information
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_type_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    location TEXT,
    max_participants INTEGER,
    is_active BOOLEAN DEFAULT 1,
    FOREIGN KEY (group_type_id) REFERENCES study_group_types(id),
    CHECK (end_datetime > start_datetime)
);

-- Junction table for participant-session many-to-many relationship
CREATE TABLE IF NOT EXISTS participant_sessions (
    participant_id INTEGER NOT NULL,
    session_id INTEGER NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    attendance_status TEXT CHECK(attendance_status IN ('registered', 'attended', 'cancelled')),
    PRIMARY KEY (participant_id, session_id),
    FOREIGN KEY (participant_id) REFERENCES participants(id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE
);

-- Table for storing session materials
CREATE TABLE IF NOT EXISTS session_materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    file_path TEXT NOT NULL,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE
);

-- Table for storing session feedback
CREATE TABLE IF NOT EXISTS session_feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    participant_id INTEGER NOT NULL,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    submission_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE,
    FOREIGN KEY (participant_id) REFERENCES participants(id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_participants_email ON participants(email);
CREATE INDEX IF NOT EXISTS idx_sessions_group_type ON sessions(group_type_id);
CREATE INDEX IF NOT EXISTS idx_sessions_datetime ON sessions(start_datetime, end_datetime);
CREATE INDEX IF NOT EXISTS idx_participant_sessions ON participant_sessions(participant_id, session_id);
```
