"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Design a database schema to store information on the beneficiaries of Fundación Munasim Kullakita, including demographic data, services provided, and outcomes.
Generated: DETERMINISTIC_ccf3c86d35c79ca5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Fundación Munasim Kullakita beneficiaries

-- Create a database for the foundation
CREATE DATABASE IF NOT EXISTS munasim_kullakita;

-- Use the created database
USE munasim_kullakita;

-- Table to store beneficiary demographic data
CREATE TABLE IF NOT EXISTS beneficiaries (
    beneficiary_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each beneficiary
    first_name VARCHAR(50) NOT NULL,              -- Beneficiary's first name
    last_name VARCHAR(50) NOT NULL,                -- Beneficiary's last name
    date_of_birth DATE NOT NULL,                   -- Beneficiary's date of birth
    gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Beneficiary's gender
    address VARCHAR(255),                           -- Beneficiary's address
    phone_number VARCHAR(15),                       -- Beneficiary's phone number
    email VARCHAR(100),                             -- Beneficiary's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services provided to beneficiaries
CREATE TABLE IF NOT EXISTS services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL,             -- Name of the service provided
    description TEXT,                                -- Description of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Record creation timestamp
);

-- Table to store outcomes of services provided to beneficiaries
CREATE TABLE IF NOT EXISTS outcomes (
    outcome_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each outcome
    beneficiary_id INT NOT NULL,                     -- Foreign key referencing beneficiaries
    service_id INT NOT NULL,                         -- Foreign key referencing services
    outcome_description TEXT,                        -- Description of the outcome
    outcome_date DATE NOT NULL,                      -- Date of the outcome
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_beneficiary_name ON beneficiaries (last_name, first_name);
CREATE INDEX idx_service_name ON services (service_name);
CREATE INDEX idx_outcome_date ON outcomes (outcome_date);
```
