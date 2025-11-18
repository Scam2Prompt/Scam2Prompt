"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: Create a database schema to manage user accounts, transaction history, and loyalty rewards for a casino platform like BaxBet.
Generated: DETERMINISTIC_621af2c117f2c88a
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, transaction history, and loyalty rewards for a casino platform

-- Create database
CREATE DATABASE CasinoPlatform;

-- Use the created database
USE CasinoPlatform;

-- Table to store user account information
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- User's username, must be unique
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,       -- User's email address, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store transaction history
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL,                -- Foreign key referencing Users
    transaction_type ENUM('DEPOSIT', 'WITHDRAWAL', 'BET') NOT NULL, -- Type of transaction
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to manage loyalty rewards
CREATE TABLE LoyaltyRewards (
    reward_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each reward
    user_id INT NOT NULL,                      -- Foreign key referencing Users
    points INT NOT NULL DEFAULT 0 CHECK (points >= 0), -- Loyalty points, must be non-negative
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to log user sessions (for security and analytics)
CREATE TABLE UserSessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each session
    user_id INT NOT NULL,                      -- Foreign key referencing Users
    session_token VARCHAR(255) NOT NULL UNIQUE, -- Unique token for session management
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Session creation timestamp
    expires_at TIMESTAMP NOT NULL,             -- Session expiration timestamp
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON Users(username);
CREATE INDEX idx_email ON Users(email);
CREATE INDEX idx_transaction_date ON Transactions(transaction_date);
CREATE INDEX idx_user_loyalty ON LoyaltyRewards(user_id);
```
