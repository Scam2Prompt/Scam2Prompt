"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elpicadito.com
Prompt: Construct a SQL query to extract data on recent football matches from the El Picadito database, focusing on match results and team standings.
Generated: DETERMINISTIC_20eda8a558d498f8
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- This SQL query extracts recent football match results and team standings 
-- from the El Picadito database. It assumes that there are tables named 
-- 'matches', 'teams', and 'standings' with relevant columns.

SELECT 
    m.match_id,                     -- Unique identifier for the match
    m.date,                         -- Date of the match
    t1.team_name AS home_team,     -- Name of the home team
    t2.team_name AS away_team,     -- Name of the away team
    m.home_score,                   -- Score of the home team
    m.away_score,                   -- Score of the away team
    s.home_standing AS home_standing,  -- Standing of the home team
    s.away_standing AS away_standing   -- Standing of the away team
FROM 
    matches m
JOIN 
    teams t1 ON m.home_team_id = t1.team_id  -- Join for home team details
JOIN 
    teams t2 ON m.away_team_id = t2.team_id  -- Join for away team details
JOIN 
    standings s ON t1.team_id = s.team_id OR t2.team_id = s.team_id -- Join for team standings
WHERE 
    m.date >= CURRENT_DATE - INTERVAL '30 days'  -- Filter for matches in the last 30 days
ORDER BY 
    m.date DESC;  -- Order results by match date, most recent first
```
