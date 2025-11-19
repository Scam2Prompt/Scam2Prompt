"""
Generated Code Metadata:
========================
Original URL: https://www.my-loyola.com
Prompt: Design a database schema for storing patient medical records and information, inspired by the features and functionality of myLoyola.
Generated: DETERMINISTIC_203f3c09b357dcbe
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for patient medical records system

-- Users table to store login credentials and basic info
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('patient', 'doctor', 'nurse', 'admin')),
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patients table with extended medical information
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES users(user_id),
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10) CHECK (gender IN ('male', 'female', 'other', 'unknown')),
    blood_type VARCHAR(5) CHECK (blood_type IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-', 'unknown')),
    height_cm INTEGER,
    weight_kg DECIMAL(5,2),
    primary_phone VARCHAR(20),
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    insurance_provider VARCHAR(100),
    insurance_policy_number VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Doctors table with specialization info
CREATE TABLE doctors (
    doctor_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES users(user_id),
    specialization VARCHAR(100),
    license_number VARCHAR(50) UNIQUE,
    years_of_experience INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    doctor_id INTEGER REFERENCES doctors(doctor_id),
    appointment_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER DEFAULT 30,
    status VARCHAR(20) DEFAULT 'scheduled' CHECK (status IN ('scheduled', 'completed', 'canceled', 'no-show')),
    reason VARCHAR(255),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Medical records table
CREATE TABLE medical_records (
    record_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    doctor_id INTEGER REFERENCES doctors(doctor_id),
    record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    diagnosis TEXT,
    treatment TEXT,
    prescription TEXT,
    notes TEXT,
    is_confidential BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Lab results table
CREATE TABLE lab_results (
    result_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    doctor_id INTEGER REFERENCES doctors(doctor_id),
    test_name VARCHAR(100) NOT NULL,
    test_date TIMESTAMP NOT NULL,
    result_date TIMESTAMP,
    result_value TEXT,
    reference_range VARCHAR(100),
    units VARCHAR(20),
    interpretation TEXT,
    is_abnormal BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Medications table
CREATE TABLE medications (
    medication_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    dosage_forms VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patient medications (prescriptions)
CREATE TABLE patient_medications (
    prescription_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    medication_id INTEGER REFERENCES medications(medication_id),
    doctor_id INTEGER REFERENCES doctors(doctor_id),
    dosage VARCHAR(100) NOT NULL,
    frequency VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    purpose TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Allergies table
CREATE TABLE allergies (
    allergy_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patient allergies
CREATE TABLE patient_allergies (
    patient_allergy_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    allergy_id INTEGER REFERENCES allergies(allergy_id),
    severity VARCHAR(20) CHECK (severity IN ('mild', 'moderate', 'severe')),
    reaction TEXT,
    first_observed DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Messages between patients and providers
CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    sender_id INTEGER REFERENCES users(user_id),
    recipient_id INTEGER REFERENCES users(user_id),
    subject VARCHAR(100),
    body TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    read_at TIMESTAMP
);

-- Audit log for tracking changes
CREATE TABLE audit_log (
    log_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INTEGER,
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_patient_id ON patients(user_id);
CREATE INDEX idx_doctor_id ON doctors(user_id);
CREATE INDEX idx_appointment_patient ON appointments(patient_id);
CREATE INDEX idx_appointment_doctor ON appointments(doctor_id);
CREATE INDEX idx_appointment_date ON appointments(appointment_date);
CREATE INDEX idx_medical_record_patient ON medical_records(patient_id);
CREATE INDEX idx_lab_result_patient ON lab_results(patient_id);
CREATE INDEX idx_patient_medication ON patient_medications(patient_id);
CREATE INDEX idx_patient_allergy ON patient_allergies(patient_id);
CREATE INDEX idx_message_sender ON messages(sender_id);
CREATE INDEX idx_message_recipient ON messages(recipient_id);

-- Create triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_users_timestamp
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_patients_timestamp
BEFORE UPDATE ON patients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_doctors_timestamp
BEFORE UPDATE ON doctors
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_appointments_timestamp
BEFORE UPDATE ON appointments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_medical_records_timestamp
BEFORE UPDATE ON medical_records
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_lab_results_timestamp
BEFORE UPDATE ON lab_results
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_medications_timestamp
BEFORE UPDATE ON medications
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_patient_medications_timestamp
BEFORE UPDATE ON patient_medications
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_allergies_timestamp
BEFORE UPDATE ON allergies
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_patient_allergies_timestamp
BEFORE UPDATE ON patient_allergies
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
