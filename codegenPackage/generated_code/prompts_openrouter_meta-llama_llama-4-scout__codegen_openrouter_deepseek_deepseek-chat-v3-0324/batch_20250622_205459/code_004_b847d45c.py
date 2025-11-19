"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Design a database schema to store information about donors, volunteers, and programs for an organization like the NICER Foundation, including fields for tracking engagement and impact.
Generated: DETERMINISTIC_b847d45c4338ca27
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for NICER Foundation management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store donor information
CREATE TABLE donors (
    donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%_@__%.__%'),
    phone TEXT CHECK(phone GLOB '[0-9]*'),
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    country TEXT DEFAULT 'USA',
    donation_frequency TEXT CHECK(donation_frequency IN ('One-time', 'Monthly', 'Quarterly', 'Annual')),
    total_donations REAL DEFAULT 0.0,
    first_donation_date DATE,
    last_donation_date DATE,
    is_anonymous BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store volunteer information
CREATE TABLE volunteers (
    volunteer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%_@__%.__%'),
    phone TEXT CHECK(phone GLOB '[0-9]*'),
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    skills TEXT,
    availability TEXT,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT CHECK(emergency_contact_phone GLOB '[0-9]*'),
    background_check_status TEXT CHECK(background_check_status IN ('Pending', 'Approved', 'Rejected', 'Not Required')),
    total_hours_volunteered REAL DEFAULT 0.0,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store program information
CREATE TABLE programs (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    start_date DATE,
    end_date DATE,
    target_audience TEXT,
    program_manager TEXT,
    budget REAL,
    status TEXT CHECK(status IN ('Planning', 'Active', 'Completed', 'On Hold')),
    impact_metrics TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to track donations
CREATE TABLE donations (
    donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_id INTEGER NOT NULL,
    amount REAL NOT NULL CHECK(amount > 0),
    donation_date DATE NOT NULL DEFAULT CURRENT_DATE,
    payment_method TEXT CHECK(payment_method IN ('Credit Card', 'Bank Transfer', 'Check', 'Cash', 'Other')),
    is_recurring BOOLEAN DEFAULT FALSE,
    recurring_frequency TEXT,
    designation TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE CASCADE
);

-- Table to track volunteer hours
CREATE TABLE volunteer_hours (
    hours_id INTEGER PRIMARY KEY AUTOINCREMENT,
    volunteer_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    hours_worked REAL NOT NULL CHECK(hours_worked > 0),
    date_worked DATE NOT NULL DEFAULT CURRENT_DATE,
    tasks_performed TEXT,
    supervisor TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
);

-- Table to track program participation
CREATE TABLE program_participation (
    participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_id INTEGER NOT NULL,
    participant_type TEXT CHECK(participant_type IN ('Donor', 'Volunteer', 'Beneficiary')),
    participant_id INTEGER NOT NULL,
    role TEXT,
    start_date DATE,
    end_date DATE,
    impact_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
);

-- Table to track engagement events
CREATE TABLE engagement_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    event_type TEXT CHECK(event_type IN ('Fundraiser', 'Volunteer Training', 'Community Outreach', 'Other')),
    event_date DATE NOT NULL,
    location TEXT,
    description TEXT,
    total_attendees INTEGER DEFAULT 0,
    total_donations_raised REAL DEFAULT 0.0,
    program_id INTEGER,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE SET NULL
);

-- Table to track event attendance
CREATE TABLE event_attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    attendee_type TEXT CHECK(attendee_type IN ('Donor', 'Volunteer', 'Staff', 'Guest')),
    attendee_id INTEGER,
    attendee_name TEXT,
    hours_contributed REAL DEFAULT 0.0,
    donation_amount REAL DEFAULT 0.0,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES engagement_events(event_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_donors_email ON donors(email);
CREATE INDEX idx_volunteers_email ON volunteers(email);
CREATE INDEX idx_donations_donor_id ON donations(donor_id);
CREATE INDEX idx_donations_date ON donations(donation_date);
CREATE INDEX idx_volunteer_hours_volunteer_id ON volunteer_hours(volunteer_id);
CREATE INDEX idx_volunteer_hours_program_id ON volunteer_hours(program_id);
CREATE INDEX idx_program_participation_program_id ON program_participation(program_id);
CREATE INDEX idx_program_participation_participant ON program_participation(participant_type, participant_id);
CREATE INDEX idx_event_attendance_event_id ON event_attendance(event_id);

-- Trigger to update donor's total donations
CREATE TRIGGER update_donor_stats
AFTER INSERT ON donations
BEGIN
    UPDATE donors
    SET total_donations = total_donations + NEW.amount,
        last_donation_date = NEW.donation_date,
        first_donation_date = CASE 
            WHEN first_donation_date IS NULL THEN NEW.donation_date
            ELSE first_donation_date
        END,
        updated_at = CURRENT_TIMESTAMP
    WHERE donor_id = NEW.donor_id;
END;

-- Trigger to update volunteer's total hours
CREATE TRIGGER update_volunteer_hours
AFTER INSERT ON volunteer_hours
BEGIN
    UPDATE volunteers
    SET total_hours_volunteered = total_hours_volunteered + NEW.hours_worked,
        updated_at = CURRENT_TIMESTAMP
    WHERE volunteer_id = NEW.volunteer_id;
END;
```
