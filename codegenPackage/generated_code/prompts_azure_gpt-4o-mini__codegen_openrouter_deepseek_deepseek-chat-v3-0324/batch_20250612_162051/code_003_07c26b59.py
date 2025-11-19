"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Create a sample database schema for a staffing agency that specializes in placing healthcare professionals, referencing the unique roles mentioned on Amazing Grace Medical Recruitment's site.
Generated: DETERMINISTIC_07c26b594a1daeef
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a healthcare staffing agency

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Table for healthcare professionals
CREATE TABLE professionals (
    professional_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    license_number TEXT,
    license_state TEXT,
    specialty TEXT NOT NULL,
    years_experience INTEGER NOT NULL,
    resume_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (years_experience >= 0)
);

-- Table for healthcare facilities
CREATE TABLE facilities (
    facility_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    phone TEXT NOT NULL,
    contact_person TEXT NOT NULL,
    facility_type TEXT NOT NULL, -- e.g., Hospital, Clinic, Nursing Home
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for job positions
CREATE TABLE positions (
    position_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL, -- e.g., Travel Nurse, Locum Tenens Physician, etc.
    description TEXT NOT NULL,
    specialty_required TEXT NOT NULL,
    min_experience INTEGER NOT NULL,
    license_required BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (min_experience >= 0)
);

-- Table for assignments (placements)
CREATE TABLE assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    professional_id INTEGER NOT NULL,
    position_id INTEGER NOT NULL,
    facility_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    status TEXT NOT NULL, -- e.g., Active, Completed, Cancelled
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (professional_id) REFERENCES professionals(professional_id) ON DELETE CASCADE,
    FOREIGN KEY (position_id) REFERENCES positions(position_id) ON DELETE CASCADE,
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id) ON DELETE CASCADE,
    CHECK (hourly_rate > 0),
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Table for credentials/certifications
CREATE TABLE credentials (
    credential_id INTEGER PRIMARY KEY AUTOINCREMENT,
    professional_id INTEGER NOT NULL,
    credential_name TEXT NOT NULL, -- e.g., BLS, ACLS, PALS, etc.
    issuing_organization TEXT NOT NULL,
    issue_date DATE NOT NULL,
    expiration_date DATE,
    credential_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (professional_id) REFERENCES professionals(professional_id) ON DELETE CASCADE,
    CHECK (expiration_date IS NULL OR expiration_date >= issue_date)
);

-- Table for availability
CREATE TABLE availability (
    availability_id INTEGER PRIMARY KEY AUTOINCREMENT,
    professional_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    preferred_location_state TEXT,
    preferred_facility_type TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (professional_id) REFERENCES professionals(professional_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Table for invoices
CREATE TABLE invoices (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL,
    invoice_number TEXT NOT NULL UNIQUE,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    status TEXT NOT NULL, -- e.g., Paid, Unpaid, Overdue
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (assignment_id) REFERENCES assignments(assignment_id) ON DELETE CASCADE,
    CHECK (amount > 0),
    CHECK (due_date >= issue_date)
);

-- Create indexes for performance
CREATE INDEX idx_professionals_specialty ON professionals(specialty);
CREATE INDEX idx_professionals_experience ON professionals(years_experience);
CREATE INDEX idx_positions_specialty ON positions(specialty_required);
CREATE INDEX idx_assignments_status ON assignments(status);
CREATE INDEX idx_credentials_professional ON credentials(professional_id);
CREATE INDEX idx_availability_professional ON availability(professional_id);
```
