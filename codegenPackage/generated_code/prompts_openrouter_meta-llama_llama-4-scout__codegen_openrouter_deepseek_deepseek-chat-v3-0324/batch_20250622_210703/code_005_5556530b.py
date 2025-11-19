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
-- Database schema for PSHP (Professional Society of Healthcare Professionals)
-- Tables: members, events, achievements, member_achievements, event_attendees

-- Members table stores information about society members
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    membership_type VARCHAR(20) NOT NULL CHECK (membership_type IN ('Regular', 'Student', 'Lifetime', 'Honorary')),
    specialty VARCHAR(50),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    bio TEXT,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Events table stores information about society events
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    description TEXT,
    event_date TIMESTAMP NOT NULL,
    location VARCHAR(100) NOT NULL,
    max_attendees INTEGER CHECK (max_attendees > 0),
    registration_deadline TIMESTAMP,
    is_cancelled BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Achievements table stores types of achievements members can earn
CREATE TABLE achievements (
    achievement_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    criteria TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for member achievements
CREATE TABLE member_achievements (
    member_achievement_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    achievement_id INTEGER NOT NULL REFERENCES achievements(achievement_id) ON DELETE CASCADE,
    date_awarded DATE NOT NULL DEFAULT CURRENT_DATE,
    awarded_by VARCHAR(100),
    notes TEXT,
    UNIQUE (member_id, achievement_id)
);

-- Junction table for event attendees
CREATE TABLE event_attendees (
    attendee_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    attended BOOLEAN DEFAULT FALSE,
    feedback TEXT,
    UNIQUE (event_id, member_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_members_email ON members(email);
CREATE INDEX idx_members_membership_type ON members(membership_type);
CREATE INDEX idx_events_date ON events(event_date);
CREATE INDEX idx_member_achievements_member ON member_achievements(member_id);
CREATE INDEX idx_member_achievements_achievement ON member_achievements(achievement_id);
CREATE INDEX idx_event_attendees_event ON event_attendees(event_id);
CREATE INDEX idx_event_attendees_member ON event_attendees(member_id);
```
