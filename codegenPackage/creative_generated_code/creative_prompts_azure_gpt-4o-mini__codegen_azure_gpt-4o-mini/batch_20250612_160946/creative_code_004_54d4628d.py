"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Design a database schema in SQL to manage the records of beneficiaries receiving support from the Rakhshanda Memorial's medical camps and psychological health services.
Generated: DETERMINISTIC_54d4628dca4aeffc
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing beneficiaries of Rakhshanda Memorial's medical camps and psychological health services

-- Create a table to store beneficiary information
CREATE TABLE Beneficiaries (
    beneficiary_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each beneficiary
    first_name VARCHAR(100) NOT NULL,               -- First name of the beneficiary
    last_name VARCHAR(100) NOT NULL,                 -- Last name of the beneficiary
    date_of_birth DATE NOT NULL,                     -- Date of birth of the beneficiary
    gender ENUM('Male', 'Female', 'Other') NOT NULL,-- Gender of the beneficiary
    contact_number VARCHAR(15) UNIQUE NOT NULL,     -- Unique contact number
    email VARCHAR(255) UNIQUE,                       -- Email address (optional)
    address TEXT NOT NULL,                           -- Address of the beneficiary
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store medical camp records
CREATE TABLE Medical_Camps (
    camp_id INT PRIMARY KEY AUTO_INCREMENT,           -- Unique identifier for each medical camp
    camp_name VARCHAR(255) NOT NULL,                 -- Name of the medical camp
    camp_date DATE NOT NULL,                          -- Date of the medical camp
    location VARCHAR(255) NOT NULL,                  -- Location of the medical camp
    services_offered TEXT,                            -- Description of services offered
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a junction table to link beneficiaries with medical camps
CREATE TABLE Beneficiary_Medical_Camp (
    beneficiary_id INT NOT NULL,                      -- ID of the beneficiary
    camp_id INT NOT NULL,                             -- ID of the medical camp
    PRIMARY KEY (beneficiary_id, camp_id),          -- Composite primary key
    FOREIGN KEY (beneficiary_id) REFERENCES Beneficiaries(beneficiary_id) ON DELETE CASCADE,  -- Foreign key reference to Beneficiaries
    FOREIGN KEY (camp_id) REFERENCES Medical_Camps(camp_id) ON DELETE CASCADE  -- Foreign key reference to Medical_Camps
);

-- Create a table to store psychological health service records
CREATE TABLE Psychological_Health_Services (
    service_id INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each service record
    beneficiary_id INT NOT NULL,                       -- ID of the beneficiary receiving the service
    service_date DATE NOT NULL,                        -- Date of the service provided
    service_type VARCHAR(255) NOT NULL,               -- Type of psychological service
    notes TEXT,                                       -- Notes regarding the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (beneficiary_id) REFERENCES Beneficiaries(beneficiary_id) ON DELETE CASCADE  -- Foreign key reference to Beneficiaries
);

-- Create an index on contact_number for faster lookups
CREATE INDEX idx_contact_number ON Beneficiaries(contact_number);

-- Create an index on email for faster lookups
CREATE INDEX idx_email ON Beneficiaries(email);
```
