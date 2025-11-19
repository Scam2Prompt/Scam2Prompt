"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: "Design a simple database schema for managing condominium properties, including details like unit numbers, amenities, and owner information, as seen on residencialviladagraca.com.br."
Generated: DETERMINISTIC_7bc0cb2695bb69ec
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Managing Condominium Properties

-- Table to store information about condominium units
CREATE TABLE CondominiumUnits (
    UnitID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each unit
    UnitNumber VARCHAR(10) NOT NULL,       -- Unit number (e.g., "101", "A2")
    Floor INT NOT NULL,                    -- Floor number where the unit is located
    SquareFootage DECIMAL(10, 2) NOT NULL, -- Size of the unit in square feet
    NumberOfBedrooms INT NOT NULL,         -- Number of bedrooms in the unit
    NumberOfBathrooms INT NOT NULL,        -- Number of bathrooms in the unit
    OwnerID INT,                           -- Foreign key to the Owners table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about unit owners
CREATE TABLE Owners (
    OwnerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each owner
    FirstName VARCHAR(50) NOT NULL,         -- Owner's first name
    LastName VARCHAR(50) NOT NULL,          -- Owner's last name
    Email VARCHAR(100) NOT NULL UNIQUE,     -- Owner's email address
    PhoneNumber VARCHAR(15),                -- Owner's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about amenities available in the condominium
CREATE TABLE Amenities (
    AmenityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each amenity
    AmenityName VARCHAR(100) NOT NULL,        -- Name of the amenity (e.g., "Swimming Pool", "Gym")
    Description TEXT,                         -- Description of the amenity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store the relationship between units and amenities
CREATE TABLE UnitAmenities (
    UnitAmenityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    UnitID INT NOT NULL,                          -- Foreign key to the CondominiumUnits table
    AmenityID INT NOT NULL,                       -- Foreign key to the Amenities table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (UnitID) REFERENCES CondominiumUnits(UnitID) ON DELETE CASCADE,
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID) ON DELETE CASCADE
);

-- Add indexes for faster lookups
CREATE INDEX idx_unit_number ON CondominiumUnits(UnitNumber);
CREATE INDEX idx_owner_email ON Owners(Email);
CREATE INDEX idx_amenity_name ON Amenities(AmenityName);
```
