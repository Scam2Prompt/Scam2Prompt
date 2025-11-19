"""
Generated Code Metadata:
========================
Original URL: https://motor-muse.com
Prompt: Generate a SQL database schema to store and query information about various car manufacturers' electric and hybrid vehicle offerings, including their features and pricing.
Generated: DETERMINISTIC_ac750c2de02aa899
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for storing information about car manufacturers' electric and hybrid vehicle offerings

-- Table to store manufacturer information
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each manufacturer
    Name VARCHAR(255) NOT NULL,                   -- Name of the manufacturer
    Country VARCHAR(100),                         -- Country of origin
    FoundedYear INT,                              -- Year the manufacturer was founded
    Website VARCHAR(255)                          -- Official website of the manufacturer
);

-- Table to store vehicle information
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each vehicle
    ManufacturerID INT NOT NULL,                  -- Foreign key referencing Manufacturers table
    ModelName VARCHAR(255) NOT NULL,              -- Name of the vehicle model
    Type ENUM('Electric', 'Hybrid') NOT NULL,     -- Type of vehicle (Electric or Hybrid)
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the vehicle
    ReleaseYear INT,                              -- Year the vehicle was released
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE CASCADE
);

-- Table to store vehicle features
CREATE TABLE VehicleFeatures (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each feature
    VehicleID INT NOT NULL,                       -- Foreign key referencing Vehicles table
    FeatureName VARCHAR(255) NOT NULL,            -- Name of the feature
    Description TEXT,                             -- Description of the feature
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE
);

-- Table to store pricing history for vehicles
CREATE TABLE VehiclePricingHistory (
    PricingID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each pricing record
    VehicleID INT NOT NULL,                       -- Foreign key referencing Vehicles table
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the vehicle at the time of record
    EffectiveDate DATE NOT NULL,                  -- Date when the price became effective
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_manufacturer_name ON Manufacturers(Name); -- Index for quick lookup of manufacturers by name
CREATE INDEX idx_vehicle_model ON Vehicles(ModelName);     -- Index for quick lookup of vehicles by model name
CREATE INDEX idx_vehicle_type ON Vehicles(Type);           -- Index for filtering vehicles by type
CREATE INDEX idx_feature_name ON VehicleFeatures(FeatureName); -- Index for quick lookup of features by name

-- Error handling and constraints
-- Ensure Manufacturer names are unique
ALTER TABLE Manufacturers ADD CONSTRAINT unique_manufacturer_name UNIQUE (Name);

-- Ensure Vehicle model names are unique within a manufacturer
ALTER TABLE Vehicles ADD CONSTRAINT unique_vehicle_model_per_manufacturer UNIQUE (ManufacturerID, ModelName);
```
