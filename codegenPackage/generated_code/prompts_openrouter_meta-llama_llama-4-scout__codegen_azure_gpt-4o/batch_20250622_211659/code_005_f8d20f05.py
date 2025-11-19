"""
Generated Code Metadata:
========================
Original URL: https://piscorealestate.com
Prompt: "Create a SQL database schema to store information about properties, including features like price, location, number of bedrooms, and amenities."
Generated: DETERMINISTIC_f8d20f05efd80fc0
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema to store information about properties

-- Create a table to store property details
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Name VARCHAR(255) NOT NULL,                -- Name or title of the property
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the property
    Location VARCHAR(255) NOT NULL,            -- Location of the property
    Bedrooms INT NOT NULL,                     -- Number of bedrooms in the property
    Bathrooms INT NOT NULL,                    -- Number of bathrooms in the property
    SquareFeet INT,                            -- Size of the property in square feet
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create a table to store amenities associated with properties
CREATE TABLE Amenities (
    AmenityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each amenity
    Name VARCHAR(255) NOT NULL UNIQUE         -- Name of the amenity (e.g., "Pool", "Gym", "WiFi")
);

-- Create a junction table to associate properties with amenities (many-to-many relationship)
CREATE TABLE PropertyAmenities (
    PropertyID INT NOT NULL,                  -- Foreign key referencing Properties table
    AmenityID INT NOT NULL,                   -- Foreign key referencing Amenities table
    PRIMARY KEY (PropertyID, AmenityID),      -- Composite primary key to ensure uniqueness
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID) ON DELETE CASCADE     -- Cascade delete
);

-- Create indexes for faster querying
CREATE INDEX idx_properties_location ON Properties(Location); -- Index for location-based queries
CREATE INDEX idx_properties_price ON Properties(Price);       -- Index for price-based queries
CREATE INDEX idx_properties_bedrooms ON Properties(Bedrooms); -- Index for bedroom-based queries
```
