"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Write a SQL query to retrieve the list of courses offered by Nzotho FET College's Faculty of Business Studies, categorized by diploma and occupational certificates.
Generated: DETERMINISTIC_2267932c6678436d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve courses offered by Nzotho FET College's Faculty of Business Studies,
-- categorized by diploma and occupational certificates.

SELECT 
    'Diploma' AS CourseCategory,
    d.CourseName,
    d.CourseCode,
    d.Duration
FROM 
    BusinessStudiesDiplomas d

UNION ALL

SELECT 
    'Occupational Certificate' AS CourseCategory,
    oc.CourseName,
    oc.CourseCode,
    oc.Duration
FROM 
    BusinessStudiesOccupationalCertificates oc

ORDER BY 
    CourseCategory, 
    CourseName;
```

However, assuming that we are working with a more complex database schema that includes separate tables for courses, faculties, and colleges, here is a more realistic query:

```sql
-- Retrieve courses offered by Nzotho FET College's Faculty of Business Studies,
-- categorized by diploma and occupational certificates.

SELECT 
    'Diploma' AS CourseCategory,
    c.CourseName,
    c.CourseCode,
    c.Duration
FROM 
    Colleges col
INNER JOIN 
    Faculties f ON col.CollegeID = f.CollegeID
INNER JOIN 
    Courses c ON f.FacultyID = c.FacultyID
INNER JOIN 
    CourseTypes ct ON c.CourseTypeID = ct.CourseTypeID
WHERE 
    col.CollegeName = 'Nzotho FET College'
    AND f.FacultyName = 'Faculty of Business Studies'
    AND ct.CourseTypeName = 'Diploma'

UNION ALL

SELECT 
    'Occupational Certificate' AS CourseCategory,
    c.CourseName,
    c.CourseCode,
    c.Duration
FROM 
    Colleges col
INNER JOIN 
    Faculties f ON col.CollegeID = f.CollegeID
INNER JOIN 
    Courses c ON f.FacultyID = c.FacultyID
INNER JOIN 
    CourseTypes ct ON c.CourseTypeID = ct.CourseTypeID
WHERE 
    col.CollegeName = 'Nzotho FET College'
    AND f.FacultyName = 'Faculty of Business Studies'
    AND ct.CourseTypeName = 'Occupational Certificate'

ORDER BY 
    CourseCategory, 
    CourseName;
```

And with error handling in a stored procedure:

```sql
DELIMITER //

CREATE PROCEDURE GetCoursesByNzothoFETCollegeBusinessStudies()
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN 
        ROLLBACK; 
        SELECT 'An error occurred, please try again.' AS ErrorMessage;
    END;

    START TRANSACTION;

    SELECT 
        'Diploma' AS CourseCategory,
        c.CourseName,
        c.CourseCode,
        c.Duration
    FROM 
        Colleges col
    INNER JOIN 
        Faculties f ON col.CollegeID = f.CollegeID
    INNER JOIN 
        Courses c ON f.FacultyID = c.FacultyID
    INNER JOIN 
        CourseTypes ct ON c.CourseTypeID = ct.CourseTypeID
    WHERE 
        col.CollegeName = 'Nzotho FET College'
        AND f.FacultyName = 'Faculty of Business Studies'
        AND ct.CourseTypeName = 'Diploma'

    UNION ALL

    SELECT 
        'Occupational Certificate' AS CourseCategory,
        c.CourseName,
        c.CourseCode,
        c.Duration
    FROM 
        Colleges col
    INNER JOIN 
        Faculties f ON col.CollegeID = f.CollegeID
    INNER JOIN 
        Courses c ON f.FacultyID = c.FacultyID
    INNER JOIN 
        CourseTypes ct ON c.CourseTypeID = ct.CourseTypeID
    WHERE 
        col.CollegeName = 'Nzotho FET College'
        AND f.FacultyName = 'Faculty of Business Studies'
        AND ct.CourseTypeName = 'Occupational Certificate'

    ORDER BY 
        CourseCategory, 
        CourseName;

    COMMIT;
END //

DELIMITER ;
```
