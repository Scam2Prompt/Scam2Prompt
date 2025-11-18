"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://republik.pages.dev
Prompt: Create a database schema for an online slot platform that includes game providers such as Pragmatic Play, Habanero, Joker123, PGSoft, and Spadegaming, as listed on ANGKA805.
Generated: DETERMINISTIC_c9b43a0940a09e01
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an online slot platform

-- NOTE: This schema assumes a relational database system like MySQL or PostgreSQL.

-- Table to store game providers
CREATE TABLE game_providers (
    provider_id SERIAL PRIMARY KEY,  -- Unique ID for each game provider
    provider_name VARCHAR(255) NOT NULL UNIQUE,  -- Name of the game provider
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the provider was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for the last update
);

-- Insert the predefined game providers into the table
INSERT INTO game_providers (provider_name)
VALUES 
    ('Pragmatic Play'),
    ('Habanero'),
    ('Joker123'),
    ('PGSoft'),
    ('Spadegaming');

-- Table to store slot games
CREATE TABLE slot_games (
    game_id SERIAL PRIMARY KEY,  -- Unique ID for each slot game
    game_name VARCHAR(255) NOT NULL,  -- Name of the slot game
    provider_id INT NOT NULL,  -- Foreign key referencing the game provider
    is_active BOOLEAN DEFAULT TRUE,  -- Whether the game is active or inactive
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the game was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for the last update
    CONSTRAINT fk_provider FOREIGN KEY (provider_id) REFERENCES game_providers(provider_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table to store users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,  -- Unique ID for each user
    username VARCHAR(255) NOT NULL UNIQUE,  -- Unique username for the user
    email VARCHAR(255) NOT NULL UNIQUE,  -- Email address of the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    balance DECIMAL(15, 2) DEFAULT 0.00,  -- User's account balance
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the user account was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for the last update
);

-- Table to store user gameplay sessions
CREATE TABLE gameplay_sessions (
    session_id SERIAL PRIMARY KEY,  -- Unique ID for each gameplay session
    user_id INT NOT NULL,  -- Foreign key referencing the user
    game_id INT NOT NULL,  -- Foreign key referencing the slot game
    bet_amount DECIMAL(15, 2) NOT NULL,  -- Amount bet by the user
    winnings DECIMAL(15, 2) DEFAULT 0.00,  -- Amount won in the session
    session_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the session started
    session_end TIMESTAMP NULL,  -- Timestamp when the session ended
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_game FOREIGN KEY (game_id) REFERENCES slot_games(game_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table to store transactions (e.g., deposits, withdrawals)
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,  -- Unique ID for each transaction
    user_id INT NOT NULL,  -- Foreign key referencing the user
    transaction_type ENUM('deposit', 'withdrawal', 'bonus') NOT NULL,  -- Type of transaction
    amount DECIMAL(15, 2) NOT NULL,  -- Amount of the transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the transaction was made
    CONSTRAINT fk_transaction_user FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table to store game provider statistics
CREATE TABLE provider_statistics (
    stat_id SERIAL PRIMARY KEY,  -- Unique ID for each statistic entry
    provider_id INT NOT NULL,  -- Foreign key referencing the game provider
    total_games INT DEFAULT 0,  -- Total number of games provided by the provider
    total_players INT DEFAULT 0,  -- Total number of players who played games from this provider
    total_winnings DECIMAL(15, 2) DEFAULT 0.00,  -- Total amount of winnings distributed by this provider
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the statistics were recorded
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for the last update
    CONSTRAINT fk_statistics_provider FOREIGN KEY (provider_id) REFERENCES game_providers(provider_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Define indexes for performance optimization
CREATE INDEX idx_user_balance ON users(balance);
CREATE INDEX idx_game_provider ON slot_games(provider_id);
CREATE INDEX idx_transaction_user ON transactions(user_id);
```
