"""
Generated Code Metadata:
========================
Original URL: https://globaljournalpress.com
Prompt: Write a SQL query that retrieves data on the latest trends in online slots, based on user preferences and gameplay statistics.
Generated: DETERMINISTIC_0d12c4d07a748f7f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve latest trends in online slots based on user preferences and gameplay statistics

-- Define the query
WITH 
  -- Calculate user preference scores for each slot game
  user_preferences AS (
    SELECT 
      u.user_id,
      s.slot_id,
      COUNT(CASE WHEN u.preferred_genre = s.genre THEN 1 END) AS genre_match,
      COUNT(CASE WHEN u.preferred_theme = s.theme THEN 1 END) AS theme_match
    FROM 
      users u
    CROSS JOIN 
      slot_games s
    GROUP BY 
      u.user_id, s.slot_id
  ),

  -- Calculate gameplay statistics for each slot game
  gameplay_stats AS (
    SELECT 
      g.slot_id,
      COUNT(g.game_id) AS total_games,
      SUM(g.winnings) AS total_winnings,
      AVG(g RTP) AS avg_RTP
    FROM 
      gameplay g
    GROUP BY 
      g.slot_id
  ),

  -- Combine user preferences and gameplay statistics
  combined_data AS (
    SELECT 
      up.user_id,
      up.slot_id,
      up.genre_match,
      up.theme_match,
      gs.total_games,
      gs.total_winnings,
      gs.avg_RTP,
      -- Calculate a score based on user preferences and gameplay statistics
      (up.genre_match + up.theme_match) * gs.total_games * gs.avg_RTP AS score
    FROM 
      user_preferences up
    JOIN 
      gameplay_stats gs ON up.slot_id = gs.slot_id
  )

-- Retrieve the top 10 trending slot games for each user
SELECT 
  cd.user_id,
  cd.slot_id,
  s.game_name,
  s.genre,
  s.theme,
  cd.total_games,
  cd.total_winnings,
  cd.avg_RTP,
  cd.score
FROM 
  combined_data cd
JOIN 
  slot_games s ON cd.slot_id = s.slot_id
ORDER BY 
  cd.user_id, cd.score DESC;

-- Create indexes for better performance
CREATE INDEX idx_users_preferred_genre ON users (preferred_genre);
CREATE INDEX idx_users_preferred_theme ON users (preferred_theme);
CREATE INDEX idx_slot_games_genre ON slot_games (genre);
CREATE INDEX idx_slot_games_theme ON slot_games (theme);
CREATE INDEX idx_gameplay_slot_id ON gameplay (slot_id);

-- Example use case:
-- Suppose we have the following tables:
-- users (user_id, preferred_genre, preferred_theme)
-- slot_games (slot_id, game_name, genre, theme)
-- gameplay (game_id, slot_id, user_id, winnings, RTP)

-- Insert sample data:
-- INSERT INTO users (user_id, preferred_genre, preferred_theme) VALUES (1, 'action', 'adventure');
-- INSERT INTO slot_games (slot_id, game_name, genre, theme) VALUES (1, 'Game 1', 'action', 'adventure');
-- INSERT INTO gameplay (game_id, slot_id, user_id, winnings, RTP) VALUES (1, 1, 1, 100, 0.95);

-- Run the query to retrieve the latest trends in online slots.
```
