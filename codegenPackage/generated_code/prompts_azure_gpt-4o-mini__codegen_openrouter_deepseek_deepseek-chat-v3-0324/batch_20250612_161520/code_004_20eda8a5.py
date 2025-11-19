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
-- SQL query to extract recent football match data and team standings from El Picadito database
WITH recent_matches AS (
    SELECT 
        m.match_id,
        m.match_date,
        ht.team_name AS home_team,
        at.team_name AS away_team,
        m.home_goals,
        m.away_goals,
        CASE 
            WHEN m.home_goals > m.away_goals THEN ht.team_name
            WHEN m.away_goals > m.home_goals THEN at.team_name
            ELSE 'Draw'
        END AS winner,
        l.league_name,
        m.venue
    FROM 
        matches m
    JOIN 
        teams ht ON m.home_team_id = ht.team_id
    JOIN 
        teams at ON m.away_team_id = at.team_id
    JOIN 
        leagues l ON m.league_id = l.league_id
    WHERE 
        m.match_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
    ORDER BY 
        m.match_date DESC
),
team_standings AS (
    SELECT 
        t.team_id,
        t.team_name,
        l.league_name,
        COUNT(*) AS matches_played,
        SUM(CASE 
            WHEN (m.home_team_id = t.team_id AND m.home_goals > m.away_goals) 
                 OR (m.away_team_id = t.team_id AND m.away_goals > m.home_goals) 
            THEN 1 ELSE 0 END) AS wins,
        SUM(CASE WHEN m.home_goals = m.away_goals THEN 1 ELSE 0 END) AS draws,
        SUM(CASE 
            WHEN (m.home_team_id = t.team_id AND m.home_goals < m.away_goals) 
                 OR (m.away_team_id = t.team_id AND m.away_goals < m.home_goals) 
            THEN 1 ELSE 0 END) AS losses,
        SUM(CASE 
            WHEN m.home_team_id = t.team_id THEN m.home_goals 
            ELSE m.away_goals END) AS goals_for,
        SUM(CASE 
            WHEN m.home_team_id = t.team_id THEN m.away_goals 
            ELSE m.home_goals END) AS goals_against,
        SUM(CASE 
            WHEN (m.home_team_id = t.team_id AND m.home_goals > m.away_goals) 
                 OR (m.away_team_id = t.team_id AND m.away_goals > m.home_goals) 
            THEN 3 
            WHEN m.home_goals = m.away_goals THEN 1 
            ELSE 0 END) AS points
    FROM 
        teams t
    JOIN 
        matches m ON (t.team_id = m.home_team_id OR t.team_id = m.away_team_id)
    JOIN 
        leagues l ON m.league_id = l.league_id
    WHERE 
        m.match_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
    GROUP BY 
        t.team_id, t.team_name, l.league_name
)

-- Main query combining recent matches and team standings
SELECT 
    'match' AS data_type,
    match_id,
    match_date,
    home_team,
    away_team,
    home_goals,
    away_goals,
    winner,
    league_name,
    venue,
    NULL AS matches_played,
    NULL AS wins,
    NULL AS draws,
    NULL AS losses,
    NULL AS goals_for,
    NULL AS goals_against,
    NULL AS points
FROM 
    recent_matches

UNION ALL

SELECT 
    'standing' AS data_type,
    NULL AS match_id,
    NULL AS match_date,
    team_name AS home_team,
    NULL AS away_team,
    NULL AS home_goals,
    NULL AS away_goals,
    NULL AS winner,
    league_name,
    NULL AS venue,
    matches_played,
    wins,
    draws,
    losses,
    goals_for,
    goals_against,
    points
FROM 
    team_standings
ORDER BY 
    data_type DESC, 
    CASE WHEN data_type = 'match' THEN match_date END DESC,
    CASE WHEN data_type = 'standing' THEN points END DESC;
```
