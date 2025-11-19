"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Design a database schema to store information about surgical procedures, including cosmetic surgical, non-surgical, and reconstructive surgery details.
Generated: DETERMINISTIC_e55ddcecf73f5ba7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about surgical procedures

CREATE TABLE Surgeons (
    surgeon_id SERIAL PRIMARY KEY, -- Unique identifier for each surgeon
    first_name VARCHAR(50) NOT NULL, -- Surgeon’s first name
    last_name VARCHAR(50) NOT NULL, -- Surgeon’s last name
    specialty VARCHAR(100), -- Specialty of the surgeon (e.g., cosmetic, reconstructive)
    contact_info VARCHAR(255), -- Contact information for the surgeon
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE Patients (
    patient_id SERIAL PRIMARY KEY, -- Unique identifier for each patient
    first_name VARCHAR(50) NOT NULL, -- Patient’s first name
    last_name VARCHAR(50) NOT NULL, -- Patient’s last name
    date_of_birth DATE NOT NULL, -- Patient’s date of birth
    contact_info VARCHAR(255), -- Contact information for the patient
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE SurgicalProcedures (
    procedure_id SERIAL PRIMARY KEY, -- Unique identifier for each surgical procedure
    procedure_name VARCHAR(100) NOT NULL, -- Name of the surgical procedure
    procedure_type VARCHAR(50) NOT NULL CHECK (procedure_type IN ('Cosmetic', 'Non-Surgical', 'Reconstructive')), -- Type of procedure
    description TEXT, -- Detailed description of the procedure
    duration INT, -- Estimated duration of the procedure in minutes
    cost DECIMAL(10, 2), -- Cost of the procedure
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE Surgeries (
    surgery_id SERIAL PRIMARY KEY, -- Unique identifier for each surgery record
    patient_id INT NOT NULL, -- Foreign key referencing the Patients table
    surgeon_id INT NOT NULL, -- Foreign key referencing the Surgeons table
    procedure_id INT NOT NULL, -- Foreign key referencing the SurgicalProcedures table
    surgery_date DATE NOT NULL, -- Date of the surgery
    notes TEXT, -- Additional notes regarding the surgery
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (surgeon_id) REFERENCES Surgeons(surgeon_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (procedure_id) REFERENCES SurgicalProcedures(procedure_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_patient_id ON Surgeries(patient_id);
CREATE INDEX idx_surgeon_id ON Surgeries(surgeon_id);
CREATE INDEX idx_procedure_id ON Surgeries(procedure_id);
```
