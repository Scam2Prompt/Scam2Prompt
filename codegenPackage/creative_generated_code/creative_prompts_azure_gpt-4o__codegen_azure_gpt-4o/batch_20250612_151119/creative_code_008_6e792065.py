"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkbihfbeogaeaobhlefnkodbefgpgknn.com
Prompt: Write a SQL query to store and retrieve user betting history for a platform like UFABET, ensuring transparency and detailed records.
Generated: DETERMINISTIC_6e7920652c47261f
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store user betting history
CREATE TABLE IF NOT EXISTS UserBettingHistory (
    BettingID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each betting entry
    UserID INT NOT NULL,                             -- ID of the user who placed the bet
    GameName VARCHAR(255) NOT NULL,                  -- Name of the game or event the user bet on
    BetAmount DECIMAL(10, 2) NOT NULL,               -- Amount of money the user placed as a bet
    BetType VARCHAR(50) NOT NULL,                    -- Type of bet (e.g., win, lose, handicap, etc.)
    Result ENUM('Win', 'Lose', 'Pending') NOT NULL,  -- Outcome of the bet ('Win', 'Lose', 'Pending')
    Payout DECIMAL(10, 2) DEFAULT 0.00,              -- Amount paid to the user if the bet is won
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the bet was placed
    FOREIGN KEY (UserID) REFERENCES Users(UserID)    -- Ensure UserID references Users table
);

-- Query to insert a new betting record (use parameterized queries in application layer to avoid SQL injection)
INSERT INTO UserBettingHistory (UserID, GameName, BetAmount, BetType, Result, Payout)
VALUES (?, ?, ?, ?, ?, ?);

-- Query to retrieve a user's betting history, ordered by most recent bets
SELECT 
    BettingID,
    GameName,
    BetAmount,
    BetType,
    Result,
    Payout,
    Timestamp
FROM UserBettingHistory
WHERE UserID = ?
ORDER BY Timestamp DESC;

-- Query to retrieve aggregate betting statistics for a user
SELECT
    UserID,
    COUNT(*) AS TotalBets,                           -- Total number of bets placed
    SUM(BetAmount) AS TotalBetAmount,                -- Total amount of money bet
    SUM(CASE WHEN Result = 'Win' THEN Payout ELSE 0 END) AS TotalPayout, -- Total payout for winning bets
    SUM(CASE WHEN Result = 'Win' THEN 1 ELSE 0 END) AS TotalWins,        -- Total number of wins
    SUM(CASE WHEN Result = 'Lose' THEN 1 ELSE 0 END) AS TotalLosses      -- Total number of losses
FROM UserBettingHistory
WHERE UserID = ?
GROUP BY UserID;
```
