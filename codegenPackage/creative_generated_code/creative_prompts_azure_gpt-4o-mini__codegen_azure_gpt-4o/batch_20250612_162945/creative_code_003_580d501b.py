"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Develop a SQL query to extract data about the faculty members involved in the MBA programs at SOMTU, focusing on their qualifications and areas of expertise.
Generated: DETERMINISTIC_580d501b7e916509
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to extract data about faculty members involved in MBA programs at SOMTU
-- focusing on their qualifications and areas of expertise.

-- This query assumes the following:
-- 1. There is a "faculty" table containing information about faculty members.
-- 2. There is a "programs" table containing information about various programs.
-- 3. There is a "faculty_programs" table for mapping faculty members to programs.
-- 4. SOMTU MBA programs are identified by a specific name or code in the "programs" table.
-- 5. The "faculty" table includes columns for qualifications and areas of expertise.

SELECT 
    f.faculty_id,           -- Unique identifier for the faculty member
    f.name AS faculty_name, -- Full name of the faculty member
    f.qualifications,       -- Faculty member's qualifications
    f.expertise,            -- Faculty member's areas of expertise
    p.program_name          -- Name of the MBA program
FROM 
    faculty AS f
INNER JOIN 
    faculty_programs AS fp ON f.faculty_id = fp.faculty_id -- Map faculty members to programs
INNER JOIN 
    programs AS p ON fp.program_id = p.program_id         -- Match programs to MBA
WHERE 
    p.program_name LIKE '%MBA%'                           -- Filter only MBA programs
    AND p.institution_name = 'SOMTU';                     -- Ensure the program belongs to SOMTU
```
