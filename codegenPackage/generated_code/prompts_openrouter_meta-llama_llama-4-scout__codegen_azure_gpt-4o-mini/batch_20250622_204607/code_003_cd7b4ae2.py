"""
Generated Code Metadata:
========================
Original URL: https://alps.foundation
Prompt: Design a database schema for storing information about events, conferences, and summer schools organized by ALPS Foundation, including speaker details and attendee registration.
Generated: DETERMINISTIC_cd7b4ae2ad53c6a1
Batch ID: 20250622_204607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ALPS Foundation events, conferences, and summer schools

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Attendees;
DROP TABLE IF EXISTS Speakers;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Registrations;

-- Table to store information about events, conferences, and summer schools
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each event
    event_name VARCHAR(255) NOT NULL, -- Name of the event
    event_type VARCHAR(50) NOT NULL CHECK (event_type IN ('Conference', 'Summer School', 'Workshop')), -- Type of the event
    start_date DATE NOT NULL, -- Start date of the event
    end_date DATE NOT NULL, -- End date of the event
    location VARCHAR(255), -- Location of the event
    description TEXT, -- Description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the event was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store speaker details
CREATE TABLE Speakers (
    speaker_id SERIAL PRIMARY KEY, -- Unique identifier for each speaker
    first_name VARCHAR(100) NOT NULL, -- Speaker's first name
    last_name VARCHAR(100) NOT NULL, -- Speaker's last name
    bio TEXT, -- Biography of the speaker
    email VARCHAR(255) UNIQUE NOT NULL, -- Speaker's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the speaker was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store attendee registration details
CREATE TABLE Attendees (
    attendee_id SERIAL PRIMARY KEY, -- Unique identifier for each attendee
    first_name VARCHAR(100) NOT NULL, -- Attendee's first name
    last_name VARCHAR(100) NOT NULL, -- Attendee's last name
    email VARCHAR(255) UNIQUE NOT NULL, -- Attendee's email address
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the attendee registered
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the attendee record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to link attendees to events they registered for
CREATE TABLE Registrations (
    registration_id SERIAL PRIMARY KEY, -- Unique identifier for each registration
    attendee_id INT NOT NULL, -- Foreign key referencing Attendees
    event_id INT NOT NULL, -- Foreign key referencing Events
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the registration occurred
    FOREIGN KEY (attendee_id) REFERENCES Attendees(attendee_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to link speakers to events they are speaking at
CREATE TABLE Event_Speakers (
    event_speaker_id SERIAL PRIMARY KEY, -- Unique identifier for each event-speaker link
    event_id INT NOT NULL, -- Foreign key referencing Events
    speaker_id INT NOT NULL, -- Foreign key referencing Speakers
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (speaker_id) REFERENCES Speakers(speaker_id) ON DELETE CASCADE -- Ensures referential integrity
);
```
