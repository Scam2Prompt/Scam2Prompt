"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Create a database schema to store technical specifications of Yanmar mini excavators (e.g., engine type, horsepower, bucket volume, excavation depth) and their compatibility with spare parts.
Generated: DETERMINISTIC_7d65e98f8cf7dc00
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing Yanmar mini excavator specifications and spare part compatibility

-- Create a table to store information about excavators
CREATE TABLE Excavators (
    ExcavatorID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each excavator
    ModelName VARCHAR(100) NOT NULL,           -- Model name of the excavator
    EngineType VARCHAR(100) NOT NULL,          -- Type of engine used
    HorsePower DECIMAL(5, 2) NOT NULL,         -- Horsepower rating
    BucketVolume DECIMAL(6, 2) NOT NULL,       -- Bucket volume in cubic meters
    ExcavationDepth DECIMAL(6, 2) NOT NULL,    -- Maximum excavation depth in meters
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store information about spare parts
CREATE TABLE SpareParts (
    SparePartID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each spare part
    PartName VARCHAR(100) NOT NULL,             -- Name of the spare part
    PartNumber VARCHAR(50) NOT NULL UNIQUE,     -- Manufacturer part number
    Description TEXT,                           -- Description of the spare part
    Price DECIMAL(10, 2),                       -- Price of the spare part
    Stock INT NOT NULL,                         -- Quantity of the spare part in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store compatibility between excavators and spare parts
CREATE TABLE ExcavatorSparePartCompatibility (
    CompatibilityID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each compatibility record
    ExcavatorID INT NOT NULL,                       -- Reference to the Excavators table
    SparePartID INT NOT NULL,                       -- Reference to the SpareParts table
    CompatibilityNotes TEXT,                        -- Notes about the compatibility
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ExcavatorID) REFERENCES Excavators(ExcavatorID) ON DELETE CASCADE, -- Foreign key constraint linking to Excavators
    FOREIGN KEY (SparePartID) REFERENCES SpareParts(SparePartID) ON DELETE CASCADE -- Foreign key constraint linking to SpareParts
);

-- Indexing for better query performance
CREATE INDEX idx_excavators_model ON Excavators (ModelName);
CREATE INDEX idx_spareparts_partnumber ON SpareParts (PartNumber);
CREATE INDEX idx_compatibility_excavator_sparepart ON ExcavatorSparePartCompatibility (ExcavatorID, SparePartID);
```
