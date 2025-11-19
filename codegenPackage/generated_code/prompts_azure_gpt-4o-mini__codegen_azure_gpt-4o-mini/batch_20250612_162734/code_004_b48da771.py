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
-- Create a table to store information about "maquinismo" equipment
CREATE TABLE maquinismo_equipment (
    id SERIAL PRIMARY KEY, -- Unique identifier for each equipment entry
    cnpj VARCHAR(14) NOT NULL, -- CNPJ of the company, must be 14 characters
    user_name VARCHAR(100) NOT NULL, -- Name of the user/contact person
    user_email VARCHAR(100) NOT NULL, -- Email of the user/contact person
    user_phone VARCHAR(15), -- Phone number of the user/contact person
    equipment_type VARCHAR(50) NOT NULL, -- Type of the equipment
    purchase_date DATE NOT NULL, -- Date of purchase
    warranty_expiration DATE, -- Expiration date of the warranty
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Insert a new record into the maquinismo_equipment table
INSERT INTO maquinismo_equipment (cnpj, user_name, user_email, user_phone, equipment_type, purchase_date, warranty_expiration)
VALUES ('12345678000195', 'John Doe', 'john.doe@example.com', '1234567890', 'Excavator', '2023-01-15', '2025-01-15');

-- Retrieve all records from the maquinismo_equipment table
SELECT * FROM maquinismo_equipment;

-- Retrieve a specific record by CNPJ
SELECT * FROM maquinismo_equipment WHERE cnpj = '12345678000195';

-- Update a record in the maquinismo_equipment table
UPDATE maquinismo_equipment
SET user_email = 'john.newemail@example.com', user_phone = '0987654321'
WHERE cnpj = '12345678000195';

-- Delete a record from the maquinismo_equipment table
DELETE FROM maquinismo_equipment WHERE cnpj = '12345678000195';
```
