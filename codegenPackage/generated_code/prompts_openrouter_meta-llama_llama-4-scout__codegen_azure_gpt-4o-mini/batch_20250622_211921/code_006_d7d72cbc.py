"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Design a database schema for a small accounting firm in Peru, using a database management system like MySQL or PostgreSQL to manage client data, financial statements, and tax returns."
Generated: DETERMINISTIC_d7d72cbcfbec5c28
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a small accounting firm in Peru

-- Create a database for the accounting firm
CREATE DATABASE accounting_firm;

-- Switch to the newly created database
USE accounting_firm;

-- Table to store client information
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    address TEXT, -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store financial statements
CREATE TABLE financial_statements (
    statement_id SERIAL PRIMARY KEY, -- Unique identifier for each financial statement
    client_id INT NOT NULL, -- Foreign key referencing the client
    statement_type VARCHAR(50) NOT NULL, -- Type of financial statement (e.g., Balance Sheet, Income Statement)
    statement_date DATE NOT NULL, -- Date of the financial statement
    file_path VARCHAR(255), -- Path to the file storing the financial statement
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store tax returns
CREATE TABLE tax_returns (
    return_id SERIAL PRIMARY KEY, -- Unique identifier for each tax return
    client_id INT NOT NULL, -- Foreign key referencing the client
    tax_year INT NOT NULL, -- Year of the tax return
    return_type VARCHAR(50) NOT NULL, -- Type of tax return (e.g., Individual, Corporate)
    file_path VARCHAR(255), -- Path to the file storing the tax return
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store payment records
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY, -- Unique identifier for each payment
    client_id INT NOT NULL, -- Foreign key referencing the client
    amount DECIMAL(10, 2) NOT NULL, -- Amount of the payment
    payment_date DATE NOT NULL, -- Date of the payment
    payment_method VARCHAR(50), -- Method of payment (e.g., Cash, Credit Card, Bank Transfer)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_financial_client ON financial_statements(client_id);
CREATE INDEX idx_tax_client ON tax_returns(client_id);
CREATE INDEX idx_payment_client ON payments(client_id);
```
