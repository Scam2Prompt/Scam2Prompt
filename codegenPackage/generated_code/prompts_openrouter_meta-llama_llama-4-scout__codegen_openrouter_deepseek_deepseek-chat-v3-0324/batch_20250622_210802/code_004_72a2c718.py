"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Design a basic database schema for storing client information, credits, and educational programs for a cooperative like Cooprometa.
Generated: DETERMINISTIC_72a2c718827b14fb
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Cooprometa client management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT CHECK(length(phone) >= 10),
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    country TEXT DEFAULT 'Colombia',
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive', 'suspended')),
    notes TEXT
);

-- Credit types table
CREATE TABLE credit_types (
    credit_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    interest_rate DECIMAL(5,2) NOT NULL CHECK(interest_rate >= 0),
    max_amount DECIMAL(10,2) NOT NULL CHECK(max_amount > 0),
    term_months INTEGER NOT NULL CHECK(term_months > 0),
    is_active BOOLEAN DEFAULT 1
);

-- Client credits table
CREATE TABLE client_credits (
    credit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    credit_type_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK(amount > 0),
    start_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    end_date DATETIME NOT NULL,
    status TEXT DEFAULT 'active' CHECK(status IN ('active', 'paid', 'defaulted', 'cancelled')),
    remaining_balance DECIMAL(10,2) NOT NULL CHECK(remaining_balance >= 0),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE RESTRICT,
    FOREIGN KEY (credit_type_id) REFERENCES credit_types(credit_type_id) ON DELETE RESTRICT
);

-- Payment history table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    credit_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK(amount > 0),
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT CHECK(payment_method IN ('cash', 'transfer', 'debit', 'credit')),
    receipt_number TEXT UNIQUE,
    notes TEXT,
    FOREIGN KEY (credit_id) REFERENCES client_credits(credit_id) ON DELETE CASCADE
);

-- Educational programs table
CREATE TABLE educational_programs (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    duration_hours INTEGER CHECK(duration_hours > 0),
    cost DECIMAL(10,2) CHECK(cost >= 0),
    is_active BOOLEAN DEFAULT 1
);

-- Client program enrollments
CREATE TABLE client_programs (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    completion_date DATETIME,
    status TEXT DEFAULT 'enrolled' CHECK(status IN ('enrolled', 'completed', 'dropped')),
    certificate_issued BOOLEAN DEFAULT 0,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES educational_programs(program_id) ON DELETE RESTRICT
);

-- Audit log table
CREATE TABLE audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT NOT NULL,
    record_id INTEGER NOT NULL,
    action TEXT NOT NULL CHECK(action IN ('insert', 'update', 'delete')),
    old_values TEXT,
    new_values TEXT,
    changed_by TEXT,
    change_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_client_credits_client ON client_credits(client_id);
CREATE INDEX idx_client_credits_type ON client_credits(credit_type_id);
CREATE INDEX idx_payments_credit ON payments(credit_id);
CREATE INDEX idx_client_programs_client ON client_programs(client_id);
CREATE INDEX idx_client_programs_program ON client_programs(program_id);
```
