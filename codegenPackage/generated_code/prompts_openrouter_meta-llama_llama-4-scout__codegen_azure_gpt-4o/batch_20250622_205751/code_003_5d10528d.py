"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: "Design a database schema to store information about different types of acrylic yarns, such as Grey Yarns, Dyed Yarns, and Milange Yarns."
Generated: DETERMINISTIC_5d10528d529c61cb
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema to store information about different types of acrylic yarns

-- Table to store general information about yarn types
CREATE TABLE YarnTypes (
    YarnTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each yarn type
    YarnTypeName VARCHAR(50) NOT NULL,         -- Name of the yarn type (e.g., Grey Yarns, Dyed Yarns, Milange Yarns)
    Description TEXT                           -- Optional description of the yarn type
);

-- Table to store specific details about acrylic yarns
CREATE TABLE AcrylicYarns (
    YarnID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each yarn
    YarnTypeID INT NOT NULL,                   -- Foreign key referencing YarnTypes table
    YarnName VARCHAR(100) NOT NULL,            -- Name or identifier for the yarn
    Color VARCHAR(50),                         -- Color of the yarn (e.g., Grey, Red, Blue)
    Weight DECIMAL(10, 2),                     -- Weight of the yarn in grams
    MaterialComposition VARCHAR(255),         -- Material composition details (e.g., 100% Acrylic)
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the yarn
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity of yarn available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (YarnTypeID) REFERENCES YarnTypes(YarnTypeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store additional attributes or metadata for yarns
CREATE TABLE YarnAttributes (
    AttributeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attribute
    YarnID INT NOT NULL,                        -- Foreign key referencing AcrylicYarns table
    AttributeName VARCHAR(50) NOT NULL,         -- Name of the attribute (e.g., Twist, Ply)
    AttributeValue VARCHAR(255) NOT NULL,       -- Value of the attribute (e.g., High Twist, 2-Ply)
    FOREIGN KEY (YarnID) REFERENCES AcrylicYarns(YarnID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Example indexes for performance optimization
CREATE INDEX idx_yarn_type ON AcrylicYarns(YarnTypeID); -- Index for YarnTypeID in AcrylicYarns
CREATE INDEX idx_yarn_name ON AcrylicYarns(YarnName);   -- Index for YarnName in AcrylicYarns
CREATE INDEX idx_attribute_name ON YarnAttributes(AttributeName); -- Index for AttributeName in YarnAttributes
```
