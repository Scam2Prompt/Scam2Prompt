"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buylibracoins.com
Prompt: Suggest a database schema for tracking wallet transactions, slot game bonuses, and user activity, optimized for platforms like "สล็อตใช้วอเลท."
Generated: DETERMINISTIC_cfa6696f6dab1c52
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking wallet transactions, slot game bonuses, and user activity

-- Create a table for users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,         -- Unique identifier for each user
    username VARCHAR(50) NOT NULL,     -- Username of the user
    email VARCHAR(100) UNIQUE NOT NULL, -- User's email, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for wallet transactions
CREATE TABLE wallet_transactions (
    transaction_id SERIAL PRIMARY KEY,  -- Unique identifier for each transaction
    user_id INT NOT NULL,                -- Foreign key referencing users
    amount DECIMAL(10, 2) NOT NULL,      -- Amount of the transaction
    transaction_type VARCHAR(20) NOT NULL, -- Type of transaction (e.g., deposit, withdrawal)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for slot game bonuses
CREATE TABLE slot_game_bonuses (
    bonus_id SERIAL PRIMARY KEY,         -- Unique identifier for each bonus
    user_id INT NOT NULL,                -- Foreign key referencing users
    bonus_amount DECIMAL(10, 2) NOT NULL, -- Amount of the bonus
    bonus_type VARCHAR(50) NOT NULL,      -- Type of bonus (e.g., welcome, loyalty)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Bonus allocation timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for user activity logs
CREATE TABLE user_activity_logs (
    activity_id SERIAL PRIMARY KEY,      -- Unique identifier for each activity log
    user_id INT NOT NULL,                -- Foreign key referencing users
    activity_type VARCHAR(50) NOT NULL,  -- Type of activity (e.g., login, game play)
    activity_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the activity
    details TEXT,                        -- Additional details about the activity
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on user_id for faster lookups
CREATE INDEX idx_wallet_transactions_user ON wallet_transactions(user_id);
CREATE INDEX idx_slot_game_bonuses_user ON slot_game_bonuses(user_id);
CREATE INDEX idx_user_activity_logs_user ON user_activity_logs(user_id);

-- Add constraints for data validation
ALTER TABLE wallet_transactions
    ADD CONSTRAINT chk_transaction_type CHECK (transaction_type IN ('deposit', 'withdrawal'));

ALTER TABLE slot_game_bonuses
    ADD CONSTRAINT chk_bonus_type CHECK (bonus_type IN ('welcome', 'loyalty', 'referral'));

-- Note: Ensure to handle errors and exceptions in your application code 
-- when interacting with this database schema to maintain data integrity.
```
