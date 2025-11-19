"""
Generated Code Metadata:
========================
Original URL: https://cle.com
Prompt: Design a database schema to store information about CLE conferences, including speaker names, topics, and locations, based on the data available on the CLE International website.
Generated: DETERMINISTIC_31407738e1fb82d3
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for CLE conferences

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for conference locations
CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'USA',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for conference topics/categories
CREATE TABLE topics (
    topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for speakers
CREATE TABLE speakers (
    speaker_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    bio TEXT,
    organization TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Table for conferences
CREATE TABLE conferences (
    conference_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    location_id INTEGER NOT NULL,
    max_attendees INTEGER,
    price DECIMAL(10,2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    CHECK (end_date >= start_date)
);

-- Junction table for conference topics
CREATE TABLE conference_topics (
    conference_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,
    PRIMARY KEY (conference_id, topic_id),
    FOREIGN KEY (conference_id) REFERENCES conferences(conference_id) ON DELETE CASCADE,
    FOREIGN KEY (topic_id) REFERENCES topics(topic_id) ON DELETE CASCADE
);

-- Junction table for conference speakers
CREATE TABLE conference_speakers (
    conference_id INTEGER NOT NULL,
    speaker_id INTEGER NOT NULL,
    is_keynote BOOLEAN DEFAULT FALSE,
    session_title TEXT,
    session_description TEXT,
    session_time TIMESTAMP,
    PRIMARY KEY (conference_id, speaker_id),
    FOREIGN KEY (conference_id) REFERENCES conferences(conference_id) ON DELETE CASCADE,
    FOREIGN KEY (speaker_id) REFERENCES speakers(speaker_id) ON DELETE CASCADE
);

-- Table for attendees
CREATE TABLE attendees (
    attendee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    organization TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Table for registrations
CREATE TABLE registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    conference_id INTEGER NOT NULL,
    attendee_id INTEGER NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_status TEXT CHECK(payment_status IN ('pending', 'paid', 'cancelled', 'refunded')),
    payment_amount DECIMAL(10,2),
    payment_date TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (conference_id) REFERENCES conferences(conference_id),
    FOREIGN KEY (attendee_id) REFERENCES attendees(attendee_id)
);

-- Create indexes for performance
CREATE INDEX idx_conferences_dates ON conferences(start_date, end_date);
CREATE INDEX idx_conferences_location ON conferences(location_id);
CREATE INDEX idx_speakers_name ON speakers(last_name, first_name);
CREATE INDEX idx_attendees_email ON attendees(email);
CREATE INDEX idx_registrations_conference ON registrations(conference_id);
CREATE INDEX idx_registrations_attendee ON registrations(attendee_id);

-- Trigger to update timestamp on row update
CREATE TRIGGER update_locations_timestamp
AFTER UPDATE ON locations
FOR EACH ROW
BEGIN
    UPDATE locations SET updated_at = CURRENT_TIMESTAMP WHERE location_id = OLD.location_id;
END;

CREATE TRIGGER update_topics_timestamp
AFTER UPDATE ON topics
FOR EACH ROW
BEGIN
    UPDATE topics SET updated_at = CURRENT_TIMESTAMP WHERE topic_id = OLD.topic_id;
END;

CREATE TRIGGER update_speakers_timestamp
AFTER UPDATE ON speakers
FOR EACH ROW
BEGIN
    UPDATE speakers SET updated_at = CURRENT_TIMESTAMP WHERE speaker_id = OLD.speaker_id;
END;

CREATE TRIGGER update_conferences_timestamp
AFTER UPDATE ON conferences
FOR EACH ROW
BEGIN
    UPDATE conferences SET updated_at = CURRENT_TIMESTAMP WHERE conference_id = OLD.conference_id;
END;

CREATE TRIGGER update_attendees_timestamp
AFTER UPDATE ON attendees
FOR EACH ROW
BEGIN
    UPDATE attendees SET updated_at = CURRENT_TIMESTAMP WHERE attendee_id = OLD.attendee_id;
END;
```
