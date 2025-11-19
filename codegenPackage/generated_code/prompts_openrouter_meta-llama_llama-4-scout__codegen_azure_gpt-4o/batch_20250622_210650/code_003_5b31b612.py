"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: "Design a database schema to store information about car bearings, including product codes, vehicle models, and technical specifications, as used by یاتاقان گلدن."
Generated: DETERMINISTIC_5b31b612a78f0f77
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about car bearings

-- Table to store information about car bearings
CREATE TABLE Bearings (
    BearingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bearing
    ProductCode VARCHAR(50) NOT NULL,         -- Product code for the bearing
    Name VARCHAR(100) NOT NULL,               -- Name or description of the bearing
    Manufacturer VARCHAR(100),                -- Manufacturer of the bearing
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store vehicle models associated with bearings
CREATE TABLE VehicleModels (
    VehicleModelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle model
    ModelName VARCHAR(100) NOT NULL,               -- Name of the vehicle model
    Manufacturer VARCHAR(100),                     -- Manufacturer of the vehicle
    Year INT,                                      -- Year of the vehicle model
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store technical specifications of bearings
CREATE TABLE TechnicalSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    BearingID INT NOT NULL,                          -- Foreign key referencing Bearings table
    SpecificationKey VARCHAR(100) NOT NULL,         -- Key for the specification (e.g., "Diameter", "Material")
    SpecificationValue VARCHAR(255) NOT NULL,       -- Value for the specification (e.g., "50mm", "Steel")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (BearingID) REFERENCES Bearings(BearingID) ON DELETE CASCADE -- Cascade delete if bearing is removed
);

-- Table to associate bearings with vehicle models
CREATE TABLE BearingVehicleMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each mapping
    BearingID INT NOT NULL,                   -- Foreign key referencing Bearings table
    VehicleModelID INT NOT NULL,              -- Foreign key referencing VehicleModels table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (BearingID) REFERENCES Bearings(BearingID) ON DELETE CASCADE, -- Cascade delete if bearing is removed
    FOREIGN KEY (VehicleModelID) REFERENCES VehicleModels(VehicleModelID) ON DELETE CASCADE -- Cascade delete if vehicle model is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_product_code ON Bearings(ProductCode); -- Index for quick lookup by product code
CREATE INDEX idx_model_name ON VehicleModels(ModelName); -- Index for quick lookup by model name
CREATE INDEX idx_spec_key ON TechnicalSpecifications(SpecificationKey); -- Index for quick lookup by specification key
```
