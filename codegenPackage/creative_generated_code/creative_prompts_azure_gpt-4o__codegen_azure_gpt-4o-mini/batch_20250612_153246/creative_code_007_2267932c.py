"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzothofetcollege.co.za
Prompt: Write a SQL query to retrieve the list of courses offered by Nzotho FET College's Faculty of Business Studies, categorized by diploma and occupational certificates.
Generated: DETERMINISTIC_2267932c6678436d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve courses offered by Nzotho FET College's Faculty of Business Studies
-- The results are categorized by diploma and occupational certificates

SELECT 
    course_id,                -- Unique identifier for the course
    course_name,              -- Name of the course
    course_type,              -- Type: Diploma or Occupational Certificate
    duration,                 -- Duration of the course
    faculty                   -- Faculty offering the course
FROM 
    courses                   -- Table containing all courses
WHERE 
    faculty = 'Business Studies'  -- Filter for courses in the Faculty of Business Studies
    AND course_type IN ('Diploma', 'Occupational Certificate')  -- Filter for specific course types
ORDER BY 
    course_type,              -- Order results first by course type
    course_name;              -- Then by course name
```
