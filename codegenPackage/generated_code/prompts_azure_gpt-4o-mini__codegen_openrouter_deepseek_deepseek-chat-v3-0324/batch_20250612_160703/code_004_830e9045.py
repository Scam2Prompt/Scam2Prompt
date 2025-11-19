"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: Create a sample database schema for managing therapy sessions and outcomes based on the ICON Foundation's outcome-based mindset in clinical practice.
Generated: DETERMINISTIC_830e9045a059c4c2
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing therapy sessions and outcomes
-- Based on ICON Foundation's outcome-based mindset in clinical practice

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    email TEXT UNIQUE,
    phone TEXT,
    address TEXT,
    registration_date DATE DEFAULT CURRENT_DATE,
    active BOOLEAN DEFAULT 1,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS therapists (
    therapist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    license_number TEXT UNIQUE NOT NULL,
    specialization TEXT,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    active BOOLEAN DEFAULT 1
);

CREATE TABLE IF NOT EXISTS outcome_measures (
    measure_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    scale_min INTEGER NOT NULL,
    scale_max INTEGER NOT NULL,
    interpretation_guide TEXT
);

CREATE TABLE IF NOT EXISTS sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    therapist_id INTEGER NOT NULL,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    session_type TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE,
    CHECK (end_time > start_time)
);

CREATE TABLE IF NOT EXISTS session_outcomes (
    outcome_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    measure_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    comments TEXT,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE,
    FOREIGN KEY (measure_id) REFERENCES outcome_measures(measure_id) ON DELETE CASCADE,
    CHECK (score >= (SELECT scale_min FROM outcome_measures WHERE measure_id = session_outcomes.measure_id)),
    CHECK (score <= (SELECT scale_max FROM outcome_measures WHERE measure_id = session_outcomes.measure_id))
);

CREATE TABLE IF NOT EXISTS treatment_plans (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    therapist_id INTEGER NOT NULL,
    creation_date DATE DEFAULT CURRENT_DATE,
    target_outcome TEXT NOT NULL,
    frequency TEXT NOT NULL,
    duration TEXT NOT NULL,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS plan_sessions (
    plan_session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER NOT NULL,
    session_id INTEGER NOT NULL,
    FOREIGN KEY (plan_id) REFERENCES treatment_plans(plan_id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE,
    UNIQUE (plan_id, session_id)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_sessions_patient ON sessions(patient_id);
CREATE INDEX IF NOT EXISTS idx_sessions_therapist ON sessions(therapist_id);
CREATE INDEX IF NOT EXISTS idx_sessions_date ON sessions(session_date);
CREATE INDEX IF NOT EXISTS idx_outcomes_session ON session_outcomes(session_id);
CREATE INDEX IF NOT EXISTS idx_outcomes_measure ON session_outcomes(measure_id);
CREATE INDEX IF NOT EXISTS idx_plans_patient ON treatment_plans(patient_id);
```
