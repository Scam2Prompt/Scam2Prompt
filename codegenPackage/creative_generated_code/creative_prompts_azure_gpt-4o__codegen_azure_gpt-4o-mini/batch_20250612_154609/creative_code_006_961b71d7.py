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

WITH LatestTransactions AS (
    -- Get the latest deposit transactions for each user
    SELECT 
        user_id,
        transaction_type,
        amount,
        transaction_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date DESC) AS rn
    FROM 
        transactions
    WHERE 
        transaction_type = 'deposit'
    
    UNION ALL

    -- Get the latest withdrawal transactions for each user
    SELECT 
        user_id,
        transaction_type,
        amount,
        transaction_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date DESC) AS rn
    FROM 
        transactions
    WHERE 
        transaction_type = 'withdrawal'
)

-- Select the latest deposit and withdrawal transactions for each user
SELECT 
    user_id,
    MAX(CASE WHEN transaction_type = 'deposit' AND rn = 1 THEN amount END) AS latest_deposit,
    MAX(CASE WHEN transaction_type = 'withdrawal' AND rn = 1 THEN amount END) AS latest_withdrawal
FROM 
    LatestTransactions
GROUP BY 
    user_id;

-- Note: Assumes the transactions table has columns: user_id, transaction_type, amount, transaction_date
-- transaction_type must contain values 'deposit' and 'withdrawal'
```
