"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Create a database schema for storing information about beneficiaries of social programs, including fields for personal details, program participation, and reintegration status, inspired by Fundación Munasim Kullakita's initiatives.
Generated: DETERMINISTIC_27ab3b22b83065fd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about beneficiaries of social programs

CREATE TABLE beneficiaries (
    id SERIAL PRIMARY KEY,                          -- Unique identifier for each beneficiary
    first_name VARCHAR(50) NOT NULL,               -- Beneficiary's first name
    last_name VARCHAR(50) NOT NULL,                 -- Beneficiary's last name
    date_of_birth DATE NOT NULL,                    -- Beneficiary's date of birth
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')),  -- Beneficiary's gender
    contact_number VARCHAR(15),                     -- Beneficiary's contact number
    email VARCHAR(100) UNIQUE,                      -- Beneficiary's email address
    address TEXT,                                   -- Beneficiary's residential address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

CREATE TABLE programs (
    id SERIAL PRIMARY KEY,                          -- Unique identifier for each program
    program_name VARCHAR(100) NOT NULL,            -- Name of the social program
    description TEXT,                               -- Description of the program
    start_date DATE NOT NULL,                       -- Program start date
    end_date DATE NOT NULL,                         -- Program end date
    status VARCHAR(20) CHECK (status IN ('Active', 'Inactive', 'Completed')) -- Program status
);

CREATE TABLE beneficiary_programs (
    id SERIAL PRIMARY KEY,                          -- Unique identifier for each record
    beneficiary_id INT REFERENCES beneficiaries(id) ON DELETE CASCADE, -- Reference to beneficiary
    program_id INT REFERENCES programs(id) ON DELETE CASCADE,           -- Reference to program
    participation_date DATE NOT NULL,              -- Date of participation in the program
    reintegration_status VARCHAR(20) CHECK (reintegration_status IN ('Pending', 'Successful', 'Unsuccessful')), -- Reintegration status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    UNIQUE (beneficiary_id, program_id)            -- Ensures a beneficiary can participate in a program only once
);

-- Index for fast lookups
CREATE INDEX idx_beneficiary_last_name ON beneficiaries(last_name);
CREATE INDEX idx_program_name ON programs(program_name);
CREATE INDEX idx_participation ON beneficiary_programs(beneficiary_id, program_id);
```
