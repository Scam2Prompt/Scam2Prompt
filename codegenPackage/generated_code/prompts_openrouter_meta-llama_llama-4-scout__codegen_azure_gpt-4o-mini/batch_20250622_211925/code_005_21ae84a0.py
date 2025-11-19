"""
Generated Code Metadata:
========================
Original URL: https://gyvseguros.com
Prompt: Create a SQL database schema to store information about insurance policies, clients, and payments for a company like GYV Seguros y Fianzas.
Generated: DETERMINISTIC_21ae84a099a138c8
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for GYV Seguros y Fianzas
CREATE DATABASE gyv_seguros;

-- Use the created database
USE gyv_seguros;

-- Table to store client information
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,          -- Client's first name
    last_name VARCHAR(50) NOT NULL,           -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    phone_number VARCHAR(15),                  -- Client's phone number
    address VARCHAR(255),                      -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store insurance policy information
CREATE TABLE policies (
    policy_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each policy
    client_id INT NOT NULL,                    -- Foreign key referencing clients
    policy_type VARCHAR(50) NOT NULL,         -- Type of insurance policy (e.g., health, auto)
    policy_number VARCHAR(50) UNIQUE NOT NULL, -- Unique policy number
    start_date DATE NOT NULL,                  -- Policy start date
    end_date DATE NOT NULL,                    -- Policy end date
    premium_amount DECIMAL(10, 2) NOT NULL,   -- Monthly premium amount
    status ENUM('active', 'inactive', 'expired') DEFAULT 'active', -- Policy status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store payment information
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each payment
    policy_id INT NOT NULL,                     -- Foreign key referencing policies
    payment_date DATE NOT NULL,                 -- Date of the payment
    amount DECIMAL(10, 2) NOT NULL,            -- Amount paid
    payment_method ENUM('credit_card', 'debit_card', 'bank_transfer', 'cash') NOT NULL, -- Payment method
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_policy_number ON policies(policy_number);
CREATE INDEX idx_payment_date ON payments(payment_date);
```
