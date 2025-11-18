"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panther-ai.pages.dev
Prompt: Design a database schema for tracking PantherAI token transactions, staking rewards, and user-generated items within the PantherAI ecosystem.
Generated: DETERMINISTIC_b5dec956503053e1
Batch ID: 20250612_145510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking PantherAI token transactions, staking rewards, and user-generated items.

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Username of the user
    email VARCHAR(100) NOT NULL UNIQUE,        -- Email of the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user was created
);

CREATE TABLE tokens (
    token_id SERIAL PRIMARY KEY,                -- Unique identifier for each token transaction
    user_id INT NOT NULL,                       -- Foreign key referencing users
    transaction_type VARCHAR(20) NOT NULL,     -- Type of transaction (e.g., 'purchase', 'sale')
    amount DECIMAL(18, 8) NOT NULL,            -- Amount of tokens involved in the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

CREATE TABLE staking (
    staking_id SERIAL PRIMARY KEY,              -- Unique identifier for each staking reward
    user_id INT NOT NULL,                       -- Foreign key referencing users
    amount_staked DECIMAL(18, 8) NOT NULL,     -- Amount of tokens staked
    reward DECIMAL(18, 8) NOT NULL,             -- Reward earned from staking
    staking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when staking occurred
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

CREATE TABLE user_items (
    item_id SERIAL PRIMARY KEY,                 -- Unique identifier for each user-generated item
    user_id INT NOT NULL,                       -- Foreign key referencing users
    item_name VARCHAR(100) NOT NULL,           -- Name of the item
    item_description TEXT NOT NULL,             -- Description of the item
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the item was created
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes to improve query performance
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_transaction_date ON tokens(transaction_date);
CREATE INDEX idx_staking_date ON staking(staking_date);
CREATE INDEX idx_item_name ON user_items(item_name);
```
