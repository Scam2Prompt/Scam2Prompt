"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzocash.com
Prompt: Create a database schema for tracking user investments, referrals, and transaction history, similar to the functionality described on Renzo Cash's platform.
Generated: DETERMINISTIC_2e573852beecde73
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking user investments, referrals, and transaction history

-- Create a table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store investment information
CREATE TABLE investments (
    investment_id SERIAL PRIMARY KEY, -- Unique identifier for each investment
    user_id INT NOT NULL, -- Foreign key referencing the user making the investment
    amount DECIMAL(10, 2) NOT NULL, -- Investment amount
    investment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the investment
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store referral information
CREATE TABLE referrals (
    referral_id SERIAL PRIMARY KEY, -- Unique identifier for each referral
    referrer_id INT NOT NULL, -- Foreign key referencing the user who made the referral
    referred_id INT NOT NULL, -- Foreign key referencing the user who was referred
    referral_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the referral
    FOREIGN KEY (referrer_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (referred_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store transaction history
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL, -- Foreign key referencing the user making the transaction
    transaction_type VARCHAR(50) NOT NULL, -- Type of the transaction (e.g., deposit, withdrawal, investment)
    amount DECIMAL(10, 2) NOT NULL, -- Transaction amount
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create indexes for faster lookups
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_investment_user ON investments(user_id);
CREATE INDEX idx_referral_user ON referrals(referrer_id);
CREATE INDEX idx_transaction_user ON transactions(user_id);

-- Add a sample user for testing
INSERT INTO users (username, email, password_hash) VALUES
('sampleuser', 'sample@example.com', 'hashed_password_here');

-- Note: Passwords should be hashed before inserting into the database.
-- Use a strong hashing algorithm like bcrypt for secure password storage.
```
