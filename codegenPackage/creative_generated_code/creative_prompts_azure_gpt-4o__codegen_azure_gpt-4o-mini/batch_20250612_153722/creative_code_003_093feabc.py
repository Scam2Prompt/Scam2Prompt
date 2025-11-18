"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dbm.pro
Prompt: Suggest a database schema design for managing user transactions, including deposits and withdrawals, as described on the PANSOS4D website.
Generated: DETERMINISTIC_093feabc92678e37
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing User Transactions (Deposits and Withdrawals)

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,            -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,     -- Unique email for each user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store transaction types (Deposit or Withdrawal)
CREATE TABLE transaction_types (
    transaction_type_id SERIAL PRIMARY KEY,  -- Unique identifier for each transaction type
    type_name VARCHAR(20) NOT NULL UNIQUE     -- Name of the transaction type (e.g., 'Deposit', 'Withdrawal')
);

-- Table to store user transactions
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,                -- Unique identifier for each transaction
    user_id INT NOT NULL REFERENCES users(user_id),   -- Foreign key referencing the user
    transaction_type_id INT NOT NULL REFERENCES transaction_types(transaction_type_id),  -- Foreign key referencing transaction type
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount of the transaction (must be positive)
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    status VARCHAR(20) DEFAULT 'Pending',  -- Status of the transaction (e.g., 'Pending', 'Completed', 'Failed')
    CONSTRAINT chk_status CHECK (status IN ('Pending', 'Completed', 'Failed')) -- Status must be one of the predefined values
);

-- Index for faster access to transactions by user
CREATE INDEX idx_user_transactions ON transactions(user_id);

-- Index for faster access to transactions by type
CREATE INDEX idx_transaction_type ON transactions(transaction_type_id);

-- Seed initial transaction types
INSERT INTO transaction_types (type_name) VALUES
('Deposit'),
('Withdrawal');
```
