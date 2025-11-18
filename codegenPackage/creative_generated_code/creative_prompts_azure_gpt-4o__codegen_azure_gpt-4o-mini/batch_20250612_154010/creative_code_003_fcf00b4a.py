"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Create a database schema for a cloud-based time-tracking application designed for lawyers, referencing the structure used by BillYourTime.com.
Generated: DETERMINISTIC_fcf00b4a437d5489
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for a Cloud-Based Time-Tracking Application for Lawyers

-- Create a table for users to store their account information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL, -- Username for login, must be unique
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) UNIQUE NOT NULL,   -- Unique email for notifications and recovery 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for clients to store client information
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,          -- Unique identifier for each client
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key to users
    client_name VARCHAR(100) NOT NULL,    -- Name of the client
    email VARCHAR(100),                    -- Contact email for client
    phone VARCHAR(15),                     -- Contact phone number for client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for client creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table to track billable hours
CREATE TABLE time_entries (
    entry_id SERIAL PRIMARY KEY,           -- Unique identifier for each time entry
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key to users
    client_id INT REFERENCES clients(client_id) ON DELETE SET NULL, -- Foreign key to clients
    start_time TIMESTAMP NOT NULL,         -- Start time of the tracked period
    end_time TIMESTAMP NOT NULL,           -- End time of the tracked period
    description TEXT,                      -- Description of the work done
    billable BOOLEAN DEFAULT TRUE,         -- Indicates if the time is billable
    hourly_rate DECIMAL(10, 2) NOT NULL,  -- Hourly rate for the work
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for entry creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for invoices to manage billing
CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,         -- Unique identifier for each invoice
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key to users
    client_id INT REFERENCES clients(client_id) ON DELETE SET NULL, -- Foreign key to clients
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount of the invoice
    status VARCHAR(20) DEFAULT 'Pending',  -- Status of the invoice (Pending, Paid, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for invoice creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for payments made against invoices
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,         -- Unique identifier for each payment
    invoice_id INT REFERENCES invoices(invoice_id) ON DELETE CASCADE, -- Foreign key to invoices
    amount DECIMAL(10, 2) NOT NULL,       -- Amount paid
    payment_date TIMESTAMP NOT NULL,       -- Date of payment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for payment creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Indexes for optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_clients_user_id ON clients(user_id);
CREATE INDEX idx_time_entries_user_id ON time_entries(user_id);
CREATE INDEX idx_time_entries_client_id ON time_entries(client_id);
CREATE INDEX idx_invoices_user_id ON invoices(user_id);
CREATE INDEX idx_invoices_client_id ON invoices(client_id);
CREATE INDEX idx_payments_invoice_id ON payments(invoice_id);
```
