"""
Generated Code Metadata:
========================
Original URL: https://buildstock-finance.com
Prompt: Design a database schema to store information about Buildstock-Finance Investment's clients, their investment plans, and transaction history.
Generated: DETERMINISTIC_c44e98cf9d4e9344
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Buildstock-Finance Investments

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT CHECK(phone GLOB '[0-9]*'),
    date_of_birth DATE NOT NULL CHECK(date_of_birth <= DATE('now')),
    ssn TEXT UNIQUE CHECK(LENGTH(ssn) = 9),
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL CHECK(LENGTH(zip_code) = 5),
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('active', 'inactive', 'pending')),
    risk_tolerance TEXT NOT NULL CHECK(risk_tolerance IN ('low', 'medium', 'high')),
    notes TEXT,
    CONSTRAINT email_format CHECK(email LIKE '%@%.%')
);

-- Investment plans table
CREATE TABLE investment_plans (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    min_investment_amount DECIMAL(15, 2) NOT NULL CHECK(min_investment_amount > 0),
    max_investment_amount DECIMAL(15, 2) CHECK(max_investment_amount > min_investment_amount),
    expected_return_rate DECIMAL(5, 2) NOT NULL,
    risk_level TEXT NOT NULL CHECK(risk_level IN ('low', 'medium', 'high')),
    lock_in_period_months INTEGER CHECK(lock_in_period_months >= 0),
    management_fee_percentage DECIMAL(5, 2) NOT NULL CHECK(management_fee_percentage >= 0),
    is_active BOOLEAN DEFAULT 1
);

-- Client investment accounts
CREATE TABLE client_accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    plan_id INTEGER NOT NULL,
    account_number TEXT UNIQUE NOT NULL,
    date_opened TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    current_balance DECIMAL(15, 2) NOT NULL DEFAULT 0 CHECK(current_balance >= 0),
    status TEXT NOT NULL CHECK(status IN ('active', 'closed', 'suspended')),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES investment_plans(plan_id),
    CONSTRAINT unique_client_plan UNIQUE (client_id, plan_id)
);

-- Transaction types
CREATE TABLE transaction_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    affects_balance BOOLEAN NOT NULL
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    amount DECIMAL(15, 2) NOT NULL CHECK(amount > 0),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    status TEXT NOT NULL CHECK(status IN ('pending', 'completed', 'failed', 'reversed')),
    reference_number TEXT UNIQUE,
    FOREIGN KEY (account_id) REFERENCES client_accounts(account_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES transaction_types(type_id)
);

-- Client documents table
CREATE TABLE client_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    document_type TEXT NOT NULL CHECK(document_type IN ('id_proof', 'address_proof', 'tax_form', 'contract', 'other')),
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expiration_date DATE,
    status TEXT NOT NULL CHECK(status IN ('pending', 'approved', 'rejected', 'expired')),
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_client_status ON clients(status);
CREATE INDEX idx_account_client ON client_accounts(client_id);
CREATE INDEX idx_account_plan ON client_accounts(plan_id);
CREATE INDEX idx_transaction_account ON transactions(account_id);
CREATE INDEX idx_transaction_date ON transactions(transaction_date);
CREATE INDEX idx_transaction_status ON transactions(status);
CREATE INDEX idx_documents_client ON client_documents(client_id);
CREATE INDEX idx_documents_status ON client_documents(status);

-- Insert default transaction types
INSERT INTO transaction_types (type_name, description, affects_balance) VALUES 
    ('deposit', 'Initial investment deposit', 1),
    ('withdrawal', 'Funds withdrawal', 1),
    ('dividend', 'Dividend payment', 1),
    ('interest', 'Interest payment', 1),
    ('fee', 'Management fee deduction', 1),
    ('transfer_in', 'Transfer from another account', 1),
    ('transfer_out', 'Transfer to another account', 1),
    ('adjustment', 'Balance adjustment', 1);
```
