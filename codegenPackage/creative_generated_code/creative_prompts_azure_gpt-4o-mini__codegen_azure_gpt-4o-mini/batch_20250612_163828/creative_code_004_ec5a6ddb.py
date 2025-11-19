"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Design a SQL query to extract data on student enrollments in the Salud Ocupacional diplomado from ENACIP's course management system.
Generated: DETERMINISTIC_ec5a6ddb69d91574
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to extract data on student enrollments in the Salud Ocupacional diplomado
-- from ENACIP's course management system.

SELECT 
    s.student_id,                 -- Student's unique identifier
    s.first_name,                 -- Student's first name
    s.last_name,                  -- Student's last name
    e.enrollment_date,            -- Date of enrollment
    c.course_name,                -- Name of the course
    c.diplomado_name              -- Name of the diplomado
FROM 
    students s                    -- Students table
JOIN 
    enrollments e ON s.student_id = e.student_id  -- Joining enrollments on student_id
JOIN 
    courses c ON e.course_id = c.course_id  -- Joining courses on course_id
WHERE 
    c.diplomado_name = 'Salud Ocupacional'  -- Filtering for the specific diplomado
ORDER BY 
    e.enrollment_date DESC;        -- Ordering results by enrollment date in descending order

-- Ensure to handle exceptions and errors in your application that utilizes this query,
-- such as managing connection issues and invalid SQL execution states.
```
