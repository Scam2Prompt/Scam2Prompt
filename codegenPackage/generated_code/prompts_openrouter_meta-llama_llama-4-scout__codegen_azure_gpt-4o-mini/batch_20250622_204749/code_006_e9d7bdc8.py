"""
Generated Code Metadata:
========================
Original URL: https://usdtclaim.com
Prompt: Design a basic database schema for storing user accounts, referrals, and transaction history for a USDT claim faucet service, ensuring data integrity and security.
Generated: DETERMINISTIC_e9d7bdc809c53ffd
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a USDT claim faucet service

-- Create a table to store user accounts
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store referral information
CREATE TABLE referrals (
    referral_id SERIAL PRIMARY KEY, -- Unique identifier for each referral
    referrer_id INT NOT NULL, -- User ID of the referrer
    referred_id INT NOT NULL, -- User ID of the referred user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of referral creation
    FOREIGN KEY (referrer_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure referer exists
    FOREIGN KEY (referred_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referred user exists
);

-- Create a table to store transaction history
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL, -- User ID of the account making the transaction
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount of USDT involved in the transaction
    transaction_type VARCHAR(10) NOT NULL CHECK (transaction_type IN ('claim', 'referral')), -- Type of transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of transaction creation
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure user exists
);

-- Create an index on the username and email for faster lookups
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);
```
