"""
Generated Code Metadata:
========================
Original URL: https://www.celestiadao.app
Prompt: Create a database schema for managing user transactions and gameplay history in a slot game platform like BONANZASLOT, ensuring transparency and accountability.
Generated: DETERMINISTIC_bbc93881ecffc58f
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a slot game platform

-- Users table to store player information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    salt VARCHAR(100) NOT NULL,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE,
    verification_token VARCHAR(100),
    CONSTRAINT balance_non_negative CHECK (balance >= 0)
);

-- User profiles for additional information
CREATE TABLE user_profiles (
    profile_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    country VARCHAR(50),
    phone_number VARCHAR(20),
    address TEXT,
    kyc_status VARCHAR(20) DEFAULT 'pending' CHECK (kyc_status IN ('pending', 'verified', 'rejected')),
    kyc_documents JSONB,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Game types available on the platform
CREATE TABLE game_types (
    game_type_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    volatility VARCHAR(20),
    rtp DECIMAL(5, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Individual games
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,
    game_type_id INTEGER NOT NULL REFERENCES game_types(game_type_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    version VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    min_bet DECIMAL(10, 2) NOT NULL,
    max_bet DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_bet_range CHECK (max_bet >= min_bet AND min_bet > 0)
);

-- Game sessions to track each play session
CREATE TABLE game_sessions (
    session_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    game_id INTEGER NOT NULL REFERENCES games(game_id),
    start_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP WITH TIME ZONE,
    initial_balance DECIMAL(15, 2) NOT NULL,
    final_balance DECIMAL(15, 2),
    CONSTRAINT valid_session_time CHECK (end_time IS NULL OR end_time >= start_time)
);

-- Game rounds to track individual spins/plays
CREATE TABLE game_rounds (
    round_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES game_sessions(session_id),
    round_number INTEGER NOT NULL,
    bet_amount DECIMAL(10, 2) NOT NULL,
    win_amount DECIMAL(10, 2) DEFAULT 0.00,
    round_data JSONB NOT NULL, -- Stores game-specific data like symbols, multipliers
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_bet CHECK (bet_amount > 0),
    CONSTRAINT positive_win CHECK (win_amount >= 0)
);

-- Transaction types
CREATE TABLE transaction_types (
    type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    affects_balance BOOLEAN DEFAULT TRUE,
    is_deposit BOOLEAN DEFAULT FALSE,
    is_withdrawal BOOLEAN DEFAULT FALSE,
    is_bonus BOOLEAN DEFAULT FALSE
);

-- Financial transactions
CREATE TABLE transactions (
    transaction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    type_id INTEGER NOT NULL REFERENCES transaction_types(type_id),
    amount DECIMAL(15, 2) NOT NULL,
    balance_before DECIMAL(15, 2) NOT NULL,
    balance_after DECIMAL(15, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'cancelled')),
    reference_id VARCHAR(100),
    round_id UUID REFERENCES game_rounds(round_id),
    session_id UUID REFERENCES game_sessions(session_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP WITH TIME ZONE,
    notes TEXT,
    CONSTRAINT valid_balance_transition CHECK (
        (amount >= 0 AND balance_after = balance_before + amount) OR
        (amount < 0 AND balance_after = balance_before + amount)
    )
);

-- Bonus offers
CREATE TABLE bonuses (
    bonus_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    bonus_type VARCHAR(50) NOT NULL,
    amount DECIMAL(15, 2),
    percentage DECIMAL(5, 2),
    min_deposit DECIMAL(15, 2),
    wagering_requirement DECIMAL(5, 2),
    valid_from TIMESTAMP WITH TIME ZONE NOT NULL,
    valid_to TIMESTAMP WITH TIME ZONE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_bonus_dates CHECK (valid_to > valid_from)
);

-- User bonuses
CREATE TABLE user_bonuses (
    user_bonus_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    bonus_id INTEGER NOT NULL REFERENCES bonuses(bonus_id),
    transaction_id UUID REFERENCES transactions(transaction_id),
    amount_awarded DECIMAL(15, 2) NOT NULL,
    amount_remaining DECIMAL(15, 2) NOT NULL,
    wagering_remaining DECIMAL(15, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'used', 'expired', 'cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    CONSTRAINT valid_bonus_amounts CHECK (amount_remaining >= 0 AND amount_remaining <= amount_awarded)
);

-- Audit log for important actions
CREATE TABLE audit_log (
    log_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    action VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50),
    entity_id VARCHAR(100),
    old_value JSONB,
    new_value JSONB,
    ip_address VARCHAR(50),
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_game_rounds_session_id ON game_rounds(session_id);
CREATE INDEX idx_game_sessions_user_id ON game_sessions(user_id);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_created_at ON transactions(created_at);
CREATE INDEX idx_user_bonuses_user_id ON user_bonuses(user_id);
CREATE INDEX idx_audit_log_created_at ON audit_log(created_at);
```
