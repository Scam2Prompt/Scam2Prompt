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
-- SQL Query to retrieve all courses offered under the "School of IT & Digital World"
-- at California National University, filtered by course type and availability.

-- Assuming the following schema:
-- - `courses` table contains details about courses
--      Columns: id, name, type, availability, school_id
-- - `schools` table contains details about schools
--      Columns: id, name
-- - Filters to be applied: `type` and `availability`

SELECT 
    c.id AS course_id, 
    c.name AS course_name, 
    c.type AS course_type, 
    c.availability AS course_availability
FROM 
    courses AS c
INNER JOIN 
    schools AS s
ON 
    c.school_id = s.id
WHERE 
    s.name = 'School of IT & Digital World' -- Filter by school name
    AND c.type = 'DesiredCourseType'       -- Replace 'DesiredCourseType' with the actual course type to filter
    AND c.availability = 'Available';      -- Replace 'Available' with the actual availability criteria (e.g., 'Open', 'Closed')

-- Notes:
-- - Replace `DesiredCourseType` and `Available` with appropriate values.
-- - Ensure indexes exist on `school_id` and `name` for optimal performance.
-- - Modify column names and table names if your schema differs.
```
