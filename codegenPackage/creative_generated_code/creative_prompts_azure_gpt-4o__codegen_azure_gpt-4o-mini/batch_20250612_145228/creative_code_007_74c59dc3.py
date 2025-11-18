"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Develop a database schema for SGFC Finance to manage client information, loan types, repayment schedules, and community outreach activities.
Generated: DETERMINISTIC_74c59dc3f9a4bc41
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for SGFC Finance
CREATE DATABASE sgfc_finance;

-- Use the created database
USE sgfc_finance;

-- Table to store client information
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,           -- Client's first name
    last_name VARCHAR(50) NOT NULL,            -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL,        -- Client's email address (unique)
    phone_number VARCHAR(15),                  -- Client's phone number
    address VARCHAR(255),                       -- Client's residential address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table to store loan types
CREATE TABLE loan_types (
    loan_type_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each loan type
    loan_name VARCHAR(100) NOT NULL,              -- Name of the loan type
    interest_rate DECIMAL(5, 2) NOT NULL,        -- Interest rate for the loan type
    max_amount DECIMAL(15, 2) NOT NULL,          -- Maximum loan amount
    duration_months INT NOT NULL,                 -- Duration in months for repayment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table to store repayment schedules
CREATE TABLE repayment_schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each repayment schedule
    client_id INT NOT NULL,                        -- Foreign key referencing the client
    loan_type_id INT NOT NULL,                     -- Foreign key referencing the loan type
    repayment_date DATE NOT NULL,                  -- Date of the repayment
    amount DECIMAL(15, 2) NOT NULL,               -- Amount to be repaid
    status ENUM('Pending', 'Completed', 'Missed') DEFAULT 'Pending',  -- Status of the repayment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Last update timestamp
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (loan_type_id) REFERENCES loan_types(loan_type_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store community outreach activities
CREATE TABLE outreach_activities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each outreach activity
    activity_name VARCHAR(100) NOT NULL,           -- Name of the outreach activity
    description TEXT,                               -- Description of the outreach activity
    activity_date DATE NOT NULL,                   -- Date of the outreach activity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table to link clients to outreach activities (many-to-many relationship)
CREATE TABLE client_outreach (
    client_id INT NOT NULL,                         -- Foreign key referencing the client
    activity_id INT NOT NULL,                       -- Foreign key referencing the outreach activity
    PRIMARY KEY (client_id, activity_id),          -- Composite primary key
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (activity_id) REFERENCES outreach_activities(activity_id) ON DELETE CASCADE  -- Ensure referential integrity
);
```
