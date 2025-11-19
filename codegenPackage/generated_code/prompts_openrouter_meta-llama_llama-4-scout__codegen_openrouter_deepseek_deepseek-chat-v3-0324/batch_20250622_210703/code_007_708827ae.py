"""
Generated Code Metadata:
========================
Original URL: https://www.spanisheyeclinic.com
Prompt: Create a simple database schema to store information about eye surgeries, including LASIK, cataract, and keratoconus treatments, with fields for patient details and surgery specifics.
Generated: DETERMINISTIC_708827ae14198170
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for eye surgery clinic
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code VARCHAR(20),
    country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE eye_conditions (
    condition_id SERIAL PRIMARY KEY,
    condition_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Pre-populate common eye conditions
INSERT INTO eye_conditions (condition_name, description) VALUES
    ('Myopia', 'Nearsightedness'),
    ('Hyperopia', 'Farsightedness'),
    ('Astigmatism', 'Irregular cornea shape'),
    ('Presbyopia', 'Age-related farsightedness'),
    ('Keratoconus', 'Corneal thinning and bulging'),
    ('Cataract', 'Clouding of the eye lens');

CREATE TABLE surgeries (
    surgery_id SERIAL PRIMARY KEY,
    surgery_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    average_duration_minutes INT,
    recovery_time_days INT
);

-- Pre-populate common eye surgeries
INSERT INTO surgeries (surgery_name, description, average_duration_minutes, recovery_time_days) VALUES
    ('LASIK', 'Laser-assisted in situ keratomileusis', 15, 3),
    ('PRK', 'Photorefractive keratectomy', 15, 7),
    ('Cataract Surgery', 'Removal of cloudy lens and replacement with artificial lens', 30, 14),
    ('Corneal Cross-Linking', 'Treatment for keratoconus', 60, 30),
    ('ICL', 'Implantable Collamer Lens', 30, 7),
    ('PTK', 'Phototherapeutic keratectomy', 20, 14);

CREATE TABLE patient_conditions (
    patient_condition_id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE,
    condition_id INT NOT NULL REFERENCES eye_conditions(condition_id) ON DELETE CASCADE,
    diagnosis_date DATE NOT NULL,
    severity VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE patient_surgeries (
    surgery_record_id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE,
    surgery_id INT NOT NULL REFERENCES surgeries(surgery_id) ON DELETE CASCADE,
    surgeon_name VARCHAR(200) NOT NULL,
    surgery_date TIMESTAMP NOT NULL,
    pre_op_vision VARCHAR(20),
    post_op_vision VARCHAR(20),
    anesthesia_type VARCHAR(100),
    complications TEXT,
    follow_up_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE surgery_medications (
    medication_id SERIAL PRIMARY KEY,
    surgery_id INT NOT NULL REFERENCES surgeries(surgery_id) ON DELETE CASCADE,
    medication_name VARCHAR(200) NOT NULL,
    purpose VARCHAR(200),
    dosage VARCHAR(100),
    frequency VARCHAR(100),
    duration_days INT
);

-- Create indexes for performance
CREATE INDEX idx_patient_surgeries_patient_id ON patient_surgeries(patient_id);
CREATE INDEX idx_patient_surgeries_surgery_id ON patient_surgeries(surgery_id);
CREATE INDEX idx_patient_conditions_patient_id ON patient_conditions(patient_id);
CREATE INDEX idx_patient_conditions_condition_id ON patient_conditions(condition_id);

-- Create a function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for automatic timestamp updates
CREATE TRIGGER update_patient_timestamp
BEFORE UPDATE ON patients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_patient_condition_timestamp
BEFORE UPDATE ON patient_conditions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_patient_surgery_timestamp
BEFORE UPDATE ON patient_surgeries
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
