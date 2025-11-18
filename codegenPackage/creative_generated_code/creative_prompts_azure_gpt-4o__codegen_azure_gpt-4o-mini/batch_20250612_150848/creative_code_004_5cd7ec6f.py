"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eos-token.org
Prompt: Create a database schema for managing user accounts, transaction history, and VIP rewards programs, modeled after the spacex168 system.
Generated: DETERMINISTIC_5cd7ec6fbbe072f8
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, transaction history, and VIP rewards programs

-- Create a table for user accounts
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for contacting the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for secure authentication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the account was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for transaction history
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL, -- Reference to the user making the transaction
    amount DECIMAL(10, 2) NOT NULL, -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    transaction_type VARCHAR(50) NOT NULL, -- Type of transaction (e.g., 'deposit', 'withdrawal')
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Referencing the user table
);

-- Create a table for VIP rewards programs
CREATE TABLE vip_rewards (
    reward_id SERIAL PRIMARY KEY, -- Unique identifier for each reward program
    user_id INT NOT NULL, -- Reference to the user receiving the reward
    reward_points INT NOT NULL DEFAULT 0, -- Points accumulated by the user
    reward_level VARCHAR(50) NOT NULL, -- Current VIP level of the user
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Referencing the user table
);

-- Optional: Create an index for faster searching by username
CREATE INDEX idx_username ON users(username);

-- Optional: Create an index for faster transaction searches by user_id
CREATE INDEX idx_user_transactions ON transactions(user_id);

-- Optional: Create an index for faster searches by user_id in vip_rewards
CREATE INDEX idx_vip_user ON vip_rewards(user_id);
```
