"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Construct a SQL query to analyze player data from DominoBet, focusing on win rates and game preferences for different poker variants.
Generated: DETERMINISTIC_b41524b022a6cbdf
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to analyze player data for win rates and game preferences in different poker variants
-- Assumes a table structure similar to the following (adjust table/column names as needed):
-- Table: player_stats
-- Columns:
-- - player_id (INT): Unique identifier for the player
-- - game_variant (VARCHAR): Poker variant (e.g., Texas Hold'em, Omaha, etc.)
-- - total_games (INT): Total games played by the player in the specific variant
-- - games_won (INT): Games won by the player in the specific variant

-- Calculate win rates and game preferences for each player across poker variants
WITH PlayerWinRates AS (
    SELECT 
        player_id,
        game_variant,
        total_games,
        games_won,
        -- Calculate the win rate (percentage of games won)
        CASE 
            WHEN total_games > 0 THEN ROUND((games_won * 100.0 / total_games), 2)
            ELSE 0.0
        END AS win_rate
    FROM 
        player_stats
),
PlayerPreferences AS (
    SELECT 
        player_id,
        game_variant,
        total_games,
        games_won,
        win_rate,
        -- Rank the player's game preferences by the total number of games played
        RANK() OVER (PARTITION BY player_id ORDER BY total_games DESC) AS preference_rank
    FROM 
        PlayerWinRates
)

-- Final output combining win rates and ranked game preferences
SELECT 
    player_id,
    game_variant,
    total_games,
    games_won,
    win_rate,
    preference_rank
FROM 
    PlayerPreferences
ORDER BY 
    player_id, preference_rank;

-- Notes:
-- 1. This query calculates win rates for each player by poker variant.
-- 2. It ranks the player's game preferences by the number of games played.
-- 3. Results are ordered by player ID and their top game preference.
-- 4. Adjust table/column names as needed for your specific database schema.
-- 5. Ensure indexes are in place on columns like player_id and game_variant for performance optimization.
```
