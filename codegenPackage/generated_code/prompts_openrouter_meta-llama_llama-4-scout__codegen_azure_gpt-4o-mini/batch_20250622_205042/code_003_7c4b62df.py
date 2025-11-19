"""
Generated Code Metadata:
========================
Original URL: https://bitmixr.biz
Prompt: Design a database schema for a slot game platform with tables for users, games, bonuses, and transactions.
Generated: DETERMINISTIC_7c4b62df7a00d06d
Batch ID: 20250622_205042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a slot game platform

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store game information
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,           -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,      -- Name of the game
    game_description TEXT,                 -- Description of the game
    release_date DATE NOT NULL,            -- Release date of the game
    min_bet DECIMAL(10, 2) NOT NULL,      -- Minimum bet amount for the game
    max_bet DECIMAL(10, 2) NOT NULL,      -- Maximum bet amount for the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Game creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store bonus information
CREATE TABLE bonuses (
    bonus_id SERIAL PRIMARY KEY,           -- Unique identifier for each bonus
    bonus_name VARCHAR(100) NOT NULL,      -- Name of the bonus
    bonus_description TEXT,                 -- Description of the bonus
    bonus_amount DECIMAL(10, 2) NOT NULL,  -- Amount of the bonus
    expiration_date DATE NOT NULL,          -- Expiration date of the bonus
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Bonus creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store transaction information
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,     -- Unique identifier for each transaction
    user_id INT NOT NULL,                   -- Foreign key referencing users
    game_id INT NOT NULL,                   -- Foreign key referencing games
    bonus_id INT,                           -- Foreign key referencing bonuses (nullable)
    transaction_type VARCHAR(50) NOT NULL,  -- Type of transaction (e.g., 'bet', 'win', 'bonus')
    amount DECIMAL(10, 2) NOT NULL,        -- Amount involved in the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure user integrity
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE, -- Ensure game integrity
    FOREIGN KEY (bonus_id) REFERENCES bonuses(bonus_id) ON DELETE SET NULL -- Allow bonuses to be nullable
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_games_game_name ON games(game_name);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_game_id ON transactions(game_id);
```
