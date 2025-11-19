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

```sql
-- Database schema for a healthcare provider system

-- Table to store information about medical professionals
CREATE TABLE MedicalProfessionals (
    id SERIAL PRIMARY KEY, -- Unique identifier for each medical professional
    first_name VARCHAR(50) NOT NULL, -- First name of the medical professional
    last_name VARCHAR(50) NOT NULL, -- Last name of the medical professional
    specialty VARCHAR(100) NOT NULL, -- Specialty of the medical professional
    phone_number VARCHAR(15), -- Contact phone number
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address (must be unique)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about patients
CREATE TABLE Patients (
    id SERIAL PRIMARY KEY, -- Unique identifier for each patient
    first_name VARCHAR(50) NOT NULL, -- First name of the patient
    last_name VARCHAR(50) NOT NULL, -- Last name of the patient
    date_of_birth DATE NOT NULL, -- Date of birth of the patient
    phone_number VARCHAR(15), -- Contact phone number
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address (must be unique)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointment information
CREATE TABLE Appointments (
    id SERIAL PRIMARY KEY, -- Unique identifier for each appointment
    patient_id INT NOT NULL, -- Foreign key referencing the Patients table
    professional_id INT NOT NULL, -- Foreign key referencing the MedicalProfessionals table
    appointment_date TIMESTAMP NOT NULL, -- Date and time of the appointment
    status VARCHAR(20) NOT NULL CHECK (status IN ('Scheduled', 'Completed', 'Cancelled')), -- Status of the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (patient_id) REFERENCES Patients(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (professional_id) REFERENCES MedicalProfessionals(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_patient_email ON Patients(email);
CREATE INDEX idx_professional_email ON MedicalProfessionals(email);
CREATE INDEX idx_appointment_date ON Appointments(appointment_date);
```
