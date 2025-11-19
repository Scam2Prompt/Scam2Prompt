"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Construct a SQL query to store and retrieve data on "maquinismo" equipment, ensuring it includes fields for "CNPJ" and user contact information.
Generated: DETERMINISTIC_b48da7713ea40be0
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database and table for maquinismo equipment
-- ==============================================

-- Create database
CREATE DATABASE IF NOT EXISTS maquinismo_db;

-- Use database
USE maquinismo_db;

-- Create table for maquinismo equipment
CREATE TABLE IF NOT EXISTS maquinismo_equipment (
    id INT AUTO_INCREMENT,
    cnpj VARCHAR(14) NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    user_phone VARCHAR(20) NOT NULL,
    equipment_name VARCHAR(255) NOT NULL,
    equipment_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY (cnpj)
);

-- Create index on cnpj for efficient retrieval
CREATE INDEX idx_cnpj ON maquinismo_equipment (cnpj);

-- Stored procedure to insert new equipment data
-- ==============================================

DELIMITER $$

CREATE PROCEDURE sp_insert_equipment(
    IN p_cnpj VARCHAR(14),
    IN p_user_name VARCHAR(255),
    IN p_user_email VARCHAR(255),
    IN p_user_phone VARCHAR(20),
    IN p_equipment_name VARCHAR(255),
    IN p_equipment_description TEXT
)
BEGIN
    IF EXISTS (SELECT 1 FROM maquinismo_equipment WHERE cnpj = p_cnpj) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'CNPJ already exists';
    END IF;

    INSERT INTO maquinismo_equipment (
        cnpj,
        user_name,
        user_email,
        user_phone,
        equipment_name,
        equipment_description
    ) VALUES (
        p_cnpj,
        p_user_name,
        p_user_email,
        p_user_phone,
        p_equipment_name,
        p_equipment_description
    );
END$$

DELIMITER ;

-- Stored procedure to retrieve equipment data by CNPJ
-- ==============================================

DELIMITER $$

CREATE PROCEDURE sp_get_equipment_by_cnpj(
    IN p_cnpj VARCHAR(14)
)
BEGIN
    SELECT 
        id,
        cnpj,
        user_name,
        user_email,
        user_phone,
        equipment_name,
        equipment_description,
        created_at,
        updated_at
    FROM 
        maquinismo_equipment
    WHERE 
        cnpj = p_cnpj;
END$$

DELIMITER ;

-- Example usage
-- ==============

-- Insert new equipment data
CALL sp_insert_equipment(
    '12345678000190',
    'John Doe',
    'john.doe@example.com',
    '+1 123 456 7890',
    'Equipment 1',
    'This is equipment 1'
);

-- Retrieve equipment data by CNPJ
CALL sp_get_equipment_by_cnpj('12345678000190');
```
