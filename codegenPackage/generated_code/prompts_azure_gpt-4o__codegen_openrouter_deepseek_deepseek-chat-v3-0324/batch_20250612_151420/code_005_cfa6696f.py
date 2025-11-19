"""
Generated Code Metadata:
========================
Original URL: https://buylibracoins.com
Prompt: Suggest a database schema for tracking wallet transactions, slot game bonuses, and user activity, optimized for platforms like "สล็อตใช้วอเลท."
Generated: DETERMINISTIC_cfa6696f6dab1c52
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking wallet transactions, slot game bonuses, and user activity
-- Designed for platforms like "สล็อตใช้วอเลท"

-- Users table to store basic user information
CREATE TABLE users (
    user_id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    salt VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20),
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    account_status VARCHAR(20) DEFAULT 'active' CHECK (account_status IN ('active', 'suspended', 'banned')),
    verification_status VARCHAR(20) DEFAULT 'unverified' CHECK (verification_status IN ('unverified', 'pending', 'verified')),
    balance DECIMAL(18, 2) DEFAULT 0.00 CHECK (balance >= 0)
);

-- User wallet transactions
CREATE TABLE wallet_transactions (
    transaction_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(user_id),
    amount DECIMAL(18, 2) NOT NULL,
    transaction_type VARCHAR(20) NOT NULL CHECK (transaction_type IN ('deposit', 'withdrawal', 'win', 'bet', 'bonus', 'adjustment')),
    transaction_status VARCHAR(20) DEFAULT 'pending' CHECK (transaction_status IN ('pending', 'completed', 'failed', 'cancelled')),
    reference_id VARCHAR(100),
    transaction_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    balance_before DECIMAL(18, 2) NOT NULL,
    balance_after DECIMAL(18, 2) NOT NULL,
    payment_method VARCHAR(50),
    ip_address VARCHAR(45)
);

-- Slot games information
CREATE TABLE slot_games (
    game_id BIGSERIAL PRIMARY KEY,
    game_name VARCHAR(100) NOT NULL,
    game_provider VARCHAR(50) NOT NULL,
    release_date DATE,
    rtp_percentage DECIMAL(5, 2),
    volatility VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    thumbnail_url VARCHAR(255)
);

-- User game sessions
CREATE TABLE game_sessions (
    session_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(user_id),
    game_id BIGINT NOT NULL REFERENCES slot_games(game_id),
    start_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP WITH TIME ZONE,
    total_bet DECIMAL(18, 2) DEFAULT 0.00,
    total_win DECIMAL(18, 2) DEFAULT 0.00,
    ip_address VARCHAR(45),
    device_info TEXT
);

-- Game transactions (individual spins/bets)
CREATE TABLE game_transactions (
    game_transaction_id BIGSERIAL PRIMARY KEY,
    session_id BIGINT NOT NULL REFERENCES game_sessions(session_id),
    transaction_id BIGINT REFERENCES wallet_transactions(transaction_id),
    bet_amount DECIMAL(18, 2) NOT NULL,
    win_amount DECIMAL(18, 2) DEFAULT 0.00,
    transaction_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    game_data JSONB,
    outcome_details TEXT
);

-- Bonus information
CREATE TABLE bonuses (
    bonus_id BIGSERIAL PRIMARY KEY,
    bonus_name VARCHAR(100) NOT NULL,
    bonus_type VARCHAR(50) NOT NULL CHECK (bonus_type IN ('welcome', 'deposit', 'free_spins', 'loyalty', 'promotional')),
    description TEXT,
    start_date TIMESTAMP WITH TIME ZONE,
    end_date TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    min_deposit DECIMAL(18, 2),
    max_bonus_amount DECIMAL(18, 2),
    wagering_requirement DECIMAL(5, 2),
    applicable_games JSONB
);

-- User bonuses
CREATE TABLE user_bonuses (
    user_bonus_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(user_id),
    bonus_id BIGINT NOT NULL REFERENCES bonuses(bonus_id),
    awarded_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expiry_date TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'used', 'expired', 'cancelled')),
    bonus_amount DECIMAL(18, 2) NOT NULL,
    remaining_amount DECIMAL(18, 2) NOT NULL,
    wagering_requirement DECIMAL(18, 2) NOT NULL,
    wagering_progress DECIMAL(18, 2) DEFAULT 0.00
);

-- User activity log
CREATE TABLE user_activity (
    activity_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(user_id),
    activity_type VARCHAR(50) NOT NULL CHECK (activity_type IN ('login', 'logout', 'game_play', 'deposit', 'withdrawal', 'account_change')),
    activity_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    device_info TEXT,
    details TEXT
);

-- Indexes for performance optimization
CREATE INDEX idx_wallet_transactions_user_id ON wallet_transactions(user_id);
CREATE INDEX idx_wallet_transactions_date ON wallet_transactions(transaction_date);
CREATE INDEX idx_game_sessions_user_id ON game_sessions(user_id);
CREATE INDEX idx_game_transactions_session_id ON game_transactions(session_id);
CREATE INDEX idx_user_activity_user_id ON user_activity(user_id);
CREATE INDEX idx_user_activity_time ON user_activity(activity_time);
```
