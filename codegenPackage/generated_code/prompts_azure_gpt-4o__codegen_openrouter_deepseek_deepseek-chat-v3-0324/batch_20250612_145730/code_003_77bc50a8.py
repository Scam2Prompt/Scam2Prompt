"""
Generated Code Metadata:
========================
Original URL: https://pansos4dz.com
Prompt: Create a database schema in SQL to store and manage user transactions, including deposits via bank transfers, e-wallets, and pulsa, as outlined on PANSOS4D.
Generated: DETERMINISTIC_77bc50a89e619789
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for PANSOS4D transaction management system

-- Users table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20) UNIQUE,
    full_name VARCHAR(100),
    date_of_birth DATE,
    address TEXT,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    account_status VARCHAR(20) DEFAULT 'active' CHECK (account_status IN ('active', 'suspended', 'banned')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);

-- Bank accounts table for bank transfer deposits
CREATE TABLE user_bank_accounts (
    bank_account_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    bank_name VARCHAR(100) NOT NULL,
    account_number VARCHAR(50) NOT NULL,
    account_holder_name VARCHAR(100) NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, bank_name, account_number)
);

-- E-wallets table for e-wallet deposits
CREATE TABLE user_ewallets (
    ewallet_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    ewallet_type VARCHAR(50) NOT NULL CHECK (ewallet_type IN ('OVO', 'DANA', 'GOPAY', 'LinkAja', 'ShopeePay')),
    phone_number VARCHAR(20) NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, ewallet_type, phone_number)
);

-- Transaction types
CREATE TABLE transaction_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Predefined transaction types
INSERT INTO transaction_types (type_name, description) VALUES 
    ('deposit_bank', 'Deposit via bank transfer'),
    ('deposit_ewallet', 'Deposit via e-wallet'),
    ('deposit_pulsa', 'Deposit via pulsa'),
    ('withdrawal', 'Withdrawal request'),
    ('bet', 'Bet placed'),
    ('win', 'Bet win'),
    ('bonus', 'Bonus credit');

-- Transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    type_id INTEGER REFERENCES transaction_types(type_id),
    amount DECIMAL(15, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'cancelled')),
    reference_id VARCHAR(100),
    description TEXT,
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE
);

-- Bank transfer deposits table
CREATE TABLE bank_transfer_deposits (
    deposit_id SERIAL PRIMARY KEY,
    transaction_id INTEGER REFERENCES transactions(transaction_id) ON DELETE CASCADE,
    bank_account_id INTEGER REFERENCES user_bank_accounts(bank_account_id) ON DELETE SET NULL,
    sender_bank_name VARCHAR(100),
    sender_account_number VARCHAR(50),
    sender_account_name VARCHAR(100),
    proof_image_url VARCHAR(255),
    admin_notes TEXT
);

-- E-wallet deposits table
CREATE TABLE ewallet_deposits (
    deposit_id SERIAL PRIMARY KEY,
    transaction_id INTEGER REFERENCES transactions(transaction_id) ON DELETE CASCADE,
    ewallet_id INTEGER REFERENCES user_ewallets(ewallet_id) ON DELETE SET NULL,
    payment_reference VARCHAR(100),
    admin_notes TEXT
);

-- Pulsa deposits table
CREATE TABLE pulsa_deposits (
    deposit_id SERIAL PRIMARY KEY,
    transaction_id INTEGER REFERENCES transactions(transaction_id) ON DELETE CASCADE,
    phone_number VARCHAR(20) NOT NULL,
    operator VARCHAR(50) NOT NULL CHECK (operator IN ('Telkomsel', 'XL', 'Indosat', 'Tri', 'Smartfren', 'Axis')),
    voucher_code VARCHAR(50),
    admin_notes TEXT
);

-- Transaction history view
CREATE VIEW transaction_history AS
SELECT 
    t.transaction_id,
    u.user_id,
    u.username,
    tt.type_name AS transaction_type,
    t.amount,
    t.status,
    t.reference_id,
    t.description,
    t.created_at,
    t.completed_at
FROM 
    transactions t
JOIN 
    users u ON t.user_id = u.user_id
JOIN 
    transaction_types tt ON t.type_id = tt.type_id;

-- Balance audit log
CREATE TABLE balance_audit_log (
    log_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    transaction_id INTEGER REFERENCES transactions(transaction_id) ON DELETE SET NULL,
    previous_balance DECIMAL(15, 2) NOT NULL,
    new_balance DECIMAL(15, 2) NOT NULL,
    change_amount DECIMAL(15, 2) NOT NULL,
    change_type VARCHAR(20) NOT NULL CHECK (change_type IN ('deposit', 'withdrawal', 'bet', 'win', 'bonus', 'adjustment')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Function to update balance and log changes
CREATE OR REPLACE FUNCTION update_user_balance()
RETURNS TRIGGER AS $$
BEGIN
    -- Only process completed transactions
    IF NEW.status = 'completed' AND (OLD.status IS NULL OR OLD.status != 'completed') THEN
        -- Update user balance
        UPDATE users 
        SET balance = balance + NEW.amount 
        WHERE user_id = NEW.user_id;
        
        -- Log balance change
        INSERT INTO balance_audit_log (
            user_id, 
            transaction_id, 
            previous_balance, 
            new_balance, 
            change_amount, 
            change_type,
            notes
        )
        SELECT 
            NEW.user_id,
            NEW.transaction_id,
            u.balance - NEW.amount,
            u.balance,
            NEW.amount,
            CASE 
                WHEN tt.type_name LIKE 'deposit%' THEN 'deposit'
                WHEN tt.type_name = 'withdrawal' THEN 'withdrawal'
                WHEN tt.type_name = 'bet' THEN 'bet'
                WHEN tt.type_name = 'win' THEN 'win'
                WHEN tt.type_name = 'bonus' THEN 'bonus'
                ELSE 'adjustment'
            END,
            NEW.description
        FROM 
            users u
        JOIN 
            transaction_types tt ON NEW.type_id = tt.type_id
        WHERE 
            u.user_id = NEW.user_id;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to update balance when transaction is completed
CREATE TRIGGER transaction_completed_trigger
AFTER UPDATE ON transactions
FOR EACH ROW
EXECUTE FUNCTION update_user_balance();

-- Indexes for performance
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_transactions_created_at ON transactions(created_at);
CREATE INDEX idx_bank_transfer_deposits_transaction_id ON bank_transfer_deposits(transaction_id);
CREATE INDEX idx_ewallet_deposits_transaction_id ON ewallet_deposits(transaction_id);
CREATE INDEX idx_pulsa_deposits_transaction_id ON pulsa_deposits(transaction_id);
```
