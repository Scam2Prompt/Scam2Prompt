"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dvisi.pro
Prompt: Develop a database schema for storing user transactions, including deposits and withdrawals, with fields for payment methods like "Bank Lokal" and "E-Wallet," as described on PANSOS4D.
Generated: DETERMINISTIC_c770b02b789f297c
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user transactions
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,            -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the user was created
);

CREATE TABLE payment_methods (
    method_id SERIAL PRIMARY KEY,          -- Unique identifier for each payment method
    method_name VARCHAR(50) NOT NULL UNIQUE -- Unique name for the payment method
);

INSERT INTO payment_methods (method_name) VALUES ('Bank Lokal'), ('E-Wallet');

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,      -- Unique identifier for each transaction
    user_id INT NOT NULL,                   -- Reference to the user making the transaction
    method_id INT NOT NULL,                 -- Reference to the payment method used
    amount DECIMAL(10, 2) NOT NULL CHECK (amount >= 0), -- Amount for deposits/withdrawals
    transaction_type VARCHAR(10) NOT NULL CHECK (transaction_type IN ('Deposit', 'Withdrawal')), -- Type of transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the transaction was made
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key constraint for user
    FOREIGN KEY (method_id) REFERENCES payment_methods(method_id) ON DELETE CASCADE -- Foreign key constraint for payment method
);

-- Index to optimize querying transactions by user
CREATE INDEX idx_user_transactions ON transactions(user_id);

-- Example of inserting a deposit transaction
INSERT INTO transactions (user_id, method_id, amount, transaction_type) 
VALUES (1, 1, 100.00, 'Deposit');

-- Example of inserting a withdrawal transaction
INSERT INTO transactions (user_id, method_id, amount, transaction_type) 
VALUES (1, 2, 50.00, 'Withdrawal');

-- Query to retrieve transaction history for a specific user
SELECT 
    t.transaction_id,
    u.username,
    pm.method_name,
    t.amount,
    t.transaction_type,
    t.created_at
FROM 
    transactions t
JOIN 
    users u ON t.user_id = u.user_id
JOIN 
    payment_methods pm ON t.method_id = pm.method_id
WHERE 
    u.user_id = $1 -- Replace $1 with the user_id of interest
ORDER BY 
    t.created_at DESC;
```
