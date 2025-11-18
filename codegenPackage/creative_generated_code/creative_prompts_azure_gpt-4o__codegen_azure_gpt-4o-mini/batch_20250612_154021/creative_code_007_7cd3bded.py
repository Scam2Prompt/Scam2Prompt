"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Write SQL queries to retrieve information about students enrolled in programs like "Bachelor’s in Psychology" and "Master’s in Education Leadership," referencing the program details from CNU.
Generated: DETERMINISTIC_7cd3bdedd55a9181
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve information about students enrolled in specified programs

-- This query selects the student details along with their program information
-- from the CNU database.

SELECT 
    s.student_id,            -- Unique identifier for each student
    s.first_name,            -- Student's first name
    s.last_name,             -- Student's last name
    p.program_name,          -- Name of the program the student is enrolled in
    p.degree_level,          -- Degree level of the program (e.g., Bachelor’s, Master’s)
    p.program_start_date,    -- Start date of the program
    p.program_end_date       -- End date of the program
FROM 
    students s               -- Students table alias
JOIN 
    programs p               -- Programs table alias
ON 
    s.program_id = p.program_id  -- Joining condition: matches student to their program
WHERE 
    p.program_name IN ('Bachelor’s in Psychology', 'Master’s in Education Leadership'); -- Filter for specific programs

-- Note: Ensure that the database schema has the 'students' and 'programs' tables
-- properly defined with the relevant fields for this query to execute successfully.
```
