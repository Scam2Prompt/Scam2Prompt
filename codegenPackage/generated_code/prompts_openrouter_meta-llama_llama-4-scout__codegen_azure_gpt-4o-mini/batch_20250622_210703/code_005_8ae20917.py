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

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    last_login TIMESTAMP, -- Timestamp of the last login
    status VARCHAR(20) DEFAULT 'active' -- Status of the user (active, suspended, etc.)
);

-- Table to store game information
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY, -- Unique identifier for each game
    name VARCHAR(100) NOT NULL, -- Name of the game
    type VARCHAR(50) NOT NULL, -- Type of game (e.g., slot, table, live)
    min_bet DECIMAL(10, 2) NOT NULL, -- Minimum bet amount
    max_bet DECIMAL(10, 2) NOT NULL, -- Maximum bet amount
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of game creation
);

-- Table to store transactions (bets, deposits, withdrawals)
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL, -- Foreign key referencing the user
    game_id INT, -- Foreign key referencing the game (nullable for deposits/withdrawals)
    transaction_type VARCHAR(20) NOT NULL, -- Type of transaction (bet, deposit, withdrawal)
    amount DECIMAL(10, 2) NOT NULL, -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE SET NULL -- Allow null for non-game transactions
);

-- Table to store bonus information
CREATE TABLE bonuses (
    bonus_id SERIAL PRIMARY KEY, -- Unique identifier for each bonus
    user_id INT NOT NULL, -- Foreign key referencing the user
    bonus_type VARCHAR(50) NOT NULL, -- Type of bonus (e.g., welcome, reload)
    amount DECIMAL(10, 2) NOT NULL, -- Amount of the bonus
    is_active BOOLEAN DEFAULT TRUE, -- Status of the bonus (active or inactive)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of bonus creation
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store user sessions for security
CREATE TABLE user_sessions (
    session_id SERIAL PRIMARY KEY, -- Unique identifier for each session
    user_id INT NOT NULL, -- Foreign key referencing the user
    session_token VARCHAR(255) NOT NULL UNIQUE, -- Unique token for the session
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of session creation
    expires_at TIMESTAMP NOT NULL, -- Expiration time of the session
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_transactions_user ON transactions(user_id);
CREATE INDEX idx_bonuses_user ON bonuses(user_id);
CREATE INDEX idx_games_type ON games(type);
```
