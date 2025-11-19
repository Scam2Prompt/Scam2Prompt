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
-- SQL query to extract participant feedback from VSport's basketball summer training camps
-- focusing on skill improvement and coaching effectiveness.

-- Assumes there is a table named `feedback` with relevant columns:
-- - `participant_id`: ID of the participant
-- - `training_camp_id`: ID of the basketball summer training camp
-- - `feedback_date`: Date when the feedback was submitted
-- - `skill_improvement_score`: Numeric score for skill improvement (e.g., 1-10 scale)
-- - `coaching_effectiveness_score`: Numeric score for coaching effectiveness (e.g., 1-10 scale)
-- - `comments`: Free-text comments provided by the participant

-- Query starts here
SELECT 
    f.participant_id,
    f.training_camp_id,
    f.feedback_date,
    f.skill_improvement_score,
    f.coaching_effectiveness_score,
    f.comments,
    tc.camp_name,
    tc.camp_location
FROM 
    feedback AS f
INNER JOIN 
    training_camps AS tc
    ON f.training_camp_id = tc.camp_id  -- Join to get additional details about the camp
WHERE 
    f.feedback_date >= '2023-01-01'  -- Filter for feedback submitted after January 1, 2023
    AND f.skill_improvement_score IS NOT NULL  -- Ensure skill improvement score is provided
    AND f.coaching_effectiveness_score IS NOT NULL  -- Ensure coaching effectiveness score is provided
ORDER BY 
    f.feedback_date DESC;  -- Order feedback by most recent first
```
