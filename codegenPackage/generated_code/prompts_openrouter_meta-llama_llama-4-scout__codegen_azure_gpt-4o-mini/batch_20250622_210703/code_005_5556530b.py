"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Design a database schema to store information about PSHP members, events, and achievements.
Generated: DETERMINISTIC_5556530b9a6f1960
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about PSHP members, events, and achievements

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Achievements;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Members;

-- Table to store information about PSHP members
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,          -- Unique identifier for each member
    first_name VARCHAR(50) NOT NULL,      -- Member's first name
    last_name VARCHAR(50) NOT NULL,       -- Member's last name
    email VARCHAR(100) UNIQUE NOT NULL,    -- Member's email address (unique)
    phone_number VARCHAR(15),              -- Member's phone number
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the member joined
    status VARCHAR(20) DEFAULT 'active'     -- Status of the member (active/inactive)
);

-- Table to store information about events
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY,            -- Unique identifier for each event
    event_name VARCHAR(100) NOT NULL,      -- Name of the event
    event_date TIMESTAMP NOT NULL,          -- Date and time of the event
    location VARCHAR(100),                   -- Location of the event
    description TEXT,                        -- Description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the event was created
);

-- Table to store achievements related to members
CREATE TABLE Achievements (
    achievement_id SERIAL PRIMARY KEY,      -- Unique identifier for each achievement
    member_id INT NOT NULL,                 -- Foreign key referencing Members
    event_id INT NOT NULL,                  -- Foreign key referencing Events
    achievement_date TIMESTAMP NOT NULL,    -- Date the achievement was earned
    description TEXT,                        -- Description of the achievement
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE      -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_member_email ON Members(email);
CREATE INDEX idx_event_date ON Events(event_date);
CREATE INDEX idx_achievement_member ON Achievements(member_id);
CREATE INDEX idx_achievement_event ON Achievements(event_id);
```
