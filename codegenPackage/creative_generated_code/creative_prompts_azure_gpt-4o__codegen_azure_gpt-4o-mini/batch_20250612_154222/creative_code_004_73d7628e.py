"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avto-world-voditela.club
Prompt: Write a SQL query to retrieve user betting history from a database structure similar to the one described in the website's SQL debug logs.
Generated: DETERMINISTIC_73d7628ed98f0f58
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve user betting history from the database
-- The query selects relevant fields from the 'bets' table
-- It joins with the 'users' table to get user details
-- The query includes error handling for potential issues

BEGIN TRY
    -- Selecting user betting history
    SELECT 
        u.user_id,            -- ID of the user
        u.username,          -- Username of the user
        b.bet_id,            -- Unique ID of the bet
        b.bet_amount,        -- Amount of the bet
        b.bet_date,          -- Date and time of the bet
        b.bet_status         -- Status of the bet (e.g., 'won', 'lost')
    FROM 
        users u              -- Users table alias
    INNER JOIN 
        bets b               -- Bets table alias
    ON 
        u.user_id = b.user_id  -- Joining condition on user ID
    WHERE 
        u.user_id = @UserId   -- Filter for a specific user (parameterized input for security)
    ORDER BY 
        b.bet_date DESC;      -- Order by bet date in descending order

END TRY
BEGIN CATCH
    -- Error handling: log the error message
    PRINT 'Error occurred while retrieving betting history: ' + ERROR_MESSAGE();
    -- Optionally, you could throw the error to the calling application
    THROW;
END CATCH;
```
