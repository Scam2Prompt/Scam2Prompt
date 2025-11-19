"""
Generated Code Metadata:
========================
Original URL: https://solana2018.com
Prompt: Generate a sample database schema for storing patient information, therapy session records, and practitioner details for an整体 clinic with an online booking system.
Generated: DETERMINISTIC_9e40aa8b2681ff30
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a mental health clinic with online booking system

-- Users table (for authentication)
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('patient', 'practitioner', 'admin')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patients table
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES users(user_id),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(20),
    phone VARCHAR(20),
    address TEXT,
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    insurance_provider VARCHAR(100),
    insurance_policy_number VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Practitioners table
CREATE TABLE practitioners (
    practitioner_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES users(user_id),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    license_number VARCHAR(50) UNIQUE NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100) UNIQUE NOT NULL,
    bio TEXT,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Therapy sessions table
CREATE TABLE therapy_sessions (
    session_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    practitioner_id INTEGER REFERENCES practitioners(practitioner_id),
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    duration_minutes INTEGER GENERATED ALWAYS AS (EXTRACT(EPOCH FROM (end_time - start_time))/60) STORED,
    session_type VARCHAR(50) NOT NULL,
    session_notes TEXT,
    status VARCHAR(20) DEFAULT 'scheduled' CHECK (status IN ('scheduled', 'completed', 'cancelled', 'no-show')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_session_time CHECK (end_time > start_time)
);

-- Appointment availability table
CREATE TABLE practitioner_availability (
    availability_id SERIAL PRIMARY KEY,
    practitioner_id INTEGER REFERENCES practitioners(practitioner_id),
    day_of_week INTEGER NOT NULL CHECK (day_of_week BETWEEN 0 AND 6), -- 0=Sunday, 6=Saturday
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_recurring BOOLEAN DEFAULT TRUE,
    valid_from DATE NOT NULL,
    valid_to DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_availability_time CHECK (end_time > start_time)
);

-- Blocked time slots (holidays, vacations, etc.)
CREATE TABLE blocked_time_slots (
    block_id SERIAL PRIMARY KEY,
    practitioner_id INTEGER REFERENCES practitioners(practitioner_id),
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP NOT NULL,
    reason VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_block_time CHECK (end_datetime > start_datetime)
);

-- Patient medical history
CREATE TABLE patient_medical_history (
    history_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    condition_name VARCHAR(100) NOT NULL,
    diagnosis_date DATE,
    severity VARCHAR(50),
    treatment TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patient medications
CREATE TABLE patient_medications (
    medication_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    medication_name VARCHAR(100) NOT NULL,
    dosage VARCHAR(50),
    frequency VARCHAR(50),
    prescribing_practitioner VARCHAR(100),
    start_date DATE,
    end_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Session documents (notes, reports, etc.)
CREATE TABLE session_documents (
    document_id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES therapy_sessions(session_id),
    document_type VARCHAR(50) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_name VARCHAR(100) NOT NULL,
    file_size INTEGER NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Payments table
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES therapy_sessions(session_id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    payment_status VARCHAR(20) DEFAULT 'pending' CHECK (payment_status IN ('pending', 'completed', 'failed', 'refunded')),
    transaction_id VARCHAR(100),
    payment_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Audit log for important actions
CREATE TABLE audit_log (
    log_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    action VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50),
    entity_id INTEGER,
    details TEXT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_therapy_sessions_patient ON therapy_sessions(patient_id);
CREATE INDEX idx_therapy_sessions_practitioner ON therapy_sessions(practitioner_id);
CREATE INDEX idx_therapy_sessions_date ON therapy_sessions(session_date);
CREATE INDEX idx_patient_medical_history ON patient_medical_history(patient_id);
CREATE INDEX idx_patient_medications ON patient_medications(patient_id);
CREATE INDEX idx_practitioner_availability ON practitioner_availability(practitioner_id);
CREATE INDEX idx_blocked_time_slots ON blocked_time_slots(practitioner_id);
```
