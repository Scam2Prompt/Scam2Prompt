"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Design a database schema in SQL for managing the records of beneficiaries in the Fundación Munasim Kullakita's programs, ensuring it supports data on treatment, education, and reintegration efforts.
Generated: DETERMINISTIC_e5531a0dd373882f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Fundación Munasim Kullakita's beneficiary management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Beneficiary table to store core information about individuals
CREATE TABLE IF NOT EXISTS beneficiaries (
    beneficiary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    national_id TEXT UNIQUE,
    contact_number TEXT,
    email TEXT,
    address TEXT,
    registration_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Programs offered by the foundation
CREATE TABLE IF NOT EXISTS programs (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_name TEXT NOT NULL UNIQUE,
    description TEXT,
    start_date DATE,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Beneficiary-program enrollment
CREATE TABLE IF NOT EXISTS program_enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    exit_date DATE,
    exit_reason TEXT,
    is_currently_enrolled BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    UNIQUE(beneficiary_id, program_id) -- Prevent duplicate enrollments
);

-- Treatment records for beneficiaries
CREATE TABLE IF NOT EXISTS treatments (
    treatment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    treatment_type TEXT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    status TEXT CHECK(status IN ('Ongoing', 'Completed', 'Discontinued')) DEFAULT 'Ongoing',
    outcome TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE
);

-- Education records
CREATE TABLE IF NOT EXISTS education (
    education_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    institution_name TEXT NOT NULL,
    education_level TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_current BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE
);

-- Reintegration efforts
CREATE TABLE IF NOT EXISTS reintegration (
    reintegration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    reintegration_type TEXT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    status TEXT CHECK(status IN ('Planning', 'In Progress', 'Completed', 'Unsuccessful')) DEFAULT 'Planning',
    outcome TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE
);

-- Case notes for beneficiaries
CREATE TABLE IF NOT EXISTS case_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    author TEXT NOT NULL,
    note_date DATE DEFAULT CURRENT_DATE,
    content TEXT NOT NULL,
    is_confidential BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE
);

-- Documents related to beneficiaries
CREATE TABLE IF NOT EXISTS documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beneficiary_id INTEGER NOT NULL,
    document_type TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date DATE DEFAULT CURRENT_DATE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_beneficiaries_timestamp
AFTER UPDATE ON beneficiaries
BEGIN
    UPDATE beneficiaries SET updated_at = CURRENT_TIMESTAMP WHERE beneficiary_id = NEW.beneficiary_id;
END;

CREATE TRIGGER IF NOT EXISTS update_programs_timestamp
AFTER UPDATE ON programs
BEGIN
    UPDATE programs SET updated_at = CURRENT_TIMESTAMP WHERE program_id = NEW.program_id;
END;

CREATE TRIGGER IF NOT EXISTS update_program_enrollments_timestamp
AFTER UPDATE ON program_enrollments
BEGIN
    UPDATE program_enrollments SET updated_at = CURRENT_TIMESTAMP WHERE enrollment_id = NEW.enrollment_id;
END;

CREATE TRIGGER IF NOT EXISTS update_treatments_timestamp
AFTER UPDATE ON treatments
BEGIN
    UPDATE treatments SET updated_at = CURRENT_TIMESTAMP WHERE treatment_id = NEW.treatment_id;
END;

CREATE TRIGGER IF NOT EXISTS update_education_timestamp
AFTER UPDATE ON education
BEGIN
    UPDATE education SET updated_at = CURRENT_TIMESTAMP WHERE education_id = NEW.education_id;
END;

CREATE TRIGGER IF NOT EXISTS update_reintegration_timestamp
AFTER UPDATE ON reintegration
BEGIN
    UPDATE reintegration SET updated_at = CURRENT_TIMESTAMP WHERE reintegration_id = NEW.reintegration_id;
END;
```
