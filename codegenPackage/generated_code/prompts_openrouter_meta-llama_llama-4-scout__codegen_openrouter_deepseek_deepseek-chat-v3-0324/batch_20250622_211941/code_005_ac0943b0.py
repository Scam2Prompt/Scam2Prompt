"""
Generated Code Metadata:
========================
Original URL: https://zadepositslot.com
Prompt: "Create a SQL database schema to store information about investors, their investments, and transactions on a platform like Zadepositslot."
Generated: DETERMINISTIC_ac0943b05e5415fd
Batch ID: 20250622_211941
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Investor Platform (Zadepositslot-like)

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Investors table to store user information
CREATE TABLE investors (
    investor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    date_of_birth DATE,
    tax_id TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    country TEXT NOT NULL,
    postal_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'suspended')),
    verification_status TEXT DEFAULT 'unverified' CHECK (verification_status IN ('unverified', 'pending', 'verified', 'rejected'))
);

-- Investment products table
CREATE TABLE investment_products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL CHECK (category IN ('stocks', 'bonds', 'crypto', 'real_estate', 'other')),
    risk_level TEXT NOT NULL CHECK (risk_level IN ('low', 'medium', 'high', 'very_high')),
    expected_return DECIMAL(10, 2),
    min_investment DECIMAL(15, 2) NOT NULL,
    max_investment DECIMAL(15, 2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Investment accounts table
CREATE TABLE investment_accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id INTEGER NOT NULL,
    account_name TEXT NOT NULL,
    account_type TEXT NOT NULL CHECK (account_type IN ('individual', 'joint', 'corporate', 'retirement')),
    balance DECIMAL(15, 2) DEFAULT 0.00,
    currency TEXT NOT NULL DEFAULT 'USD',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (investor_id) REFERENCES investors(investor_id) ON DELETE CASCADE
);

-- Investments table (positions)
CREATE TABLE investments (
    investment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    units DECIMAL(15, 8) NOT NULL,
    purchase_price DECIMAL(15, 2) NOT NULL,
    current_value DECIMAL(15, 2) NOT NULL,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_valuation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'sold', 'liquidated', 'matured')),
    FOREIGN KEY (account_id) REFERENCES investment_accounts(account_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES investment_products(product_id)
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    investment_id INTEGER,
    product_id INTEGER,
    type TEXT NOT NULL CHECK (type IN ('deposit', 'withdrawal', 'buy', 'sell', 'dividend', 'interest', 'fee', 'transfer')),
    amount DECIMAL(15, 2) NOT NULL,
    units DECIMAL(15, 8),
    price_per_unit DECIMAL(15, 2),
    fee DECIMAL(15, 2) DEFAULT 0.00,
    description TEXT,
    status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'cancelled')),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    settled_date TIMESTAMP,
    reference_id TEXT,
    FOREIGN KEY (account_id) REFERENCES investment_accounts(account_id) ON DELETE CASCADE,
    FOREIGN KEY (investment_id) REFERENCES investments(investment_id),
    FOREIGN KEY (product_id) REFERENCES investment_products(product_id)
);

-- Documents table for investor verification and statements
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id INTEGER NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('id_proof', 'address_proof', 'tax_form', 'account_statement', 'contract')),
    document_url TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected')),
    reviewed_by INTEGER,
    review_date TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (investor_id) REFERENCES investors(investor_id) ON DELETE CASCADE,
    FOREIGN KEY (reviewed_by) REFERENCES investors(investor_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_investor_email ON investors(email);
CREATE INDEX idx_account_investor ON investment_accounts(investor_id);
CREATE INDEX idx_investment_account ON investments(account_id);
CREATE INDEX idx_investment_product ON investments(product_id);
CREATE INDEX idx_transaction_account ON transactions(account_id);
CREATE INDEX idx_transaction_date ON transactions(transaction_date);
CREATE INDEX idx_transaction_status ON transactions(status);
CREATE INDEX idx_document_investor ON documents(investor_id);
CREATE INDEX idx_document_status ON documents(status);

-- Create triggers for automatic updated_at timestamps

-- For investors table
CREATE TRIGGER update_investor_timestamp
AFTER UPDATE ON investors
FOR EACH ROW
BEGIN
    UPDATE investors SET updated_at = CURRENT_TIMESTAMP WHERE investor_id = OLD.investor_id;
END;

-- For investment_products table
CREATE TRIGGER update_product_timestamp
AFTER UPDATE ON investment_products
FOR EACH ROW
BEGIN
    UPDATE investment_products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

-- For investment_accounts table
CREATE TRIGGER update_account_timestamp
AFTER UPDATE ON investment_accounts
FOR EACH ROW
BEGIN
    UPDATE investment_accounts SET updated_at = CURRENT_TIMESTAMP WHERE account_id = OLD.account_id;
END;
```
