"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Design a database schema for a luxury villa rental service that includes tables for properties, amenities, and customer reviews, reflecting the offerings of Diamond Villa in Corfu.
Generated: DETERMINISTIC_d37a16456d6c00db
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Luxury Villa Rental Service: Diamond Villa in Corfu

-- Table: Properties
-- Stores information about rental properties.
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Name VARCHAR(255) NOT NULL,                -- Name of the property
    Description TEXT,                          -- Detailed description of the property
    Location VARCHAR(255) NOT NULL,            -- Location of the property
    PricePerNight DECIMAL(10, 2) NOT NULL,     -- Cost per night for renting the property
    MaxGuests INT NOT NULL,                    -- Maximum number of guests allowed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table: Amenities
-- Stores amenities available for properties.
CREATE TABLE Amenities (
    AmenityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each amenity
    Name VARCHAR(255) NOT NULL,               -- Name of the amenity (e.g., Swimming Pool, Wi-Fi)
    Description TEXT,                         -- Detailed description of the amenity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the amenity was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table: PropertyAmenities
-- Many-to-Many mapping between Properties and Amenities.
CREATE TABLE PropertyAmenities (
    PropertyID INT NOT NULL,                  -- Foreign key referencing Properties table
    AmenityID INT NOT NULL,                   -- Foreign key referencing Amenities table
    PRIMARY KEY (PropertyID, AmenityID),      -- Composite primary key
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID) ON DELETE CASCADE      -- Cascade delete
);

-- Table: CustomerReviews
-- Stores customer reviews for properties.
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each review
    PropertyID INT NOT NULL,                  -- Foreign key referencing Properties table
    CustomerName VARCHAR(255) NOT NULL,       -- Name of the customer leaving the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1-5 scale)
    Comment TEXT,                             -- Review comment left by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE  -- Cascade delete
);

-- Table: Bookings
-- Stores booking information for properties.
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    PropertyID INT NOT NULL,                  -- Foreign key referencing Properties table
    CustomerName VARCHAR(255) NOT NULL,       -- Name of the customer making the booking
    CheckInDate DATE NOT NULL,                -- Check-in date
    CheckOutDate DATE NOT NULL,               -- Check-out date
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was created
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE  -- Cascade delete
);

-- Additional Notes:
-- 1. Foreign keys ensure relational integrity between tables.
-- 2. Error handling for constraints should be managed by the application interacting with the database.
-- 3. Indexes can be added for better query performance depending on usage patterns.
```
