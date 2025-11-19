"""
Generated Code Metadata:
========================
Original URL: https://cryptexbit.com
Prompt: Create a SQL database schema to manage CryptexBit's user accounts, transactions, and deposits, ensuring transparency and security.
Generated: DETERMINISTIC_e190459379ba6942
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for CryptexBit

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table to store account information
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone_number VARCHAR(20),
    is_verified BOOLEAN DEFAULT FALSE,
    verification_token VARCHAR(255),
    verification_expires TIMESTAMP,
    two_factor_enabled BOOLEAN DEFAULT FALSE,
    two_factor_secret VARCHAR(255),
    last_login TIMESTAMP,
    account_status VARCHAR(20) DEFAULT 'active' CHECK (account_status IN ('active', 'suspended', 'banned')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User security logs for audit trail
CREATE TABLE user_security_logs (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    action VARCHAR(50) NOT NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Wallet table to store cryptocurrency balances
CREATE TABLE wallets (
    wallet_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    currency_code VARCHAR(10) NOT NULL,
    balance DECIMAL(30, 18) NOT NULL DEFAULT 0,
    locked_balance DECIMAL(30, 18) NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, currency_code)
);

-- Deposit addresses table
CREATE TABLE deposit_addresses (
    address_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    wallet_id UUID NOT NULL REFERENCES wallets(wallet_id) ON DELETE CASCADE,
    address VARCHAR(255) NOT NULL,
    currency_code VARCHAR(10) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(wallet_id, currency_code)
);

-- Deposits table
CREATE TABLE deposits (
    deposit_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    wallet_id UUID NOT NULL REFERENCES wallets(wallet_id) ON DELETE CASCADE,
    transaction_hash VARCHAR(255) NOT NULL,
    currency_code VARCHAR(10) NOT NULL,
    amount DECIMAL(30, 18) NOT NULL,
    confirmations INTEGER NOT NULL DEFAULT 0,
    required_confirmations INTEGER NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'cancelled')),
    address VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    UNIQUE(transaction_hash, currency_code)
);

-- Transactions table (withdrawals and transfers)
CREATE TABLE transactions (
    transaction_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    sender_wallet_id UUID REFERENCES wallets(wallet_id) ON DELETE SET NULL,
    receiver_wallet_id UUID REFERENCES wallets(wallet_id) ON DELETE SET NULL,
    external_address VARCHAR(255),
    currency_code VARCHAR(10) NOT NULL,
    amount DECIMAL(30, 18) NOT NULL,
    fee DECIMAL(30, 18) NOT NULL DEFAULT 0,
    transaction_type VARCHAR(20) NOT NULL CHECK (transaction_type IN ('withdrawal', 'transfer', 'deposit')),
    status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'cancelled')),
    transaction_hash VARCHAR(255),
    memo TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);

-- Transaction logs for audit trail
CREATE TABLE transaction_logs (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    transaction_id UUID NOT NULL REFERENCES transactions(transaction_id) ON DELETE CASCADE,
    action VARCHAR(50) NOT NULL,
    details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- API keys table
CREATE TABLE api_keys (
    api_key_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    api_key VARCHAR(255) NOT NULL,
    api_secret VARCHAR(255) NOT NULL,
    label VARCHAR(100),
    permissions TEXT[],
    is_active BOOLEAN DEFAULT TRUE,
    last_used TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_wallets_user_id ON wallets(user_id);
CREATE INDEX idx_deposits_wallet_id ON deposits(wallet_id);
CREATE INDEX idx_deposits_status ON deposits(status);
CREATE INDEX idx_transactions_sender_wallet_id ON transactions(sender_wallet_id);
CREATE INDEX idx_transactions_receiver_wallet_id ON transactions(receiver_wallet_id);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_transactions_created_at ON transactions(created_at);
CREATE INDEX idx_api_keys_user_id ON api_keys(user_id);

-- Triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_users_timestamp
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_wallets_timestamp
BEFORE UPDATE ON wallets
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_transactions_timestamp
BEFORE UPDATE ON transactions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_api_keys_timestamp
BEFORE UPDATE ON api_keys
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
