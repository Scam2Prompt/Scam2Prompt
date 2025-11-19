"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: Write SQL queries to retrieve information about students enrolled in programs like "Bachelor’s in Psychology" and "Master’s in Education Leadership," referencing the program details from CNU.
Generated: DETERMINISTIC_7cd3bdedd55a9181
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve information about students enrolled in programs like "Bachelor’s in Psychology" and "Master’s in Education Leadership"

-- Assuming the following database schema:
-- - students table: student_id (primary key), name, email
-- - programs table: program_id (primary key), program_name
-- - enrollments table: enrollment_id (primary key), student_id (foreign key), program_id (foreign key)

-- Query to retrieve student information for specific programs
SELECT 
    s.student_id,
    s.name,
    s.email,
    p.program_name
FROM 
    students s
INNER JOIN 
    enrollments e ON s.student_id = e.student_id
INNER JOIN 
    programs p ON e.program_id = p.program_id
WHERE 
    p.program_name IN (
        'Bachelor’s in Psychology', 
        'Master’s in Education Leadership'
    );

-- Query to retrieve program details from CNU (assuming CNU prefix for program names)
SELECT 
    s.student_id,
    s.name,
    s.email,
    p.program_name
FROM 
    students s
INNER JOIN 
    enrollments e ON s.student_id = e.student_id
INNER JOIN 
    programs p ON e.program_id = p.program_id
WHERE 
    p.program_name LIKE 'CNU - Bachelor’s%' 
    OR p.program_name LIKE 'CNU - Master’s%';

-- Stored procedure to encapsulate the query
DELIMITER //
CREATE PROCEDURE GetStudentInfoByProgram(
    IN programName1 VARCHAR(255),
    IN programName2 VARCHAR(255)
)
BEGIN
    SELECT 
        s.student_id,
        s.name,
        s.email,
        p.program_name
    FROM 
        students s
    INNER JOIN 
        enrollments e ON s.student_id = e.student_id
    INNER JOIN 
        programs p ON e.program_id = p.program_id
    WHERE 
        p.program_name IN (programName1, programName2);
END//
DELIMITER ;

-- Example usage:
CALL GetStudentInfoByProgram('Bachelor’s in Psychology', 'Master’s in Education Leadership');
```
