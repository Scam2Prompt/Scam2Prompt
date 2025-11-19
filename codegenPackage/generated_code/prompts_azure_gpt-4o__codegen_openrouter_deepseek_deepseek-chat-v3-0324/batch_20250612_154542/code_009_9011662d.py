"""
Generated Code Metadata:
========================
Original URL: https://globalarbitrageinv.com
Prompt: Create a database schema using SQL to manage user accounts, investment plans, referral data, and transaction history for a platform like Global Arbitrage Investments.
Generated: DETERMINISTIC_9011662dbb0a8d45
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Global Arbitrage Investments platform

-- Users table to store account information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20),
    country VARCHAR(50),
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    account_status VARCHAR(20) DEFAULT 'active' CHECK (account_status IN ('active', 'suspended', 'banned', 'inactive')),
    kyc_verified BOOLEAN DEFAULT FALSE,
    two_factor_enabled BOOLEAN DEFAULT FALSE,
    profile_image_url VARCHAR(255),
    wallet_balance DECIMAL(20, 8) DEFAULT 0.00,
    total_invested DECIMAL(20, 8) DEFAULT 0.00,
    total_earned DECIMAL(20, 8) DEFAULT 0.00
);

-- Investment plans table
CREATE TABLE investment_plans (
    plan_id SERIAL PRIMARY KEY,
    plan_name VARCHAR(100) NOT NULL,
    description TEXT,
    min_amount DECIMAL(20, 8) NOT NULL,
    max_amount DECIMAL(20, 8),
    duration_days INTEGER NOT NULL,
    daily_interest_rate DECIMAL(5, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User investments table
CREATE TABLE user_investments (
    investment_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    plan_id INTEGER REFERENCES investment_plans(plan_id) ON DELETE RESTRICT,
    amount DECIMAL(20, 8) NOT NULL,
    start_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP WITH TIME ZONE,
    expected_profit DECIMAL(20, 8),
    actual_profit DECIMAL(20, 8) DEFAULT 0.00,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'completed', 'cancelled')),
    last_payout_date TIMESTAMP WITH TIME ZONE,
    next_payout_date TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Referral system tables
CREATE TABLE referral_codes (
    code_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES users(user_id) ON DELETE CASCADE,
    referral_code VARCHAR(20) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE referral_relationships (
    relationship_id SERIAL PRIMARY KEY,
    referrer_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    referred_id INTEGER UNIQUE REFERENCES users(user_id) ON DELETE CASCADE,
    referral_code_used VARCHAR(20) REFERENCES referral_codes(referral_code) ON DELETE SET NULL,
    relationship_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE referral_bonuses (
    bonus_id SERIAL PRIMARY KEY,
    relationship_id INTEGER REFERENCES referral_relationships(relationship_id) ON DELETE CASCADE,
    amount DECIMAL(20, 8) NOT NULL,
    bonus_type VARCHAR(20) CHECK (bonus_type IN ('signup', 'investment', 'profit')),
    investment_id INTEGER REFERENCES user_investments(investment_id) ON DELETE SET NULL,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'paid', 'cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    paid_at TIMESTAMP WITH TIME ZONE
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    amount DECIMAL(20, 8) NOT NULL,
    transaction_type VARCHAR(20) NOT NULL CHECK (transaction_type IN ('deposit', 'withdrawal', 'investment', 'payout', 'referral_bonus', 'transfer')),
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'cancelled')),
    payment_method VARCHAR(50),
    payment_reference VARCHAR(255),
    investment_id INTEGER REFERENCES user_investments(investment_id) ON DELETE SET NULL,
    bonus_id INTEGER REFERENCES referral_bonuses(bonus_id) ON DELETE SET NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE
);

-- Wallet addresses table
CREATE TABLE wallet_addresses (
    wallet_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    currency VARCHAR(10) NOT NULL,
    address VARCHAR(255) NOT NULL,
    network VARCHAR(50),
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, currency, network)
);

-- User sessions table
CREATE TABLE user_sessions (
    session_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    session_token VARCHAR(255) UNIQUE NOT NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Audit log table
CREATE TABLE audit_log (
    log_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    action VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50),
    entity_id INTEGER,
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_user_investments_user_id ON user_investments(user_id);
CREATE INDEX idx_user_investments_status ON user_investments(status);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_transactions_type ON transactions(transaction_type);
CREATE INDEX idx_referral_relationships_referrer ON referral_relationships(referrer_id);
CREATE INDEX idx_referral_relationships_referred ON referral_relationships(referred_id);
```
