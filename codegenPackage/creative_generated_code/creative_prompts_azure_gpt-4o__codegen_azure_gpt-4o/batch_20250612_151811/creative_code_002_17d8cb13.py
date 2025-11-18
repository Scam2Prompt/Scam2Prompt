"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Create a database schema for KEK Insurance Brokers to manage customer information, insurance policies (e.g., accident insurance, liability insurance), and claims processing, based on the services mentioned on their site.
Generated: DETERMINISTIC_17d8cb13e724e886
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- KEK Insurance Brokers Database Schema
-- This schema includes tables to manage customers, insurance policies, and claims for an insurance system.

-- Create the customers table to store customer information
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL,            -- Customer's first name
    last_name VARCHAR(50) NOT NULL,             -- Customer's last name
    email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email (must be unique)
    phone_number VARCHAR(15),                   -- Customer's phone number
    address TEXT,                               -- Customer's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create the insurance_policies table to store information about insurance policies
CREATE TABLE insurance_policies (
    policy_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each policy
    customer_id INT NOT NULL,                  -- Foreign key referencing customers table
    policy_type ENUM('Accident Insurance', 'Liability Insurance', 'Property Insurance') NOT NULL, -- Type of policy
    coverage_amount DECIMAL(10, 2) NOT NULL,   -- Coverage amount for the policy
    premium DECIMAL(10, 2) NOT NULL,           -- Premium amount
    start_date DATE NOT NULL,                  -- Policy start date
    end_date DATE NOT NULL,                    -- Policy end date
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Policy creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) -- Relationship with customers table
);

-- Create the claims table to store information about claims processing
CREATE TABLE claims (
    claim_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each claim
    policy_id INT NOT NULL,                    -- Foreign key referencing insurance_policies table
    claim_date DATE NOT NULL,                  -- Date the claim was filed
    claim_amount DECIMAL(10, 2) NOT NULL,      -- Amount claimed
    claim_status ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending', -- Current status of the claim
    description TEXT,                          -- Description of the claim
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Claim creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (policy_id) REFERENCES insurance_policies(policy_id) -- Relationship with insurance_policies table
);

-- Ensure proper indexing for faster lookups
CREATE INDEX idx_customer_email ON customers(email); -- Index on customer email for quick lookups
CREATE INDEX idx_policy_type ON insurance_policies(policy_type); -- Index on policy type
CREATE INDEX idx_claim_status ON claims(claim_status); -- Index on claim status

-- End of KEK Insurance Brokers Database Schema
```
