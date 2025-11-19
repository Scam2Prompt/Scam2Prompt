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
-- Database schema to store information about silage types and their nutritional content

-- Table to store silage types
CREATE TABLE SilageTypes (
    SilageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each silage type
    Name VARCHAR(100) NOT NULL,              -- Name of the silage type (e.g., corn, sugarcane)
    Description TEXT,                        -- Optional description of the silage type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store nutritional content for each silage type
CREATE TABLE NutritionalContent (
    NutritionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each nutritional record
    SilageID INT NOT NULL,                      -- Foreign key referencing SilageTypes
    DryMatterPercentage DECIMAL(5, 2) NOT NULL, -- Dry matter percentage (e.g., 35.50%)
    CrudeProteinPercentage DECIMAL(5, 2) NOT NULL, -- Crude protein percentage (e.g., 8.50%)
    FiberPercentage DECIMAL(5, 2) NOT NULL,     -- Fiber percentage (e.g., 20.00%)
    EnergyContent DECIMAL(10, 2) NOT NULL,      -- Energy content in megajoules (e.g., 10.50 MJ/kg)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (SilageID) REFERENCES SilageTypes(SilageID) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for faster querying
CREATE INDEX idx_silage_name ON SilageTypes(Name); -- Index on silage name for quick lookups
CREATE INDEX idx_silage_id ON NutritionalContent(SilageID); -- Index on SilageID for efficient joins

-- Example error handling: Ensure SilageID exists before inserting nutritional content
DELIMITER $$
CREATE TRIGGER ValidateSilageIDBeforeInsert
BEFORE INSERT ON NutritionalContent
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM SilageTypes WHERE SilageID = NEW.SilageID) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid SilageID: Silage type does not exist.';
    END IF;
END;
$$
DELIMITER ;
```
