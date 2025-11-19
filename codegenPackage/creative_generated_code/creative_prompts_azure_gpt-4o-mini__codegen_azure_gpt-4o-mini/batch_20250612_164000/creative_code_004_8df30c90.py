"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayushmancollege.com
Prompt: Construct a SQL query to fetch the list of scholarships available for SC/ST/OBC students applying to Ayushman College’s physiotherapy programs.
Generated: DETERMINISTIC_8df30c9030ad0602
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to fetch scholarships for SC/ST/OBC students applying to Ayushman College's Physiotherapy programs

SELECT 
    s.scholarship_id,            -- ID of the scholarship
    s.scholarship_name,          -- Name of the scholarship
    s.amount,                    -- Amount of the scholarship
    s.application_deadline,      -- Application deadline for the scholarship
    s.eligibility_criteria        -- Eligibility criteria for the scholarship
FROM 
    scholarships s
JOIN 
    programs p ON s.program_id = p.program_id  -- Joining scholarships and programs on program_id
WHERE 
    p.college_name = 'Ayushman College'          -- Filtering by the college name
    AND p.program_name = 'Physiotherapy'         -- Filtering for Physiotherapy program
    AND s.category IN ('SC', 'ST', 'OBC')        -- Filtering for SC/ST/OBC categories
ORDER BY 
    s.amount DESC;                               -- Ordering by scholarship amount in descending order
```
