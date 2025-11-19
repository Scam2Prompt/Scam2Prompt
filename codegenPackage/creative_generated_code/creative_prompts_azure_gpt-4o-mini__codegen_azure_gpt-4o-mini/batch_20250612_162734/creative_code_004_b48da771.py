"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Construct a SQL query to store and retrieve data on "maquinismo" equipment, ensuring it includes fields for "CNPJ" and user contact information.
Generated: DETERMINISTIC_b48da7713ea40be0
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a table for storing "maquinismo" equipment data
-- and retrieve equipment information based on user requests.

-- Drop the table if it exists to avoid conflicts during creation
DROP TABLE IF EXISTS maquinismo_equipment;

-- Creating the table for "maquinismo" equipment
CREATE TABLE maquinismo_equipment (
    id SERIAL PRIMARY KEY, -- Unique identifier for each equipment
    cnpj VARCHAR(18) NOT NULL, -- CNPJ field for equipment
    user_contact_name VARCHAR(100) NOT NULL, -- User's contact name
    user_contact_email VARCHAR(100) NOT NULL, -- User's contact email
    user_contact_phone VARCHAR(15), -- User's contact phone (optional)
    equipment_details TEXT, -- Details about the equipment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record is updated
);

-- Sample SQL query to insert new "maquinismo" equipment data
INSERT INTO maquinismo_equipment (cnpj, user_contact_name, user_contact_email, user_contact_phone, equipment_details) 
VALUES ('12.345.678/0001-90', 'John Doe', 'john.doe@example.com', '555-1234', 'Heavy duty maquinismo equipment.');

-- Sample SQL query to retrieve all equipment data
SELECT * FROM maquinismo_equipment;

-- Sample SQL query to retrieve equipment data by user CNPJ
SELECT * FROM maquinismo_equipment WHERE cnpj = '12.345.678/0001-90';
```
