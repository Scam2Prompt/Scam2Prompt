"""
Generated Code Metadata:
========================
Original URL: https://lidofi.us.com
Prompt: Write a SQL query to analyze user data for WW88's "Sảnh nổ hũ" slot games and calculate the average jackpot payouts.
Generated: DETERMINISTIC_eb13c62f2032c30c
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Calculate average jackpot payouts for WW88's "Sảnh nổ hũ" slot games

-- Define the query
WITH 
  -- Filter and aggregate jackpot payouts
  jackpot_payouts AS (
    SELECT 
      game_id,
      payout_amount,
      payout_date
    FROM 
      ww88_slot_games
    WHERE 
      game_name = 'Sảnh nổ hũ'
      AND payout_amount > 0  -- Ensure only jackpot payouts are considered
  ),

  -- Calculate average jackpot payout
  average_payout AS (
    SELECT 
      AVG(payout_amount) AS avg_jackpot_payout
    FROM 
      jackpot_payouts
  )

-- Select and display the result
SELECT 
  'Average Jackpot Payout' AS metric,
  COALESCE(ROUND(avg_jackpot_payout, 2), 0) AS value
FROM 
  average_payout;

-- Error handling: Check for potential division-by-zero or null values
-- Note: This is implicitly handled by COALESCE and the WHERE clause.

-- Indexing suggestion for optimization:
-- CREATE INDEX idx_ww88_slot_games_game_name_payout_amount ON ww88_slot_games (game_name, payout_amount);
```
