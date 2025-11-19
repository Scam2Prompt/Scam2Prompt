"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Design a database schema in SQL for managing the records of beneficiaries in the Fundación Munasim Kullakita's programs, ensuring it supports data on treatment, education, and reintegration efforts.
Generated: DETERMINISTIC_e5531a0dd373882f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing beneficiaries in Fundación Munasim Kullakita's programs

-- Create a table to store information about beneficiaries
CREATE TABLE Beneficiaries (
    beneficiary_id SERIAL PRIMARY KEY, -- Unique identifier for each beneficiary
    first_name VARCHAR(50) NOT NULL,   -- Beneficiary's first name
    last_name VARCHAR(50) NOT NULL,    -- Beneficiary's last name
    date_of_birth DATE NOT NULL,        -- Beneficiary's date of birth
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')), -- Gender of the beneficiary
    contact_number VARCHAR(15),         -- Contact number of the beneficiary
    email VARCHAR(100),                 -- Email address of the beneficiary
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store treatment records
CREATE TABLE Treatments (
    treatment_id SERIAL PRIMARY KEY,     -- Unique identifier for each treatment record
    beneficiary_id INT NOT NULL,         -- Foreign key referencing the beneficiary
    treatment_type VARCHAR(100) NOT NULL, -- Type of treatment provided
    treatment_date DATE NOT NULL,        -- Date when the treatment was provided
    provider_name VARCHAR(100),          -- Name of the treatment provider
    notes TEXT,                          -- Additional notes about the treatment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (beneficiary_id) REFERENCES Beneficiaries(beneficiary_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store education records
CREATE TABLE Education (
    education_id SERIAL PRIMARY KEY,     -- Unique identifier for each education record
    beneficiary_id INT NOT NULL,         -- Foreign key referencing the beneficiary
    institution_name VARCHAR(100) NOT NULL, -- Name of the educational institution
    program_name VARCHAR(100) NOT NULL, -- Name of the program or course
    enrollment_date DATE NOT NULL,       -- Date of enrollment
    graduation_date DATE,                 -- Date of graduation (nullable)
    status VARCHAR(20) CHECK (status IN ('Enrolled', 'Graduated', 'Dropped Out')), -- Current status of the education
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (beneficiary_id) REFERENCES Beneficiaries(beneficiary_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store reintegration efforts
CREATE TABLE Reintegration (
    reintegration_id SERIAL PRIMARY KEY, -- Unique identifier for each reintegration record
    beneficiary_id INT NOT NULL,         -- Foreign key referencing the beneficiary
    program_name VARCHAR(100) NOT NULL, -- Name of the reintegration program
    start_date DATE NOT NULL,            -- Start date of the reintegration program
    end_date DATE,                       -- End date of the reintegration program (nullable)
    outcome VARCHAR(100),                -- Outcome of the reintegration effort
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (beneficiary_id) REFERENCES Beneficiaries(beneficiary_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the Beneficiaries table for faster searches by last name
CREATE INDEX idx_last_name ON Beneficiaries(last_name);

-- Create an index on the Treatments table for faster searches by treatment date
CREATE INDEX idx_treatment_date ON Treatments(treatment_date);

-- Create an index on the Education table for faster searches by institution name
CREATE INDEX idx_institution_name ON Education(institution_name);

-- Create an index on the Reintegration table for faster searches by program name
CREATE INDEX idx_program_name ON Reintegration(program_name);
```
