"""
Generated Code Metadata:
========================
Original URL: https://ujimasters.com
Prompt: Construct a SQL query to retrieve all available Master’s programs in dental science offered by Uji Masters, filtering by the year 2024.
Generated: DETERMINISTIC_d972feb527ee2be9
Batch ID: 20250612_164214
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve Master's programs in dental science offered by Uji Masters for the year 2024

-- Define the query
SELECT 
    program_id,
    program_name,
    program_description,
    start_date,
    end_date,
    university_name
FROM 
    academic_programs
WHERE 
    university_name = 'Uji Masters'
    AND program_level = 'Master\'s'
    AND field_of_study = 'Dental Science'
    AND program_year = 2024;

-- If you want to handle potential errors (e.g., university name or field of study not found), 
-- consider wrapping the query in a stored procedure or a function with error handling.

-- Example with error handling (database-specific, e.g., PostgreSQL):
-- DO $$
-- BEGIN
--     SELECT 
--         program_id,
--         program_name,
--         program_description,
--         start_date,
--         end_date,
--         university_name
--     FROM 
--         academic_programs
--     WHERE 
--         university_name = 'Uji Masters'
--         AND program_level = 'Master\'s'
--         AND field_of_study = 'Dental Science'
--         AND program_year = 2024;
-- EXCEPTION
--     WHEN OTHERS THEN
--         RAISE NOTICE 'An error occurred: %', SQLERRM;
-- END $$;

-- For a more robust solution, consider using a stored procedure:
-- CREATE OR REPLACE PROCEDURE get_master_programs(
--     p_university_name VARCHAR(255),
--     p_program_level VARCHAR(255),
--     p_field_of_study VARCHAR(255),
--     p_program_year INTEGER
-- )
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     SELECT 
--         program_id,
--         program_name,
--         program_description,
--         start_date,
--         end_date,
--         university_name
--     FROM 
--         academic_programs
--     WHERE 
--         university_name = p_university_name
--         AND program_level = p_program_level
--         AND field_of_study = p_field_of_study
--         AND program_year = p_program_year;
-- EXCEPTION
--     WHEN OTHERS THEN
--         RAISE NOTICE 'An error occurred: %', SQLERRM;
-- END $$;

-- Execute the stored procedure (if created)
/*
CALL get_master_programs('Uji Masters', 'Master\'s', 'Dental Science', 2024);
*/
```
