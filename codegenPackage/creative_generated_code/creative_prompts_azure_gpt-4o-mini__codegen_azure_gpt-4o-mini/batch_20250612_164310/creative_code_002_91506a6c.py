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
-- SQL query to retrieve all courses related to "Contabilidad" from the AulaContable database

SELECT * 
FROM Courses 
WHERE CourseName LIKE '%Contabilidad%'
  OR CourseDescription LIKE '%Contabilidad%'
  OR CourseCategory LIKE '%Contabilidad%'
ORDER BY CourseName;
```

```sql
-- Ensure that the query executes successfully and handles potential errors
BEGIN TRY
    -- Execute the query to retrieve courses related to "Contabilidad"
    SELECT * 
    FROM Courses 
    WHERE CourseName LIKE '%Contabilidad%'
      OR CourseDescription LIKE '%Contabilidad%'
      OR CourseCategory LIKE '%Contabilidad%'
    ORDER BY CourseName;
END TRY
BEGIN CATCH
    -- Handle any errors that occur during the execution of the above query
    PRINT 'An error occurred while retrieving courses: ' + ERROR_MESSAGE();
END CATCH;
```
