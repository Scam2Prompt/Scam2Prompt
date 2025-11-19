"""
Generated Code Metadata:
========================
Original URL: https://jewelautismcentre.org
Prompt: Design a basic database schema to store patient information, treatment plans, and progress tracking for a child developmental centre like Jewel Autism Centre.
Generated: DETERMINISTIC_447edd772814e753
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Jewel Autism Centre patient management system

-- Patients table to store basic patient information
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(100),
    guardian_name VARCHAR(100),
    guardian_relationship VARCHAR(50),
    guardian_phone VARCHAR(20),
    date_of_admission DATE NOT NULL,
    diagnosis TEXT,
    additional_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Therapists table
CREATE TABLE therapists (
    therapist_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    hire_date DATE,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Treatment types table
CREATE TABLE treatment_types (
    treatment_type_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INTEGER,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Treatment plans table
CREATE TABLE treatment_plans (
    plan_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    therapist_id INTEGER REFERENCES therapists(therapist_id),
    start_date DATE NOT NULL,
    end_date DATE,
    active BOOLEAN DEFAULT TRUE,
    goals TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Plan treatments junction table
CREATE TABLE plan_treatments (
    plan_treatment_id SERIAL PRIMARY KEY,
    plan_id INTEGER REFERENCES treatment_plans(plan_id) ON DELETE CASCADE,
    treatment_type_id INTEGER REFERENCES treatment_types(treatment_type_id),
    frequency_per_week INTEGER,
    duration_weeks INTEGER,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sessions table
CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    plan_treatment_id INTEGER REFERENCES plan_treatments(plan_treatment_id) ON DELETE CASCADE,
    therapist_id INTEGER REFERENCES therapists(therapist_id),
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status VARCHAR(20) CHECK (status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Progress tracking table
CREATE TABLE progress_metrics (
    metric_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    unit VARCHAR(20),
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Progress records table
CREATE TABLE progress_records (
    record_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    metric_id INTEGER REFERENCES progress_metrics(metric_id),
    recorded_date DATE NOT NULL,
    value DECIMAL(10,2),
    notes TEXT,
    recorded_by INTEGER REFERENCES therapists(therapist_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_patients_name ON patients(last_name, first_name);
CREATE INDEX idx_treatment_plans_patient ON treatment_plans(patient_id);
CREATE INDEX idx_sessions_date ON sessions(session_date);
CREATE INDEX idx_progress_records_patient ON progress_records(patient_id);
CREATE INDEX idx_progress_records_metric ON progress_records(metric_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for all tables with updated_at field
CREATE TRIGGER update_patients_timestamp
BEFORE UPDATE ON patients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_therapists_timestamp
BEFORE UPDATE ON therapists
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_treatment_types_timestamp
BEFORE UPDATE ON treatment_types
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_treatment_plans_timestamp
BEFORE UPDATE ON treatment_plans
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_plan_treatments_timestamp
BEFORE UPDATE ON plan_treatments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_sessions_timestamp
BEFORE UPDATE ON sessions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_progress_metrics_timestamp
BEFORE UPDATE ON progress_metrics
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_progress_records_timestamp
BEFORE UPDATE ON progress_records
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
