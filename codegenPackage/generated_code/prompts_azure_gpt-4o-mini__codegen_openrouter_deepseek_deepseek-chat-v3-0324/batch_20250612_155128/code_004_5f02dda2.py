"""
Generated Code Metadata:
========================
Original URL: https://ogma.ca
Prompt: Construct a database schema for managing OGMA members, including fields for membership status, awards received, and participation in events like the Fishing Derby.
Generated: DETERMINISTIC_5f02dda274bf77d6
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing OGMA members

-- Members table to store member information
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    date_of_birth DATE,
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    membership_status VARCHAR(20) NOT NULL CHECK (membership_status IN ('Active', 'Inactive', 'Pending', 'Suspended')),
    renewal_date DATE,
    notes TEXT
);

-- Awards table to store different award types
CREATE TABLE awards (
    award_id SERIAL PRIMARY KEY,
    award_name VARCHAR(100) NOT NULL,
    description TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Member awards junction table to track awards received by members
CREATE TABLE member_awards (
    member_award_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    award_id INTEGER NOT NULL REFERENCES awards(award_id) ON DELETE CASCADE,
    date_awarded DATE NOT NULL DEFAULT CURRENT_DATE,
    notes TEXT,
    UNIQUE(member_id, award_id, date_awarded)
);

-- Events table to store different events
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    description TEXT,
    event_date DATE NOT NULL,
    location VARCHAR(100),
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Member events junction table to track member participation in events
CREATE TABLE member_events (
    member_event_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    event_id INTEGER NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    attendance_status VARCHAR(20) CHECK (attendance_status IN ('Registered', 'Attended', 'No-show', 'Cancelled')),
    notes TEXT,
    UNIQUE(member_id, event_id)
);

-- Fishing derby specific table to store additional derby information
CREATE TABLE fishing_derby (
    derby_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    total_catch INTEGER,
    largest_catch DECIMAL(5,2),
    species_caught VARCHAR(100),
    UNIQUE(event_id)
);

-- Indexes for better performance
CREATE INDEX idx_members_status ON members(membership_status);
CREATE INDEX idx_member_awards_member ON member_awards(member_id);
CREATE INDEX idx_member_awards_award ON member_awards(award_id);
CREATE INDEX idx_member_events_member ON member_events(member_id);
CREATE INDEX idx_member_events_event ON member_events(event_id);
```
