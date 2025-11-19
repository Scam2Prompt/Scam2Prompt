"""
Generated Code Metadata:
========================
Original URL: https://villasdeloix.com
Prompt: "Write a SQL query to design a database schema for storing villa details, such as number of bedrooms, pool availability, and location, inspired by the data presented on Villas de Loix."
Generated: DETERMINISTIC_d579c312e5991036
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing villa details

-- Create a database
CREATE DATABASE VillaDatabase;

-- Use the database
USE VillaDatabase;

-- Create a table for locations
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT,
    City VARCHAR(255) NOT NULL,
    Region VARCHAR(255) NOT NULL,
    Country VARCHAR(255) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Latitude DECIMAL(10, 8) NOT NULL,
    Longitude DECIMAL(11, 8) NOT NULL,
    PRIMARY KEY (LocationID)
);

-- Create a table for villa types
CREATE TABLE VillaTypes (
    VillaTypeID INT AUTO_INCREMENT,
    VillaTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (VillaTypeID)
);

-- Create a table for villa amenities
CREATE TABLE VillaAmenities (
    AmenityID INT AUTO_INCREMENT,
    AmenityName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (AmenityID)
);

-- Create a table for villas
CREATE TABLE Villas (
    VillaID INT AUTO_INCREMENT,
    VillaName VARCHAR(255) NOT NULL,
    Description TEXT,
    NumberOfBedrooms INT NOT NULL,
    NumberOfBathrooms INT NOT NULL,
    VillaTypeID INT,
    LocationID INT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VillaID),
    FOREIGN KEY (VillaTypeID) REFERENCES VillaTypes(VillaTypeID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

-- Create a many-to-many relationship table for villa amenities
CREATE TABLE VillaAmenitiesMap (
    VillaID INT NOT NULL,
    AmenityID INT NOT NULL,
    PRIMARY KEY (VillaID, AmenityID),
    FOREIGN KEY (VillaID) REFERENCES Villas(VillaID),
    FOREIGN KEY (AmenityID) REFERENCES VillaAmenities(AmenityID)
);

-- Create a table for pool details
CREATE TABLE PoolDetails (
    PoolID INT AUTO_INCREMENT,
    VillaID INT,
    PoolType VARCHAR(255) NOT NULL,
    Length DECIMAL(5, 2) NOT NULL,
    Width DECIMAL(5, 2) NOT NULL,
    Depth DECIMAL(5, 2) NOT NULL,
    PRIMARY KEY (PoolID),
    FOREIGN KEY (VillaID) REFERENCES Villas(VillaID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_Villas_LocationID ON Villas(LocationID);
CREATE INDEX idx_Villas_VillaTypeID ON Villas(VillaTypeID);
CREATE INDEX idx_VillaAmenitiesMap_VillaID ON VillaAmenitiesMap(VillaID);
CREATE INDEX idx_VillaAmenitiesMap_AmenityID ON VillaAmenitiesMap(AmenityID);
```
