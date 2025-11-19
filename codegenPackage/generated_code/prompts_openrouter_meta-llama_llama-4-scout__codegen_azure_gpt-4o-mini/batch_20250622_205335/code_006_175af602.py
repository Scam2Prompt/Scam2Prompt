"""
Generated Code Metadata:
========================
Original URL: https://boomchange.io
Prompt: "Design a database schema to store exchange pairs, transaction history, and user information for a platform like Boomchange."
Generated: DETERMINISTIC_175af602771d85c5
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a currency exchange platform like Boomchange

-- Create a table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store currency exchange pairs
CREATE TABLE exchange_pairs (
    pair_id SERIAL PRIMARY KEY, -- Unique identifier for each exchange pair
    base_currency VARCHAR(3) NOT NULL, -- Base currency code (e.g., 'USD')
    quote_currency VARCHAR(3) NOT NULL, -- Quote currency code (e.g., 'EUR')
    exchange_rate DECIMAL(18, 6) NOT NULL, -- Current exchange rate
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of pair creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    UNIQUE (base_currency, quote_currency) -- Ensure unique pairs
);

-- Create a table to store transaction history
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL, -- Foreign key referencing the user
    pair_id INT NOT NULL, -- Foreign key referencing the exchange pair
    amount DECIMAL(18, 6) NOT NULL, -- Amount of base currency being exchanged
    exchanged_amount DECIMAL(18, 6) NOT NULL, -- Amount of quote currency received
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'completed', 'failed')), -- Status of the transaction
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Cascade delete for user
    FOREIGN KEY (pair_id) REFERENCES exchange_pairs(pair_id) ON DELETE CASCADE -- Cascade delete for exchange pair
);

-- Create an index on the transactions table for faster querying by user_id
CREATE INDEX idx_user_id ON transactions(user_id);

-- Create an index on the transactions table for faster querying by pair_id
CREATE INDEX idx_pair_id ON transactions(pair_id);
```
