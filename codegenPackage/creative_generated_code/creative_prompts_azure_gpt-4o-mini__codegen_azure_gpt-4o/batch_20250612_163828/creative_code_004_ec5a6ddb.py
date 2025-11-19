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
-- SQL Query to extract data on student enrollments for the "Salud Ocupacional" diplomado
-- Assuming the database structure follows standard conventions.
-- This query fetches details about enrolled students and their enrollment data.

SELECT 
    students.student_id,         -- Unique identifier for the student
    students.first_name,         -- First name of the student
    students.last_name,          -- Last name of the student
    students.email,              -- Email of the student
    enrollments.enrollment_date, -- Date of enrollment
    courses.course_name          -- Name of the course
FROM 
    enrollments
INNER JOIN 
    students 
ON 
    enrollments.student_id = students.student_id -- Join students table to get student info
INNER JOIN 
    courses 
ON 
    enrollments.course_id = courses.course_id -- Join courses table to get course info
WHERE 
    courses.course_name = 'Salud Ocupacional'   -- Filter for the "Salud Ocupacional" diplomado
AND 
    enrollments.status = 'active';             -- Ensure that only active enrollments are fetched

-- Notes:
-- 1. Replace table and column names if your schema uses different naming conventions.
-- 2. Add additional filters or sorting as needed.
-- 3. Ensure indexes are in place for optimal performance on large datasets.
```
