"""
Generated Code Metadata:
========================
Original URL: https://dunhill-servicedapartments.com
Prompt: Design a simple database schema using SQL to store information about serviced apartments, including apartment details, locations, and booking status, inspired by the types of data presented on the Dunhill Serviced and Furnished Apartments website.
Generated: DETERMINISTIC_84aa6bd6e59a47ef
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing serviced apartment information

-- Table to store apartment details
CREATE TABLE Apartments (
    ApartmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each apartment
    Name VARCHAR(255) NOT NULL,                 -- Name of the apartment
    Description TEXT,                           -- Description of the apartment
    NumberOfRooms INT NOT NULL,                 -- Number of rooms in the apartment
    PricePerNight DECIMAL(10, 2) NOT NULL,      -- Price per night for the apartment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store location details
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    City VARCHAR(100) NOT NULL,                -- City where the apartment is located
    State VARCHAR(100),                        -- State where the apartment is located
    Country VARCHAR(100) NOT NULL,             -- Country where the apartment is located
    PostalCode VARCHAR(20),                    -- Postal code of the location
    AddressLine1 VARCHAR(255) NOT NULL,        -- First line of the address
    AddressLine2 VARCHAR(255),                 -- Second line of the address (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store booking status
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each booking
    ApartmentID INT NOT NULL,                  -- Foreign key referencing Apartments table
    CustomerName VARCHAR(255) NOT NULL,        -- Name of the customer who made the booking
    CustomerEmail VARCHAR(255) NOT NULL,       -- Email of the customer
    CheckInDate DATE NOT NULL,                 -- Check-in date for the booking
    CheckOutDate DATE NOT NULL,                -- Check-out date for the booking
    BookingStatus ENUM('Pending', 'Confirmed', 'Cancelled') NOT NULL, -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (ApartmentID) REFERENCES Apartments(ApartmentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to associate apartments with locations
CREATE TABLE ApartmentLocations (
    ApartmentLocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    ApartmentID INT NOT NULL,                           -- Foreign key referencing Apartments table
    LocationID INT NOT NULL,                            -- Foreign key referencing Locations table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (ApartmentID) REFERENCES Apartments(ApartmentID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_apartment_name ON Apartments(Name);
CREATE INDEX idx_location_city ON Locations(City);
CREATE INDEX idx_booking_status ON Bookings(BookingStatus);
```
