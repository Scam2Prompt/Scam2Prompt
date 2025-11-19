"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Design a database schema for storing patient data, treatment plans, and medical records for a cardiology clinic.
Generated: DETERMINISTIC_7e7873822fb2fd0b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Cardiology Clinic Management System

-- Patients table stores basic patient information
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100) CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    emergency_contact_name VARCHAR(200),
    emergency_contact_phone VARCHAR(20),
    blood_type VARCHAR(5) CHECK (blood_type IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_patient_email UNIQUE (email)
);

-- Medical staff table
CREATE TABLE medical_staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    license_number VARCHAR(50) UNIQUE,
    phone VARCHAR(20),
    email VARCHAR(100) CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patient medical history
CREATE TABLE medical_history (
    history_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    condition_name VARCHAR(200) NOT NULL,
    diagnosis_date DATE,
    severity VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Medications table
CREATE TABLE medications (
    medication_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    dosage_form VARCHAR(100),
    manufacturer VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patient allergies
CREATE TABLE allergies (
    allergy_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    allergen VARCHAR(200) NOT NULL,
    reaction TEXT,
    severity VARCHAR(50) CHECK (severity IN ('Mild', 'Moderate', 'Severe')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cardiology-specific tests
CREATE TABLE cardiac_tests (
    test_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    preparation_instructions TEXT,
    typical_duration_minutes INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patient appointments
CREATE TABLE appointments (
    appointment_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    staff_id INTEGER REFERENCES medical_staff(staff_id) ON DELETE SET NULL,
    appointment_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER DEFAULT 30,
    reason TEXT,
    status VARCHAR(20) DEFAULT 'Scheduled' CHECK (status IN ('Scheduled', 'Completed', 'Cancelled', 'No-Show')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patient test results
CREATE TABLE test_results (
    result_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    test_id INTEGER REFERENCES cardiac_tests(test_id) ON DELETE CASCADE,
    staff_id INTEGER REFERENCES medical_staff(staff_id) ON DELETE SET NULL,
    appointment_id INTEGER REFERENCES appointments(appointment_id) ON DELETE SET NULL,
    test_date TIMESTAMP NOT NULL,
    result_value TEXT,
    reference_range TEXT,
    interpretation TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Treatment plans
CREATE TABLE treatment_plans (
    plan_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    staff_id INTEGER REFERENCES medical_staff(staff_id) ON DELETE SET NULL,
    diagnosis TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    status VARCHAR(20) DEFAULT 'Active' CHECK (status IN ('Active', 'Completed', 'Cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Treatment plan medications
CREATE TABLE plan_medications (
    plan_medication_id SERIAL PRIMARY KEY,
    plan_id INTEGER REFERENCES treatment_plans(plan_id) ON DELETE CASCADE,
    medication_id INTEGER REFERENCES medications(medication_id) ON DELETE CASCADE,
    dosage VARCHAR(100) NOT NULL,
    frequency VARCHAR(100) NOT NULL,
    route VARCHAR(50),
    start_date DATE,
    end_date DATE,
    instructions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patient vital signs
CREATE TABLE vital_signs (
    vital_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    staff_id INTEGER REFERENCES medical_staff(staff_id) ON DELETE SET NULL,
    appointment_id INTEGER REFERENCES appointments(appointment_id) ON DELETE SET NULL,
    measurement_date TIMESTAMP NOT NULL,
    systolic_bp INTEGER,
    diastolic_bp INTEGER,
    heart_rate INTEGER,
    respiratory_rate INTEGER,
    temperature DECIMAL(5,2),
    oxygen_saturation DECIMAL(5,2),
    weight_kg DECIMAL(7,2),
    height_cm DECIMAL(7,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Procedures table
CREATE TABLE procedures (
    procedure_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    typical_duration_minutes INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patient procedures
CREATE TABLE patient_procedures (
    patient_procedure_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    procedure_id INTEGER REFERENCES procedures(procedure_id) ON DELETE CASCADE,
    staff_id INTEGER REFERENCES medical_staff(staff_id) ON DELETE SET NULL,
    appointment_id INTEGER REFERENCES appointments(appointment_id) ON DELETE SET NULL,
    procedure_date TIMESTAMP NOT NULL,
    notes TEXT,
    complications TEXT,
    outcome TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_patients_last_name ON patients(last_name);
CREATE INDEX idx_appointments_patient_id ON appointments(patient_id);
CREATE INDEX idx_appointments_staff_id ON appointments(staff_id);
CREATE INDEX idx_appointments_date ON appointments(appointment_date);
CREATE INDEX idx_test_results_patient_id ON test_results(patient_id);
CREATE INDEX idx_treatment_plans_patient_id ON treatment_plans(patient_id);
CREATE INDEX idx_vital_signs_patient_id ON vital_signs(patient_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for tables with updated_at fields
CREATE TRIGGER update_patients_timestamp
BEFORE UPDATE ON patients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_medical_staff_timestamp
BEFORE UPDATE ON medical_staff
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_medical_history_timestamp
BEFORE UPDATE ON medical_history
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_allergies_timestamp
BEFORE UPDATE ON allergies
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_appointments_timestamp
BEFORE UPDATE ON appointments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_test_results_timestamp
BEFORE UPDATE ON test_results
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_treatment_plans_timestamp
BEFORE UPDATE ON treatment_plans
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_plan_medications_timestamp
BEFORE UPDATE ON plan_medications
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_vital_signs_timestamp
BEFORE UPDATE ON vital_signs
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_patient_procedures_timestamp
BEFORE UPDATE ON patient_procedures
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
