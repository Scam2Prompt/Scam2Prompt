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
-- SQL query to extract data about faculty members involved in MBA programs at SOMTU
-- This query retrieves the qualifications and areas of expertise of the faculty members.

SELECT 
    f.faculty_id,                       -- Unique identifier for the faculty member
    f.first_name,                       -- Faculty member's first name
    f.last_name,                        -- Faculty member's last name
    f.email,                            -- Faculty member's email address
    f.qualification,                    -- Academic qualifications of the faculty member
    f.expertise_area                    -- Areas of expertise of the faculty member
FROM 
    faculty f                          -- Faculty table
JOIN 
    mba_programs mp                    -- MBA programs table
ON 
    f.faculty_id = mp.faculty_id      -- Joining condition on faculty ID
WHERE 
    mp.university_name = 'SOMTU'       -- Focus on faculty members from SOMTU
    AND mp.program_type = 'MBA';       -- Filter for MBA program faculty
```
