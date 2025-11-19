"""
Generated Code Metadata:
========================
Original URL: https://eyemagazine.gr
Prompt: Create a database schema to store information about optometry-related events, such as AthenaVision 2025 and ZEUS+DIONE boutique openings, as described on Eye Magazine.
Generated: DETERMINISTIC_26b287db63451619
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing optometry-related events

CREATE TABLE Event (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each event
    event_name VARCHAR(255) NOT NULL, -- Name of the event
    event_date DATE NOT NULL, -- Date of the event
    event_location VARCHAR(255) NOT NULL, -- Location of the event
    event_description TEXT, -- Description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the event was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

CREATE TABLE Organizer (
    organizer_id SERIAL PRIMARY KEY, -- Unique identifier for each organizer
    organizer_name VARCHAR(255) NOT NULL, -- Name of the organizer
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Contact email for the organizer
    phone_number VARCHAR(20), -- Phone number for the organizer
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the organizer was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

CREATE TABLE EventOrganizer (
    event_organizer_id SERIAL PRIMARY KEY, -- Unique identifier for the event-organizer relationship
    event_id INT NOT NULL, -- Foreign key referencing the Event table
    organizer_id INT NOT NULL, -- Foreign key referencing the Organizer table
    FOREIGN KEY (event_id) REFERENCES Event(event_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (organizer_id) REFERENCES Organizer(organizer_id) ON DELETE CASCADE, -- Ensures referential integrity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the relationship was created
);

-- Indexes for faster querying
CREATE INDEX idx_event_name ON Event(event_name);
CREATE INDEX idx_organizer_name ON Organizer(organizer_name);
```
