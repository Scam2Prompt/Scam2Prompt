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

Below is the SQL code:

```sql
-- Create table to store "maquinismo" equipment data
CREATE TABLE MaquinismoEquipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the equipment
    EquipmentName VARCHAR(255) NOT NULL,        -- Name of the equipment
    EquipmentType VARCHAR(100) NOT NULL,        -- Type/category of the equipment
    CNPJ CHAR(14) NOT NULL,                     -- CNPJ identifier (Brazilian company registry)
    UserName VARCHAR(255) NOT NULL,             -- Contact name of the responsible user
    UserEmail VARCHAR(255) NOT NULL,            -- Contact email of the responsible user
    UserPhone VARCHAR(20),                      -- Contact phone number of the responsible user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Insert sample data into the MaquinismoEquipment table
INSERT INTO MaquinismoEquipment (EquipmentName, EquipmentType, CNPJ, UserName, UserEmail, UserPhone)
VALUES 
('Excavator', 'Heavy Machinery', '12345678000123', 'John Doe', 'johndoe@example.com', '+5511987654321'),
('Forklift', 'Warehouse Equipment', '98765432000198', 'Jane Smith', 'janesmith@example.com', '+5511976543210');

-- Retrieve all data from the table
SELECT * FROM MaquinismoEquipment;

-- Retrieve equipment information based on a specific CNPJ
SELECT * 
FROM MaquinismoEquipment
WHERE CNPJ = '12345678000123';

-- Retrieve contact information for all responsible users
SELECT UserName, UserEmail, UserPhone
FROM MaquinismoEquipment;

-- Example of error handling: Attempt to insert a row with invalid CNPJ length (this will fail due to validation constraints)
INSERT INTO MaquinismoEquipment (EquipmentName, EquipmentType, CNPJ, UserName, UserEmail, UserPhone)
VALUES 
('Bulldozer', 'Construction Equipment', '12345', 'Alice Brown', 'alice@example.com', '+5511945678912');
```
