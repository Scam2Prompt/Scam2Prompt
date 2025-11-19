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
-- Create a database for ALPS Foundation events
CREATE DATABASE alps_foundation;

-- Use the alps_foundation database
USE alps_foundation;

-- Create a table for events
CREATE TABLE events (
    event_id INT AUTO_INCREMENT,
    event_type ENUM('conference', 'summer_school', 'other') NOT NULL,
    event_name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    location VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (event_id)
);

-- Create a table for speakers
CREATE TABLE speakers (
    speaker_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (speaker_id)
);

-- Create a table for event speakers
CREATE TABLE event_speakers (
    event_id INT NOT NULL,
    speaker_id INT NOT NULL,
    role ENUM('main_speaker', 'guest_speaker', 'panelist') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (event_id, speaker_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (speaker_id) REFERENCES speakers(speaker_id) ON DELETE CASCADE
);

-- Create a table for attendees
CREATE TABLE attendees (
    attendee_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (attendee_id)
);

-- Create a table for event registrations
CREATE TABLE event_registrations (
    event_id INT NOT NULL,
    attendee_id INT NOT NULL,
    registration_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (event_id, attendee_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (attendee_id) REFERENCES attendees(attendee_id) ON DELETE CASCADE
);

-- Create a table for event organizers
CREATE TABLE event_organizers (
    event_id INT NOT NULL,
    organizer_id INT NOT NULL,
    role ENUM('lead_organizer', 'co_organizer') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (event_id, organizer_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (organizer_id) REFERENCES attendees(attendee_id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO events (event_type, event_name, start_date, end_date, location, description)
VALUES 
('conference', 'ALPS Conference 2024', '2024-06-01', '2024-06-03', 'New York', 'Annual conference for ALPS Foundation');

INSERT INTO speakers (first_name, last_name, email, bio)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'Expert in AI and Machine Learning');

INSERT INTO event_speakers (event_id, speaker_id, role)
VALUES 
(1, 1, 'main_speaker');

INSERT INTO attendees (first_name, last_name, email)
VALUES 
('Jane', 'Doe', 'jane.doe@example.com');

INSERT INTO event_registrations (event_id, attendee_id, registration_date)
VALUES 
(1, 1, '2024-04-01');

INSERT INTO event_organizers (event_id, organizer_id, role)
VALUES 
(1, 1, 'lead_organizer');
```
