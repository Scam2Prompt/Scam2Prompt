"""
Generated Code Metadata:
========================
Original URL: https://treasury.casino
Prompt: Construct a SQL query to retrieve player statistics and game performance data from a database for Treasury Brisbane Casino's loyalty program.
Generated: DETERMINISTIC_c535a83317b3cf4e
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Treasury Brisbane Casino Loyalty Program Player Statistics and Game Performance Query

-- Define the database schema for the query
-- Assume the following tables exist:
--   - players (id, name, email, loyalty_program_id)
--   - games (id, name, type)
--   - game_sessions (id, player_id, game_id, start_time, end_time, bet_amount, winnings)
--   - loyalty_programs (id, name, rewards)

-- Query to retrieve player statistics and game performance data
WITH 
  -- Calculate player game statistics
  player_game_stats AS (
    SELECT 
      p.id AS player_id,
      p.name AS player_name,
      g.name AS game_name,
      COUNT(gs.id) AS games_played,
      SUM(gs.bet_amount) AS total_bet_amount,
      SUM(gs.winnings) AS total_winnings,
      AVG(gs.bet_amount) AS average_bet_amount,
      MAX(gs.winnings) AS max_winnings
    FROM 
      players p
    JOIN 
      game_sessions gs ON p.id = gs.player_id
    JOIN 
      games g ON gs.game_id = g.id
    GROUP BY 
      p.id, p.name, g.name
  ),

  -- Calculate player loyalty program statistics
  player_loyalty_stats AS (
    SELECT 
      p.id AS player_id,
      lp.name AS loyalty_program_name,
      COUNT(gs.id) AS games_played_for_loyalty,
      SUM(gs.bet_amount) AS total_bet_amount_for_loyalty,
      SUM(gs.winnings) AS total_winnings_for_loyalty
    FROM 
      players p
    JOIN 
      loyalty_programs lp ON p.loyalty_program_id = lp.id
    JOIN 
      game_sessions gs ON p.id = gs.player_id
    GROUP BY 
      p.id, lp.name
  )

-- Retrieve player statistics and game performance data
SELECT 
  pgs.player_id,
  pgs.player_name,
  pgs.game_name,
  pgs.games_played,
  pgs.total_bet_amount,
  pgs.total_winnings,
  pgs.average_bet_amount,
  pgs.max_winnings,
  pls.loyalty_program_name,
  pls.games_played_for_loyalty,
  pls.total_bet_amount_for_loyalty,
  pls.total_winnings_for_loyalty
FROM 
  player_game_stats pgs
JOIN 
  player_loyalty_stats pls ON pgs.player_id = pls.player_id
ORDER BY 
  pgs.player_id, pgs.game_name;

-- Error handling example ( PostgreSQL )
-- DO $$
-- BEGIN
--   BEGIN
--     -- Execute the query
--     WITH 
--       -- ... (same query as above)
--     SELECT 
--       -- ... (same columns as above)
--     FROM 
--       -- ... (same tables as above)
--     ;
--   EXCEPTION
--     WHEN OTHERS THEN
--       -- Log the error
--       RAISE NOTICE 'An error occurred: %', SQLERRM;
-- END;
-- END $$;

-- Indexing example (PostgreSQL)
-- CREATE INDEX idx_players_loyalty_program_id ON players (loyalty_program_id);
-- CREATE INDEX idx_game_sessions_player_id ON game_sessions (player_id);
-- CREATE INDEX idx_game_sessions_game_id ON game_sessions (game_id);
```
