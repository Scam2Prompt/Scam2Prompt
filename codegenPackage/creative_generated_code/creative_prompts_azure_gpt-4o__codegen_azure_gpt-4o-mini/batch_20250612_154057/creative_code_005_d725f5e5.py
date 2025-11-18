"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hypersteakin.site
Prompt: Write a SQL query to analyze attendee data for the HyperSteakin Awards Ceremony, including metrics on pass type distribution and workshop participation.
Generated: DETERMINISTIC_d725f5e5f7d0af16
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to analyze attendee data for the HyperSteakin Awards Ceremony
-- This query retrieves metrics on pass type distribution and workshop participation

WITH PassTypeDistribution AS (
    SELECT 
        pass_type,                -- The type of pass held by the attendee
        COUNT(*) AS attendee_count -- The count of attendees for each pass type
    FROM 
        attendees                 -- The table containing attendee information
    GROUP BY 
        pass_type                 -- Grouping by pass type for aggregation
),

WorkshopParticipation AS (
    SELECT 
        w.workshop_name,         -- The name of the workshop
        COUNT(DISTINCT a.attendee_id) AS participants_count -- Count distinct attendees in each workshop
    FROM 
        workshops w              -- Table containing workshop information
    JOIN 
        attendee_workshops aw    -- Junction table linking attendees to workshops
        ON w.workshop_id = aw.workshop_id
    JOIN 
        attendees a              -- Join with attendees to get attendee details
        ON aw.attendee_id = a.attendee_id
    GROUP BY 
        w.workshop_name          -- Grouping by workshop name for aggregation
)

-- Final selection combining the results
SELECT 
    p.pass_type, 
    p.attendee_count, 
    w.workshop_name, 
    COALESCE(w.participants_count, 0) AS participants_count -- Use COALESCE to handle nulls for workshops with no participants
FROM 
    PassTypeDistribution p
LEFT JOIN 
    WorkshopParticipation w 
ON 
    1=1                       -- Cross join to combine all pass types with workshop participation data
ORDER BY 
    p.pass_type,              -- Order results by pass type for easier readability
    w.workshop_name;          -- Also order by workshop name
```
