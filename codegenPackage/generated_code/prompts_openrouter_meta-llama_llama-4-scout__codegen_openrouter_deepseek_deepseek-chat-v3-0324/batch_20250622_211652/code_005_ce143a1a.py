"""
Generated Code Metadata:
========================
Original URL: https://cimedweb.org
Prompt: "Develop a data model for storing information about educational events, such as CIMEd's jornadas and simposios, and provide a SQL code snippet for creating the database schema."
Generated: DETERMINISTIC_ce143a1a0ac9c54a
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL schema for educational events management system
-- Supports storing information about conferences, jornadas, simposios, and related entities

CREATE TABLE event_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_event_type_name UNIQUE (name)
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    event_type_id INTEGER NOT NULL REFERENCES event_types(id),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    end_date TIMESTAMP WITH TIME ZONE NOT NULL,
    location VARCHAR(200) NOT NULL,
    organizer VARCHAR(200) NOT NULL,
    website_url VARCHAR(255),
    registration_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (end_date >= start_date)
);

CREATE TABLE speakers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    bio TEXT,
    organization VARCHAR(200),
    photo_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    room VARCHAR(100),
    max_attendees INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_session_times CHECK (end_time >= start_time)
);

CREATE TABLE session_speakers (
    session_id INTEGER NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    speaker_id INTEGER NOT NULL REFERENCES speakers(id) ON DELETE CASCADE,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (session_id, speaker_id)
);

CREATE TABLE attendees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    organization VARCHAR(200),
    profession VARCHAR(200),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE registrations (
    id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(id) ON DELETE CASCADE,
    attendee_id INTEGER NOT NULL REFERENCES attendees(id) ON DELETE CASCADE,
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    payment_status VARCHAR(50) DEFAULT 'pending',
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_event_attendee UNIQUE (event_id, attendee_id)
);

CREATE TABLE session_attendances (
    registration_id INTEGER NOT NULL REFERENCES registrations(id) ON DELETE CASCADE,
    session_id INTEGER NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    attended BOOLEAN DEFAULT FALSE,
    feedback TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (registration_id, session_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_events_event_type ON events(event_type_id);
CREATE INDEX idx_sessions_event ON sessions(event_id);
CREATE INDEX idx_session_speakers_session ON session_speakers(session_id);
CREATE INDEX idx_session_speakers_speaker ON session_speakers(speaker_id);
CREATE INDEX idx_registrations_event ON registrations(event_id);
CREATE INDEX idx_registrations_attendee ON registrations(attendee_id);
CREATE INDEX idx_session_attendances_registration ON session_attendances(registration_id);
CREATE INDEX idx_session_attendances_session ON session_attendances(session_id);

-- Trigger to update updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_event_types_timestamp
BEFORE UPDATE ON event_types
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_events_timestamp
BEFORE UPDATE ON events
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_speakers_timestamp
BEFORE UPDATE ON speakers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_sessions_timestamp
BEFORE UPDATE ON sessions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_attendees_timestamp
BEFORE UPDATE ON attendees
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_registrations_timestamp
BEFORE UPDATE ON registrations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_session_attendances_timestamp
BEFORE UPDATE ON session_attendances
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
