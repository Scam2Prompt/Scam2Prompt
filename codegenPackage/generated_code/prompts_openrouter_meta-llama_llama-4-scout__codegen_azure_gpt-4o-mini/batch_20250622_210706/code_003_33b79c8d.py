"""
Generated Code Metadata:
========================
Original URL: https://ai-rex.xyz
Prompt: Design a simple database schema using SQL for a website that manages domain names and their hosting status, like the one seemingly planned for ai-rex.xyz on Porkbun.com.
Generated: DETERMINISTIC_33b79c8d1bc76d9d
Batch ID: 20250622_210706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing domain names and their hosting status

-- Create a table to store information about domain names
CREATE TABLE domains (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each domain
    domain_name VARCHAR(255) NOT NULL,   -- The domain name (e.g., example.com)
    registration_date DATE NOT NULL,      -- Date when the domain was registered
    expiration_date DATE NOT NULL,        -- Date when the domain registration expires
    status VARCHAR(50) NOT NULL,          -- Current status of the domain (e.g., active, expired, pending)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store hosting information related to domains
CREATE TABLE hosting (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each hosting record
    domain_id INT NOT NULL,               -- Foreign key referencing the domains table
    hosting_provider VARCHAR(255) NOT NULL, -- Name of the hosting provider (e.g., AWS, DigitalOcean)
    plan VARCHAR(100) NOT NULL,           -- Hosting plan type (e.g., shared, VPS, dedicated)
    start_date DATE NOT NULL,             -- Date when hosting started
    end_date DATE,                        -- Date when hosting ends (NULL if ongoing)
    status VARCHAR(50) NOT NULL,          -- Current status of the hosting (e.g., active, suspended)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (domain_id) REFERENCES domains(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the domain_name column for faster lookups
CREATE INDEX idx_domain_name ON domains(domain_name);

-- Create an index on the domain_id column in the hosting table for faster lookups
CREATE INDEX idx_domain_id ON hosting(domain_id);
```
