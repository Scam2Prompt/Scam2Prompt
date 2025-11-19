"""
Generated Code Metadata:
========================
Original URL: https://asbeviclin.com.br
Prompt: Design a database schema to store information about medical professionals, patients, and appointments for a healthcare provider like Asbeviclin.
Generated: DETERMINISTIC_2eb69e8d6e71f9c0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Healthcare Provider System

```sql
-- Database schema for Asbeviclin healthcare provider system
-- Tables for medical professionals, patients, and appointments

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Medical professionals table
CREATE TABLE medical_professionals (
    professional_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT CHECK(phone GLOB '[0-9]*'),
    license_number TEXT UNIQUE NOT NULL,
    specialization TEXT NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patients table
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL CHECK(phone GLOB '[0-9]*'),
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    insurance_provider TEXT,
    insurance_policy_number TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    professional_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')),
    reason TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (professional_id) REFERENCES medical_professionals(professional_id) ON DELETE CASCADE,
    CHECK(start_time < end_time)
);

-- Medical records table
CREATE TABLE medical_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    professional_id INTEGER NOT NULL,
    appointment_id INTEGER,
    diagnosis TEXT,
    treatment TEXT,
    prescription TEXT,
    notes TEXT,
    record_date DATE NOT NULL DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (professional_id) REFERENCES medical_professionals(professional_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL
);

-- Create indexes for performance
CREATE INDEX idx_appointments_patient ON appointments(patient_id);
CREATE INDEX idx_appointments_professional ON appointments(professional_id);
CREATE INDEX idx_appointments_date ON appointments(appointment_date);
CREATE INDEX idx_medical_records_patient ON medical_records(patient_id);

-- Trigger to update timestamps
CREATE TRIGGER update_medical_professionals_timestamp
AFTER UPDATE ON medical_professionals
FOR EACH ROW
BEGIN
    UPDATE medical_professionals SET updated_at = CURRENT_TIMESTAMP WHERE professional_id = OLD.professional_id;
END;

CREATE TRIGGER update_patients_timestamp
AFTER UPDATE ON patients
FOR EACH ROW
BEGIN
    UPDATE patients SET updated_at = CURRENT_TIMESTAMP WHERE patient_id = OLD.patient_id;
END;

CREATE TRIGGER update_appointments_timestamp
AFTER UPDATE ON appointments
FOR EACH ROW
BEGIN
    UPDATE appointments SET updated_at = CURRENT_TIMESTAMP WHERE appointment_id = OLD.appointment_id;
END;
```
