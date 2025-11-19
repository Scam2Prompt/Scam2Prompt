"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Develop a SQL database schema to store information about health insurance plans, including provider details, benefits, and pricing, similar to the comparison service offered by Health Insurance Shop.
Generated: DETERMINISTIC_4a66081104a09e57
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Health Insurance Plans

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Providers;
DROP TABLE IF EXISTS Plans;
DROP TABLE IF EXISTS Benefits;
DROP TABLE IF EXISTS PlanBenefits;

-- Table to store provider details
CREATE TABLE Providers (
    provider_id SERIAL PRIMARY KEY, -- Unique identifier for each provider
    provider_name VARCHAR(255) NOT NULL, -- Name of the provider
    contact_number VARCHAR(15), -- Contact number for the provider
    email VARCHAR(255), -- Email address for the provider
    address TEXT, -- Address of the provider
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store health insurance plans
CREATE TABLE Plans (
    plan_id SERIAL PRIMARY KEY, -- Unique identifier for each plan
    provider_id INT NOT NULL, -- Foreign key referencing Providers
    plan_name VARCHAR(255) NOT NULL, -- Name of the insurance plan
    monthly_premium DECIMAL(10, 2) NOT NULL, -- Monthly premium cost
    deductible DECIMAL(10, 2) NOT NULL, -- Deductible amount
    out_of_pocket_max DECIMAL(10, 2) NOT NULL, -- Maximum out-of-pocket expense
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (provider_id) REFERENCES Providers(provider_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store benefits associated with each plan
CREATE TABLE Benefits (
    benefit_id SERIAL PRIMARY KEY, -- Unique identifier for each benefit
    benefit_description TEXT NOT NULL, -- Description of the benefit
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to associate benefits with plans
CREATE TABLE PlanBenefits (
    plan_benefit_id SERIAL PRIMARY KEY, -- Unique identifier for each plan-benefit association
    plan_id INT NOT NULL, -- Foreign key referencing Plans
    benefit_id INT NOT NULL, -- Foreign key referencing Benefits
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (plan_id) REFERENCES Plans(plan_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (benefit_id) REFERENCES Benefits(benefit_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_provider_name ON Providers(provider_name);
CREATE INDEX idx_plan_name ON Plans(plan_name);
CREATE INDEX idx_benefit_description ON Benefits(benefit_description);
```
