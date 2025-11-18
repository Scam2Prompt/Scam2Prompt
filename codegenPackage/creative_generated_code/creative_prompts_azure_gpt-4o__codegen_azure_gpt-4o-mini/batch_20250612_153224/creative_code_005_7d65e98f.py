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
-- SQL script to create a database schema for Yanmar mini excavators and their spare parts compatibility

-- Create a database for the Yanmar mini excavators
CREATE DATABASE YanmarExcavators;

-- Use the created database
USE YanmarExcavators;

-- Table to store information about the excavators
CREATE TABLE Excavators (
    ExcavatorID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each excavator
    Model VARCHAR(50) NOT NULL,                   -- Model name of the excavator
    EngineType VARCHAR(30) NOT NULL,              -- Type of engine (e.g., diesel, electric)
    Horsepower INT NOT NULL,                       -- Horsepower of the excavator
    BucketVolume DECIMAL(5,2) NOT NULL,           -- Volume of the bucket in cubic meters
    ExcavationDepth DECIMAL(5,2) NOT NULL         -- Maximum excavation depth in meters
);

-- Table to store spare parts information
CREATE TABLE SpareParts (
    PartID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each spare part
    PartName VARCHAR(50) NOT NULL,                 -- Name of the spare part (e.g., bucket, engine)
    Compatibility VARCHAR(50) NOT NULL              -- Model compatibility (e.g., specific excavator models)
);

-- Junction table to establish a many-to-many relationship between Excavators and SpareParts
CREATE TABLE ExcavatorSpareParts (
    ExcavatorID INT,                               -- Foreign key referencing Excavators
    PartID INT,                                    -- Foreign key referencing SpareParts
    PRIMARY KEY (ExcavatorID, PartID),            -- Composite primary key for the relationship
    FOREIGN KEY (ExcavatorID) REFERENCES Excavators(ExcavatorID) ON DELETE CASCADE,
    FOREIGN KEY (PartID) REFERENCES SpareParts(PartID) ON DELETE CASCADE
);

-- Sample data insertion (not part of the schema, just for testing purposes)
INSERT INTO Excavators (Model, EngineType, Horsepower, BucketVolume, ExcavationDepth)
VALUES
    ('Yanmar Vio17', 'Diesel', 14, 0.045, 2.3),
    ('Yanmar Vio25', 'Diesel', 19, 0.055, 2.5);

INSERT INTO SpareParts (PartName, Compatibility)
VALUES
    ('Standard Bucket', 'Vio17'),
    ('Heavy Duty Bucket', 'Vio25');

INSERT INTO ExcavatorSpareParts (ExcavatorID, PartID)
VALUES
    (1, 1), -- Vio17 compatible with Standard Bucket
    (2, 2); -- Vio25 compatible with Heavy Duty Bucket
```
