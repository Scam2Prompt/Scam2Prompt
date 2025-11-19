"""
Generated Code Metadata:
========================
Original URL: https://sand.claims
Prompt: Design a basic database schema for storing information about claims, including fields for claimant details, claim status, and dates, which could be managed through a site like sand.claims.
Generated: DETERMINISTIC_87853e7ea4b38553
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a basic database schema for storing information about claims

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Claims;
DROP TABLE IF EXISTS Claimants;

-- Create a table to store claimant details
CREATE TABLE Claimants (
    claimant_id SERIAL PRIMARY KEY, -- Unique identifier for each claimant
    first_name VARCHAR(50) NOT NULL, -- First name of the claimant
    last_name VARCHAR(50) NOT NULL, -- Last name of the claimant
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address of the claimant
    phone_number VARCHAR(15), -- Phone number of the claimant
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the claimant was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store claims information
CREATE TABLE Claims (
    claim_id SERIAL PRIMARY KEY, -- Unique identifier for each claim
    claimant_id INT NOT NULL, -- Foreign key referencing the claimant
    claim_status VARCHAR(20) NOT NULL CHECK (claim_status IN ('Pending', 'Approved', 'Rejected')), -- Status of the claim
    claim_date DATE NOT NULL, -- Date when the claim was filed
    resolution_date DATE, -- Date when the claim was resolved (if applicable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the claim was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (claimant_id) REFERENCES Claimants(claimant_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_claimant_email ON Claimants(email);
CREATE INDEX idx_claim_status ON Claims(claim_status);
```
