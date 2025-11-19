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
CREATE TABLE MaquinismoEquipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each equipment
    EquipmentName VARCHAR(255) NOT NULL,        -- Name of the equipment
    EquipmentType VARCHAR(255),                 -- Type/category of the equipment
    Manufacturer VARCHAR(255),                  -- Manufacturer of the equipment
    CNPJ CHAR(14) NOT NULL,                     -- CNPJ (Brazilian company identifier) associated with the equipment
    UserContactName VARCHAR(255) NOT NULL,      -- Name of the user/contact person
    UserContactEmail VARCHAR(255) NOT NULL,     -- Email of the user/contact person
    UserContactPhone VARCHAR(20),               -- Phone number of the user/contact person
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was added
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Insert sample data into the MaquinismoEquipment table
INSERT INTO MaquinismoEquipment (
    EquipmentName, EquipmentType, Manufacturer, CNPJ, UserContactName, UserContactEmail, UserContactPhone
) VALUES
    ('Excavator X200', 'Excavator', 'Machinery Co.', '12345678000195', 'John Doe', 'john.doe@example.com', '+55 11 98765-4321'),
    ('Bulldozer B300', 'Bulldozer', 'HeavyDuty Inc.', '98765432000123', 'Jane Smith', 'jane.smith@example.com', '+55 21 91234-5678');

-- Retrieve all data from the MaquinismoEquipment table
SELECT * FROM MaquinismoEquipment;

-- Retrieve specific data based on CNPJ
SELECT EquipmentName, EquipmentType, Manufacturer, UserContactName, UserContactEmail, UserContactPhone
FROM MaquinismoEquipment
WHERE CNPJ = '12345678000195';

-- Error handling: Ensure CNPJ is always 14 characters long and valid
-- This can be enforced using a CHECK constraint (if supported by the SQL dialect)
ALTER TABLE MaquinismoEquipment
ADD CONSTRAINT chk_cnpj_length CHECK (LENGTH(CNPJ) = 14);
```
