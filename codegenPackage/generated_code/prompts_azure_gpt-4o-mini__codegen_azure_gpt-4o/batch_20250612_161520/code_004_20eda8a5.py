"""
Generated Code Metadata:
========================
Original URL: https://elpicadito.com
Prompt: Construct a SQL query to extract data on recent football matches from the El Picadito database, focusing on match results and team standings.
Generated: DETERMINISTIC_20eda8a558d498f8
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to extract recent football match results and team standings from the El Picadito database

-- Ensure the query retrieves relevant data and is optimized for performance
SELECT 
    m.match_id,                -- Unique identifier for the match
    m.match_date,              -- Date of the match
    m.home_team_id,            -- ID of the home team
    ht.team_name AS home_team, -- Name of the home team
    m.away_team_id,            -- ID of the away team
    at.team_name AS away_team, -- Name of the away team
    m.home_team_score,         -- Score of the home team
    m.away_team_score,         -- Score of the away team
    ts.team_id,                -- Team ID for standings
    ts.team_name,              -- Team name for standings
    ts.matches_played,         -- Total matches played by the team
    ts.wins,                   -- Total wins by the team
    ts.draws,                  -- Total draws by the team
    ts.losses,                 -- Total losses by the team
    ts.points                  -- Total points accumulated by the team
FROM 
    matches m                  -- Table containing match details
JOIN 
    teams ht                   -- Table containing team details (home team)
    ON m.home_team_id = ht.team_id
JOIN 
    teams at                   -- Table containing team details (away team)
    ON m.away_team_id = at.team_id
JOIN 
    team_standings ts          -- Table containing team standings
    ON ts.team_id IN (m.home_team_id, m.away_team_id)
WHERE 
    m.match_date >= CURRENT_DATE - INTERVAL '30 days' -- Filter for matches in the last 30 days
ORDER BY 
    m.match_date DESC;         -- Sort results by match date in descending order
```
