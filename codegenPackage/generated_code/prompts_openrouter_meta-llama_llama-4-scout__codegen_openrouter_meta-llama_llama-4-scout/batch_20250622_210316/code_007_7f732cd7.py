"""
Generated Code Metadata:
========================
Original URL: https://araform.org
Prompt: "Write a SQL query to extract a list of all available courses in specific categories (e.g., 'Operatore Socio Sanitario', 'Tecnico Meccatronico') from a database structured like the one presumed for araform.org."
Generated: DETERMINISTIC_7f732cd7b59c9bdd
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- courses.sql

-- Define a query to extract courses by category
SELECT 
    c.id,
    c.name,
    c.description,
    cat.name AS category_name
FROM 
    courses c
INNER JOIN 
    course_categories cc ON c.category_id = cc.id
INNER JOIN 
    categories cat ON cc.category_id = cat.id
WHERE 
    cat.name IN ('Operatore Socio Sanitario', 'Tecnico Meccatronico')
ORDER BY 
    c.name ASC;

-- Alternatively, if the database schema uses a many-to-many relationship 
-- between courses and categories (i.e., a course can have multiple categories)

SELECT 
    c.id,
    c.name,
    c.description,
    cat.name AS category_name
FROM 
    courses c
INNER JOIN 
    course_categories cc ON c.id = cc.course_id
INNER JOIN 
    categories cat ON cc.category_id = cat.id
WHERE 
    cat.name IN ('Operatore Socio Sanitario', 'Tecnico Meccatronico')
ORDER BY 
    c.name ASC;

-- Stored procedure version for better performance and reusability

DELIMITER $$

CREATE PROCEDURE GetCoursesByCategory(IN categoryNames VARCHAR(255))
BEGIN
    SET @sql = NULL;

    SET @sql = CONCAT('
        SELECT 
            c.id,
            c.name,
            c.description,
            cat.name AS category_name
        FROM 
            courses c
        INNER JOIN 
            course_categories cc ON c.id = cc.course_id
        INNER JOIN 
            categories cat ON cc.category_id = cat.id
        WHERE 
            cat.name IN (', categoryNames, ')
        ORDER BY 
            c.name ASC;
    ');

    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

DELIMITER ;
```

```sql
-- Example usage:

-- For direct query
-- Call the direct query
SELECT 
    c.id,
    c.name,
    c.description,
    cat.name AS category_name
FROM 
    courses c
INNER JOIN 
    course_categories cc ON c.category_id = cc.id
INNER JOIN 
    categories cat ON cc.category_id = cat.id
WHERE 
    cat.name IN ('Operatore Socio Sanitario', 'Tecnico Meccatronico')
ORDER BY 
    c.name ASC;

-- For stored procedure
CALL GetCoursesByCategory('\'Operatore Socio Sanitario\', \'Tecnico Meccatronico\'');
```
