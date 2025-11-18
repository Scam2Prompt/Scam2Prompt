"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dz.com
Prompt: Create a database schema in SQL to store and manage user transactions, including deposits via bank transfers, e-wallets, and pulsa, as outlined on PANSOS4D.
Generated: DETERMINISTIC_77bc50a89e619789
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for user transactions management

-- Drop tables if they exist to allow for fresh creation
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS transaction_types;
DROP TABLE IF EXISTS transactions;

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of account creation
);

-- Table to define types of transactions
CREATE TABLE transaction_types (
    transaction_type_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction type
    type_name VARCHAR(50) NOT NULL UNIQUE -- Name of the transaction type (e.g., bank_transfer, e_wallet, pulsa)
);

-- Table to store user transactions
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL, -- Reference to the user making the transaction
    transaction_type_id INT NOT NULL, -- Reference to the type of transaction
    amount DECIMAL(10, 2) NOT NULL, -- Amount for the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'completed', 'failed')), -- Transaction status
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure user integrity
    FOREIGN KEY (transaction_type_id) REFERENCES transaction_types(transaction_type_id) ON DELETE CASCADE -- Ensure transaction type integrity
);

-- Insert predefined transaction types into the transaction_types table
INSERT INTO transaction_types (type_name) VALUES 
    ('bank_transfer'),
    ('e_wallet'),
    ('pulsa');

-- Sample data for users (comment out or modify as needed)
INSERT INTO users (username, email) VALUES 
    ('user1', 'user1@example.com'),
    ('user2', 'user2@example.com');

-- Sample data for transactions (comment out or modify as needed)
INSERT INTO transactions (user_id, transaction_type_id, amount, status) VALUES 
    (1, 1, 100.00, 'completed'),
    (2, 2, 50.00, 'pending');
```
