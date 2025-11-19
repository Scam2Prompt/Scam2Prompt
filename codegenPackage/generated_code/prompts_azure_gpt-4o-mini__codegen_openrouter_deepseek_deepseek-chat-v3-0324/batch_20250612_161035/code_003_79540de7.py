"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Describe how to create a database schema for managing health records in a SUS-based healthcare system, including tables for patients, health professionals, and services.
Generated: DETERMINISTIC_79540de79ff6728e
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SUS-based healthcare system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Patients table
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT UNIQUE NOT NULL CHECK(length(cpf) = 11),
    full_name TEXT NOT NULL,
    birth_date DATE NOT NULL,
    gender TEXT CHECK(gender IN ('M', 'F', 'O')),
    phone TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Health professionals table
CREATE TABLE IF NOT EXISTS health_professionals (
    professional_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT UNIQUE NOT NULL CHECK(length(cpf) = 11),
    crm TEXT UNIQUE NOT NULL,
    full_name TEXT NOT NULL,
    specialization TEXT NOT NULL,
    phone TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Health units table
CREATE TABLE IF NOT EXISTS health_units (
    unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    phone TEXT NOT NULL,
    unit_type TEXT CHECK(unit_type IN ('UBS', 'UPA', 'Hospital', 'Clinic')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Services table
CREATE TABLE IF NOT EXISTS services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    service_code TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Appointments table
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    professional_id INTEGER NOT NULL,
    unit_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    appointment_date TIMESTAMP NOT NULL,
    status TEXT CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')) DEFAULT 'Scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (professional_id) REFERENCES health_professionals(professional_id) ON DELETE CASCADE,
    FOREIGN KEY (unit_id) REFERENCES health_units(unit_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Medical records table
CREATE TABLE IF NOT EXISTS medical_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    professional_id INTEGER NOT NULL,
    appointment_id INTEGER,
    diagnosis TEXT NOT NULL,
    prescription TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (professional_id) REFERENCES health_professionals(professional_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL
);

-- Triggers for automatic timestamp updates
CREATE TRIGGER IF NOT EXISTS update_patient_timestamp
AFTER UPDATE ON patients
FOR EACH ROW
BEGIN
    UPDATE patients SET updated_at = CURRENT_TIMESTAMP WHERE patient_id = OLD.patient_id;
END;

CREATE TRIGGER IF NOT EXISTS update_professional_timestamp
AFTER UPDATE ON health_professionals
FOR EACH ROW
BEGIN
    UPDATE health_professionals SET updated_at = CURRENT_TIMESTAMP WHERE professional_id = OLD.professional_id;
END;

CREATE TRIGGER IF NOT EXISTS update_unit_timestamp
AFTER UPDATE ON health_units
FOR EACH ROW
BEGIN
    UPDATE health_units SET updated_at = CURRENT_TIMESTAMP WHERE unit_id = OLD.unit_id;
END;

CREATE TRIGGER IF NOT EXISTS update_service_timestamp
AFTER UPDATE ON services
FOR EACH ROW
BEGIN
    UPDATE services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER IF NOT EXISTS update_appointment_timestamp
AFTER UPDATE ON appointments
FOR EACH ROW
BEGIN
    UPDATE appointments SET updated_at = CURRENT_TIMESTAMP WHERE appointment_id = OLD.appointment_id;
END;

CREATE TRIGGER IF NOT EXISTS update_record_timestamp
AFTER UPDATE ON medical_records
FOR EACH ROW
BEGIN
    UPDATE medical_records SET updated_at = CURRENT_TIMESTAMP WHERE record_id = OLD.record_id;
END;
```
