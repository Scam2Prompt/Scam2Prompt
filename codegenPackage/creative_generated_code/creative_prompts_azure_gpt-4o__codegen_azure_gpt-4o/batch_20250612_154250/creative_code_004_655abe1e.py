"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://denshaven.com
Prompt: Create a database schema using SQL to store details about the 22 villas in the Dens Haven project, including size (3000-4500 sq.ft), number of bedrooms, and amenities.
Generated: DETERMINISTIC_655abe1e72a4ba3d
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing information about villas in the Dens Haven project.
-- This schema includes details about villa size, number of bedrooms, and amenities.

-- Create the main table to store villa information
CREATE TABLE Villas (
    VillaID INT PRIMARY KEY AUTO_INCREMENT,            -- Unique identifier for each villa
    Name VARCHAR(100) NOT NULL,                        -- Name of the villa
    SizeSqFt INT CHECK(SizeSqFt BETWEEN 3000 AND 4500), -- Size of the villa in square feet (3000-4500 sq.ft)
    NumBedrooms INT CHECK(NumBedrooms > 0),            -- Number of bedrooms in the villa (must be > 0)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when the villa record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the villa record was last updated
);

-- Create a table to store villa amenities
CREATE TABLE Amenities (
    AmenityID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each amenity
    AmenityName VARCHAR(100) NOT NULL,                 -- Name of the amenity (e.g., Pool, Gym, Garden)
    Description TEXT                                   -- Description of the amenity
);

-- Create a junction table to associate villas with multiple amenities
CREATE TABLE VillaAmenities (
    VillaID INT NOT NULL,                              -- Reference to the Villa ID
    AmenityID INT NOT NULL,                            -- Reference to the Amenity ID
    PRIMARY KEY (VillaID, AmenityID),                  -- Composite primary key ensures uniqueness per villa-amenity pair
    FOREIGN KEY (VillaID) REFERENCES Villas(VillaID) ON DELETE CASCADE, -- Cascade deletions for villas
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID) ON DELETE CASCADE -- Cascade deletions for amenities
);

-- Insert sample data into Villas table (optional; remove in production if unnecessary)
INSERT INTO Villas (Name, SizeSqFt, NumBedrooms)
VALUES 
('Villa A', 3200, 4),
('Villa B', 4500, 5),
('Villa C', 3700, 3),
('Villa D', 3000, 4),
('Villa E', 4200, 5);

-- Insert sample data into Amenities table (optional; remove in production if unnecessary)
INSERT INTO Amenities (AmenityName, Description)
VALUES 
('Swimming Pool', 'A large private pool available for residents.'),
('Gym', 'A fully equipped fitness center.'),
('Garden', 'A lush landscaped garden.'),
('Play Area', 'A safe play area for children.');

-- Sample associations between Villas and Amenities (optional; remove in production if unnecessary)
INSERT INTO VillaAmenities (VillaID, AmenityID)
VALUES 
(1, 1), -- Villa A has a Swimming Pool
(1, 2), -- Villa A has access to Gym
(2, 1), -- Villa B has a Swimming Pool
(2, 3), -- Villa B has a Garden
(3, 4), -- Villa C has a Play Area
(4, 3), -- Villa D has a Garden
(5, 2), -- Villa E has access to Gym
(5, 1); -- Villa E has a Swimming Pool
```
