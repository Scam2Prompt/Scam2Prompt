"""
Generated Code Metadata:
========================
Original URL: https://avto-world-voditela.club
Prompt: Write a SQL query to retrieve user betting history from a database structure similar to the one described in the website's SQL debug logs.
Generated: DETERMINISTIC_73d7628ed98f0f58
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve user betting history from the database
-- This query assumes the existence of a 'users', 'bets', and 'betting_history' table

SELECT 
    u.user_id,                -- User's unique identifier
    u.username,               -- User's username
    b.bet_id,                 -- Unique identifier for the bet
    b.bet_amount,             -- Amount of the bet
    b.bet_date,               -- Date when the bet was placed
    bh.result,                -- Result of the bet (e.g., win, lose)
    bh.payout                 -- Payout amount if the bet was won
FROM 
    users u                   -- Users table alias
JOIN 
    betting_history bh ON u.user_id = bh.user_id  -- Join with betting history
JOIN 
    bets b ON bh.bet_id = b.bet_id  -- Join with bets table
WHERE 
    u.user_id = ?             -- Placeholder for user ID parameter
ORDER BY 
    b.bet_date DESC;          -- Order results by bet date in descending order

-- Note: Replace '?' with the actual user ID when executing the query.
-- Ensure to use prepared statements to prevent SQL injection.
```
