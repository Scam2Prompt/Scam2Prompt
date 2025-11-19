"""
Generated Code Metadata:
========================
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Design a database schema for a luxury villa rental service that includes tables for properties, amenities, and customer reviews, reflecting the offerings of Diamond Villa in Corfu.
Generated: DETERMINISTIC_d37a16456d6c00db
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a luxury villa rental service

-- Table: Properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Name VARCHAR(255) NOT NULL,                -- Name of the property
    Location VARCHAR(255) NOT NULL,            -- Location of the property
    Description TEXT,                          -- Detailed description of the property
    PricePerNight DECIMAL(10, 2) NOT NULL,     -- Price per night for renting the property
    MaxGuests INT NOT NULL,                    -- Maximum number of guests allowed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Amenities
CREATE TABLE Amenities (
    AmenityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each amenity
    Name VARCHAR(255) NOT NULL,               -- Name of the amenity (e.g., Pool, WiFi, Air Conditioning)
    Description TEXT                          -- Detailed description of the amenity
);

-- Table: PropertyAmenities (Many-to-Many relationship between Properties and Amenities)
CREATE TABLE PropertyAmenities (
    PropertyID INT NOT NULL,                  -- Foreign key referencing Properties table
    AmenityID INT NOT NULL,                   -- Foreign key referencing Amenities table
    PRIMARY KEY (PropertyID, AmenityID),      -- Composite primary key
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID) ON DELETE CASCADE     -- Cascade delete
);

-- Table: CustomerReviews
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each review
    PropertyID INT NOT NULL,                  -- Foreign key referencing Properties table
    CustomerName VARCHAR(255) NOT NULL,       -- Name of the customer leaving the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),-- Rating given by the customer (1-5 scale)
    ReviewText TEXT,                          -- Detailed review text
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for performance optimization
CREATE INDEX idx_properties_location ON Properties(Location); -- Index for searching properties by location
CREATE INDEX idx_reviews_property ON CustomerReviews(PropertyID); -- Index for fetching reviews by property
```
