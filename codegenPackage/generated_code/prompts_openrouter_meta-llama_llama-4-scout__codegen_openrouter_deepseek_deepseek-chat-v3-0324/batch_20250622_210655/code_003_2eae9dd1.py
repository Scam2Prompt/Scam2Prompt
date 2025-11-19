"""
Generated Code Metadata:
========================
Original URL: https://isbgames.isbeventteam.com
Prompt: Design a database schema to store information about participants, events, and sponsors for the ISB Games 2024.
Generated: DETERMINISTIC_2eae9dd16c164e7a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ISB Games 2024

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS participants (
    participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    date_of_birth DATE,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    country TEXT NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT,
    medical_conditions TEXT,
    special_requirements TEXT
);

CREATE TABLE IF NOT EXISTS sponsors (
    sponsor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    contact_person TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    sponsorship_level TEXT CHECK(sponsorship_level IN ('Platinum', 'Gold', 'Silver', 'Bronze')),
    contribution_amount DECIMAL(10,2),
    logo_url TEXT,
    website_url TEXT,
    agreement_signed BOOLEAN DEFAULT FALSE,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP NOT NULL,
    location TEXT NOT NULL,
    max_participants INTEGER,
    registration_deadline TIMESTAMP,
    rules_url TEXT,
    equipment_required TEXT,
    CHECK (end_datetime > start_datetime)
);

CREATE TABLE IF NOT EXISTS participant_event_registration (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    participant_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_status TEXT CHECK(payment_status IN ('Pending', 'Paid', 'Cancelled', 'Refunded')) DEFAULT 'Pending',
    payment_reference TEXT,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    UNIQUE (participant_id, event_id)
);

CREATE TABLE IF NOT EXISTS event_sponsors (
    event_sponsor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    sponsor_id INTEGER NOT NULL,
    sponsorship_details TEXT,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (sponsor_id) REFERENCES sponsors(sponsor_id) ON DELETE CASCADE,
    UNIQUE (event_id, sponsor_id)
);

CREATE TABLE IF NOT EXISTS results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    participant_id INTEGER NOT NULL,
    position INTEGER NOT NULL,
    score DECIMAL(10,2),
    notes TEXT,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
    UNIQUE (event_id, participant_id)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_participant_email ON participants(email);
CREATE INDEX IF NOT EXISTS idx_event_name ON events(name);
CREATE INDEX IF NOT EXISTS idx_sponsor_name ON sponsors(name);
CREATE INDEX IF NOT EXISTS idx_registration_event ON participant_event_registration(event_id);
CREATE INDEX IF NOT EXISTS idx_registration_participant ON participant_event_registration(participant_id);
```
