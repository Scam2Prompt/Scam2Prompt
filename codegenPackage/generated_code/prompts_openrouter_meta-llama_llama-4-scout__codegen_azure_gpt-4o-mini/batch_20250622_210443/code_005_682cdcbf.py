"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Design a database schema to store information about independent pharmacies, their owners, and their patients, considering the requirements of a member-owned co-operative structure.
Generated: DETERMINISTIC_682cdcbfa29b502c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a member-owned co-operative structure for independent pharmacies

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Owners;
DROP TABLE IF EXISTS Pharmacies;

-- Table to store information about pharmacies
CREATE TABLE Pharmacies (
    pharmacy_id SERIAL PRIMARY KEY, -- Unique identifier for each pharmacy
    name VARCHAR(255) NOT NULL, -- Name of the pharmacy
    address VARCHAR(255) NOT NULL, -- Address of the pharmacy
    phone_number VARCHAR(15), -- Contact number for the pharmacy
    email VARCHAR(255), -- Email address for the pharmacy
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the pharmacy was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about pharmacy owners
CREATE TABLE Owners (
    owner_id SERIAL PRIMARY KEY, -- Unique identifier for each owner
    pharmacy_id INT NOT NULL, -- Foreign key referencing the pharmacy
    name VARCHAR(255) NOT NULL, -- Name of the owner
    email VARCHAR(255) UNIQUE NOT NULL, -- Unique email address for the owner
    phone_number VARCHAR(15), -- Contact number for the owner
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the owner was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (pharmacy_id) REFERENCES Pharmacies(pharmacy_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about patients
CREATE TABLE Patients (
    patient_id SERIAL PRIMARY KEY, -- Unique identifier for each patient
    pharmacy_id INT NOT NULL, -- Foreign key referencing the pharmacy
    name VARCHAR(255) NOT NULL, -- Name of the patient
    date_of_birth DATE NOT NULL, -- Date of birth of the patient
    email VARCHAR(255) UNIQUE NOT NULL, -- Unique email address for the patient
    phone_number VARCHAR(15), -- Contact number for the patient
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the patient was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (pharmacy_id) REFERENCES Pharmacies(pharmacy_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_pharmacy_name ON Pharmacies(name);
CREATE INDEX idx_owner_email ON Owners(email);
CREATE INDEX idx_patient_email ON Patients(email);
```
