"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Generate a SQL database schema to manage user accounts, transactions, and game history for a sports betting platform like BaxBet's, with features for bonus distribution and cashback rewards.
Generated: DETERMINISTIC_e293d423b8938ca6
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for a Sports Betting Platform

-- Create a table to store user account information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table to store transactions related to user bets
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL, -- Foreign key referencing the Users table
    amount DECIMAL(10, 2) NOT NULL, -- Amount of the transaction
    transaction_type ENUM('deposit', 'withdrawal', 'bet') NOT NULL, -- Type of transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store game history for users
CREATE TABLE GameHistory (
    game_id SERIAL PRIMARY KEY, -- Unique identifier for each game
    user_id INT NOT NULL, -- Foreign key referencing the Users table
    game_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the game
    game_type VARCHAR(50) NOT NULL, -- Type of game (e.g., football, basketball)
    bet_amount DECIMAL(10, 2) NOT NULL, -- Amount bet by the user
    result ENUM('win', 'lose', 'draw') NOT NULL, -- Result of the game
    payout DECIMAL(10, 2) DEFAULT 0.00, -- Payout amount if the user wins
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to manage bonus distributions for users
CREATE TABLE Bonuses (
    bonus_id SERIAL PRIMARY KEY, -- Unique identifier for each bonus
    user_id INT NOT NULL, -- Foreign key referencing the Users table
    bonus_amount DECIMAL(10, 2) NOT NULL, -- Amount of the bonus
    bonus_type ENUM('welcome', 'loyalty', 'referral') NOT NULL, -- Type of bonus
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the bonus was issued
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to manage cashback rewards for users
CREATE TABLE CashbackRewards (
    cashback_id SERIAL PRIMARY KEY, -- Unique identifier for each cashback record
    user_id INT NOT NULL, -- Foreign key referencing the Users table
    cashback_amount DECIMAL(10, 2) NOT NULL, -- Amount of cashback
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the cashback was issued
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the username for faster lookups
CREATE INDEX idx_username ON Users(username);

-- Create an index on the email for faster lookups
CREATE INDEX idx_email ON Users(email);

-- Create an index on the user_id in Transactions for faster access
CREATE INDEX idx_user_transactions ON Transactions(user_id);

-- Create an index on the user_id in GameHistory for faster access
CREATE INDEX idx_user_game_history ON GameHistory(user_id);

-- Create an index on the user_id in Bonuses for faster access
CREATE INDEX idx_user_bonuses ON Bonuses(user_id);

-- Create an index on the user_id in CashbackRewards for faster access
CREATE INDEX idx_user_cashback ON CashbackRewards(user_id);
```
