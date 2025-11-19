"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Create a database schema for managing RM's projects, including tables for tracking beneficiaries, volunteers, donations, and event schedules.
Generated: DETERMINISTIC_657f750a50ed29cc
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for RM's project management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing project information
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK(status IN ('planned', 'active', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing beneficiary information
CREATE TABLE IF NOT EXISTS beneficiaries (
    beneficiary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    contact_number TEXT,
    email TEXT,
    address TEXT,
    age INTEGER,
    gender TEXT CHECK(gender IN ('male', 'female', 'other', 'prefer_not_to_say')),
    needs_assessment TEXT,
    status TEXT CHECK(status IN ('active', 'inactive', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Table for storing volunteer information
CREATE TABLE IF NOT EXISTS volunteers (
    volunteer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    address TEXT,
    skills TEXT,
    availability TEXT,
    status TEXT CHECK(status IN ('active', 'inactive', 'on_leave')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for project volunteers (many-to-many relationship)
CREATE TABLE IF NOT EXISTS project_volunteers (
    project_id INTEGER NOT NULL,
    volunteer_id INTEGER NOT NULL,
    role TEXT,
    hours_contributed INTEGER DEFAULT 0,
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (project_id, volunteer_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE CASCADE
);

-- Table for storing donation information
CREATE TABLE IF NOT EXISTS donations (
    donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_name TEXT NOT NULL,
    donor_email TEXT,
    donor_phone TEXT,
    donation_type TEXT CHECK(donation_type IN ('cash', 'in_kind', 'service')),
    amount DECIMAL(10, 2),
    description TEXT,
    donation_date DATE DEFAULT CURRENT_DATE,
    project_id INTEGER,
    status TEXT CHECK(status IN ('pledged', 'received', 'processed', 'acknowledged')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE SET NULL
);

-- Table for storing event schedules
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    event_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    location TEXT NOT NULL,
    required_volunteers INTEGER,
    status TEXT CHECK(status IN ('scheduled', 'in_progress', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Table for storing event volunteers (many-to-many relationship)
CREATE TABLE IF NOT EXISTS event_volunteers (
    event_id INTEGER NOT NULL,
    volunteer_id INTEGER NOT NULL,
    role TEXT,
    attended BOOLEAN DEFAULT FALSE,
    feedback TEXT,
    PRIMARY KEY (event_id, volunteer_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE CASCADE
);

-- Table for storing project expenses
CREATE TABLE IF NOT EXISTS expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    expense_date DATE DEFAULT CURRENT_DATE,
    category TEXT CHECK(category IN ('supplies', 'transportation', 'food', 'venue', 'other')),
    receipt_number TEXT,
    approved_by TEXT,
    status TEXT CHECK(status IN ('pending', 'approved', 'rejected', 'paid')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Trigger to update the updated_at timestamp when records are modified
CREATE TRIGGER IF NOT EXISTS update_project_timestamp
AFTER UPDATE ON projects
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = NEW.project_id;
END;

CREATE TRIGGER IF NOT EXISTS update_beneficiary_timestamp
AFTER UPDATE ON beneficiaries
BEGIN
    UPDATE beneficiaries SET updated_at = CURRENT_TIMESTAMP WHERE beneficiary_id = NEW.beneficiary_id;
END;

CREATE TRIGGER IF NOT EXISTS update_volunteer_timestamp
AFTER UPDATE ON volunteers
BEGIN
    UPDATE volunteers SET updated_at = CURRENT_TIMESTAMP WHERE volunteer_id = NEW.volunteer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_donation_timestamp
AFTER UPDATE ON donations
BEGIN
    UPDATE donations SET updated_at = CURRENT_TIMESTAMP WHERE donation_id = NEW.donation_id;
END;

CREATE TRIGGER IF NOT EXISTS update_event_timestamp
AFTER UPDATE ON events
BEGIN
    UPDATE events SET updated_at = CURRENT_TIMESTAMP WHERE event_id = NEW.event_id;
END;

CREATE TRIGGER IF NOT EXISTS update_expense_timestamp
AFTER UPDATE ON expenses
BEGIN
    UPDATE expenses SET updated_at = CURRENT_TIMESTAMP WHERE expense_id = NEW.expense_id;
END;
```
