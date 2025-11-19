"""
Generated Code Metadata:
========================
Original URL: https://travelobay.com
Prompt: Write a SQL query to retrieve user transaction history from a database for an online casino, ensuring it aligns with the features offered by R7 Casino.
Generated: DETERMINISTIC_1f0321b591be8a38
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve user transaction history for an online casino (R7 Casino style)
-- Includes deposits, withdrawals, bets, wins, and bonuses with proper filtering and sorting

SELECT 
    t.transaction_id,
    t.user_id,
    u.username,
    t.transaction_type,
    CASE 
        WHEN t.transaction_type = 'DEPOSIT' THEN 'Deposit'
        WHEN t.transaction_type = 'WITHDRAWAL' THEN 'Withdrawal'
        WHEN t.transaction_type = 'BET' THEN 'Bet'
        WHEN t.transaction_type = 'WIN' THEN 'Win'
        WHEN t.transaction_type = 'BONUS' THEN 'Bonus'
        ELSE 'Other'
    END AS transaction_type_name,
    t.amount,
    t.currency,
    t.transaction_status,
    t.game_id,
    g.game_name,
    t.payment_method,
    t.created_at,
    t.updated_at,
    t.reference_id,
    t.description
FROM 
    transactions t
JOIN 
    users u ON t.user_id = u.user_id
LEFT JOIN 
    games g ON t.game_id = g.game_id
WHERE 
    t.user_id = :user_id  -- Parameterized for security
    AND t.transaction_status = 'COMPLETED'  -- Only show completed transactions
    AND t.created_at BETWEEN :start_date AND :end_date  -- Date range filter
ORDER BY 
    t.created_at DESC  -- Show most recent transactions first
LIMIT 100;  -- Limit results for pagination
```
