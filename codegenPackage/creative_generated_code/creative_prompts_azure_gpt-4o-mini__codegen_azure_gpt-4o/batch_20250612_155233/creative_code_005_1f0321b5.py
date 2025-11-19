"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travelobay.com
Prompt: Write a SQL query to retrieve user transaction history from a database for an online casino, ensuring it aligns with the features offered by R7 Casino.
Generated: DETERMINISTIC_1f0321b591be8a38
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Query to retrieve user transaction history for an online casino
-- This assumes proper database design with tables for users and transactions

-- Using Common Table Expressions (CTE) for clarity
WITH UserTransactionHistory AS (
    SELECT 
        t.transaction_id,         -- Unique ID of the transaction
        t.user_id,                -- The ID of the user associated with the transaction
        u.username AS user_name,  -- The username of the user
        t.transaction_type,       -- Type of transaction (e.g., 'Deposit', 'Withdrawal', 'Bet')
        t.amount,                 -- Amount involved in the transaction
        t.transaction_date,       -- Date and time of the transaction
        t.status                  -- Status of the transaction (e.g., 'Completed', 'Pending', 'Failed')
    FROM 
        transactions AS t         -- Transactions table
    JOIN 
        users AS u                -- Users table
    ON 
        t.user_id = u.user_id     -- Match transactions to users
    WHERE 
        t.status = 'Completed'    -- Only retrieve completed transactions
        AND t.transaction_date >= DATEADD(DAY, -30, GETDATE()) -- Include only transactions from the last 30 days
)
SELECT 
    *
FROM 
    UserTransactionHistory
ORDER BY 
    transaction_date DESC;        -- Order transactions by most recent first

-- Notes:
-- - Replace `transactions` and `users` with actual table names if different.
-- - Ensure date handling aligns with your SQL dialect (e.g., `GETDATE()` for SQL Server).
-- - Add additional WHERE clauses to filter by user_id or other criteria as needed.
-- - Implement necessary indexing on `transaction_date` and `user_id` fields for performance.
```
