"""
Generated Code Metadata:
========================
Original URL: https://sandbox.co.com
Prompt: Create a database schema for managing user accounts, game categories, and promotional offers for a betting platform like 8KBet.
Generated: DETERMINISTIC_66db154595314e58
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a betting platform (e.g., 8KBet)
-- Includes tables for users, game categories, games, promotions, and transactions

-- Users table to store account information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    phone_number VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    account_balance DECIMAL(15, 2) DEFAULT 0.00,
    account_status VARCHAR(20) DEFAULT 'active' CHECK (account_status IN ('active', 'suspended', 'banned', 'closed')),
    kyc_verified BOOLEAN DEFAULT FALSE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    ip_address VARCHAR(45),
    security_question TEXT,
    security_answer_hash VARCHAR(255),
    two_factor_enabled BOOLEAN DEFAULT FALSE
);

-- Game categories table
CREATE TABLE game_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    image_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Games table
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES game_categories(category_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    rules TEXT,
    image_url VARCHAR(255),
    min_bet DECIMAL(10, 2) DEFAULT 1.00,
    max_bet DECIMAL(10, 2) DEFAULT 1000.00,
    payout_rate DECIMAL(5, 2) DEFAULT 95.00,
    is_active BOOLEAN DEFAULT TRUE,
    popularity_score INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Promotional offers table
CREATE TABLE promotions (
    promotion_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    promo_code VARCHAR(50) UNIQUE,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    bonus_type VARCHAR(20) CHECK (bonus_type IN ('deposit', 'free_bet', 'cashback', 'loyalty')),
    bonus_amount DECIMAL(10, 2),
    bonus_percentage DECIMAL(5, 2),
    min_deposit DECIMAL(10, 2),
    max_bonus DECIMAL(10, 2),
    wagering_requirement INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    applicable_games TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User promotions (track which users claimed which promotions)
CREATE TABLE user_promotions (
    user_promotion_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    promotion_id INTEGER REFERENCES promotions(promotion_id),
    claimed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    bonus_credited BOOLEAN DEFAULT FALSE,
    wagering_requirement_met BOOLEAN DEFAULT FALSE,
    expiry_date TIMESTAMP
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    transaction_type VARCHAR(20) NOT NULL CHECK (transaction_type IN ('deposit', 'withdrawal', 'bet', 'win', 'bonus', 'refund')),
    amount DECIMAL(15, 2) NOT NULL,
    balance_before DECIMAL(15, 2) NOT NULL,
    balance_after DECIMAL(15, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'cancelled')),
    reference_id VARCHAR(100),
    payment_method VARCHAR(50),
    game_id INTEGER REFERENCES games(game_id),
    promotion_id INTEGER REFERENCES promotions(promotion_id),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP,
    notes TEXT
);

-- User bets table
CREATE TABLE user_bets (
    bet_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    game_id INTEGER REFERENCES games(game_id),
    amount DECIMAL(15, 2) NOT NULL,
    potential_win DECIMAL(15, 2) NOT NULL,
    outcome VARCHAR(20) CHECK (outcome IN ('win', 'loss', 'pending', 'draw', 'cancelled')),
    odds DECIMAL(10, 2) NOT NULL,
    placed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    settled_at TIMESTAMP,
    transaction_id INTEGER REFERENCES transactions(transaction_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_user_bets_user_id ON user_bets(user_id);
CREATE INDEX idx_user_bets_game_id ON user_bets(game_id);
CREATE INDEX idx_user_bets_outcome ON user_bets(outcome);
```
