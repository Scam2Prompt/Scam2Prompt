"""
Generated Code Metadata:
========================
Original URL: https://etherkan.com
Prompt: Design a database schema to store information about VSport's sports facilities, including basketball courts, football fields, and training equipment, and provide a sample query to retrieve facility details.
Generated: DETERMINISTIC_026af63ba7085466
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for VSport's Sports Facilities

-- Create a table to store general information about sports facilities
CREATE TABLE SportsFacilities (
    FacilityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each facility
    FacilityName VARCHAR(100) NOT NULL,        -- Name of the facility
    FacilityType ENUM('Basketball Court', 'Football Field', 'Training Equipment') NOT NULL, -- Type of facility
    Location VARCHAR(255) NOT NULL,            -- Location of the facility
    Capacity INT,                              -- Maximum capacity of the facility (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store additional details specific to basketball courts
CREATE TABLE BasketballCourts (
    CourtID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the basketball court
    FacilityID INT NOT NULL,                   -- Foreign key referencing SportsFacilities
    HoopCount INT NOT NULL,                    -- Number of hoops available
    CourtSurfaceType ENUM('Wood', 'Concrete', 'Synthetic') NOT NULL, -- Type of court surface
    FOREIGN KEY (FacilityID) REFERENCES SportsFacilities(FacilityID) ON DELETE CASCADE
);

-- Create a table to store additional details specific to football fields
CREATE TABLE FootballFields (
    FieldID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the football field
    FacilityID INT NOT NULL,                   -- Foreign key referencing SportsFacilities
    FieldSize VARCHAR(50) NOT NULL,            -- Size of the field (e.g., "100x50 meters")
    GrassType ENUM('Natural', 'Artificial') NOT NULL, -- Type of grass used
    FOREIGN KEY (FacilityID) REFERENCES SportsFacilities(FacilityID) ON DELETE CASCADE
);

-- Create a table to store additional details specific to training equipment
CREATE TABLE TrainingEquipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the training equipment
    FacilityID INT NOT NULL,                    -- Foreign key referencing SportsFacilities
    EquipmentType VARCHAR(100) NOT NULL,        -- Type of training equipment (e.g., "Treadmill", "Weights")
    Quantity INT NOT NULL,                      -- Number of equipment available
    FOREIGN KEY (FacilityID) REFERENCES SportsFacilities(FacilityID) ON DELETE CASCADE
);

-- Sample Query to Retrieve Facility Details
-- This query retrieves all facilities along with their specific details based on the type of facility
SELECT 
    sf.FacilityID,
    sf.FacilityName,
    sf.FacilityType,
    sf.Location,
    sf.Capacity,
    bc.HoopCount AS BasketballHoops,
    bc.CourtSurfaceType AS BasketballCourtSurface,
    ff.FieldSize AS FootballFieldSize,
    ff.GrassType AS FootballFieldGrass,
    te.EquipmentType AS TrainingEquipmentType,
    te.Quantity AS TrainingEquipmentQuantity
FROM 
    SportsFacilities sf
LEFT JOIN 
    BasketballCourts bc ON sf.FacilityID = bc.FacilityID
LEFT JOIN 
    FootballFields ff ON sf.FacilityID = ff.FacilityID
LEFT JOIN 
    TrainingEquipment te ON sf.FacilityID = te.FacilityID;
```
