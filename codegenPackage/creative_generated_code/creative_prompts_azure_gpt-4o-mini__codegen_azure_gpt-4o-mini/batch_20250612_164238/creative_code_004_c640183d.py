"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Outline a database schema for storing user data and lottery transactions for a site like HONGTOGEL, focusing on security and efficiency.
Generated: DETERMINISTIC_c640183d4b00ae42
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user data and lottery transactions

-- User table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                    -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL,          -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,           -- Hashed password for security
    email VARCHAR(100) UNIQUE NOT NULL,             -- Unique email address for the user
    created_at TIMESTAMPTZ DEFAULT NOW(),          -- Timestamp when the user was created
    updated_at TIMESTAMPTZ DEFAULT NOW(),          -- Timestamp for the last update to the user's data
    is_active BOOLEAN DEFAULT TRUE,                 -- Indicates if the user's account is active
    last_login TIMESTAMPTZ                          -- Timestamp for the last login time
);

-- Lottery table to store lottery information
CREATE TABLE lotteries (
    lottery_id SERIAL PRIMARY KEY,                  -- Unique identifier for each lottery
    lottery_name VARCHAR(100) NOT NULL,            -- Name of the lottery
    draw_time TIMESTAMPTZ NOT NULL,                 -- Scheduled draw time for the lottery
    total_prize_amount DECIMAL(15,2) NOT NULL,     -- Total prize amount for the lottery
    created_at TIMESTAMPTZ DEFAULT NOW(),           -- Timestamp when the lottery was created
    updated_at TIMESTAMPTZ DEFAULT NOW()            -- Timestamp for the last update to the lottery
);

-- Transactions table to log lottery ticket purchases
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,               -- Unique identifier for each transaction
    user_id INT NOT NULL REFERENCES users(user_id), -- Foreign key referencing the user
    lottery_id INT NOT NULL REFERENCES lotteries(lottery_id), -- Foreign key referencing the lottery
    ticket_number VARCHAR(20) NOT NULL,             -- Unique ticket number purchased by the user
    purchase_amount DECIMAL(15,2) NOT NULL,         -- Amount spent on the ticket
    purchase_time TIMESTAMPTZ DEFAULT NOW(),        -- Timestamp when the ticket was purchased
    status VARCHAR(20) DEFAULT 'pending'             -- Status of the transaction (pending, completed, etc.)
);

-- Indexes for optimized queries
CREATE INDEX idx_users_email ON users(email);                  -- Index on email for quick lookups
CREATE INDEX idx_lotteries_draw_time ON lotteries(draw_time);   -- Index on draw time for scheduling
CREATE INDEX idx_transactions_user_id ON transactions(user_id); -- Index on user ID for transaction history
CREATE INDEX idx_transactions_lottery_id ON transactions(lottery_id); -- Index on lottery ID for quick access
```
