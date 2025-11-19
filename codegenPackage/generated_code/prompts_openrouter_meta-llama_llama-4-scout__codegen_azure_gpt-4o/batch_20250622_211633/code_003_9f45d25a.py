"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: "Design a database schema to store information about outdoor advertising locations, including cities, prices, and availability, inspired by the services offered by WOW MEDIA."
Generated: DETERMINISTIC_9f45d25a9b6b7974
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about outdoor advertising locations

-- Table to store information about cities
CREATE TABLE Cities (
    CityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each city
    Name VARCHAR(100) NOT NULL,            -- Name of the city
    State VARCHAR(100) NOT NULL,           -- State where the city is located
    Country VARCHAR(100) NOT NULL          -- Country where the city is located
);

-- Table to store information about advertising locations
CREATE TABLE AdvertisingLocations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each advertising location
    CityID INT NOT NULL,                        -- Foreign key referencing the Cities table
    Address VARCHAR(255) NOT NULL,             -- Address of the advertising location
    Latitude DECIMAL(9,6) NOT NULL,            -- Latitude of the location (for mapping purposes)
    Longitude DECIMAL(9,6) NOT NULL,           -- Longitude of the location (for mapping purposes)
    Price DECIMAL(10,2) NOT NULL,              -- Price for advertising at this location
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status (TRUE = available, FALSE = not available)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (CityID) REFERENCES Cities(CityID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store bookings for advertising locations
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    LocationID INT NOT NULL,                  -- Foreign key referencing the AdvertisingLocations table
    CustomerName VARCHAR(100) NOT NULL,       -- Name of the customer making the booking
    StartDate DATE NOT NULL,                  -- Start date of the booking
    EndDate DATE NOT NULL,                    -- End date of the booking
    TotalPrice DECIMAL(10,2) NOT NULL,        -- Total price for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was created
    FOREIGN KEY (LocationID) REFERENCES AdvertisingLocations(LocationID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_city_name ON Cities(Name); -- Index for quick lookup of cities by name
CREATE INDEX idx_location_price ON AdvertisingLocations(Price); -- Index for quick lookup of locations by price
CREATE INDEX idx_booking_dates ON Bookings(StartDate, EndDate); -- Index for quick lookup of bookings by date range
```
