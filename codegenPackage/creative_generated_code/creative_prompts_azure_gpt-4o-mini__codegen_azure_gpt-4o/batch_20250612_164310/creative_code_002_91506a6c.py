"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Create a sample SQL query to retrieve all courses related to "Contabilidad" from the AulaContable database.
Generated: DETERMINISTIC_91506a6cc2eaed0b
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to retrieve all courses related to "Contabilidad" from the AulaContable database.
-- This query assumes there is a table named 'courses' with relevant columns.

-- Query starts here
SELECT 
    course_id,           -- Unique identifier for the course
    course_name,         -- Name of the course
    course_description,  -- Detailed description of the course
    created_at,          -- Timestamp when the course was created
    updated_at           -- Timestamp when the course was last updated
FROM 
    courses              -- Table containing course information
WHERE 
    course_name LIKE '%Contabilidad%'  -- Filter courses related to "Contabilidad"
ORDER BY 
    created_at DESC;     -- Sorting courses by the most recently created ones, descending order

-- Notes:
-- 1. The LIKE operator is used to match course names containing "Contabilidad".
-- 2. '%' is a wildcard allowing for partial matches before or after "Contabilidad".
-- 3. Adjust column names and table name as per the actual database schema.
```
