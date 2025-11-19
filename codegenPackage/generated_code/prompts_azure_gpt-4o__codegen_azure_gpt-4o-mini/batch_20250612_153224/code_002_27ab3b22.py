"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Create a database schema for storing information about beneficiaries of social programs, including fields for personal details, program participation, and reintegration status, inspired by Fundación Munasim Kullakita's initiatives.
Generated: DETERMINISTIC_27ab3b22b83065fd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about beneficiaries of social programs
-- Inspired by Fundación Munasim Kullakita's initiatives

CREATE TABLE beneficiaries (
    beneficiary_id SERIAL PRIMARY KEY, -- Unique identifier for each beneficiary
    first_name VARCHAR(50) NOT NULL,   -- Beneficiary's first name
    last_name VARCHAR(50) NOT NULL,    -- Beneficiary's last name
    date_of_birth DATE NOT NULL,        -- Beneficiary's date of birth
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')), -- Gender of the beneficiary
    address TEXT NOT NULL,              -- Address of the beneficiary
    phone_number VARCHAR(15),           -- Phone number of the beneficiary
    email VARCHAR(100) UNIQUE,          -- Email address of the beneficiary
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE programs (
    program_id SERIAL PRIMARY KEY,      -- Unique identifier for each program
    program_name VARCHAR(100) NOT NULL, -- Name of the social program
    description TEXT,                   -- Description of the program
    start_date DATE NOT NULL,           -- Start date of the program
    end_date DATE,                      -- End date of the program (nullable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE participation (
    participation_id SERIAL PRIMARY KEY, -- Unique identifier for each participation record
    beneficiary_id INT NOT NULL,         -- Foreign key referencing beneficiaries
    program_id INT NOT NULL,             -- Foreign key referencing programs
    participation_date DATE NOT NULL,    -- Date of participation
    status VARCHAR(20) CHECK (status IN ('Active', 'Completed', 'Dropped')), -- Status of participation
    reintegration_status VARCHAR(20) CHECK (reintegration_status IN ('Pending', 'Successful', 'Failed')), -- Reintegration status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_beneficiary_last_name ON beneficiaries(last_name);
CREATE INDEX idx_program_name ON programs(program_name);
CREATE INDEX idx_participation_status ON participation(status);
```
