"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconfoundation.online
Prompt: Create a sample database schema for managing therapy sessions and outcomes based on the ICON Foundation's outcome-based mindset in clinical practice.
Generated: DETERMINISTIC_830e9045a059c4c2
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Sample Database Schema for Managing Therapy Sessions and Outcomes
-- Following the ICON Foundation's outcome-based mindset in clinical practice

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Therapist;
DROP TABLE IF EXISTS Patient;
DROP TABLE IF EXISTS TherapySession;
DROP TABLE IF EXISTS OutcomeMeasure;

-- Table to store therapist information
CREATE TABLE Therapist (
    therapist_id SERIAL PRIMARY KEY,                       -- Unique identifier for each therapist
    first_name VARCHAR(50) NOT NULL,                      -- Therapist's first name
    last_name VARCHAR(50) NOT NULL,                       -- Therapist's last name
    specialty VARCHAR(100),                                -- Area of expertise (e.g., CBT, DBT)
    license_number VARCHAR(50) UNIQUE NOT NULL,           -- Unique license number for professional practice
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP        -- Timestamp of record creation
);

-- Table to store patient information
CREATE TABLE Patient (
    patient_id SERIAL PRIMARY KEY,                         -- Unique identifier for each patient
    first_name VARCHAR(50) NOT NULL,                      -- Patient's first name
    last_name VARCHAR(50) NOT NULL,                       -- Patient's last name
    date_of_birth DATE NOT NULL,                          -- Patient's date of birth
    gender VARCHAR(10),                                   -- Patient's gender
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP        -- Timestamp of record creation
);

-- Table to store therapy session details
CREATE TABLE TherapySession (
    session_id SERIAL PRIMARY KEY,                        -- Unique identifier for each session
    therapist_id INT NOT NULL REFERENCES Therapist(therapist_id), -- Reference to the therapist
    patient_id INT NOT NULL REFERENCES Patient(patient_id),       -- Reference to the patient
    session_date TIMESTAMP NOT NULL,                      -- Date and time of the session
    session_notes TEXT,                                   -- Additional notes for the session
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP        -- Timestamp of record creation
);

-- Table to store outcome measures associated with therapy sessions
CREATE TABLE OutcomeMeasure (
    outcome_id SERIAL PRIMARY KEY,                        -- Unique identifier for each outcome measure
    session_id INT NOT NULL REFERENCES TherapySession(session_id), -- Reference to the therapy session
    outcome_type VARCHAR(50) NOT NULL,                   -- Type of outcome measure (e.g., symptom reduction)
    outcome_value NUMERIC CHECK (outcome_value >= 0),    -- Numeric value representing the outcome
    outcome_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Date of the outcome measurement
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP        -- Timestamp of record creation
);

-- Optional: Create indexes for faster queries
CREATE INDEX idx_therapist_id ON TherapySession(therapist_id);
CREATE INDEX idx_patient_id ON TherapySession(patient_id);
CREATE INDEX idx_session_id ON OutcomeMeasure(session_id);
```
