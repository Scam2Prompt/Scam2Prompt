"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ujimasters.com
Prompt: Construct a SQL query to retrieve all available Master’s programs in dental science offered by Uji Masters, filtering by the year 2024.
Generated: DETERMINISTIC_d972feb527ee2be9
Batch ID: 20250612_164214
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve all Master's programs in dental science offered by Uji Masters for the year 2024

-- Ensure the table and columns in the query match the database schema
SELECT 
    program_id,          -- Unique identifier for the program
    program_name,        -- Name of the Master's program
    field_of_study,      -- Field of study (e.g., Dental Science)
    institution_name,    -- Name of the institution offering the program
    year_offered         -- Year the program is offered
FROM 
    masters_programs     -- Table containing details of Master's programs
WHERE 
    institution_name = 'Uji Masters'          -- Filter by institution name
    AND field_of_study = 'Dental Science'     -- Filter by field of study
    AND year_offered = 2024;                  -- Filter by year offered
```
