"""
Generated Code Metadata:
========================
Original URL: https://claimcoins.net
Prompt: "Design a database schema to store faucet claim history, user information, and payout records, similar to Claimcoins' database structure."
Generated: DETERMINISTIC_86b372c3ad08d745
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing faucet claim history, user information, and payout records

-- Create a table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,  -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store faucet claim history
CREATE TABLE claims (
    claim_id SERIAL PRIMARY KEY,          -- Unique identifier for each claim
    user_id INT NOT NULL,                 -- Foreign key referencing the user
    claim_amount DECIMAL(10, 2) NOT NULL, -- Amount claimed in the faucet
    claim_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the claim
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store payout records
CREATE TABLE payouts (
    payout_id SERIAL PRIMARY KEY,          -- Unique identifier for each payout
    user_id INT NOT NULL,                  -- Foreign key referencing the user
    payout_amount DECIMAL(10, 2) NOT NULL, -- Amount paid out to the user
    payout_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the payout
    status VARCHAR(20) NOT NULL DEFAULT 'pending', -- Status of the payout (e.g., pending, completed, failed)
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_claim_user ON claims(user_id);
CREATE INDEX idx_payout_user ON payouts(user_id);
```
