"""
Generated Code Metadata:
========================
Original URL: https://ayb-sd.org
Prompt: "Design a database schema to store information about beneficiaries, projects, and donations for an organization like Ayb-Sd.org."
Generated: DETERMINISTIC_203ba8d3d7c2f2cb
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about beneficiaries, projects, and donations

-- Create a table to store information about beneficiaries
CREATE TABLE Beneficiaries (
    beneficiary_id SERIAL PRIMARY KEY, -- Unique identifier for each beneficiary
    name VARCHAR(100) NOT NULL,         -- Name of the beneficiary
    email VARCHAR(100) UNIQUE NOT NULL, -- Email of the beneficiary
    phone VARCHAR(15),                  -- Phone number of the beneficiary
    address TEXT,                       -- Address of the beneficiary
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store information about projects
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,      -- Unique identifier for each project
    title VARCHAR(200) NOT NULL,        -- Title of the project
    description TEXT,                   -- Description of the project
    start_date DATE NOT NULL,           -- Start date of the project
    end_date DATE,                      -- End date of the project (nullable)
    beneficiary_id INT NOT NULL,        -- Foreign key referencing Beneficiaries
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (beneficiary_id) REFERENCES Beneficiaries(beneficiary_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store information about donations
CREATE TABLE Donations (
    donation_id SERIAL PRIMARY KEY,      -- Unique identifier for each donation
    amount DECIMAL(10, 2) NOT NULL,     -- Amount of the donation
    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the donation
    donor_name VARCHAR(100) NOT NULL,    -- Name of the donor
    project_id INT NOT NULL,             -- Foreign key referencing Projects
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the email column in Beneficiaries for faster lookups
CREATE INDEX idx_beneficiary_email ON Beneficiaries(email);

-- Create an index on the donation_date column in Donations for faster queries
CREATE INDEX idx_donation_date ON Donations(donation_date);
```
