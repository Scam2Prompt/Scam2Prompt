"""
Generated Code Metadata:
========================
Original URL: https://scapesmania-tokenn.pages.dev
Prompt: Design a database schema in MySQL for storing user entries, referral data, and wallet connection details for the ScapesMania giveaway system.
Generated: DETERMINISTIC_ca3049f76184644a
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ScapesMania giveaway system

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS referrals;
DROP TABLE IF EXISTS wallet_connections;

-- Table to store user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store referral data
CREATE TABLE referrals (
    referral_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each referral
    referrer_id INT NOT NULL,                    -- User ID of the referrer
    referred_email VARCHAR(100) NOT NULL,        -- Email of the referred user
    referral_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of referral
    FOREIGN KEY (referrer_id) REFERENCES users(user_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Table to store wallet connection details
CREATE TABLE wallet_connections (
    wallet_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each wallet connection
    user_id INT NOT NULL,                         -- User ID associated with the wallet
    wallet_address VARCHAR(100) NOT NULL UNIQUE,  -- Unique wallet address
    connection_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of wallet connection
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_referrer ON referrals(referrer_id);
CREATE INDEX idx_user_wallet ON wallet_connections(user_id);
```
