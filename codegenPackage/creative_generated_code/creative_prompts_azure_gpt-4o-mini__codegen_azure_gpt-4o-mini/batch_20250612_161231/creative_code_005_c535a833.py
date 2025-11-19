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
-- SQL query to retrieve player statistics and game performance data
-- for Treasury Brisbane Casino's loyalty program

SELECT
    p.player_id AS PlayerID,
    p.first_name AS FirstName,
    p.last_name AS LastName,
    p.email AS Email,
    p.loyalty_points AS LoyaltyPoints,
    g.game_id AS GameID,
    g.game_name AS GameName,
    gp.total_bets AS TotalBets,
    gp.total_wins AS TotalWins,
    gp.date_played AS DatePlayed
FROM
    players p
JOIN
    game_performance gp ON p.player_id = gp.player_id
JOIN
    games g ON gp.game_id = g.game_id
WHERE
    p.loyalty_member = TRUE -- Only retrieve data for loyalty program members
    AND gp.date_played >= DATEADD(MONTH, -6, GETDATE()) -- Filter for the last 6 months
ORDER BY
    p.last_name, p.first_name, gp.date_played DESC; -- Order by player name and date played

-- Note: Ensure that the necessary indexes exist on the player_id and game_id columns
-- to optimize the query performance.
```
