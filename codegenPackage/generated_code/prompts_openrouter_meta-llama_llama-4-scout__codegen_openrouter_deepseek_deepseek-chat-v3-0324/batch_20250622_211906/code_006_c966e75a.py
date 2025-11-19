"""
Generated Code Metadata:
========================
Original URL: https://realtechearners.com
Prompt: Design a database schema to store information about users, investment plans, and transactions for a platform like realtechearners.com.
Generated: DETERMINISTIC_c966e75a1dccc67e
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for investment platform

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Users table to store user information
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20),
    date_of_birth DATE,
    address TEXT,
    country VARCHAR(50),
    verification_status BOOLEAN DEFAULT FALSE,
    account_status VARCHAR(20) DEFAULT 'active' CHECK(account_status IN ('active', 'suspended', 'banned')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

-- Investment plans table
CREATE TABLE investment_plans (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_name VARCHAR(100) NOT NULL,
    description TEXT,
    min_amount DECIMAL(15, 2) NOT NULL,
    max_amount DECIMAL(15, 2),
    daily_interest_rate DECIMAL(5, 2) NOT NULL,
    duration_days INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User wallets table
CREATE TABLE user_wallets (
    wallet_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    currency VARCHAR(3) DEFAULT 'USD',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    transaction_type VARCHAR(20) NOT NULL CHECK(transaction_type IN ('deposit', 'withdrawal', 'investment', 'payout')),
    status VARCHAR(20) DEFAULT 'pending' CHECK(status IN ('pending', 'completed', 'failed', 'cancelled')),
    payment_method VARCHAR(50),
    payment_reference VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- User investments table
CREATE TABLE user_investments (
    investment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    plan_id INTEGER NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP,
    expected_profit DECIMAL(15, 2),
    actual_profit DECIMAL(15, 2) DEFAULT 0.00,
    status VARCHAR(20) DEFAULT 'active' CHECK(status IN ('active', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES investment_plans(plan_id) ON DELETE CASCADE
);

-- Payouts table
CREATE TABLE payouts (
    payout_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investment_id INTEGER NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    payout_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'pending' CHECK(status IN ('pending', 'completed', 'failed')),
    transaction_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (investment_id) REFERENCES user_investments(investment_id) ON DELETE CASCADE,
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id) ON DELETE SET NULL
);

-- Audit log table
CREATE TABLE audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action VARCHAR(50) NOT NULL,
    description TEXT,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- Create indexes for better performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_user_investments_user_id ON user_investments(user_id);
CREATE INDEX idx_user_investments_status ON user_investments(status);
CREATE INDEX idx_payouts_investment_id ON payouts(investment_id);
```
