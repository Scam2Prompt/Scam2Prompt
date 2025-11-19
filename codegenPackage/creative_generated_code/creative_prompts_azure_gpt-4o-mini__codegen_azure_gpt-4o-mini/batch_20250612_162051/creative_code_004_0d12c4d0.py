"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globaljournalpress.com
Prompt: Write a SQL query that retrieves data on the latest trends in online slots, based on user preferences and gameplay statistics.
Generated: DETERMINISTIC_0d12c4d07a748f7f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve data on the latest trends in online slots
-- based on user preferences and gameplay statistics.

WITH UserPreferences AS (
    -- This Common Table Expression (CTE) gathers user preferences
    SELECT 
        user_id,
        preferred_game_type,
        preferred_bet_range
    FROM 
        user_preferences
),
GameStatistics AS (
    -- This CTE gathers statistics from the gameplay data
    SELECT 
        game_id,
        AVG(bet_amount) AS average_bet,
        COUNT(*) AS play_count,
        SUM(wins) AS total_wins,
        SUM(losses) AS total_losses
    FROM 
        gameplay_statistics
    GROUP BY 
        game_id
),
TrendyGames AS (
    -- This CTE identifies games that have gained popularity based on play count
    SELECT 
        gs.game_id,
        gs.average_bet,
        gs.play_count,
        gs.total_wins,
        gs.total_losses,
        ROW_NUMBER() OVER (ORDER BY gs.play_count DESC) AS popularity_rank
    FROM 
        GameStatistics gs
)

-- Final selection to retrieve games matching user preferences and that are trending
SELECT 
    tg.game_id,
    tg.average_bet,
    tg.play_count,
    tg.total_wins,
    tg.total_losses,
    up.preferred_game_type,
    up.preferred_bet_range
FROM 
    TrendyGames tg
JOIN 
    UserPreferences up ON (up.preferred_game_type = (SELECT game_type FROM games WHERE game_id = tg.game_id))
WHERE 
    tg.play_count > 100 -- Ensures we're only looking at games with significant engagement
ORDER BY 
    tg.popularity_rank
LIMIT 10; -- Limits the results to the top 10 trending games
```
