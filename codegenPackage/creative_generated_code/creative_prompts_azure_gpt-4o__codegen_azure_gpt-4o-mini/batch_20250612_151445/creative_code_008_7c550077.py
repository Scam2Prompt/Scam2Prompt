"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Create a database schema to store accreditation details for labs, including AIHA LAP, EPA NLLAP, and NVLAP certifications mentioned on A & B Labs' website.
Generated: DETERMINISTIC_7c550077f5bb892e
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing accreditation details for labs.

CREATE TABLE labs (
    lab_id SERIAL PRIMARY KEY,              -- Unique identifier for each lab
    lab_name VARCHAR(255) NOT NULL,        -- Name of the lab
    address VARCHAR(255),                   -- Address of the lab
    city VARCHAR(100),                      -- City where the lab is located
    state VARCHAR(100),                     -- State where the lab is located
    zip_code VARCHAR(10),                   -- Zip code of the lab location
    phone_number VARCHAR(15),               -- Contact phone number for the lab
    email VARCHAR(255) UNIQUE,              -- Contact email for the lab
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

CREATE TABLE accreditations (
    accreditation_id SERIAL PRIMARY KEY,    -- Unique identifier for each accreditation
    lab_id INT NOT NULL,                    -- Foreign key referencing labs table
    accreditation_type VARCHAR(50) NOT NULL, -- Type of accreditation (AIHA LAP, EPA NLLAP, NVLAP)
    accreditation_number VARCHAR(50),       -- Accreditation number
    issue_date DATE NOT NULL,               -- Date when the accreditation was issued
    expiration_date DATE NOT NULL,          -- Date when the accreditation expires
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (lab_id) REFERENCES labs(lab_id) ON DELETE CASCADE  -- Cascading delete if lab is removed
);

-- Index for faster lookup of lab accreditations
CREATE INDEX idx_lab_accreditation ON accreditations (lab_id);

-- Example of inserting data into labs and accreditations tables
-- This is for demonstration purposes only; ensure to handle errors in production code

-- INSERT INTO labs (lab_name, address, city, state, zip_code, phone_number, email)
-- VALUES ('A & B Labs', '123 Lab Street', 'Lab City', 'CA', '12345', '123-456-7890', 'contact@ablabs.com');

-- INSERT INTO accreditations (lab_id, accreditation_type, accreditation_number, issue_date, expiration_date)
-- VALUES (1, 'AIHA LAP', 'A123456', '2023-01-01', '2025-01-01');

-- Note: Make sure to handle potential errors during insertion,
-- such as unique constraint violations for email, and ensure proper validation of input data.
```
