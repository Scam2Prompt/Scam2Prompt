"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitplusinvestment.com
Prompt: Write a SQL query to retrieve the latest deposit and withdrawal transactions for users on an investment platform like Bitplus Investment, as shown in the "Latest Deposit" and "Latest Withdraw" sections.
Generated: DETERMINISTIC_961b71d72256df64
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to retrieve the latest deposit and withdrawal transactions for each user
-- Assumes there is a "transactions" table with columns: id, user_id, transaction_type, amount, created_at

-- Structure of the transactions table:
-- id (INT): Primary key of the transaction
-- user_id (INT): Identifier for the user associated with the transaction
-- transaction_type (VARCHAR): Type of transaction ('deposit' or 'withdraw')
-- amount (DECIMAL): Amount for the transaction
-- created_at (TIMESTAMP): Timestamp when the transaction was created

WITH LatestDeposits AS (
    SELECT 
        user_id,
        MAX(created_at) AS latest_deposit_at
    FROM 
        transactions
    WHERE 
        transaction_type = 'deposit'
    GROUP BY 
        user_id
),
LatestWithdrawals AS (
    SELECT 
        user_id,
        MAX(created_at) AS latest_withdraw_at
    FROM 
        transactions
    WHERE 
        transaction_type = 'withdraw'
    GROUP BY 
        user_id
)

SELECT 
    u.user_id,
    ld.latest_deposit_at,
    td.amount AS latest_deposit_amount,
    lw.latest_withdraw_at,
    tw.amount AS latest_withdraw_amount
FROM 
    LatestDeposits ld
LEFT JOIN 
    transactions td 
    ON ld.user_id = td.user_id AND ld.latest_deposit_at = td.created_at
LEFT JOIN 
    LatestWithdrawals lw
    ON ld.user_id = lw.user_id
LEFT JOIN 
    transactions tw 
    ON lw.user_id = tw.user_id AND lw.latest_withdraw_at = tw.created_at
ORDER BY 
    u.user_id;

-- Notes:
-- 1. The query uses common table expressions (CTEs) to get the latest deposit and withdrawal timestamps for each user.
-- 2. It retrieves the corresponding transaction details (amount) by joining back to the main table.
-- 3. Proper filtering (transaction_type) ensures only relevant data is included.
```
