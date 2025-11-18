"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Write SQL queries to retrieve data about students enrolled in Egatur's "Bar y Mixología" program and sort them by enrollment date.
Generated: DETERMINISTIC_9fae2408988dade7
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve student data for Egatur's "Bar y Mixología" program
-- The results will be sorted by the enrollment date in ascending order.

SELECT 
    s.student_id,            -- Unique identifier for each student
    s.first_name,            -- Student's first name
    s.last_name,             -- Student's last name
    e.enrollment_date,       -- Date when the student enrolled in the program
    p.program_name           -- Name of the program the student is enrolled in
FROM 
    students AS s            -- Table containing student information
JOIN 
    enrollments AS e ON s.student_id = e.student_id  -- Join with enrollments table to get enrollment data
JOIN 
    programs AS p ON e.program_id = p.program_id      -- Join with programs table to get program details
WHERE 
    p.program_name = 'Bar y Mixología'                 -- Filter for the specific program "Bar y Mixología"
ORDER BY 
    e.enrollment_date ASC;                             -- Sort results by enrollment date in ascending order
```
