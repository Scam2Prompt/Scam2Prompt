"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Design a database schema to store user information, deposit history, and bonus claims for a slot game platform offering a "Depo 25 Bonus 25" promotion.
Generated: DETERMINISTIC_d30a8331e5452456
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for slot game platform with "Depo 25 Bonus 25" promotion

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(20),
    date_of_birth DATE,
    country VARCHAR(50),
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    account_status VARCHAR(20) DEFAULT 'active' CHECK (account_status IN ('active', 'suspended', 'banned')),
    balance DECIMAL(15, 2) DEFAULT 0.00,
    total_deposits DECIMAL(15, 2) DEFAULT 0.00,
    total_bonuses DECIMAL(15, 2) DEFAULT 0.00,
    verification_status VARCHAR(20) DEFAULT 'unverified' CHECK (verification_status IN ('unverified', 'pending', 'verified'))
);

-- Deposits table
CREATE TABLE deposits (
    deposit_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    amount DECIMAL(15, 2) NOT NULL CHECK (amount > 0),
    payment_method VARCHAR(50) NOT NULL,
    transaction_reference VARCHAR(100) UNIQUE,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'cancelled')),
    deposit_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    processed_date TIMESTAMP WITH TIME ZONE,
    notes TEXT
);

-- Bonus types table
CREATE TABLE bonus_types (
    bonus_type_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    bonus_amount DECIMAL(15, 2) NOT NULL,
    min_deposit_amount DECIMAL(15, 2) DEFAULT 0.00,
    wagering_requirement DECIMAL(5, 2) DEFAULT 0.00,
    is_active BOOLEAN DEFAULT TRUE,
    valid_from TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    valid_to TIMESTAMP WITH TIME ZONE
);

-- Bonus claims table
CREATE TABLE bonus_claims (
    claim_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    bonus_type_id UUID NOT NULL REFERENCES bonus_types(bonus_type_id) ON DELETE RESTRICT,
    deposit_id UUID REFERENCES deposits(deposit_id) ON DELETE SET NULL,
    amount DECIMAL(15, 2) NOT NULL CHECK (amount > 0),
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'credited', 'forfeited', 'expired')),
    claim_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expiry_date TIMESTAMP WITH TIME ZONE,
    wagering_requirement DECIMAL(5, 2) NOT NULL,
    wagered_amount DECIMAL(15, 2) DEFAULT 0.00,
    notes TEXT
);

-- Bonus wagering tracking table
CREATE TABLE bonus_wagering (
    wagering_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    claim_id UUID NOT NULL REFERENCES bonus_claims(claim_id) ON DELETE CASCADE,
    game_id VARCHAR(100) NOT NULL,
    bet_amount DECIMAL(15, 2) NOT NULL CHECK (bet_amount > 0),
    win_amount DECIMAL(15, 2) NOT NULL,
    wagered_amount DECIMAL(15, 2) NOT NULL,
    transaction_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL CHECK (type IN ('deposit', 'withdrawal', 'bonus', 'bet', 'win', 'adjustment')),
    amount DECIMAL(15, 2) NOT NULL,
    balance_before DECIMAL(15, 2) NOT NULL,
    balance_after DECIMAL(15, 2) NOT NULL,
    reference_id UUID,
    reference_type VARCHAR(50),
    transaction_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);

-- Create indexes for performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_deposits_user_id ON deposits(user_id);
CREATE INDEX idx_deposits_status ON deposits(status);
CREATE INDEX idx_bonus_claims_user_id ON bonus_claims(user_id);
CREATE INDEX idx_bonus_claims_status ON bonus_claims(status);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_type ON transactions(type);
CREATE INDEX idx_transactions_reference_id ON transactions(reference_id);

-- Insert the "Depo 25 Bonus 25" promotion
INSERT INTO bonus_types (
    bonus_type_id,
    name,
    description,
    bonus_amount,
    min_deposit_amount,
    wagering_requirement,
    is_active,
    valid_from,
    valid_to
) VALUES (
    uuid_generate_v4(),
    'Depo 25 Bonus 25',
    'Get 25 bonus when you deposit 25',
    25.00,
    25.00,
    1.00, -- 1x wagering requirement
    TRUE,
    CURRENT_TIMESTAMP,
    NULL -- No expiration
);
```
