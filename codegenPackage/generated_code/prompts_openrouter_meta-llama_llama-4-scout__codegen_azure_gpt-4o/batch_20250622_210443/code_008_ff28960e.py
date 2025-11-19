"""
Generated Code Metadata:
========================
Original URL: https://tuningdesign.gr
Prompt: "Design a database schema to store information about car models, tuning accessories, and their compatibility, using the Tuning Design website as a reference."
Generated: DETERMINISTIC_ff28960e53b0a060
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing car models, tuning accessories, and their compatibility

-- Table to store car manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each manufacturer
    Name VARCHAR(100) NOT NULL,                    -- Name of the manufacturer
    Country VARCHAR(100),                          -- Country of origin
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store car models
CREATE TABLE CarModels (
    ModelID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each car model
    ManufacturerID INT NOT NULL,                   -- Foreign key referencing Manufacturers table
    Name VARCHAR(100) NOT NULL,                    -- Name of the car model
    Year INT NOT NULL,                             -- Year of manufacture
    BodyType VARCHAR(50),                          -- Type of car body (e.g., sedan, SUV, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE CASCADE
);

-- Table to store tuning accessories
CREATE TABLE TuningAccessories (
    AccessoryID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each accessory
    Name VARCHAR(100) NOT NULL,                    -- Name of the accessory
    Description TEXT,                              -- Detailed description of the accessory
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the accessory
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store compatibility between car models and tuning accessories
CREATE TABLE Compatibility (
    CompatibilityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each compatibility record
    ModelID INT NOT NULL,                           -- Foreign key referencing CarModels table
    AccessoryID INT NOT NULL,                       -- Foreign key referencing TuningAccessories table
    Notes TEXT,                                     -- Additional notes about compatibility
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ModelID) REFERENCES CarModels(ModelID) ON DELETE CASCADE,
    FOREIGN KEY (AccessoryID) REFERENCES TuningAccessories(AccessoryID) ON DELETE CASCADE
);

-- Indexes for faster lookups
CREATE INDEX idx_ManufacturerName ON Manufacturers(Name);
CREATE INDEX idx_CarModelName ON CarModels(Name);
CREATE INDEX idx_AccessoryName ON TuningAccessories(Name);
CREATE INDEX idx_Compatibility ON Compatibility(ModelID, AccessoryID);
```
