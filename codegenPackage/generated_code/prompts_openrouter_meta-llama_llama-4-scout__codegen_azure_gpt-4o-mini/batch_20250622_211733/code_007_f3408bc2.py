"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Design a simple database schema to store information about law firm clients, cases, and attorneys, using a relational database management system like MySQL.
Generated: DETERMINISTIC_f3408bc21acf4cb0
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the law firm
CREATE DATABASE law_firm;

-- Use the created database
USE law_firm;

-- Table to store information about clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,           -- Client's first name
    last_name VARCHAR(50) NOT NULL,            -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL,        -- Client's email address (unique)
    phone VARCHAR(15),                         -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about attorneys
CREATE TABLE attorneys (
    attorney_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each attorney
    first_name VARCHAR(50) NOT NULL,            -- Attorney's first name
    last_name VARCHAR(50) NOT NULL,             -- Attorney's last name
    email VARCHAR(100) UNIQUE NOT NULL,         -- Attorney's email address (unique)
    phone VARCHAR(15),                          -- Attorney's phone number
    specialty VARCHAR(100),                     -- Area of specialty for the attorney
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about cases
CREATE TABLE cases (
    case_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each case
    case_number VARCHAR(50) NOT NULL UNIQUE,     -- Unique case number
    client_id INT NOT NULL,                       -- Foreign key referencing clients
    attorney_id INT NOT NULL,                     -- Foreign key referencing attorneys
    case_status ENUM('Open', 'Closed', 'Pending') NOT NULL,  -- Status of the case
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_attorney_email ON attorneys(email);
CREATE INDEX idx_case_number ON cases(case_number);
```
