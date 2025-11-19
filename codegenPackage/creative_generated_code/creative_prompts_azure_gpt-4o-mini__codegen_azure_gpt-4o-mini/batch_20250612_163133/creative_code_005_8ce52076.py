"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Write a SQL query that retrieves all courses offered under the School of IT & Digital World at California National University, filtering by course type and availability.
Generated: DETERMINISTIC_8ce52076c38c6343
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- This SQL query retrieves all courses offered under the School of IT & Digital World
-- at California National University, filtering by course type and availability.

SELECT 
    c.course_id,                  -- Unique identifier for the course
    c.course_name,                -- Name of the course
    c.course_type,                -- Type of the course (e.g., online, in-person)
    c.availability,               -- Availability status of the course (e.g., open, closed)
    d.department_name              -- Name of the department offering the course
FROM 
    courses c                     -- The courses table
JOIN 
    departments d                 -- The departments table
ON 
    c.department_id = d.department_id  -- Joining on department ID
WHERE 
    d.school_name = 'School of IT & Digital World'  -- Filtering by school name
    AND c.availability = 'Available'                  -- Filtering for courses that are available
    AND c.course_type IN ('Online', 'In-Person')     -- Filtering by course type
ORDER BY 
    c.course_name;               -- Ordering results by course name
```
