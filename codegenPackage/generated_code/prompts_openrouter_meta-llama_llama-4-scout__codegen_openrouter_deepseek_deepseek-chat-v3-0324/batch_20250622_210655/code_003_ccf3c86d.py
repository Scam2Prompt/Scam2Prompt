"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Design a database schema to store information on the beneficiaries of Fundación Munasim Kullakita, including demographic data, services provided, and outcomes.
Generated: DETERMINISTIC_ccf3c86d35c79ca5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Fundación Munasim Kullakita beneficiaries

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Beneficiary table stores core demographic information
CREATE TABLE beneficiaries (
    beneficiary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    identification_number TEXT UNIQUE,
    identification_type TEXT CHECK(identification_type IN ('ID Card', 'Passport', 'Birth Certificate', 'Other')),
    nationality TEXT,
    ethnicity TEXT,
    address TEXT,
    city TEXT,
    phone_number TEXT,
    email TEXT,
    registration_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Services table catalogs available services
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT,
    category TEXT NOT NULL CHECK(category IN ('Education', 'Healthcare', 'Legal', 'Psychological', 'Shelter', 'Other')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Beneficiary-service junction table tracks services provided
CREATE TABLE beneficiary_services (
    beneficiary_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status TEXT NOT NULL CHECK(status IN ('Active', 'Completed', 'Cancelled', 'Pending')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    UNIQUE(beneficiary_id, service_id, start_date)
);

-- Outcomes table tracks results/achievements for beneficiaries
CREATE TABLE outcomes (
    outcome_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    outcome_type TEXT NOT NULL CHECK(outcome_type IN ('Education', 'Employment', 'Health', 'Legal', 'Housing', 'Other')),
    description TEXT NOT NULL,
    achievement_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE
);

-- Case workers/staff table
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    position TEXT NOT NULL,
    email TEXT UNIQUE,
    phone_number TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Beneficiary-case worker assignment
CREATE TABLE beneficiary_staff_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_primary BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    UNIQUE(beneficiary_id, staff_id, start_date)
);

-- Create indexes for performance
CREATE INDEX idx_beneficiaries_name ON beneficiaries(last_name, first_name);
CREATE INDEX idx_beneficiaries_dob ON beneficiaries(date_of_birth);
CREATE INDEX idx_beneficiary_services_beneficiary ON beneficiary_services(beneficiary_id);
CREATE INDEX idx_beneficiary_services_service ON beneficiary_services(service_id);
CREATE INDEX idx_outcomes_beneficiary ON outcomes(beneficiary_id);
CREATE INDEX idx_outcomes_type ON outcomes(outcome_type);
CREATE INDEX idx_assignments_beneficiary ON beneficiary_staff_assignments(beneficiary_id);
CREATE INDEX idx_assignments_staff ON beneficiary_staff_assignments(staff_id);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_beneficiary_timestamp
AFTER UPDATE ON beneficiaries
FOR EACH ROW
BEGIN
    UPDATE beneficiaries SET updated_at = CURRENT_TIMESTAMP WHERE beneficiary_id = OLD.beneficiary_id;
END;

CREATE TRIGGER update_service_timestamp
AFTER UPDATE ON services
FOR EACH ROW
BEGIN
    UPDATE services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER update_staff_timestamp
AFTER UPDATE ON staff
FOR EACH ROW
BEGIN
    UPDATE staff SET updated_at = CURRENT_TIMESTAMP WHERE staff_id = OLD.staff_id;
END;
```
