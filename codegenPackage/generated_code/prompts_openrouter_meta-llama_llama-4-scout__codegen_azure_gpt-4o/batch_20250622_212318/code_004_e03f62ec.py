"""
Generated Code Metadata:
========================
Original URL: https://villaandreas.gr
Prompt: "Design a database schema to store information about villas, including details like location (e.g., distance to Myrtos beach), amenities (e.g., swimming pool, table tennis), and capacity, inspired by the villa listings on villaandreas.gr."
Generated: DETERMINISTIC_e03f62ecfdc43519
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing villa information

-- Table to store villa details
CREATE TABLE Villas (
    VillaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each villa
    Name VARCHAR(255) NOT NULL,             -- Name of the villa
    Location VARCHAR(255) NOT NULL,         -- Location of the villa
    DistanceToBeach FLOAT NOT NULL,         -- Distance to Myrtos beach (in kilometers)
    Capacity INT NOT NULL,                  -- Maximum number of guests the villa can accommodate
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store amenities for each villa
CREATE TABLE Amenities (
    AmenityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each amenity
    Name VARCHAR(255) NOT NULL UNIQUE         -- Name of the amenity (e.g., swimming pool, table tennis)
);

-- Junction table to associate villas with their amenities
CREATE TABLE VillaAmenities (
    VillaID INT NOT NULL,                     -- Foreign key referencing Villas table
    AmenityID INT NOT NULL,                   -- Foreign key referencing Amenities table
    PRIMARY KEY (VillaID, AmenityID),         -- Composite primary key to ensure uniqueness
    FOREIGN KEY (VillaID) REFERENCES Villas(VillaID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for performance optimization
CREATE INDEX idx_villa_location ON Villas(Location); -- Index for quick location-based searches
CREATE INDEX idx_villa_capacity ON Villas(Capacity); -- Index for quick capacity-based searches
CREATE INDEX idx_amenity_name ON Amenities(Name);     -- Index for quick amenity-based searches
```
