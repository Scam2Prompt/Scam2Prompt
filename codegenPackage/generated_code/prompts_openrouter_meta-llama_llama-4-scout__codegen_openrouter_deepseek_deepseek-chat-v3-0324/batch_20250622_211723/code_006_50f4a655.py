"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Design a database schema for storing customer information and financial data for a credit union, considering the various services offered by Genesis Investment Credit Union.
Generated: DETERMINISTIC_50f4a655f10e29a9
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Genesis Investment Credit Union
-- This schema supports customer information, accounts, transactions, loans, and other financial services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table: stores core customer information
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    ssn TEXT NOT NULL UNIQUE,  -- Encrypted in production
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address_street TEXT NOT NULL,
    address_city TEXT NOT NULL,
    address_state TEXT NOT NULL,
    address_zip TEXT NOT NULL,
    date_joined DATE NOT NULL DEFAULT CURRENT_DATE,
    status TEXT NOT NULL CHECK(status IN ('active', 'inactive', 'pending')) DEFAULT 'active',
    credit_score INTEGER,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT email_format CHECK(email LIKE '%@%.%'),
    CONSTRAINT ssn_length CHECK(LENGTH(ssn) = 9)  -- Would be encrypted in production
);

-- Accounts table: stores different types of financial accounts
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    account_type TEXT NOT NULL CHECK(account_type IN ('checking', 'savings', 'money_market', 'cd', 'ira')),
    account_number TEXT NOT NULL UNIQUE,
    routing_number TEXT NOT NULL DEFAULT '123456789',  -- Would be actual routing number in production
    balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    interest_rate DECIMAL(5, 3) DEFAULT NULL,
    opened_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status TEXT NOT NULL CHECK(status IN ('active', 'closed', 'dormant')) DEFAULT 'active',
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Transactions table: records all financial transactions
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    transaction_type TEXT NOT NULL CHECK(transaction_type IN ('deposit', 'withdrawal', 'transfer', 'payment', 'fee')),
    amount DECIMAL(15, 2) NOT NULL,
    description TEXT,
    transaction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    reference_number TEXT,
    status TEXT NOT NULL CHECK(status IN ('pending', 'completed', 'failed', 'reversed')) DEFAULT 'completed',
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
);

-- Loans table: tracks all loan products
CREATE TABLE loans (
    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    account_id INTEGER,  -- Linked account for payments
    loan_type TEXT NOT NULL CHECK(loan_type IN ('auto', 'mortgage', 'personal', 'home_equity', 'student')),
    loan_number TEXT NOT NULL UNIQUE,
    original_amount DECIMAL(15, 2) NOT NULL,
    current_balance DECIMAL(15, 2) NOT NULL,
    interest_rate DECIMAL(5, 3) NOT NULL,
    term_months INTEGER NOT NULL,
    monthly_payment DECIMAL(10, 2) NOT NULL,
    start_date DATE NOT NULL,
    maturity_date DATE NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('active', 'paid', 'delinquent', 'default')) DEFAULT 'active',
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE SET NULL
);

-- Loan payments table: tracks loan payment history
CREATE TABLE loan_payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    loan_id INTEGER NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    principal_amount DECIMAL(10, 2) NOT NULL,
    interest_amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('ach', 'check', 'transfer', 'cash')),
    status TEXT NOT NULL CHECK(status IN ('pending', 'completed', 'late', 'partial')) DEFAULT 'completed',
    FOREIGN KEY (loan_id) REFERENCES loans(loan_id) ON DELETE CASCADE
);

-- Cards table: tracks debit/credit cards
CREATE TABLE cards (
    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    account_id INTEGER,  -- For debit cards
    card_type TEXT NOT NULL CHECK(card_type IN ('debit', 'credit')),
    card_number TEXT NOT NULL UNIQUE,  -- Would be encrypted in production
    expiration_date TEXT NOT NULL,  -- Format: MM/YY
    cvv TEXT NOT NULL,  -- Would be encrypted in production
    daily_limit DECIMAL(10, 2),
    status TEXT NOT NULL CHECK(status IN ('active', 'inactive', 'lost', 'stolen', 'expired')) DEFAULT 'active',
    issue_date DATE NOT NULL DEFAULT CURRENT_DATE,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE SET NULL
);

-- Beneficiaries table: tracks account beneficiaries
CREATE TABLE beneficiaries (
    beneficiary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    relationship TEXT NOT NULL CHECK(relationship IN ('primary', 'joint', 'beneficiary')),
    percentage INTEGER CHECK(percentage BETWEEN 0 AND 100),
    date_added DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Audit log table: tracks all sensitive operations
CREATE TABLE audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,  -- Employee ID if applicable
    action TEXT NOT NULL,
    table_name TEXT NOT NULL,
    record_id INTEGER NOT NULL,
    old_value TEXT,
    new_value TEXT,
    ip_address TEXT,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_customers_name ON customers(last_name, first_name);
CREATE INDEX idx_accounts_customer ON accounts(customer_id);
CREATE INDEX idx_transactions_account ON transactions(account_id);
CREATE INDEX idx_transactions_date ON transactions(transaction_date);
CREATE INDEX idx_loans_customer ON loans(customer_id);
CREATE INDEX idx_loan_payments_loan ON loan_payments(loan_id);
CREATE INDEX idx_cards_customer ON cards(customer_id);
```
