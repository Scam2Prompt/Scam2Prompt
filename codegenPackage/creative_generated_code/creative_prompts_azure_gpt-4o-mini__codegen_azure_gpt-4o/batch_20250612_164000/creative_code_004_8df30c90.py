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
-- SQL Query to fetch the list of scholarships available for SC/ST/OBC students 
-- applying to Ayushman College's physiotherapy programs.

-- Ensure the database schema includes relevant tables such as `scholarships`, `students`, 
-- `college_programs`, and appropriate columns to link the data accurately.

SELECT 
    s.scholarship_id,              -- Unique identifier for the scholarship
    s.scholarship_name,            -- Name of the scholarship
    s.scholarship_description,     -- Detailed description of the scholarship
    s.amount,                      -- Monetary value of the scholarship
    s.eligibility_criteria         -- Eligibility criteria for the scholarship
FROM 
    scholarships s
JOIN 
    college_programs cp 
ON 
    s.program_id = cp.program_id   -- Linking scholarships to specific college programs
WHERE 
    cp.college_name = 'Ayushman College'          -- Ensure the program belongs to Ayushman College
    AND cp.program_name = 'Physiotherapy'         -- Filter for physiotherapy programs
    AND s.target_group IN ('SC', 'ST', 'OBC');    -- Scholarships targeted for SC/ST/OBC students

-- Note: Ensure proper indexing in the database for optimal query performance.
-- Example indexes could include `program_id`, `college_name`, and `target_group`.
```
