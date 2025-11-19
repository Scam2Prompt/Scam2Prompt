"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherkan.com
Prompt: Write a SQL query to extract data on participant feedback from VSport's basketball summer training camps, focusing on skill improvement and coaching effectiveness.
Generated: DETERMINISTIC_21df2da96ded16e1
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to extract participant feedback on skill improvement and coaching effectiveness
-- from VSport's basketball summer training camps.

SELECT 
    p.participant_id,               -- ID of the participant
    p.name AS participant_name,     -- Name of the participant
    f.camp_id,                      -- ID of the camp
    c.name AS camp_name,            -- Name of the camp
    f.skill_improvement_rating,     -- Rating of skill improvement (1-10)
    f.coaching_effectiveness_rating, -- Rating of coaching effectiveness (1-10)
    f.comments                       -- Additional comments from the participant
FROM 
    participants p                  -- Table containing participant details
JOIN 
    feedback f ON p.participant_id = f.participant_id -- Join feedback table
JOIN 
    camps c ON f.camp_id = c.camp_id -- Join camps table to get camp details
WHERE 
    c.sport = 'Basketball' AND      -- Filter for basketball camps
    f.feedback_date BETWEEN '2023-06-01' AND '2023-08-31' -- Date range for summer training
ORDER BY 
    f.skill_improvement_rating DESC; -- Order by skill improvement rating, highest first

-- Note: 
-- This query assumes the existence of the following tables: 
-- - participants (participant_id, name)
-- - feedback (participant_id, camp_id, skill_improvement_rating, coaching_effectiveness_rating, comments, feedback_date)
-- - camps (camp_id, name, sport)
```
