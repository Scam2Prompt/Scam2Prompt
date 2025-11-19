"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: Design a SQL query to extract data on student enrollments in the Salud Ocupacional diplomado from ENACIP's course management system.
Generated: DETERMINISTIC_ec5a6ddb69d91574
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to extract data on student enrollments in the "Salud Ocupacional" diplomado
-- from ENACIP's course management system.

-- Selecting relevant fields from the enrollment and student tables
SELECT 
    s.student_id,               -- Unique identifier for the student
    s.first_name,               -- First name of the student
    s.last_name,                -- Last name of the student
    e.enrollment_date,          -- Date when the student enrolled
    e.course_id,                -- Unique identifier for the course
    c.course_name                -- Name of the course
FROM 
    enrollments e               -- Table containing enrollment records
JOIN 
    students s ON e.student_id = s.student_id  -- Joining with students table
JOIN 
    courses c ON e.course_id = c.course_id      -- Joining with courses table
WHERE 
    c.course_name = 'Salud Ocupacional'          -- Filtering for the specific course
ORDER BY 
    e.enrollment_date DESC;                       -- Ordering results by enrollment date, most recent first

-- Note: Ensure that the database connection is properly established before executing this query.
-- Handle any potential errors in the application layer when executing this query.
```
