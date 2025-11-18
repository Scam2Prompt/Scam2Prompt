"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luxteb.com
Prompt: Create a database schema for storing patient records in a digital format, including custom fields for dental quadrant annotations, inspired by LuxChart functionality in Luxteb.
Generated: DETERMINISTIC_59a3c6c21d3e1dcb
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing patient records

CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,  -- Unique identifier for each patient
    first_name VARCHAR(50) NOT NULL,  -- Patient's first name
    last_name VARCHAR(50) NOT NULL,  -- Patient's last name
    date_of_birth DATE NOT NULL,  -- Patient's date of birth
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')),  -- Patient's gender
    phone_number VARCHAR(15),  -- Patient's phone number
    email VARCHAR(100) UNIQUE,  -- Patient's email address (must be unique)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

CREATE TABLE dental_records (
    record_id SERIAL PRIMARY KEY,  -- Unique identifier for each dental record
    patient_id INT NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE,  -- Foreign key referencing patients
    visit_date DATE NOT NULL,  -- Date of the dental visit
    notes TEXT,  -- Notes from the dentist regarding the visit
    quadrant_1 VARCHAR(255),  -- Annotation for upper right quadrant
    quadrant_2 VARCHAR(255),  -- Annotation for upper left quadrant
    quadrant_3 VARCHAR(255),  -- Annotation for lower left quadrant
    quadrant_4 VARCHAR(255),  -- Annotation for lower right quadrant
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    CONSTRAINT chk_visit_date CHECK (visit_date <= CURRENT_DATE)  -- Ensure visit date is not in the future
);

CREATE TABLE allergies (
    allergy_id SERIAL PRIMARY KEY,  -- Unique identifier for each allergy record
    patient_id INT NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE,  -- Foreign key referencing patients
    allergy_name VARCHAR(100) NOT NULL,  -- Name of the allergy
    severity VARCHAR(50) CHECK (severity IN ('Mild', 'Moderate', 'Severe')),  -- Severity of the allergy
    notes TEXT,  -- Additional notes about the allergy
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

CREATE TABLE medications (
    medication_id SERIAL PRIMARY KEY,  -- Unique identifier for each medication record
    patient_id INT NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE,  -- Foreign key referencing patients
    medication_name VARCHAR(100) NOT NULL,  -- Name of the medication
    dosage VARCHAR(50) NOT NULL,  -- Dosage of the medication
    frequency VARCHAR(50),  -- Frequency of medication intake
    start_date DATE NOT NULL,  -- Start date of medication
    end_date DATE,  -- End date of medication (nullable)
    notes TEXT,  -- Additional notes about the medication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Indexing patient records for performance improvement
CREATE INDEX idx_patient_last_name ON patients (last_name);
CREATE INDEX idx_patient_email ON patients (email);
```
