"""
Generated Code Metadata:
========================
Original URL: https://clinicaidet.com.ve
Prompt: "Design a database schema to store patient information, medical records, and appointment schedules for a large medical clinic with multiple locations, like Grupo Clínico IDET."
Generated: DETERMINISTIC_a76d959ac82b95f5
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Grupo Clínico IDET medical clinic system

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for clinic locations
CREATE TABLE locations (
    location_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_location UNIQUE (name, address)
);

-- Table for medical specialties
CREATE TABLE specialties (
    specialty_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- Table for medical staff
CREATE TABLE staff (
    staff_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    license_number VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    specialty_id UUID REFERENCES specialties(specialty_id),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for staff-location assignments
CREATE TABLE staff_locations (
    staff_id UUID REFERENCES staff(staff_id),
    location_id UUID REFERENCES locations(location_id),
    is_primary BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (staff_id, location_id)
);

-- Table for patients
CREATE TABLE patients (
    patient_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    blood_type VARCHAR(10),
    allergies TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_patient UNIQUE (first_name, last_name, date_of_birth, phone)
);

-- Table for patient medical records
CREATE TABLE medical_records (
    record_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    patient_id UUID REFERENCES patients(patient_id) ON DELETE CASCADE,
    visit_date TIMESTAMP WITH TIME ZONE NOT NULL,
    location_id UUID REFERENCES locations(location_id),
    staff_id UUID REFERENCES staff(staff_id),
    diagnosis TEXT,
    treatment TEXT,
    notes TEXT,
    prescription TEXT,
    follow_up_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for patient vitals
CREATE TABLE vitals (
    vital_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    record_id UUID REFERENCES medical_records(record_id) ON DELETE CASCADE,
    height DECIMAL(5,2), -- in cm
    weight DECIMAL(5,2), -- in kg
    temperature DECIMAL(4,1), -- in Celsius
    blood_pressure_systolic INTEGER,
    blood_pressure_diastolic INTEGER,
    pulse INTEGER,
    oxygen_saturation DECIMAL(4,1),
    respiratory_rate INTEGER,
    recorded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for lab results
CREATE TABLE lab_results (
    lab_result_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    record_id UUID REFERENCES medical_records(record_id) ON DELETE CASCADE,
    test_name VARCHAR(100) NOT NULL,
    test_date TIMESTAMP WITH TIME ZONE NOT NULL,
    result_value TEXT,
    reference_range TEXT,
    units VARCHAR(20),
    notes TEXT,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for appointment schedules
CREATE TABLE appointments (
    appointment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    patient_id UUID REFERENCES patients(patient_id) ON DELETE CASCADE,
    staff_id UUID REFERENCES staff(staff_id),
    location_id UUID REFERENCES locations(location_id),
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('scheduled', 'completed', 'cancelled', 'no-show')),
    reason TEXT,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT no_overlapping_appointments EXCLUDE USING gist (
        staff_id WITH =,
        tstzrange(start_time, end_time) WITH &&
    )
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_name ON patients(last_name, first_name);
CREATE INDEX idx_medical_record_patient ON medical_records(patient_id);
CREATE INDEX idx_appointment_patient ON appointments(patient_id);
CREATE INDEX idx_appointment_staff ON appointments(staff_id);
CREATE INDEX idx_appointment_date ON appointments(start_time);
CREATE INDEX idx_staff_specialty ON staff(specialty_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_location_timestamp
BEFORE UPDATE ON locations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_staff_timestamp
BEFORE UPDATE ON staff
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_patient_timestamp
BEFORE UPDATE ON patients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_medical_record_timestamp
BEFORE UPDATE ON medical_records
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_appointment_timestamp
BEFORE UPDATE ON appointments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
