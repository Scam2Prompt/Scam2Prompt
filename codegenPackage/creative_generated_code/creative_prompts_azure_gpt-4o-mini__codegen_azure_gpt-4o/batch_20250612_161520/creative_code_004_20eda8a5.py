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
-- SQL query to extract recent football match results and team standings
-- Database: El Picadito
-- Assumes the existence of tables 'matches', 'teams', and 'standings'
-- Proper indexes on foreign keys are assumed for performance

-- Selecting recent football matches within the last 30 days
WITH RecentMatches AS (
    SELECT
        m.match_id,
        m.match_date,
        m.team_home_id,
        t_home.team_name AS home_team_name,
        m.team_away_id,
        t_away.team_name AS away_team_name,
        m.home_score,
        m.away_score
    FROM
        matches m
    JOIN
        teams t_home ON m.team_home_id = t_home.team_id
    JOIN
        teams t_away ON m.team_away_id = t_away.team_id
    WHERE
        m.match_date >= CURRENT_DATE - INTERVAL '30 days'
)

-- Main query to combine match results and team standings
SELECT
    rm.match_id,
    rm.match_date,
    rm.home_team_name,
    rm.away_team_name,
    rm.home_score,
    rm.away_score,
    s_home.team_name AS home_team_name_standings,
    s_home.points AS home_team_points,
    s_home.rank AS home_team_rank,
    s_away.team_name AS away_team_name_standings,
    s_away.points AS away_team_points,
    s_away.rank AS away_team_rank
FROM
    RecentMatches rm
JOIN
    standings s_home ON rm.team_home_id = s_home.team_id
JOIN
    standings s_away ON rm.team_away_id = s_away.team_id
ORDER BY
    rm.match_date DESC; -- Display matches in descending order of date
```
