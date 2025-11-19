"""
Generated Code Metadata:
========================
Original URL: https://eyemagazine.gr
Prompt: Design a database schema to store information about eye care events, such as the Intl. EYEDEA Forum, including details about speakers, attendees, and presentations.
Generated: DETERMINISTIC_9b4fbf3ba6238cb8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for eye care events management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store event information
CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    location TEXT NOT NULL,
    organizer TEXT,
    website_url TEXT,
    registration_deadline DATE,
    max_attendees INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date >= start_date),
    CHECK (registration_deadline <= start_date)
);

-- Table to store speaker information
CREATE TABLE speakers (
    speaker_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    organization TEXT,
    position TEXT,
    bio TEXT,
    photo_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Table to store presentation information
CREATE TABLE presentations (
    presentation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    room TEXT,
    max_attendees INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    CHECK (end_time > start_time)
);

-- Junction table for speakers and presentations (many-to-many)
CREATE TABLE presentation_speakers (
    presentation_id INTEGER NOT NULL,
    speaker_id INTEGER NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (presentation_id, speaker_id),
    FOREIGN KEY (presentation_id) REFERENCES presentations(presentation_id) ON DELETE CASCADE,
    FOREIGN KEY (speaker_id) REFERENCES speakers(speaker_id) ON DELETE CASCADE
);

-- Table to store attendee information
CREATE TABLE attendees (
    attendee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    organization TEXT,
    position TEXT,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dietary_restrictions TEXT,
    special_needs TEXT,
    CHECK (email LIKE '%@%.%')
);

-- Table to store attendee registrations for events
CREATE TABLE event_registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    attendee_id INTEGER NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_status TEXT DEFAULT 'pending',
    payment_amount DECIMAL(10,2),
    payment_date TIMESTAMP,
    ticket_type TEXT,
    UNIQUE (event_id, attendee_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (attendee_id) REFERENCES attendees(attendee_id) ON DELETE CASCADE
);

-- Table to store attendee attendance at presentations
CREATE TABLE presentation_attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    presentation_id INTEGER NOT NULL,
    attendee_id INTEGER NOT NULL,
    check_in_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    feedback TEXT,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    UNIQUE (presentation_id, attendee_id),
    FOREIGN KEY (presentation_id) REFERENCES presentations(presentation_id) ON DELETE CASCADE,
    FOREIGN KEY (attendee_id) REFERENCES attendees(attendee_id) ON DELETE CASCADE
);

-- Table to store event sponsors
CREATE TABLE sponsors (
    sponsor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    website_url TEXT,
    logo_url TEXT,
    contact_name TEXT,
    contact_email TEXT,
    contact_phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (contact_email LIKE '%@%.%')
);

-- Junction table for events and sponsors (many-to-many)
CREATE TABLE event_sponsors (
    event_id INTEGER NOT NULL,
    sponsor_id INTEGER NOT NULL,
    sponsorship_level TEXT,
    contribution_amount DECIMAL(10,2),
    PRIMARY KEY (event_id, sponsor_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (sponsor_id) REFERENCES sponsors(sponsor_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_presentations_event ON presentations(event_id);
CREATE INDEX idx_presentation_speakers_speaker ON presentation_speakers(speaker_id);
CREATE INDEX idx_event_registrations_event ON event_registrations(event_id);
CREATE INDEX idx_event_registrations_attendee ON event_registrations(attendee_id);
CREATE INDEX idx_presentation_attendance_presentation ON presentation_attendance(presentation_id);
CREATE INDEX idx_presentation_attendance_attendee ON presentation_attendance(attendee_id);
CREATE INDEX idx_event_sponsors_event ON event_sponsors(event_id);
CREATE INDEX idx_event_sponsors_sponsor ON event_sponsors(sponsor_id);

-- Triggers to update timestamps
CREATE TRIGGER update_event_timestamp
AFTER UPDATE ON events
FOR EACH ROW
BEGIN
    UPDATE events SET updated_at = CURRENT_TIMESTAMP WHERE event_id = OLD.event_id;
END;

CREATE TRIGGER update_speaker_timestamp
AFTER UPDATE ON speakers
FOR EACH ROW
BEGIN
    UPDATE speakers SET updated_at = CURRENT_TIMESTAMP WHERE speaker_id = OLD.speaker_id;
END;

CREATE TRIGGER update_presentation_timestamp
AFTER UPDATE ON presentations
FOR EACH ROW
BEGIN
    UPDATE presentations SET updated_at = CURRENT_TIMESTAMP WHERE presentation_id = OLD.presentation_id;
END;

CREATE TRIGGER update_sponsor_timestamp
AFTER UPDATE ON sponsors
FOR EACH ROW
BEGIN
    UPDATE sponsors SET updated_at = CURRENT_TIMESTAMP WHERE sponsor_id = OLD.sponsor_id;
END;
```
