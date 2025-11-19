"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Write a SQL query to retrieve student data that reflects the integration of character-building values in academic performance from the SMKN 1 Kadipaten database.
Generated: DETERMINISTIC_cdbf488a1b54e7c0
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to retrieve student data reflecting the integration of character-building values in academic performance
-- Assumes the database has tables named 'students', 'academic_performance', and 'character_values'

-- The query joins the 'students' table with 'academic_performance' and 'character_values' tables
-- Filters and retrieves relevant data for analysis

SELECT 
    s.student_id,                -- Unique identifier for the student
    s.name AS student_name,      -- Name of the student
    ap.subject,                  -- Subject name
    ap.grade AS academic_grade,  -- Academic performance grade
    cv.value_name AS character_value, -- Name of the character-building value
    cv.score AS value_score      -- Score reflecting the character-building value
FROM 
    students s
JOIN 
    academic_performance ap ON s.student_id = ap.student_id -- Join academic performance data
JOIN 
    character_values cv ON s.student_id = cv.student_id     -- Join character-building values data
WHERE 
    ap.grade IS NOT NULL          -- Ensure academic grades are available
    AND cv.score IS NOT NULL      -- Ensure character value scores are available
ORDER BY 
    s.name ASC,                   -- Sort by student name alphabetically
    ap.subject ASC;               -- Sort by subject name alphabetically
```
