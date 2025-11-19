"""
Generated Code Metadata:
========================
Original URL: https://draisabelanobre.com.br
Prompt: "Generate a SQL database schema to store information about patients, procedures, and appointments for a facial harmonization clinic like Dra. Isabela Nobre's."
Generated: DETERMINISTIC_ec6dd14fe0626da0
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Facial Harmonization Clinic

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Procedures;
DROP TABLE IF EXISTS Patients;

-- Table to store patient information
CREATE TABLE Patients (
    patient_id SERIAL PRIMARY KEY, -- Unique identifier for each patient
    first_name VARCHAR(50) NOT NULL, -- Patient's first name
    last_name VARCHAR(50) NOT NULL, -- Patient's last name
    date_of_birth DATE NOT NULL, -- Patient's date of birth
    gender VARCHAR(10), -- Patient's gender
    phone_number VARCHAR(15), -- Patient's contact number
    email VARCHAR(100), -- Patient's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store procedure information
CREATE TABLE Procedures (
    procedure_id SERIAL PRIMARY KEY, -- Unique identifier for each procedure
    procedure_name VARCHAR(100) NOT NULL, -- Name of the procedure
    description TEXT, -- Description of the procedure
    duration INT NOT NULL, -- Duration of the procedure in minutes
    cost DECIMAL(10, 2) NOT NULL, -- Cost of the procedure
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointment information
CREATE TABLE Appointments (
    appointment_id SERIAL PRIMARY KEY, -- Unique identifier for each appointment
    patient_id INT NOT NULL, -- Foreign key referencing Patients table
    procedure_id INT NOT NULL, -- Foreign key referencing Procedures table
    appointment_date TIMESTAMP NOT NULL, -- Date and time of the appointment
    status VARCHAR(20) NOT NULL CHECK (status IN ('Scheduled', 'Completed', 'Cancelled')), -- Status of the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (procedure_id) REFERENCES Procedures(procedure_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_patient_email ON Patients(email);
CREATE INDEX idx_procedure_name ON Procedures(procedure_name);
CREATE INDEX idx_appointment_date ON Appointments(appointment_date);
```
