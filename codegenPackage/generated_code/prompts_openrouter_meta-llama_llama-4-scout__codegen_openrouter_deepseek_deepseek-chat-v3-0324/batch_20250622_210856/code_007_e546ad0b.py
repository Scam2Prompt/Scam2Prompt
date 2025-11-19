"""
Generated Code Metadata:
========================
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Design a database schema to store user information, referral links, and transaction history for ScapesMania, ensuring secure and efficient data management.
Generated: DETERMINISTIC_e546ad0b8fc44be3
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ScapesMania user management system

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table to store core user information
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone_number VARCHAR(20),
    country_code VARCHAR(5),
    is_verified BOOLEAN DEFAULT FALSE,
    verification_token VARCHAR(255),
    verification_expires TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'banned')),
    two_factor_enabled BOOLEAN DEFAULT FALSE,
    two_factor_secret VARCHAR(255)
);

-- Referral links table
CREATE TABLE referral_links (
    referral_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    referral_code VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    max_uses INTEGER,
    use_count INTEGER DEFAULT 0,
    expiry_date TIMESTAMP WITH TIME ZONE
);

-- Referral relationships table
CREATE TABLE referral_relationships (
    relationship_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    referrer_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    referred_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    referral_id UUID NOT NULL REFERENCES referral_links(referral_id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (referrer_id, referred_id)
);

-- Transaction types enumeration
CREATE TYPE transaction_type AS ENUM (
    'deposit',
    'withdrawal',
    'purchase',
    'reward',
    'referral_bonus',
    'refund'
);

-- Transaction status enumeration
CREATE TYPE transaction_status AS ENUM (
    'pending',
    'completed',
    'failed',
    'cancelled',
    'refunded'
);

-- Currency table
CREATE TABLE currencies (
    currency_id SERIAL PRIMARY KEY,
    code VARCHAR(3) UNIQUE NOT NULL,
    name VARCHAR(50) NOT NULL,
    symbol VARCHAR(5) NOT NULL,
    decimal_places INTEGER DEFAULT 2
);

-- Wallet table
CREATE TABLE wallets (
    wallet_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    currency_id INTEGER NOT NULL REFERENCES currencies(currency_id),
    balance DECIMAL(20, 8) DEFAULT 0.0 CHECK (balance >= 0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, currency_id)
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    wallet_id UUID NOT NULL REFERENCES wallets(wallet_id) ON DELETE CASCADE,
    amount DECIMAL(20, 8) NOT NULL,
    transaction_type transaction_type NOT NULL,
    status transaction_status DEFAULT 'pending',
    reference VARCHAR(255),
    description TEXT,
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE
);

-- Transaction audit log
CREATE TABLE transaction_audit (
    audit_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    transaction_id UUID NOT NULL REFERENCES transactions(transaction_id) ON DELETE CASCADE,
    old_status transaction_status,
    new_status transaction_status NOT NULL,
    changed_by UUID REFERENCES users(user_id),
    reason TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_status ON users(status);
CREATE INDEX idx_referral_links_user_id ON referral_links(user_id);
CREATE INDEX idx_referral_relationships_referrer ON referral_relationships(referrer_id);
CREATE INDEX idx_referral_relationships_referred ON referral_relationships(referred_id);
CREATE INDEX idx_wallets_user_id ON wallets(user_id);
CREATE INDEX idx_transactions_wallet_id ON transactions(wallet_id);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_transactions_created_at ON transactions(created_at);

-- Triggers for automatic timestamp updates
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

-- Function to handle referral bonus transactions
CREATE OR REPLACE FUNCTION process_referral_bonus()
RETURNS TRIGGER AS $$
DECLARE
    referrer_wallet UUID;
    bonus_amount DECIMAL(20, 8);
BEGIN
    -- Only process when transaction is completed and is a deposit/purchase
    IF NEW.status = 'completed' AND (NEW.transaction_type = 'deposit' OR NEW.transaction_type = 'purchase') THEN
        -- Find referrer for this user
        SELECT r.referrer_id INTO referrer_wallet
        FROM referral_relationships r
        JOIN wallets w ON w.user_id = r.referred_id
        WHERE w.wallet_id = NEW.wallet_id;
        
        -- If referrer exists and has a wallet in the same currency
        IF referrer_wallet IS NOT NULL THEN
            SELECT w.wallet_id INTO referrer_wallet
            FROM wallets w
            WHERE w.user_id = referrer_wallet AND w.currency_id = (
                SELECT currency_id FROM wallets WHERE wallet_id = NEW.wallet_id
            );
            
            -- Calculate bonus (5% of transaction amount)
            bonus_amount := NEW.amount * 0.05;
            
            -- Create referral bonus transaction
            INSERT INTO transactions (
                wallet_id,
                amount,
                transaction_type,
                status,
                reference,
                description
            ) VALUES (
                referrer_wallet,
                bonus_amount,
                'referral_bonus',
                'completed',
                NEW.transaction_id::TEXT,
                'Referral bonus for transaction ' || NEW.transaction_id::TEXT
            );
            
            -- Update referrer's wallet balance
            UPDATE wallets
            SET balance = balance + bonus_amount
            WHERE wallet_id = referrer_wallet;
        END IF;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_referral_bonus
AFTER UPDATE ON transactions
FOR EACH ROW EXECUTE FUNCTION process_referral_bonus();
```
