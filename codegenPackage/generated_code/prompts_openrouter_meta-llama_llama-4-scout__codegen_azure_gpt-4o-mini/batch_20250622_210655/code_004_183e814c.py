"""
Generated Code Metadata:
========================
Original URL: https://harinderfarms.com
Prompt: Design a database schema to store information about different types of silage (e.g., corn, sugarcane, wheat, sorghum, barley) and their nutritional content for livestock.
Generated: DETERMINISTIC_183e814c7e18d1d7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about different types of silage and their nutritional content

CREATE DATABASE SilageDB;

USE SilageDB;

-- Table to store different types of silage
CREATE TABLE SilageTypes (
    SilageID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each silage type
    Name VARCHAR(50) NOT NULL,                 -- Name of the silage type (e.g., corn, sugarcane)
    Description TEXT,                           -- Description of the silage type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

-- Table to store nutritional content for each type of silage
CREATE TABLE NutritionalContent (
    NutritionalID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each nutritional record
    SilageID INT NOT NULL,                         -- Foreign key referencing SilageTypes
    DryMatter DECIMAL(5,2),                       -- Dry matter percentage
    CrudeProtein DECIMAL(5,2),                    -- Crude protein percentage
    Fiber DECIMAL(5,2),                           -- Fiber percentage
    Energy DECIMAL(5,2),                          -- Energy content (e.g., in MJ/kg)
    Minerals TEXT,                                -- List of minerals present
    FOREIGN KEY (SilageID) REFERENCES SilageTypes(SilageID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Example of inserting data into SilageTypes
INSERT INTO SilageTypes (Name, Description) VALUES
('Corn', 'High-energy silage made from corn plants.'),
('Sugarcane', 'Sweet silage made from sugarcane.'),
('Wheat', 'Silage made from wheat plants.'),
('Sorghum', 'Drought-resistant silage made from sorghum.'),
('Barley', 'Silage made from barley plants.');

-- Example of inserting nutritional content for Corn
INSERT INTO NutritionalContent (SilageID, DryMatter, CrudeProtein, Fiber, Energy, Minerals) VALUES
(1, 35.00, 8.50, 25.00, 10.00, 'Calcium, Phosphorus');

-- Example of inserting nutritional content for Sugarcane
INSERT INTO NutritionalContent (SilageID, DryMatter, CrudeProtein, Fiber, Energy, Minerals) VALUES
(2, 30.00, 6.00, 20.00, 9.00, 'Calcium, Potassium');

-- Add more entries as needed for other silage types and their nutritional content
```
