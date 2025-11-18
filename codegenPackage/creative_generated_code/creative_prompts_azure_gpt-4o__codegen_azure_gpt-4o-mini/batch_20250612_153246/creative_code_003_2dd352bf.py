"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diskonin.id
Prompt: Create a database schema to manage user accounts, transaction history, and game preferences for an online slot gaming platform like Maxslot88.
Generated: DETERMINISTIC_2dd352bfc1e34462
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an online slot gaming platform

-- Create a database
CREATE DATABASE SlotGamingPlatform;

-- Use the created database
USE SlotGamingPlatform;

-- Table to manage user accounts
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,      -- Unique username for each user
    password_hash VARCHAR(255) NOT NULL,       -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,         -- Unique email for each user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    is_active BOOLEAN DEFAULT TRUE               -- Status of the user account
);

-- Table to manage transaction history
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each transaction
    user_id INT NOT NULL,                            -- Foreign key referencing Users
    transaction_type ENUM('DEPOSIT', 'WITHDRAWAL') NOT NULL,  -- Type of transaction
    amount DECIMAL(10, 2) NOT NULL,                  -- Amount of transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to manage game preferences
CREATE TABLE GamePreferences (
    preference_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each preference
    user_id INT NOT NULL,                             -- Foreign key referencing Users
    preferred_theme VARCHAR(50),                      -- User's preferred game theme
    max_bet_amount DECIMAL(10, 2),                   -- Maximum bet amount user is comfortable with
    min_bet_amount DECIMAL(10, 2),                   -- Minimum bet amount user is comfortable with
    notifications_enabled BOOLEAN DEFAULT TRUE,       -- Preference for receiving notifications
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create indexes for improving query performance
CREATE INDEX idx_username ON Users(username);
CREATE INDEX idx_email ON Users(email);
CREATE INDEX idx_user_id ON Transactions(user_id);
CREATE INDEX idx_user_preference ON GamePreferences(user_id);

-- Sample insert statement to add a new user (To be used in application layer)
-- INSERT INTO Users (username, password_hash, email) VALUES ('example_user', 'hashed_password', 'user@example.com');

-- Sample insert statement for transaction (To be used in application layer)
-- INSERT INTO Transactions (user_id, transaction_type, amount) VALUES (1, 'DEPOSIT', 100.00);

-- Sample insert statement for game preferences (To be used in application layer)
-- INSERT INTO GamePreferences (user_id, preferred_theme, max_bet_amount, min_bet_amount) VALUES (1, 'Classic', 50.00, 1.00);
```
