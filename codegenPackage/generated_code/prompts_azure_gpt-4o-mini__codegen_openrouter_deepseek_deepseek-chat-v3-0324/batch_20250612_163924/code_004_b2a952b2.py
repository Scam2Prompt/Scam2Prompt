"""
Generated Code Metadata:
========================
Original URL: https://cimedweb.org
Prompt: Construct a SQL query to extract data on the number of publications from CIMEd's collection related to critical pedagogy and educational interventions.
Generated: DETERMINISTIC_b2a952b21bb9f70f
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to count publications related to critical pedagogy and educational interventions from CIMEd's collection
-- This query assumes the existence of tables with publication data and relevant metadata

SELECT 
    COUNT(DISTINCT p.publication_id) AS publication_count,
    p.publication_year,
    p.language
FROM 
    publications p
JOIN 
    publication_subjects ps ON p.publication_id = ps.publication_id
JOIN 
    subjects s ON ps.subject_id = s.subject_id
WHERE 
    -- Match terms related to critical pedagogy
    (s.subject_name LIKE '%critical pedagogy%' 
     OR s.subject_name LIKE '%critical education%'
     OR s.subject_name LIKE '%radical pedagogy%'
     OR s.subject_name LIKE '%transformative education%'
     OR s.subject_name LIKE '%liberatory education%'
     OR s.subject_name LIKE '%Freirean%')
    
    -- Match terms related to educational interventions
    OR (s.subject_name LIKE '%educational intervention%'
        OR s.subject_name LIKE '%teaching intervention%'
        OR s.subject_name LIKE '%pedagogical intervention%'
        OR s.subject_name LIKE '%education program%'
        OR s.subject_name LIKE '%learning intervention%')
GROUP BY 
    p.publication_year,
    p.language
ORDER BY 
    p.publication_year DESC,
    publication_count DESC;
```
