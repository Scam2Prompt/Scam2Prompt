"""
Generated Code Metadata:
========================
Original URL: https://podologiaenpiura.com
Prompt: Design a database schema for a podology clinic management system, including tables for patient information, treatment plans, and orthotic device designs.
Generated: DETERMINISTIC_231f55af53c45dac
Batch ID: 20250622_204849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Podology Clinic Management System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Patients table
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')) NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    insurance_provider TEXT,
    insurance_number TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CONSTRAINT email_format CHECK (email LIKE '%_@__%.__%' OR email IS NULL)
);

-- Medical history table
CREATE TABLE medical_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    condition_name TEXT NOT NULL,
    diagnosis_date DATE,
    severity TEXT,
    treatment TEXT,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    appointment_date DATETIME NOT NULL,
    duration_minutes INTEGER DEFAULT 30,
    reason TEXT NOT NULL,
    status TEXT CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')) DEFAULT 'Scheduled',
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    CONSTRAINT future_appointment CHECK (appointment_date > CURRENT_TIMESTAMP)
);

-- Treatment plans table
CREATE TABLE treatment_plans (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    diagnosis TEXT NOT NULL,
    treatment_goal TEXT NOT NULL,
    frequency TEXT,
    duration_weeks INTEGER,
    notes TEXT,
    status TEXT CHECK(status IN ('Active', 'Completed', 'Cancelled')) DEFAULT 'Active',
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Treatment sessions table
CREATE TABLE treatment_sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER NOT NULL,
    appointment_id INTEGER,
    session_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    treatment_performed TEXT NOT NULL,
    practitioner_notes TEXT,
    patient_feedback TEXT,
    FOREIGN KEY (plan_id) REFERENCES treatment_plans(plan_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL
);

-- Foot measurements table
CREATE TABLE foot_measurements (
    measurement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    measurement_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    foot_side TEXT CHECK(foot_side IN ('Left', 'Right')) NOT NULL,
    length_cm REAL NOT NULL,
    width_cm REAL NOT NULL,
    arch_height_cm REAL NOT NULL,
    ankle_circumference_cm REAL NOT NULL,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Orthotic devices table
CREATE TABLE orthotic_devices (
    device_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    prescription_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    device_type TEXT NOT NULL,
    foot_side TEXT CHECK(foot_side IN ('Left', 'Right', 'Both')) NOT NULL,
    material TEXT NOT NULL,
    durometer TEXT,
    status TEXT CHECK(status IN ('Ordered', 'In Production', 'Delivered', 'Fitted', 'Rejected')) DEFAULT 'Ordered',
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Orthotic designs table
CREATE TABLE orthotic_designs (
    design_id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id INTEGER NOT NULL,
    design_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    design_file_path TEXT,
    specifications TEXT NOT NULL,
    modifications TEXT,
    approval_status TEXT CHECK(approval_status IN ('Pending', 'Approved', 'Rejected')) DEFAULT 'Pending',
    notes TEXT,
    FOREIGN KEY (device_id) REFERENCES orthotic_devices(device_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    appointment_id INTEGER,
    amount REAL NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT CHECK(payment_method IN ('Cash', 'Credit Card', 'Debit Card', 'Insurance', 'Bank Transfer')) NOT NULL,
    status TEXT CHECK(status IN ('Pending', 'Completed', 'Refunded', 'Failed')) DEFAULT 'Completed',
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL
);

-- Create indexes for performance
CREATE INDEX idx_patient_name ON patients(last_name, first_name);
CREATE INDEX idx_appointment_date ON appointments(appointment_date);
CREATE INDEX idx_patient_appointments ON appointments(patient_id);
CREATE INDEX idx_treatment_plan_patient ON treatment_plans(patient_id);
CREATE INDEX idx_orthotic_patient ON orthotic_devices(patient_id);
```
