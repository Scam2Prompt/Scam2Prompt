"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzothofetcollege.co.za
Prompt: Write a SQL query to retrieve the list of courses offered by Nzotho FET College's Faculty of Business Studies, categorized by diploma and occupational certificates.
Generated: DETERMINISTIC_2267932c6678436d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to retrieve the list of courses offered by Nzotho FET College's Faculty of Business Studies,
-- categorized by diploma and occupational certificates.

-- Assumptions:
-- 1. The database contains a table named 'courses' that includes information about all courses.
-- 2. The table has the following columns: course_id, course_name, faculty_name, category, and course_type.
-- 3. 'Faculty of Business Studies' is the value stored in the 'faculty_name' column for the relevant faculty.
-- 4. 'Diploma' and 'Occupational Certificate' are values stored in the 'course_type' column.

-- Query starts here
SELECT 
    course_type AS CourseType,      -- Group courses by type (Diploma or Occupational Certificate)
    course_name AS CourseName       -- Display the name of each course
FROM 
    courses
WHERE 
    faculty_name = 'Faculty of Business Studies'  -- Filter courses for the specific faculty
    AND (course_type = 'Diploma' OR course_type = 'Occupational Certificate') -- Filter for specific categories
ORDER BY 
    course_type,                     -- Organize output by course type
    course_name;                     -- Sort course names alphabetically within each type

-- End of Query
```
