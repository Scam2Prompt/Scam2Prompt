"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Develop a SQL query to extract data about the faculty members involved in the MBA programs at SOMTU, focusing on their qualifications and areas of expertise.
Generated: DETERMINISTIC_580d501b7e916509
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to extract data about faculty members involved in MBA programs at SOMTU,
-- focusing on their qualifications and areas of expertise.

-- Assumptions:
-- 1. The database has a table named `faculty` containing information about faculty members.
-- 2. The table `faculty` includes columns: `faculty_id`, `name`, `department`, `qualification`, `expertise`, and `program`.
-- 3. The `program` column specifies the programs the faculty is involved in (e.g., 'MBA', 'BBA', etc.).
-- 4. The `department` column specifies the department the faculty belongs to (e.g., 'SOMTU').

-- Query starts here:
SELECT 
    faculty_id,       -- Unique identifier for the faculty member
    name,             -- Name of the faculty member
    qualification,    -- Academic qualifications of the faculty member
    expertise         -- Areas of expertise of the faculty member
FROM 
    faculty
WHERE 
    program = 'MBA'   -- Filter for faculty involved in MBA programs
    AND department = 'SOMTU'; -- Filter for faculty belonging to SOMTU department

-- Notes:
-- 1. Ensure the table `faculty` exists and has the required columns.
-- 2. If additional filtering or sorting is needed, modify the query accordingly.
-- 3. This query assumes no duplicate entries for faculty members in the table.
```
