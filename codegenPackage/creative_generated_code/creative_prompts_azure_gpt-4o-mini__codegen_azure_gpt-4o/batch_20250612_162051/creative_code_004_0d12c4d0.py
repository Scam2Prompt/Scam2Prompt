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
-- SQL Query to retrieve data on the latest trends in online slots
-- based on user preferences and gameplay statistics.

-- Assumptions:
-- 1. There is a table `user_preferences` that contains user preferences for slot games.
--    Columns: `user_id`, `slot_id`, `preference_score` (higher is better)
-- 2. There is a table `gameplay_statistics` that tracks gameplay data for slots.
--    Columns: `slot_id`, `total_plays`, `average_duration`, `last_played`
-- 3. There is a table `slots` that contains slot game details.
--    Columns: `slot_id`, `slot_name`, `category`

-- Purpose:
-- The query aims to find the top trending slots based on:
-- - High user preference scores
-- - High number of plays
-- - Recent activity (last played date)

-- Error handling is assumed to be handled at the application level using this query.

WITH RankedSlots AS (
    -- Step 1: Rank slots based on user preference scores and gameplay statistics
    SELECT 
        s.slot_id,
        s.slot_name,
        s.category,
        COALESCE(SUM(up.preference_score), 0) AS total_preference_score,
        COALESCE(gs.total_plays, 0) AS total_plays,
        COALESCE(gs.average_duration, 0) AS average_play_duration,
        COALESCE(gs.last_played, '1900-01-01') AS last_played
    FROM 
        slots s
    LEFT JOIN 
        user_preferences up 
        ON s.slot_id = up.slot_id
    LEFT JOIN 
        gameplay_statistics gs 
        ON s.slot_id = gs.slot_id
    GROUP BY 
        s.slot_id, s.slot_name, s.category, gs.total_plays, gs.average_duration, gs.last_played
),
TrendingSlots AS (
    -- Step 2: Calculate a "trend score" for each slot 
    -- Trend Score = Weighted combination of preference scores, total plays, and recency
    SELECT 
        slot_id,
        slot_name,
        category,
        total_preference_score,
        total_plays,
        average_play_duration,
        last_played,
        -- Example weighted trend score calculation:
        (total_preference_score * 0.4 + total_plays * 0.4 + 
         CASE 
             WHEN last_played >= CURRENT_DATE - INTERVAL '7 DAYS' THEN 10 -- Boost for recent activity
             ELSE 0 
         END) AS trend_score
    FROM 
        RankedSlots
)
-- Step 3: Retrieve the top trending slots sorted by trend scores
SELECT 
    slot_id,
    slot_name,
    category,
    total_preference_score,
    total_plays,
    average_play_duration,
    last_played,
    trend_score
FROM 
    TrendingSlots
WHERE 
    trend_score > 0 -- Filter for slots with measurable activity
ORDER BY 
    trend_score DESC -- Sort by highest trend score
LIMIT 10; -- Retrieve top 10 trending slots
```
