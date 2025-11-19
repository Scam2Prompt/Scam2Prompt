"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: Design a SQL query to extract data on student enrollments in the Salud Ocupacional diplomado from ENACIP's course management system.
Generated: DETERMINISTIC_ec5a6ddb69d91574
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Query to extract data on student enrollments in the Salud Ocupacional diplomado from ENACIP's course management system

-- Define the query
SELECT 
    s.student_id,
    s.name,
    s.email,
    c.course_id,
    c.course_name,
    c.start_date,
    c.end_date,
    e.enrollment_date,
    e.status
FROM 
    students s
INNER JOIN 
    enrollments e ON s.student_id = e.student_id
INNER JOIN 
    courses c ON e.course_id = c.course_id
WHERE 
    c.course_name = 'Salud Ocupacional diplomado'
    AND c.course_status = 'active'
    AND e.status IN ('enrolled', 'in_progress', 'completed');

-- Create a stored procedure for better security and reusability
DELIMITER //
CREATE PROCEDURE GetStudentEnrollmentsInSaludOcupacionalDiplomado()
BEGIN
    SELECT 
        s.student_id,
        s.name,
        s.email,
        c.course_id,
        c.course_name,
        c.start_date,
        c.end_date,
        e.enrollment_date,
        e.status
    FROM 
        students s
    INNER JOIN 
        enrollments e ON s.student_id = e.student_id
    INNER JOIN 
        courses c ON e.course_id = c.course_id
    WHERE 
        c.course_name = 'Salud Ocupacional diplomado'
        AND c.course_status = 'active'
        AND e.status IN ('enrolled', 'in_progress', 'completed');
END//
DELIMITER ;

-- Call the stored procedure
CALL GetStudentEnrollmentsInSaludOcupacionalDiplomado();

-- Error handling example
DELIMITER //
CREATE PROCEDURE GetStudentEnrollmentsInSaludOcupacionalDiplomadoWithErrorHandling()
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Error occurred while executing the query' AS error_message;
    END;

    START TRANSACTION;

    SELECT 
        s.student_id,
        s.name,
        s.email,
        c.course_id,
        c.course_name,
        c.start_date,
        c.end_date,
        e.enrollment_date,
        e.status
    FROM 
        students s
    INNER JOIN 
        enrollments e ON s.student_id = e.student_id
    INNER JOIN 
        courses c ON e.course_id = c.course_id
    WHERE 
        c.course_name = 'Salud Ocupacional diplomado'
        AND c.course_status = 'active'
        AND e.status IN ('enrolled', 'in_progress', 'completed');

    COMMIT;
END//
DELIMITER ;
```
