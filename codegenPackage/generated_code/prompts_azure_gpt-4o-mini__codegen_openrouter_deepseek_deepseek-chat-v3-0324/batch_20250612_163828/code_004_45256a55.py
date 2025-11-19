"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Design a database schema for managing the events and volunteers associated with Springs International Ministries' programs.
Generated: DETERMINISTIC_45256a5559149105
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Springs International Ministries' events and volunteers management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS volunteers (
    volunteer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    address TEXT,
    skills TEXT,
    availability TEXT,
    join_date DATE DEFAULT CURRENT_DATE,
    status TEXT CHECK(status IN ('active', 'inactive', 'on_hold')) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    location TEXT NOT NULL,
    required_volunteers INTEGER,
    status TEXT CHECK(status IN ('planned', 'ongoing', 'completed', 'cancelled')) DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_datetime > start_datetime)
);

CREATE TABLE IF NOT EXISTS volunteer_event_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    volunteer_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    role TEXT,
    hours_worked REAL,
    notes TEXT,
    status TEXT CHECK(status IN ('scheduled', 'confirmed', 'completed', 'no_show', 'cancelled')) DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    UNIQUE (volunteer_id, event_id)
);

CREATE TABLE IF NOT EXISTS event_requirements (
    requirement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    requirement_type TEXT NOT NULL,
    description TEXT,
    quantity INTEGER,
    fulfilled INTEGER DEFAULT 0,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_volunteer_timestamp
AFTER UPDATE ON volunteers
FOR EACH ROW
BEGIN
    UPDATE volunteers SET updated_at = CURRENT_TIMESTAMP WHERE volunteer_id = OLD.volunteer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_event_timestamp
AFTER UPDATE ON events
FOR EACH ROW
BEGIN
    UPDATE events SET updated_at = CURRENT_TIMESTAMP WHERE event_id = OLD.event_id;
END;

CREATE TRIGGER IF NOT EXISTS update_assignment_timestamp
AFTER UPDATE ON volunteer_event_assignments
FOR EACH ROW
BEGIN
    UPDATE volunteer_event_assignments SET updated_at = CURRENT_TIMESTAMP WHERE assignment_id = OLD.assignment_id;
END;

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_volunteer_email ON volunteers(email);
CREATE INDEX IF NOT EXISTS idx_event_dates ON events(start_datetime, end_datetime);
CREATE INDEX IF NOT EXISTS idx_assignment_volunteer ON volunteer_event_assignments(volunteer_id);
CREATE INDEX IF NOT EXISTS idx_assignment_event ON volunteer_event_assignments(event_id);
CREATE INDEX IF NOT EXISTS idx_requirements_event ON event_requirements(event_id);
```
