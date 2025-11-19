"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Design a database schema for managing records of children and adolescents served by CEFOR, including their situations and the services they receive.
Generated: DETERMINISTIC_00b1c106d2f1ac76
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for CEFOR child and adolescent management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing personal information of children/adolescents
CREATE TABLE IF NOT EXISTS individuals (
    individual_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Unknown')),
    identification_number TEXT UNIQUE,
    photo_path TEXT,
    current_status TEXT CHECK(current_status IN ('Active', 'Inactive', 'Transferred', 'Graduated', 'Deceased')),
    date_entered_program DATE NOT NULL,
    date_exited_program DATE,
    exit_reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for contact information
CREATE TABLE IF NOT EXISTS contact_information (
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    country TEXT DEFAULT 'Brazil',
    phone_number TEXT,
    email TEXT,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT,
    emergency_contact_relationship TEXT,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE
);

-- Table for family information
CREATE TABLE IF NOT EXISTS family (
    family_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    mother_name TEXT,
    mother_contact TEXT,
    father_name TEXT,
    father_contact TEXT,
    guardian_name TEXT,
    guardian_contact TEXT,
    guardian_relationship TEXT,
    siblings_count INTEGER DEFAULT 0,
    family_income DECIMAL(10, 2),
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE
);

-- Table for educational information
CREATE TABLE IF NOT EXISTS education (
    education_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    school_name TEXT,
    school_grade TEXT,
    school_attendance TEXT CHECK(school_attendance IN ('Regular', 'Irregular', 'Not Attending')),
    educational_needs TEXT,
    last_school_year_completed TEXT,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE
);

-- Table for health information
CREATE TABLE IF NOT EXISTS health (
    health_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    blood_type TEXT CHECK(blood_type IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-', 'Unknown')),
    allergies TEXT,
    chronic_conditions TEXT,
    medications TEXT,
    disabilities TEXT,
    last_medical_checkup DATE,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE
);

-- Table for risk/vulnerability factors
CREATE TABLE IF NOT EXISTS risk_factors (
    risk_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    factor_type TEXT NOT NULL CHECK(factor_type IN (
        'Abuse', 'Neglect', 'Exploitation', 'Violence', 
        'Substance Abuse', 'Family Conflict', 'Poverty', 
        'Homelessness', 'Other'
    )),
    description TEXT,
    severity TEXT CHECK(severity IN ('Low', 'Medium', 'High', 'Critical')),
    date_identified DATE NOT NULL,
    current_status TEXT CHECK(current_status IN ('Active', 'Resolved', 'Mitigated')),
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE
);

-- Table for service types
CREATE TABLE IF NOT EXISTS service_types (
    service_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    category TEXT NOT NULL CHECK(category IN (
        'Education', 'Health', 'Psychological', 'Social', 
        'Legal', 'Vocational', 'Recreational', 'Other'
    )),
    is_active BOOLEAN DEFAULT 1
);

-- Table for service providers
CREATE TABLE IF NOT EXISTS service_providers (
    provider_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    specialization TEXT,
    is_active BOOLEAN DEFAULT 1
);

-- Table for services provided to individuals
CREATE TABLE IF NOT EXISTS services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    service_type_id INTEGER NOT NULL,
    provider_id INTEGER,
    start_date DATE NOT NULL,
    end_date DATE,
    frequency TEXT,
    location TEXT,
    notes TEXT,
    status TEXT CHECK(status IN ('Planned', 'In Progress', 'Completed', 'Cancelled')),
    outcome TEXT,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE,
    FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id),
    FOREIGN KEY (provider_id) REFERENCES service_providers(provider_id)
);

-- Table for case notes and progress tracking
CREATE TABLE IF NOT EXISTS case_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    note_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    note_type TEXT CHECK(note_type IN ('Assessment', 'Progress', 'Incident', 'Follow-up', 'Other')),
    content TEXT NOT NULL,
    is_confidential BOOLEAN DEFAULT 0,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE
);

-- Table for documents (scans, reports, etc.)
CREATE TABLE IF NOT EXISTS documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    document_type TEXT NOT NULL CHECK(document_type IN (
        'Identification', 'Medical', 'Educational', 'Legal', 
        'Assessment', 'Photo', 'Other'
    )),
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE
);

-- Table for system users (staff)
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT NOT NULL CHECK(role IN ('Admin', 'Case Worker', 'Manager', 'Volunteer')),
    is_active BOOLEAN DEFAULT 1,
    last_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for audit logging
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action TEXT NOT NULL,
    table_name TEXT NOT NULL,
    record_id INTEGER,
    old_values TEXT,
    new_values TEXT,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- Trigger to update the updated_at timestamp when individual records are modified
CREATE TRIGGER IF NOT EXISTS update_individual_timestamp
AFTER UPDATE ON individuals
FOR EACH ROW
BEGIN
    UPDATE individuals SET updated_at = CURRENT_TIMESTAMP WHERE individual_id = OLD.individual_id;
END;
```
