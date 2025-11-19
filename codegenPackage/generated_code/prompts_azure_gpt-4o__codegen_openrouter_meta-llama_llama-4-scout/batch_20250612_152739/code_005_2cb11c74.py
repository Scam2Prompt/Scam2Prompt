"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: Generate a SQL query to retrieve all products related to "ARB" brand accessories, such as canisters, recovery gear, and interior storage solutions, as described on DMS Auto4x4.ro.
Generated: DETERMINISTIC_2cb11c7438bf3b1c
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve products related to ARB brand accessories
-- Assuming a database schema with 'products' table and 'brands' table

SELECT 
    p.id,
    p.name,
    p.description,
    p.price,
    b.name AS brand_name
FROM 
    products p
INNER JOIN 
    brands b ON p.brand_id = b.id
WHERE 
    b.name = 'ARB' 
    AND p.category IN (
        'Canisters', 
        'Recovery Gear', 
        'Interior Storage Solutions'
    )
ORDER BY 
    p.name ASC;

-- Stored procedure version
DELIMITER //
CREATE PROCEDURE Get_ARB_Products()
BEGIN
    SELECT 
        p.id,
        p.name,
        p.description,
        p.price,
        b.name AS brand_name
    FROM 
        products p
    INNER JOIN 
        brands b ON p.brand_id = b.id
    WHERE 
        b.name = 'ARB' 
        AND p.category IN (
            'Canisters', 
            'Recovery Gear', 
            'Interior Storage Solutions'
        )
    ORDER BY 
        p.name ASC;
END//
DELIMITER ;

-- Example usage:
-- CALL Get_ARB_Products();

-- Function to handle errors
DELIMITER //
CREATE FUNCTION Get_ARB_Products_With_Error_Handling()
RETURNS TABLE
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Error occurred while retrieving products' AS error_message;
    END;

    START TRANSACTION;

    SELECT 
        p.id,
        p.name,
        p.description,
        p.price,
        b.name AS brand_name
    FROM 
        products p
    INNER JOIN 
        brands b ON p.brand_id = b.id
    WHERE 
        b.name = 'ARB' 
        AND p.category IN (
            'Canisters', 
            'Recovery Gear', 
            'Interior Storage Solutions'
        )
    ORDER BY 
        p.name ASC;

    COMMIT;
END//
DELIMITER ;
```
