"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Design a database schema to store patient information, treatment plans, and services offered by the San Diego Sleep and TMJ Center, including information about their doctors and staff.
Generated: DETERMINISTIC_fcf587744cd5a692
Batch ID: 20250622_204623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for San Diego Sleep and TMJ Center

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Patients table
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    address TEXT,
    city TEXT,
    state TEXT DEFAULT 'CA',
    zip_code TEXT,
    phone TEXT NOT NULL,
    email TEXT,
    insurance_provider TEXT,
    insurance_policy_number TEXT,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CONSTRAINT email_format CHECK (email LIKE '%_@__%.__%')
);

-- Staff table (doctors and other staff)
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('Doctor', 'Nurse', 'Technician', 'Administrative', 'Other')),
    specialization TEXT,
    license_number TEXT,
    phone TEXT,
    email TEXT NOT NULL,
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT 1,
    notes TEXT,
    CONSTRAINT email_format CHECK (email LIKE '%_@__%.__%'),
    CONSTRAINT unique_license UNIQUE (license_number)
);

-- Services offered by the center
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    base_cost DECIMAL(10, 2) NOT NULL,
    active BOOLEAN DEFAULT 1,
    CONSTRAINT unique_service_name UNIQUE (name)
);

-- Treatment plans
CREATE TABLE treatment_plans (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    created_by_staff_id INTEGER NOT NULL,
    diagnosis TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status TEXT NOT NULL CHECK(status IN ('Active', 'Completed', 'Cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (created_by_staff_id) REFERENCES staff(staff_id)
);

-- Plan services (services included in a treatment plan)
CREATE TABLE plan_services (
    plan_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    scheduled_date DATE,
    performed_date DATE,
    performed_by_staff_id INTEGER,
    notes TEXT,
    status TEXT NOT NULL CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'Rescheduled')),
    FOREIGN KEY (plan_id) REFERENCES treatment_plans(plan_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    FOREIGN KEY (performed_by_staff_id) REFERENCES staff(staff_id)
);

-- Appointments
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    service_id INTEGER,
    scheduled_datetime TIMESTAMP NOT NULL,
    duration_minutes INTEGER NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- Patient medical history
CREATE TABLE medical_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    record_date DATE NOT NULL,
    record_type TEXT NOT NULL CHECK(record_type IN ('Allergy', 'Condition', 'Medication', 'Procedure', 'Note')),
    description TEXT NOT NULL,
    severity TEXT,
    status TEXT,
    recorded_by_staff_id INTEGER,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (recorded_by_staff_id) REFERENCES staff(staff_id)
);

-- Create indexes for performance
CREATE INDEX idx_patient_name ON patients(last_name, first_name);
CREATE INDEX idx_patient_phone ON patients(phone);
CREATE INDEX idx_staff_name ON staff(last_name, first_name);
CREATE INDEX idx_treatment_plan_patient ON treatment_plans(patient_id);
CREATE INDEX idx_plan_services_plan ON plan_services(plan_id);
CREATE INDEX idx_appointments_patient ON appointments(patient_id);
CREATE INDEX idx_appointments_staff ON appointments(staff_id);
CREATE INDEX idx_appointments_datetime ON appointments(scheduled_datetime);
CREATE INDEX idx_medical_history_patient ON medical_history(patient_id);

-- Create triggers for automatic timestamps
CREATE TRIGGER update_patient_timestamp
AFTER UPDATE ON patients
FOR EACH ROW
BEGIN
    UPDATE patients SET last_updated = CURRENT_TIMESTAMP WHERE patient_id = OLD.patient_id;
END;

CREATE TRIGGER update_treatment_plan_timestamp
AFTER UPDATE ON treatment_plans
FOR EACH ROW
BEGIN
    UPDATE treatment_plans SET last_updated = CURRENT_TIMESTAMP WHERE plan_id = OLD.plan_id;
END;

CREATE TRIGGER update_appointment_timestamp
AFTER UPDATE ON appointments
FOR EACH ROW
BEGIN
    UPDATE appointments SET last_updated = CURRENT_TIMESTAMP WHERE appointment_id = OLD.appointment_id;
END;
```
