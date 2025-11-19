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
-- Database schema for ALPS Foundation events management system

CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    event_type VARCHAR(50) NOT NULL CHECK (event_type IN ('conference', 'summer_school', 'workshop', 'seminar')),
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    location VARCHAR(255) NOT NULL,
    max_attendees INTEGER,
    registration_deadline TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (end_date >= start_date),
    CONSTRAINT valid_registration_deadline CHECK (registration_deadline <= start_date)
);

CREATE TABLE speakers (
    speaker_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    organization VARCHAR(255),
    position VARCHAR(255),
    bio TEXT,
    photo_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE event_speakers (
    event_speaker_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    speaker_id INTEGER NOT NULL REFERENCES speakers(speaker_id) ON DELETE CASCADE,
    session_title VARCHAR(255),
    session_description TEXT,
    session_time TIMESTAMP,
    duration_minutes INTEGER,
    is_keynote BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (event_id, speaker_id, session_time)
);

CREATE TABLE attendees (
    attendee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    organization VARCHAR(255),
    position VARCHAR(255),
    dietary_requirements TEXT,
    special_needs TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE registrations (
    registration_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    attendee_id INTEGER NOT NULL REFERENCES attendees(attendee_id) ON DELETE CASCADE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_status VARCHAR(50) DEFAULT 'pending' CHECK (payment_status IN ('pending', 'paid', 'cancelled', 'refunded')),
    payment_amount DECIMAL(10, 2),
    payment_date TIMESTAMP,
    ticket_type VARCHAR(100),
    notes TEXT,
    UNIQUE (event_id, attendee_id)
);

CREATE TABLE sponsors (
    sponsor_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    logo_url VARCHAR(255),
    website VARCHAR(255),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE event_sponsors (
    event_sponsor_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    sponsor_id INTEGER NOT NULL REFERENCES sponsors(sponsor_id) ON DELETE CASCADE,
    sponsorship_level VARCHAR(100),
    contribution_amount DECIMAL(10, 2),
    benefits_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (event_id, sponsor_id)
);

CREATE TABLE event_schedules (
    schedule_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    day_number INTEGER NOT NULL,
    date DATE NOT NULL,
    general_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (event_id, day_number)
);

CREATE TABLE schedule_items (
    item_id SERIAL PRIMARY KEY,
    schedule_id INTEGER NOT NULL REFERENCES event_schedules(schedule_id) ON DELETE CASCADE,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    speaker_id INTEGER REFERENCES speakers(speaker_id) ON DELETE SET NULL,
    item_type VARCHAR(50) CHECK (item_type IN ('session', 'break', 'meal', 'networking', 'workshop')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_times CHECK (end_time > start_time)
);

-- Indexes for performance optimization
CREATE INDEX idx_events_dates ON events(start_date, end_date);
CREATE INDEX idx_registrations_event ON registrations(event_id);
CREATE INDEX idx_registrations_attendee ON registrations(attendee_id);
CREATE INDEX idx_event_speakers_event ON event_speakers(event_id);
CREATE INDEX idx_event_speakers_speaker ON event_speakers(speaker_id);
CREATE INDEX idx_event_sponsors_event ON event_sponsors(event_id);
CREATE INDEX idx_event_schedules_event ON event_schedules(event_id);
CREATE INDEX idx_schedule_items_schedule ON schedule_items(schedule_id);
```
