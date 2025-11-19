"""
Generated Code Metadata:
========================
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: Design a database schema to store patient information and treatment plans for an orthopedic practice like Gelenkzentrum Mönchengladbach.
Generated: DETERMINISTIC_8cb7614a8c3f0c60
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for Orthopedic Practice Patient Management

```sql
-- Database schema for orthopedic practice patient information and treatment plans
-- Designed for PostgreSQL but compatible with most SQL databases

CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(20) CHECK (gender IN ('Male', 'Female', 'Other', 'Unknown')),
    address VARCHAR(255),
    city VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    phone_number VARCHAR(30),
    email VARCHAR(100) CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    insurance_number VARCHAR(50),
    insurance_provider VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dob CHECK (date_of_birth <= CURRENT_DATE)
);

CREATE TABLE medical_history (
    history_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    allergies TEXT,
    chronic_conditions TEXT,
    previous_surgeries TEXT,
    family_history TEXT,
    medications TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE appointments (
    appointment_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    appointment_date TIMESTAMP WITH TIME ZONE NOT NULL,
    duration_minutes INTEGER DEFAULT 30,
    reason TEXT,
    status VARCHAR(20) DEFAULT 'Scheduled' CHECK (status IN ('Scheduled', 'Completed', 'Cancelled', 'No-Show')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT future_appointment CHECK (appointment_date > CURRENT_TIMESTAMP)
);

CREATE TABLE physicians (
    physician_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    license_number VARCHAR(50),
    phone_number VARCHAR(30),
    email VARCHAR(100) CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE physician_appointments (
    physician_id INTEGER REFERENCES physicians(physician_id) ON DELETE CASCADE,
    appointment_id INTEGER REFERENCES appointments(appointment_id) ON DELETE CASCADE,
    PRIMARY KEY (physician_id, appointment_id)
);

CREATE TABLE examinations (
    examination_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    physician_id INTEGER REFERENCES physicians(physician_id) ON DELETE SET NULL,
    examination_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    body_part VARCHAR(100) NOT NULL,
    diagnosis TEXT,
    notes TEXT,
    follow_up_required BOOLEAN DEFAULT FALSE,
    follow_up_date TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE treatment_plans (
    plan_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    physician_id INTEGER REFERENCES physicians(physician_id) ON DELETE SET NULL,
    examination_id INTEGER REFERENCES examinations(examination_id) ON DELETE SET NULL,
    diagnosis_code VARCHAR(20),
    diagnosis_description TEXT,
    treatment_description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    status VARCHAR(20) DEFAULT 'Active' CHECK (status IN ('Active', 'Completed', 'Cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

CREATE TABLE treatment_steps (
    step_id SERIAL PRIMARY KEY,
    plan_id INTEGER REFERENCES treatment_plans(plan_id) ON DELETE CASCADE,
    step_number INTEGER NOT NULL,
    description TEXT NOT NULL,
    expected_outcome TEXT,
    completed BOOLEAN DEFAULT FALSE,
    completion_date DATE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (plan_id, step_number)
);

CREATE TABLE prescriptions (
    prescription_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    physician_id INTEGER REFERENCES physicians(physician_id) ON DELETE SET NULL,
    medication_name VARCHAR(100) NOT NULL,
    dosage VARCHAR(100) NOT NULL,
    frequency VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    instructions TEXT,
    refills INTEGER DEFAULT 0,
    status VARCHAR(20) DEFAULT 'Active' CHECK (status IN ('Active', 'Completed', 'Cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_prescription_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

CREATE TABLE imaging_results (
    imaging_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    physician_id INTEGER REFERENCES physicians(physician_id) ON DELETE SET NULL,
    imaging_type VARCHAR(100) NOT NULL,
    body_part VARCHAR(100) NOT NULL,
    imaging_date DATE NOT NULL,
    results_summary TEXT,
    findings TEXT,
    radiologist_notes TEXT,
    image_location VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE billing (
    bill_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    appointment_id INTEGER REFERENCES appointments(appointment_id) ON DELETE SET NULL,
    treatment_plan_id INTEGER REFERENCES treatment_plans(plan_id) ON DELETE SET NULL,
    amount DECIMAL(10, 2) NOT NULL,
    billing_date DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL DEFAULT (CURRENT_DATE + INTERVAL '30 days'),
    status VARCHAR(20) DEFAULT 'Pending' CHECK (status IN ('Pending', 'Paid', 'Overdue', 'Cancelled')),
    insurance_claim_id VARCHAR(100),
    payment_method VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (due_date >= billing_date)
);

-- Indexes for performance optimization
CREATE INDEX idx_patients_last_name ON patients(last_name);
CREATE INDEX idx_appointments_patient_id ON appointments(patient_id);
CREATE INDEX idx_appointments_date ON appointments(appointment_date);
CREATE INDEX idx_treatment_plans_patient_id ON treatment_plans(patient_id);
CREATE INDEX idx_examinations_patient_id ON examinations(patient_id);
CREATE INDEX idx_prescriptions_patient_id ON prescriptions(patient_id);
```
