"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Write a SQL query to retrieve student data that reflects the integration of character-building values in academic performance from the SMKN 1 Kadipaten database.
Generated: DETERMINISTIC_cdbf488a1b54e7c0
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to retrieve student data reflecting character-building values in academic performance
-- from the SMKN 1 Kadipaten database.

SELECT 
    s.student_id, 
    s.first_name, 
    s.last_name, 
    s.class, 
    a.academic_performance, 
    c.character_values,
    c.integration_level
FROM 
    students AS s
JOIN 
    academic_performance AS a ON s.student_id = a.student_id
JOIN 
    character_building_values AS c ON s.student_id = c.student_id
WHERE 
    a.academic_performance IS NOT NULL 
    AND c.integration_level > 0  -- Ensure we only include students with integrated character values
ORDER BY 
    a.academic_performance DESC;  -- Order by highest academic performance

-- This query retrieves a list of students along with their academic performance and character-building values,
-- ensuring that only those with relevant data are included.
```
