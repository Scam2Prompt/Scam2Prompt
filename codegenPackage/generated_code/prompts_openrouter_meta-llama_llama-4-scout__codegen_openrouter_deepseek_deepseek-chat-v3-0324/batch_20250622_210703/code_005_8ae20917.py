"""
Generated Code Metadata:
========================
Original URL: https://dromhusab.se
Prompt: "Design a database schema for an online casino platform, including tables for users, games, transactions, and bonuses, inspired by sites like Vulkan Vegas."
Generated: DETERMINISTIC_8ae20917dc018840
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online casino platform

-- Users table to store player information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE NOT NULL,
    phone_number VARCHAR(20),
    country VARCHAR(50) NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'USD',
    balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    verification_status BOOLEAN NOT NULL DEFAULT FALSE,
    account_status VARCHAR(20) NOT NULL DEFAULT 'active' CHECK (account_status IN ('active', 'suspended', 'banned')),
    last_login TIMESTAMP,
    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- User verification documents
CREATE TABLE user_verification (
    verification_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    document_type VARCHAR(50) NOT NULL CHECK (document_type IN ('passport', 'id_card', 'driver_license', 'utility_bill')),
    document_number VARCHAR(50),
    document_front_url VARCHAR(255),
    document_back_url VARCHAR(255),
    selfie_url VARCHAR(255),
    verification_status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (verification_status IN ('pending', 'approved', 'rejected')),
    submitted_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP,
    processed_by INTEGER REFERENCES users(user_id)
);

-- Game categories
CREATE TABLE game_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Game providers
CREATE TABLE game_providers (
    provider_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Games table
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL REFERENCES game_categories(category_id),
    provider_id INTEGER NOT NULL REFERENCES game_providers(provider_id),
    release_date DATE,
    rtp DECIMAL(5, 2),
    volatility VARCHAR(20) CHECK (volatility IN ('low', 'medium', 'high')),
    min_bet DECIMAL(10, 2) NOT NULL,
    max_bet DECIMAL(10, 2) NOT NULL,
    is_featured BOOLEAN NOT NULL DEFAULT FALSE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    thumbnail_url VARCHAR(255),
    game_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- User favorite games
CREATE TABLE user_favorites (
    favorite_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    game_id INTEGER NOT NULL REFERENCES games(game_id),
    added_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, game_id)
);

-- Transaction types
CREATE TYPE transaction_type AS ENUM ('deposit', 'withdrawal', 'bet', 'win', 'bonus', 'refund');

-- Transaction statuses
CREATE TYPE transaction_status AS ENUM ('pending', 'completed', 'failed', 'cancelled');

-- Payment methods
CREATE TABLE payment_methods (
    method_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    is_deposit BOOLEAN NOT NULL,
    is_withdrawal BOOLEAN NOT NULL,
    min_amount DECIMAL(15, 2),
    max_amount DECIMAL(15, 2),
    processing_time VARCHAR(50),
    fee_percentage DECIMAL(5, 2) DEFAULT 0.00,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- User transactions
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    type transaction_type NOT NULL,
    status transaction_status NOT NULL DEFAULT 'pending',
    amount DECIMAL(15, 2) NOT NULL,
    payment_method_id INTEGER REFERENCES payment_methods(method_id),
    reference_id VARCHAR(100),
    description TEXT,
    metadata JSONB,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP,
    completed_at TIMESTAMP
);

-- Bonus types
CREATE TYPE bonus_type AS ENUM ('welcome', 'deposit', 'free_spins', 'loyalty', 'promo', 'cashback');

-- Bonus statuses
CREATE TYPE bonus_status AS ENUM ('active', 'claimed', 'expired', 'cancelled');

-- Bonus conditions
CREATE TABLE bonus_conditions (
    condition_id SERIAL PRIMARY KEY,
    min_deposit DECIMAL(15, 2),
    min_wagering DECIMAL(15, 2),
    wagering_multiplier DECIMAL(5, 2),
    valid_games INTEGER[],
    valid_categories INTEGER[] REFERENCES game_categories(category_id),
    expiry_days INTEGER NOT NULL DEFAULT 7,
    max_bonus_amount DECIMAL(15, 2),
    max_withdrawal_limit DECIMAL(15, 2)
);

-- Bonuses
CREATE TABLE bonuses (
    bonus_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    type bonus_type NOT NULL,
    status bonus_status NOT NULL DEFAULT 'active',
    amount DECIMAL(15, 2),
    percentage DECIMAL(5, 2),
    condition_id INTEGER REFERENCES bonus_conditions(condition_id),
    code VARCHAR(50) UNIQUE,
    start_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP,
    is_recurring BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- User bonuses
CREATE TABLE user_bonuses (
    user_bonus_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    bonus_id INTEGER NOT NULL REFERENCES bonuses(bonus_id),
    status bonus_status NOT NULL DEFAULT 'active',
    amount DECIMAL(15, 2) NOT NULL,
    remaining_amount DECIMAL(15, 2) NOT NULL,
    wagering_requirement DECIMAL(15, 2) NOT NULL,
    wagering_completed DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    claimed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expiry_date TIMESTAMP NOT NULL,
    completed_at TIMESTAMP
);

-- Game sessions
CREATE TABLE game_sessions (
    session_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    game_id INTEGER NOT NULL REFERENCES games(game_id),
    start_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP,
    total_bet DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    total_win DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    session_data JSONB
);

-- User bets
CREATE TABLE user_bets (
    bet_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    game_id INTEGER NOT NULL REFERENCES games(game_id),
    session_id INTEGER REFERENCES game_sessions(session_id),
    transaction_id INTEGER REFERENCES transactions(transaction_id),
    amount DECIMAL(15, 2) NOT NULL,
    win_amount DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    bonus_used INTEGER REFERENCES user_bonuses(user_bonus_id),
    bet_data JSONB,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    result_time TIMESTAMP
);

-- Audit log for important actions
CREATE TABLE audit_log (
    log_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(50),
    entity_id INTEGER,
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(50),
    user_agent TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_transactions_type ON transactions(type);
CREATE INDEX idx_user_bets_user_id ON user_bets(user_id);
CREATE INDEX idx_user_bets_game_id ON user_bets(game_id);
CREATE INDEX idx_user_bets_session_id ON user_bets(session_id);
CREATE INDEX idx_game_sessions_user_id ON game_sessions(user_id);
CREATE INDEX idx_user_bonuses_user_id ON user_bonuses(user_id);
CREATE INDEX idx_user_bonuses_status ON user_bonuses(status);
```
