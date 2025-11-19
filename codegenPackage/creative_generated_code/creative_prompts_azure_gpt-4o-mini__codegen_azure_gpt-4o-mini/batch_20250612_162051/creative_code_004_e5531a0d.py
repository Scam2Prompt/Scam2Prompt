"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Design a database schema in SQL for managing the records of beneficiaries in the Fundación Munasim Kullakita's programs, ensuring it supports data on treatment, education, and reintegration efforts.
Generated: DETERMINISTIC_e5531a0dd373882f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing records of beneficiaries in Fundación Munasim Kullakita's programs

-- Create a schema for the foundation
CREATE SCHEMA IF NOT EXISTS munasim_kullakita;

-- Table to store beneficiary information
CREATE TABLE IF NOT EXISTS munasim_kullakita.beneficiaries (
    beneficiary_id SERIAL PRIMARY KEY, -- Unique identifier for each beneficiary
    first_name VARCHAR(100) NOT NULL, -- Beneficiary's first name
    last_name VARCHAR(100) NOT NULL, -- Beneficiary's last name
    date_of_birth DATE NOT NULL, -- Beneficiary's date of birth
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')), -- Beneficiary's gender
    contact_info VARCHAR(255), -- Optional contact information
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store treatment records
CREATE TABLE IF NOT EXISTS munasim_kullakita.treatment_records (
    treatment_id SERIAL PRIMARY KEY, -- Unique identifier for each treatment record
    beneficiary_id INT NOT NULL, -- Foreign key referencing the beneficiaries table
    treatment_type VARCHAR(100) NOT NULL, -- Type of treatment provided
    treatment_date DATE NOT NULL, -- Date of treatment
    provider_name VARCHAR(255) NOT NULL, -- Name of the treatment provider
    notes TEXT, -- Additional notes about the treatment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for creating record
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (beneficiary_id) REFERENCES munasim_kullakita.beneficiaries(beneficiary_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store education records
CREATE TABLE IF NOT EXISTS munasim_kullakita.education_records (
    education_id SERIAL PRIMARY KEY, -- Unique identifier for each education record
    beneficiary_id INT NOT NULL, -- Foreign key referencing the beneficiaries table
    program_name VARCHAR(255) NOT NULL, -- Name of the educational program
    enrollment_date DATE NOT NULL, -- Date of enrollment in the program
    completion_date DATE, -- Date of program completion
    status VARCHAR(50) CHECK (status IN ('Enrolled', 'Completed', 'Dropped')), -- Status of the beneficiary in the program
    notes TEXT, -- Additional notes regarding the education
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for creating record
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (beneficiary_id) REFERENCES munasim_kullakita.beneficiaries(beneficiary_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store reintegration efforts
CREATE TABLE IF NOT EXISTS munasim_kullakita.reintegration_efforts (
    reintegration_id SERIAL PRIMARY KEY, -- Unique identifier for each reintegration effort
    beneficiary_id INT NOT NULL, -- Foreign key referencing the beneficiaries table
    support_type VARCHAR(100) NOT NULL, -- Type of support provided (e.g., housing, job placement)
    support_date DATE NOT NULL, -- Date when support was provided
    provider_name VARCHAR(255) NOT NULL, -- Name of the provider offering the support
    success_status BOOLEAN NOT NULL DEFAULT FALSE, -- Indicates if the reintegration effort was successful
    notes TEXT, -- Additional notes regarding the reintegration effort
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for creating record
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (beneficiary_id) REFERENCES munasim_kullakita.beneficiaries(beneficiary_id) ON DELETE CASCADE -- Ensures referential integrity
);
```
