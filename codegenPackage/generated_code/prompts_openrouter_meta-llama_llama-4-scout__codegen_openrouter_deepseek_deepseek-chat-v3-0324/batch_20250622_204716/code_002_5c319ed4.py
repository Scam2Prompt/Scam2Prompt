"""
Generated Code Metadata:
========================
Original URL: https://cedarlake.org
Prompt: Generate a sample database schema for storing information about individuals with disabilities, their residential options, and the services they receive, inspired by Cedar Lake Foundation's services.
Generated: DETERMINISTIC_5c319ed46344ba93
Batch ID: 20250622_204716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for disability services management system
-- Inspired by Cedar Lake Foundation's services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Individuals table
CREATE TABLE individuals (
    individual_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    ssn TEXT UNIQUE, -- Social Security Number (encrypted in production)
    medicare_id TEXT UNIQUE,
    medicaid_id TEXT UNIQUE,
    primary_diagnosis TEXT,
    secondary_diagnoses TEXT,
    date_admitted DATE NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (date_admitted <= date('now'))
);

-- Contact information table
CREATE TABLE contact_info (
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    address_line1 TEXT NOT NULL,
    address_line2 TEXT,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    primary_phone TEXT NOT NULL,
    secondary_phone TEXT,
    email TEXT,
    emergency_contact_name TEXT NOT NULL,
    emergency_contact_phone TEXT NOT NULL,
    emergency_contact_relation TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE
);

-- Residential options table
CREATE TABLE residential_options (
    residence_id INTEGER PRIMARY KEY AUTOINCREMENT,
    residence_name TEXT NOT NULL UNIQUE,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    capacity INTEGER NOT NULL,
    current_occupancy INTEGER DEFAULT 0,
    description TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (current_occupancy <= capacity)
);

-- Individual residence assignments
CREATE TABLE residence_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    residence_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_current BOOLEAN DEFAULT 1,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE,
    FOREIGN KEY (residence_id) REFERENCES residential_options(residence_id) ON DELETE CASCADE,
    CHECK (start_date <= IFNULL(end_date, date('now')))
);

-- Services catalog
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    service_description TEXT,
    category TEXT NOT NULL CHECK(category IN ('Medical', 'Therapeutic', 'Educational', 'Vocational', 'Social', 'Other')),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Individual services assignments
CREATE TABLE service_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    frequency TEXT NOT NULL,
    provider TEXT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    CHECK (start_date <= IFNULL(end_date, date('now')))
);

-- Staff members
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('Caregiver', 'Nurse', 'Therapist', 'Administrator', 'Other')),
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Staff assignments to residences
CREATE TABLE staff_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_id INTEGER NOT NULL,
    residence_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_current BOOLEAN DEFAULT 1,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    FOREIGN KEY (residence_id) REFERENCES residential_options(residence_id) ON DELETE CASCADE,
    CHECK (start_date <= IFNULL(end_date, date('now')))
);

-- Medical records
CREATE TABLE medical_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    record_date DATE NOT NULL,
    record_type TEXT NOT NULL CHECK(record_type IN ('Visit', 'Hospitalization', 'Medication', 'Allergy', 'Immunization', 'Other')),
    provider TEXT NOT NULL,
    diagnosis TEXT,
    treatment TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE,
    CHECK (record_date <= date('now'))
);

-- Progress notes
CREATE TABLE progress_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    note_date DATE NOT NULL,
    note_type TEXT NOT NULL CHECK(note_type IN ('Daily', 'Incident', 'Behavioral', 'Medical', 'Other')),
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    CHECK (note_date <= date('now'))
);

-- Create indexes for better performance
CREATE INDEX idx_individual_name ON individuals(last_name, first_name);
CREATE INDEX idx_residence_name ON residential_options(residence_name);
CREATE INDEX idx_service_name ON services(service_name);
CREATE INDEX idx_staff_name ON staff(last_name, first_name);
CREATE INDEX idx_individual_residence ON residence_assignments(individual_id, residence_id);
CREATE INDEX idx_individual_service ON service_assignments(individual_id, service_id);
CREATE INDEX idx_staff_residence ON staff_assignments(staff_id, residence_id);
CREATE INDEX idx_medical_records ON medical_records(individual_id, record_date);
CREATE INDEX idx_progress_notes ON progress_notes(individual_id, note_date);
```
