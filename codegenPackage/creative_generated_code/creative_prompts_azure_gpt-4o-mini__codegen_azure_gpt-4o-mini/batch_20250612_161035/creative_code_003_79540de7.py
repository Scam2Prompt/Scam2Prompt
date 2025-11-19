"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Describe how to create a database schema for managing health records in a SUS-based healthcare system, including tables for patients, health professionals, and services.
Generated: DETERMINISTIC_79540de79ff6728e
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing health records in a SUS-based healthcare system

-- Create a schema for the healthcare system
CREATE SCHEMA sus_healthcare;

-- Table to store patient information
CREATE TABLE sus_healthcare.patients (
    patient_id SERIAL PRIMARY KEY,  -- Unique identifier for each patient
    first_name VARCHAR(50) NOT NULL,  -- Patient's first name
    last_name VARCHAR(50) NOT NULL,  -- Patient's last name
    date_of_birth DATE NOT NULL,  -- Patient's date of birth
    gender VARCHAR(10),  -- Patient's gender
    address TEXT,  -- Patient's address
    phone_number VARCHAR(15),  -- Patient's phone number
    email VARCHAR(100) UNIQUE,  -- Patient's email, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store health professional information
CREATE TABLE sus_healthcare.health_professionals (
    professional_id SERIAL PRIMARY KEY,  -- Unique identifier for each health professional
    first_name VARCHAR(50) NOT NULL,  -- Professional's first name
    last_name VARCHAR(50) NOT NULL,  -- Professional's last name
    specialty VARCHAR(50),  -- Professional's specialty (e.g., doctor, nurse)
    license_number VARCHAR(50) UNIQUE NOT NULL,  -- Professional's license number, must be unique
    phone_number VARCHAR(15),  -- Professional's phone number
    email VARCHAR(100) UNIQUE,  -- Professional's email, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about services provided
CREATE TABLE sus_healthcare.services (
    service_id SERIAL PRIMARY KEY,  -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL,  -- Name of the service
    description TEXT,  -- Description of the service
    cost DECIMAL(10, 2) NOT NULL,  -- Cost of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to link patients with health professionals and services
CREATE TABLE sus_healthcare.health_records (
    record_id SERIAL PRIMARY KEY,  -- Unique identifier for each health record
    patient_id INT NOT NULL,  -- Reference to the patient
    professional_id INT NOT NULL,  -- Reference to the health professional
    service_id INT NOT NULL,  -- Reference to the service provided
    appointment_date TIMESTAMP NOT NULL,  -- Date of the appointment
    notes TEXT,  -- Notes regarding the health record
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (patient_id) REFERENCES sus_healthcare.patients(patient_id) ON DELETE CASCADE,  -- Ensure referential integrity for patients
    FOREIGN KEY (professional_id) REFERENCES sus_healthcare.health_professionals(professional_id) ON DELETE CASCADE,  -- Ensure referential integrity for health professionals
    FOREIGN KEY (service_id) REFERENCES sus_healthcare.services(service_id) ON DELETE CASCADE  -- Ensure referential integrity for services
);
```
