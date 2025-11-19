"""
Generated Code Metadata:
========================
Original URL: https://deafah.in
Prompt: Write a SQL query to retrieve information about Deafah Hotels' properties located near the Haramain, including their addresses and available suite types.
Generated: DETERMINISTIC_a32de1c7c209cbad
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve information about Deafah Hotels' properties near Haramain

-- Define a query to get hotel properties
SELECT 
    p.property_id,
    p.name AS hotel_name,
    p.address AS hotel_address,
    p.city,
    p.country,
    st.suite_type_id,
    st.suite_type_name,
    st.description AS suite_description,
    st.rate AS suite_rate
FROM 
    properties p
INNER JOIN 
    suite_types st ON p.property_id = st.property_id
WHERE 
    p.name LIKE '%Deafah%' 
    AND (p.city = 'Makkah' OR p.city = 'Medina')
ORDER BY 
    p.property_id, 
    st.suite_type_id;

-- Define a stored procedure for better encapsulation and reusability
DELIMITER $$

CREATE PROCEDURE GetDeafahHotelsNearHaramain()
BEGIN
    SELECT 
        p.property_id,
        p.name AS hotel_name,
        p.address AS hotel_address,
        p.city,
        p.country,
        st.suite_type_id,
        st.suite_type_name,
        st.description AS suite_description,
        st.rate AS suite_rate
    FROM 
        properties p
    INNER JOIN 
        suite_types st ON p.property_id = st.property_id
    WHERE 
        p.name LIKE '%Deafah%' 
        AND (p.city = 'Makkah' OR p.city = 'Medina')
    ORDER BY 
        p.property_id, 
        st.suite_type_id;
END$$

DELIMITER ;

-- Call the stored procedure
CALL GetDeafahHotelsNearHaramain();

-- Error handling example
DELIMITER $$

CREATE PROCEDURE GetDeafahHotelsNearHaramainSafe()
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'An error occurred while retrieving data.' AS error_message;
    END;

    START TRANSACTION;

    SELECT 
        p.property_id,
        p.name AS hotel_name,
        p.address AS hotel_address,
        p.city,
        p.country,
        st.suite_type_id,
        st.suite_type_name,
        st.description AS suite_description,
        st.rate AS suite_rate
    FROM 
        properties p
    INNER JOIN 
        suite_types st ON p.property_id = st.property_id
    WHERE 
        p.name LIKE '%Deafah%' 
        AND (p.city = 'Makkah' OR p.city = 'Medina')
    ORDER BY 
        p.property_id, 
        st.suite_type_id;

    COMMIT;
END$$

DELIMITER ;
```
