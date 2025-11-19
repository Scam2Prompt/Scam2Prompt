"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Design a database schema for managing the events and volunteers associated with Springs International Ministries' programs.
Generated: DETERMINISTIC_45256a5559149105
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating a database schema for Springs International Ministries

-- Drop existing tables if they exist to prevent conflicts
DROP TABLE IF EXISTS Volunteers;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Event_Volunteers;

-- Table to store volunteers' information
CREATE TABLE Volunteers (
    volunteer_id SERIAL PRIMARY KEY,  -- Unique identifier for each volunteer
    first_name VARCHAR(100) NOT NULL, -- Volunteer first name
    last_name VARCHAR(100) NOT NULL,  -- Volunteer last name
    email VARCHAR(255) UNIQUE NOT NULL, -- Volunteer email address, must be unique
    phone VARCHAR(15),                 -- Optional phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    CONSTRAINT chk_email CHECK (email LIKE '%_@__%.__%') -- Basic email format validation
);

-- Table to store events information
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY,       -- Unique identifier for each event
    event_name VARCHAR(255) NOT NULL, -- Name of the event
    event_date TIMESTAMP NOT NULL,     -- Date and time of the event
    location VARCHAR(255),             -- Location of the event
    description TEXT,                  -- Detailed description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Junction table to associate volunteers with events
CREATE TABLE Event_Volunteers (
    event_volunteer_id SERIAL PRIMARY KEY, -- Unique identifier for each event-volunteer association
    event_id INT NOT NULL,                  -- Foreign key referencing Events
    volunteer_id INT NOT NULL,              -- Foreign key referencing Volunteers
    role VARCHAR(100),                      -- Role of the volunteer in the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (volunteer_id) REFERENCES Volunteers(volunteer_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_event_name ON Events(event_name);
CREATE INDEX idx_volunteer_email ON Volunteers(email);
CREATE INDEX idx_event_date ON Events(event_date);
```
