"""
Generated Code Metadata:
========================
Original URL: https://tekanslotcepat.site
Prompt: Generate a database schema to manage user accounts, game preferences, and transaction history for a platform similar to Tekanslot.
Generated: DETERMINISTIC_bd33a64d04787461
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a gaming platform similar to Tekanslot

-- Users table to store account information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    salt VARCHAR(100) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    phone_number VARCHAR(20),
    country VARCHAR(50),
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    account_status VARCHAR(20) DEFAULT 'active' CHECK (account_status IN ('active', 'suspended', 'banned', 'deleted')),
    verification_status BOOLEAN DEFAULT FALSE,
    two_factor_enabled BOOLEAN DEFAULT FALSE,
    profile_image_url VARCHAR(255),
    balance DECIMAL(15, 2) DEFAULT 0.00 CHECK (balance >= 0)
);

-- User sessions table
CREATE TABLE user_sessions (
    session_id UUID PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    ip_address VARCHAR(45) NOT NULL,
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Games catalog
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    developer VARCHAR(100) NOT NULL,
    release_date DATE,
    thumbnail_url VARCHAR(255),
    banner_url VARCHAR(255),
    min_bet DECIMAL(10, 2) NOT NULL,
    max_bet DECIMAL(10, 2) NOT NULL,
    rtp_percentage DECIMAL(5, 2) NOT NULL,
    volatility VARCHAR(20) CHECK (volatility IN ('low', 'medium', 'high')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Game categories
CREATE TABLE game_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

-- Game to category mapping
CREATE TABLE game_category_mapping (
    game_id INTEGER NOT NULL REFERENCES games(game_id) ON DELETE CASCADE,
    category_id INTEGER NOT NULL REFERENCES game_categories(category_id) ON DELETE CASCADE,
    PRIMARY KEY (game_id, category_id)
);

-- User game preferences
CREATE TABLE user_game_preferences (
    preference_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    game_id INTEGER NOT NULL REFERENCES games(game_id) ON DELETE CASCADE,
    favorite BOOLEAN DEFAULT FALSE,
    last_played TIMESTAMP WITH TIME ZONE,
    play_count INTEGER DEFAULT 0,
    UNIQUE (user_id, game_id)
);

-- Transaction types
CREATE TYPE transaction_type AS ENUM ('deposit', 'withdrawal', 'bet', 'win', 'bonus', 'refund');

-- Transaction status
CREATE TYPE transaction_status AS ENUM ('pending', 'completed', 'failed', 'cancelled');

-- User transactions
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    amount DECIMAL(15, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    transaction_type transaction_type NOT NULL,
    status transaction_status DEFAULT 'pending',
    reference_id VARCHAR(100),
    description TEXT,
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP WITH TIME ZONE,
    game_id INTEGER REFERENCES games(game_id) ON DELETE SET NULL
);

-- User game sessions
CREATE TABLE game_sessions (
    session_id UUID PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    game_id INTEGER NOT NULL REFERENCES games(game_id) ON DELETE CASCADE,
    start_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP WITH TIME ZONE,
    initial_balance DECIMAL(15, 2) NOT NULL,
    final_balance DECIMAL(15, 2),
    total_bet DECIMAL(15, 2) DEFAULT 0.00,
    total_win DECIMAL(15, 2) DEFAULT 0.00
);

-- Game rounds
CREATE TABLE game_rounds (
    round_id UUID PRIMARY KEY,
    session_id UUID NOT NULL REFERENCES game_sessions(session_id) ON DELETE CASCADE,
    start_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP WITH TIME ZONE,
    bet_amount DECIMAL(15, 2) NOT NULL,
    win_amount DECIMAL(15, 2) DEFAULT 0.00,
    outcome_data JSONB
);

-- Bonuses and promotions
CREATE TABLE bonuses (
    bonus_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    bonus_type VARCHAR(50) NOT NULL,
    amount DECIMAL(15, 2),
    percentage DECIMAL(5, 2),
    min_deposit DECIMAL(15, 2),
    wagering_requirement DECIMAL(10, 2),
    valid_from TIMESTAMP WITH TIME ZONE NOT NULL,
    valid_to TIMESTAMP WITH TIME ZONE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User bonuses
CREATE TABLE user_bonuses (
    user_bonus_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    bonus_id INTEGER NOT NULL REFERENCES bonuses(bonus_id) ON DELETE CASCADE,
    awarded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'used', 'expired', 'cancelled')),
    wagered_amount DECIMAL(15, 2) DEFAULT 0.00,
    remaining_requirement DECIMAL(15, 2)
);

-- Audit log for important actions
CREATE TABLE audit_log (
    log_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    action VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50),
    entity_id INTEGER,
    ip_address VARCHAR(45),
    user_agent TEXT,
    details JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_transactions_created_at ON transactions(created_at);
CREATE INDEX idx_game_sessions_user_id ON game_sessions(user_id);
CREATE INDEX idx_game_sessions_game_id ON game_sessions(game_id);
CREATE INDEX idx_game_rounds_session_id ON game_rounds(session_id);
CREATE INDEX idx_user_bonuses_user_id ON user_bonuses(user_id);
CREATE INDEX idx_user_bonuses_status ON user_bonuses(status);
```
