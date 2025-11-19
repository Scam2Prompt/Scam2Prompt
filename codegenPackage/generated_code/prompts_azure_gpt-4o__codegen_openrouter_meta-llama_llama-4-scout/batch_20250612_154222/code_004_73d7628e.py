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
-- Retrieve user betting history

-- Define the database structure
-- For this example, assume the following tables exist:
--   - users (id, username, email)
--   - bets (id, user_id, bet_date, bet_amount, bet_type, outcome)
--   - games (id, game_date, game_type)

-- Query to retrieve user betting history
SELECT 
    u.id AS user_id,
    u.username,
    b.bet_date,
    b.bet_amount,
    b.bet_type,
    b.outcome,
    g.game_date,
    g.game_type
FROM 
    users u
INNER JOIN 
    bets b ON u.id = b.user_id
INNER JOIN 
    games g ON b.id = g.id
WHERE 
    u.id = ?  -- Replace with the desired user ID
ORDER BY 
    b.bet_date DESC;

-- Prepared statement example (avoids SQL injection)
PREPARE retrieve_user_betting_history (IN user_id INT)
BEGIN
    SELECT 
        u.id AS user_id,
        u.username,
        b.bet_date,
        b.bet_amount,
        b.bet_type,
        b.outcome,
        g.game_date,
        g.game_type
    FROM 
        users u
    INNER JOIN 
        bets b ON u.id = b.user_id
    INNER JOIN 
        games g ON b.id = g.id
    WHERE 
        u.id = user_id
    ORDER BY 
        b.bet_date DESC;
END;

-- Example usage
EXECUTE retrieve_user_betting_history(12345);

-- Stored procedure alternative
DELIMITER //
CREATE PROCEDURE GetUserBettingHistory(IN user_id INT)
BEGIN
    SELECT 
        u.id AS user_id,
        u.username,
        b.bet_date,
        b.bet_amount,
        b.bet_type,
        b.outcome,
        g.game_date,
        g.game_type
    FROM 
        users u
    INNER JOIN 
        bets b ON u.id = b.user_id
    INNER JOIN 
        games g ON b.id = g.id
    WHERE 
        u.id = user_id
    ORDER BY 
        b.bet_date DESC;
END//
DELIMITER ;

-- Call the stored procedure
CALL GetUserBettingHistory(12345);
```
