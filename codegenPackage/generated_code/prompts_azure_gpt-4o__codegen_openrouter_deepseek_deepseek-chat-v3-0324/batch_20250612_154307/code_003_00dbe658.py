"""
Generated Code Metadata:
========================
Original URL: https://coinrush.bet
Prompt: Create a database schema for tracking user activity in a crypto casino, including fields for game type, bet amount, winnings, and cashback calculations.
Generated: DETERMINISTIC_00dbe65881b9c756
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking user activity in a crypto casino

-- Users table to store basic user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    wallet_address VARCHAR(100) UNIQUE NOT NULL,
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Games table to store available game types
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,
    game_name VARCHAR(50) UNIQUE NOT NULL,
    game_category VARCHAR(50) NOT NULL,
    house_edge DECIMAL(5, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Currency table to support multiple cryptocurrencies
CREATE TABLE currencies (
    currency_id SERIAL PRIMARY KEY,
    currency_code VARCHAR(10) UNIQUE NOT NULL,
    currency_name VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- User balances table
CREATE TABLE user_balances (
    balance_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    currency_id INTEGER REFERENCES currencies(currency_id),
    balance DECIMAL(20, 8) NOT NULL DEFAULT 0,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, currency_id)
);

-- Bets table to track all user bets
CREATE TABLE bets (
    bet_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    game_id INTEGER REFERENCES games(game_id),
    currency_id INTEGER REFERENCES currencies(currency_id),
    bet_amount DECIMAL(20, 8) NOT NULL,
    payout_amount DECIMAL(20, 8),
    outcome BOOLEAN, -- true for win, false for loss
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE,
    server_seed_hash VARCHAR(64),
    client_seed VARCHAR(64),
    nonce BIGINT,
    result_data JSONB,
    CONSTRAINT valid_bet CHECK (bet_amount > 0)
);

-- Cashback calculations table
CREATE TABLE cashback (
    cashback_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    currency_id INTEGER REFERENCES currencies(currency_id),
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    total_bets DECIMAL(20, 8) NOT NULL DEFAULT 0,
    total_losses DECIMAL(20, 8) NOT NULL DEFAULT 0,
    cashback_percentage DECIMAL(5, 2) NOT NULL,
    cashback_amount DECIMAL(20, 8) NOT NULL DEFAULT 0,
    paid_out BOOLEAN DEFAULT FALSE,
    payout_date TIMESTAMP WITH TIME ZONE,
    CONSTRAINT valid_period CHECK (period_end > period_start),
    CONSTRAINT valid_percentage CHECK (cashback_percentage >= 0 AND cashback_percentage <= 100)
);

-- Transaction history table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    currency_id INTEGER REFERENCES currencies(currency_id),
    amount DECIMAL(20, 8) NOT NULL,
    transaction_type VARCHAR(20) NOT NULL, -- deposit, withdrawal, cashback, etc.
    status VARCHAR(20) NOT NULL, -- pending, completed, failed
    tx_hash VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE,
    notes TEXT
);

-- User statistics table
CREATE TABLE user_statistics (
    stats_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    currency_id INTEGER REFERENCES currencies(currency_id),
    total_bets DECIMAL(20, 8) NOT NULL DEFAULT 0,
    total_wins DECIMAL(20, 8) NOT NULL DEFAULT 0,
    total_losses DECIMAL(20, 8) NOT NULL DEFAULT 0,
    biggest_win DECIMAL(20, 8) NOT NULL DEFAULT 0,
    biggest_loss DECIMAL(20, 8) NOT NULL DEFAULT 0,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, currency_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_bets_user_id ON bets(user_id);
CREATE INDEX idx_bets_created_at ON bets(created_at);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_created_at ON transactions(created_at);
CREATE INDEX idx_cashback_user_id ON cashback(user_id);
CREATE INDEX idx_cashback_period ON cashback(period_start, period_end);
```
