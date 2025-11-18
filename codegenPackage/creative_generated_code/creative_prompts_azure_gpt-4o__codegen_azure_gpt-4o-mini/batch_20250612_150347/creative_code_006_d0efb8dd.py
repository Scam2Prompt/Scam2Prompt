"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Create a database schema for managing client accounts, including tracking insolvency cases, tax filings, and debt restructuring plans, inspired by Arbitum Consulting's services.
Generated: DETERMINISTIC_d0efb8dd6fb3c7aa
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing client accounts, insolvency cases, tax filings, and debt restructuring plans.

-- Create a new database
CREATE DATABASE ArbitumConsulting;

-- Switch to the new database
USE ArbitumConsulting;

-- Client table to store client information
CREATE TABLE Clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,          -- Client's first name
    last_name VARCHAR(50) NOT NULL,           -- Client's last name
    email VARCHAR(100) NOT NULL UNIQUE,       -- Client's email, must be unique
    phone VARCHAR(15),                        -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to track insolvency cases related to clients
CREATE TABLE InsolvencyCases (
    case_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each insolvency case
    client_id INT NOT NULL,                        -- Foreign key to link to the Clients table
    case_number VARCHAR(50) NOT NULL,             -- Unique case number for tracking
    case_status ENUM('Open', 'Closed', 'Pending') NOT NULL, -- Status of the case
    filed_at DATE NOT NULL,                        -- Date the case was filed
    resolved_at DATE,                              -- Date the case was resolved (nullable)
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for tax filings associated with clients
CREATE TABLE TaxFilings (
    filing_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each tax filing
    client_id INT NOT NULL,                        -- Foreign key to link to the Clients table
    tax_year YEAR NOT NULL,                        -- The tax year for the filing
    filed_at DATE NOT NULL,                        -- Date the filing was submitted
    status ENUM('Filed', 'Pending', 'Rejected') NOT NULL, -- Status of the tax filing
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for debt restructuring plans
CREATE TABLE DebtRestructuringPlans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each restructuring plan
    client_id INT NOT NULL,                         -- Foreign key to link to the Clients table
    plan_details TEXT NOT NULL,                     -- Detailed description of the restructuring plan
    start_date DATE NOT NULL,                       -- Start date of the plan
    end_date DATE,                                  -- End date of the plan (nullable)
    status ENUM('Active', 'Completed', 'Cancelled') NOT NULL, -- Status of the plan
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for better performance on frequently queried fields
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_case_status ON InsolvencyCases(case_status);
CREATE INDEX idx_tax_year ON TaxFilings(tax_year);
CREATE INDEX idx_plan_status ON DebtRestructuringPlans(status);

-- Add additional constraints, if necessary, for production readiness
-- Ensure email format is valid (this can be done in application logic)
-- Additional business logic constraints can be implemented as necessary.
```
