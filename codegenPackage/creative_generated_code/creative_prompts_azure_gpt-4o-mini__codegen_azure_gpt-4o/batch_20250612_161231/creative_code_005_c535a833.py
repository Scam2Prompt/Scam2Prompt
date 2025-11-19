"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treasury.casino
Prompt: Construct a SQL query to retrieve player statistics and game performance data from a database for Treasury Brisbane Casino's loyalty program.
Generated: DETERMINISTIC_c535a83317b3cf4e
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to retrieve player statistics and game performance data
-- for the Treasury Brisbane Casino's loyalty program

-- This query selects relevant data from the player and game tables
-- assuming there are tables named "Players" and "GamePerformance" in the database.

-- Replace TABLE and COLUMN names with actual names in the database schema.
-- Add JOINs, WHERE clauses, or additional filters based on specific requirements.

SELECT
    p.PlayerID,                -- Unique identifier for the player
    p.PlayerName,              -- Name of the player
    p.Email,                   -- Email address of the player
    p.AccountCreationDate,     -- When the player joined the loyalty program
    p.TotalPointsEarned,       -- Total loyalty points earned by the player
    gp.GameID,                 -- Unique identifier for the game
    gp.GameName,               -- Name of the game played
    gp.DatePlayed,             -- Date when the game was played
    gp.Score,                  -- Score achieved by the player in the game
    gp.CreditsBet,             -- Amount of credits bet by the player
    gp.CreditsWon              -- Amount of credits won by the player
FROM
    Players p                  -- Players table
INNER JOIN
    GamePerformance gp         -- GamePerformance table
ON
    p.PlayerID = gp.PlayerID   -- Join condition: Match player IDs in both tables
WHERE
    p.TotalPointsEarned > 0    -- Filter: Retrieve only players who have earned points
    AND gp.DatePlayed BETWEEN '2023-01-01' AND '2023-12-31' -- Filter: Limit games played within 2023
ORDER BY
    p.TotalPointsEarned DESC,  -- Sort by total points earned (descending)
    gp.DatePlayed DESC;        -- Sort by most recent game played (descending)
```

Make sure to verify the table structure and column names in your database before running the query.
