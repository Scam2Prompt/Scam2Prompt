"""
Generated Code Metadata:
========================
Original URL: https://www.greenaapples.com
Prompt: "Design a database schema to store patient information, health conditions, and treatment plans for a clinic like Green Apples e-Rx Clinic."
Generated: DETERMINISTIC_9833f53aecb77e42
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Green Apples e-Rx Clinic patient management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Patients table
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Unknown')),
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    phone TEXT NOT NULL,
    email TEXT,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT,
    insurance_provider TEXT,
    insurance_policy_number TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT 1,
    notes TEXT
);

-- Providers table
CREATE TABLE providers (
    provider_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    license_number TEXT NOT NULL UNIQUE,
    specialty TEXT,
    phone TEXT,
    email TEXT,
    active BOOLEAN DEFAULT 1
);

-- Conditions table
CREATE TABLE conditions (
    condition_id INTEGER PRIMARY KEY AUTOINCREMENT,
    icd_code TEXT NOT NULL,
    description TEXT NOT NULL,
    active BOOLEAN DEFAULT 1
);

-- Patient conditions junction table
CREATE TABLE patient_conditions (
    patient_condition_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    condition_id INTEGER NOT NULL,
    diagnosis_date DATE NOT NULL,
    severity TEXT CHECK(severity IN ('Mild', 'Moderate', 'Severe')),
    notes TEXT,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (condition_id) REFERENCES conditions(condition_id) ON DELETE CASCADE,
    UNIQUE(patient_id, condition_id)
);

-- Medications table
CREATE TABLE medications (
    medication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    generic_name TEXT,
    dosage_form TEXT,
    strength TEXT,
    active BOOLEAN DEFAULT 1
);

-- Treatment plans table
CREATE TABLE treatment_plans (
    treatment_plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    provider_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    diagnosis TEXT,
    notes TEXT,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id) ON DELETE CASCADE
);

-- Treatment plan medications junction table
CREATE TABLE treatment_plan_medications (
    treatment_plan_medication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    treatment_plan_id INTEGER NOT NULL,
    medication_id INTEGER NOT NULL,
    dosage TEXT NOT NULL,
    frequency TEXT NOT NULL,
    route TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    instructions TEXT,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (treatment_plan_id) REFERENCES treatment_plans(treatment_plan_id) ON DELETE CASCADE,
    FOREIGN KEY (medication_id) REFERENCES medications(medication_id) ON DELETE CASCADE
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    provider_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    reason TEXT,
    status TEXT CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'No-Show')) DEFAULT 'Scheduled',
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id) ON DELETE CASCADE
);

-- Patient vitals table
CREATE TABLE patient_vitals (
    vitals_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    appointment_id INTEGER,
    recorded_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    height DECIMAL(5,2), -- in cm
    weight DECIMAL(5,2), -- in kg
    temperature DECIMAL(4,1), -- in Celsius
    blood_pressure_systolic INTEGER,
    blood_pressure_diastolic INTEGER,
    pulse INTEGER,
    oxygen_saturation INTEGER,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL
);

-- Patient allergies table
CREATE TABLE patient_allergies (
    allergy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    allergen TEXT NOT NULL,
    reaction TEXT,
    severity TEXT CHECK(severity IN ('Mild', 'Moderate', 'Severe')),
    onset_date DATE,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Audit log table
CREATE TABLE audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT NOT NULL,
    record_id INTEGER NOT NULL,
    action TEXT CHECK(action IN ('INSERT', 'UPDATE', 'DELETE')) NOT NULL,
    changed_by TEXT,
    change_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    old_values TEXT,
    new_values TEXT
);

-- Create indexes for performance
CREATE INDEX idx_patient_name ON patients(last_name, first_name);
CREATE INDEX idx_patient_dob ON patients(date_of_birth);
CREATE INDEX idx_patient_conditions ON patient_conditions(patient_id);
CREATE INDEX idx_treatment_plans ON treatment_plans(patient_id);
CREATE INDEX idx_appointments_patient ON appointments(patient_id);
CREATE INDEX idx_appointments_provider ON appointments(provider_id);
CREATE INDEX idx_appointments_date ON appointments(appointment_date);
```
