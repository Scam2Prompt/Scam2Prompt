"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezi-trade.com
Prompt: Generate SQL queries to track user transactions and account balances, ensuring compliance with the withdrawal rules mentioned on Ezi-Trade (e.g., funds not used in ongoing trades).
Generated: DETERMINISTIC_d28bdaada599fc1b
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Transactions Table to Track User Transactions
CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    transaction_type VARCHAR(10) NOT NULL, -- 'deposit', 'withdrawal', 'trade'
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Balance Table to Track User Account Balances
CREATE TABLE IF NOT EXISTS AccountBalances (
    user_id INT PRIMARY KEY,
    balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Function to Check Current Balance before Withdrawal
CREATE OR REPLACE FUNCTION check_withdrawal(user_id INT, withdrawal_amount DECIMAL(10, 2))
RETURNS BOOLEAN AS $$
DECLARE
    available_balance DECIMAL(10, 2);
BEGIN
    -- Fetch the current balance for the user
    SELECT balance INTO available_balance FROM AccountBalances WHERE user_id = user_id;

    -- Check if the withdrawal amount exceeds the available balance
    IF available_balance < withdrawal_amount THEN
        RAISE EXCEPTION 'Insufficient balance for withdrawal';
    END IF;

    -- Ensure the withdrawal amount does not exceed funds not used in ongoing trades
    -- Assuming there's a Trades table with an 'amount_invested' column
    DECLARE
        ongoing_trades DECIMAL(10, 2);
    BEGIN
        SELECT SUM(amount_invested) INTO ongoing_trades FROM Trades WHERE user_id = user_id AND status = 'ongoing';

        IF (available_balance - ongoing_trades) < withdrawal_amount THEN
            RAISE EXCEPTION 'Withdrawal exceeds funds available outside of ongoing trades';
        END IF;
    END;

    RETURN TRUE; -- Withdrawal can be processed
END;
$$ LANGUAGE plpgsql;

-- Procedure to Process Withdrawal Transactions
CREATE OR REPLACE PROCEDURE process_withdrawal(user_id INT, withdrawal_amount DECIMAL(10, 2))
LANGUAGE plpgsql AS $$
BEGIN
    -- Check if the withdrawal can be processed
    IF NOT check_withdrawal(user_id, withdrawal_amount) THEN
        RAISE NOTICE 'Withdrawal cannot be processed';
        RETURN;
    END IF;

    -- Update the account balance
    UPDATE AccountBalances SET balance = balance - withdrawal_amount WHERE user_id = user_id;

    -- Log the transaction
    INSERT INTO Transactions (user_id, transaction_type, amount) 
    VALUES (user_id, 'withdrawal', withdrawal_amount);
    
    RAISE NOTICE 'Withdrawal of % processed successfully for user_id %', withdrawal_amount, user_id;
END;
$$;

-- Example query to retrieve user transaction history
SELECT * FROM Transactions WHERE user_id = $1 ORDER BY transaction_date DESC;

-- Example query to get the current balance for a user
SELECT balance FROM AccountBalances WHERE user_id = $1;
```
