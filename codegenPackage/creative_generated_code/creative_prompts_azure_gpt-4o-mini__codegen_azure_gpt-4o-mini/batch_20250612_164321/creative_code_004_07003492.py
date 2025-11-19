"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gyvseguros.com
Prompt: Design a database schema for storing client information and insurance policy details for a company like GYV Seguros, which specializes in various insurance products.
Generated: DETERMINISTIC_07003492c9d7781b
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for GYV Seguros to store client information and insurance policy details

CREATE DATABASE gyv_seguros;

USE gyv_seguros;

-- Table to store client information
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,                     -- Client's first name
    last_name VARCHAR(50) NOT NULL,                      -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL,                  -- Client's email address (must be unique)
    phone_number VARCHAR(15),                             -- Client's phone number (optional)
    date_of_birth DATE NOT NULL,                          -- Client's date of birth
    address VARCHAR(255),                                 -- Client's address (optional)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store insurance policy details
CREATE TABLE insurance_policies (
    policy_id INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each policy
    client_id INT NOT NULL,                               -- Foreign key referencing the client
    policy_type VARCHAR(50) NOT NULL,                    -- Type of insurance policy (e.g., Health, Auto, Home)
    policy_start_date DATE NOT NULL,                      -- Date when the policy starts
    policy_end_date DATE NOT NULL,                        -- Date when the policy ends
    premium_amount DECIMAL(10, 2) NOT NULL,              -- Amount to be paid for the policy
    coverage_amount DECIMAL(10, 2),                       -- Amount covered by the policy
    status ENUM('active', 'inactive', 'expired') DEFAULT 'active', -- Status of the policy
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensure related record deletion
);

-- Table to store claims associated with policies
CREATE TABLE claims (
    claim_id INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for each claim
    policy_id INT NOT NULL,                               -- Foreign key referencing the insurance policy
    claim_date DATE NOT NULL,                             -- Date of the claim
    claim_amount DECIMAL(10, 2) NOT NULL,                -- Amount claimed
    claim_status ENUM('pending', 'approved', 'denied') DEFAULT 'pending', -- Status of the claim
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (policy_id) REFERENCES insurance_policies(policy_id) ON DELETE CASCADE -- Ensure related record deletion
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON clients (email);
CREATE INDEX idx_policy_client ON insurance_policies (client_id);
CREATE INDEX idx_claim_policy ON claims (policy_id);
```
