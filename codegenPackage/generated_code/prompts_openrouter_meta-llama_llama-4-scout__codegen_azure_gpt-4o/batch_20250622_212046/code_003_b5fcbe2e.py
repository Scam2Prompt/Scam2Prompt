"""
Generated Code Metadata:
========================
Original URL: https://viamare.com.gr
Prompt: "Design a database schema to store information about yacht charter services, VIP concierge services, and travel arrangements for a company like Viamare Yachting."
Generated: DETERMINISTIC_b5fcbe2ef7ec3bd7
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for yacht charter services, VIP concierge services, and travel arrangements

-- Table to store information about yachts available for charter
CREATE TABLE Yachts (
    YachtID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each yacht
    Name VARCHAR(100) NOT NULL,             -- Name of the yacht
    Type VARCHAR(50),                       -- Type of yacht (e.g., motor, sailing)
    Length DECIMAL(5,2),                    -- Length of the yacht in meters
    Capacity INT,                           -- Maximum number of guests
    PricePerDay DECIMAL(10,2) NOT NULL,     -- Daily charter price
    Description TEXT,                       -- Description of the yacht
    AvailabilityStatus ENUM('Available', 'Booked', 'Maintenance') DEFAULT 'Available', -- Current status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about VIP concierge services
CREATE TABLE ConciergeServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(100) NOT NULL,               -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10,2) NOT NULL,             -- Price of the service
    Availability ENUM('Available', 'Unavailable') DEFAULT 'Available', -- Service availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about travel arrangements
CREATE TABLE TravelArrangements (
    ArrangementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each arrangement
    ClientName VARCHAR(100) NOT NULL,             -- Name of the client
    ContactInfo VARCHAR(255) NOT NULL,            -- Contact information (email, phone, etc.)
    Destination VARCHAR(100) NOT NULL,            -- Travel destination
    StartDate DATE NOT NULL,                      -- Start date of the travel
    EndDate DATE NOT NULL,                        -- End date of the travel
    TransportationMode ENUM('Air', 'Sea', 'Land'), -- Mode of transportation
    SpecialRequests TEXT,                         -- Any special requests from the client
    TotalCost DECIMAL(10,2) NOT NULL,             -- Total cost of the arrangement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store bookings for yacht charters
CREATE TABLE YachtBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    YachtID INT NOT NULL,                     -- Foreign key referencing Yachts table
    ClientName VARCHAR(100) NOT NULL,         -- Name of the client
    ContactInfo VARCHAR(255) NOT NULL,        -- Contact information (email, phone, etc.)
    StartDate DATE NOT NULL,                  -- Start date of the charter
    EndDate DATE NOT NULL,                    -- End date of the charter
    TotalCost DECIMAL(10,2) NOT NULL,         -- Total cost of the booking
    Status ENUM('Confirmed', 'Pending', 'Cancelled') DEFAULT 'Pending', -- Booking status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (YachtID) REFERENCES Yachts(YachtID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store bookings for VIP concierge services
CREATE TABLE ConciergeBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    ServiceID INT NOT NULL,                   -- Foreign key referencing ConciergeServices table
    ClientName VARCHAR(100) NOT NULL,         -- Name of the client
    ContactInfo VARCHAR(255) NOT NULL,        -- Contact information (email, phone, etc.)
    BookingDate DATE NOT NULL,                -- Date of the booking
    TotalCost DECIMAL(10,2) NOT NULL,         -- Total cost of the booking
    Status ENUM('Confirmed', 'Pending', 'Cancelled') DEFAULT 'Pending', -- Booking status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ServiceID) REFERENCES ConciergeServices(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store bookings for travel arrangements
CREATE TABLE TravelBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    ArrangementID INT NOT NULL,               -- Foreign key referencing TravelArrangements table
    ClientName VARCHAR(100) NOT NULL,         -- Name of the client
    ContactInfo VARCHAR(255) NOT NULL,        -- Contact information (email, phone, etc.)
    BookingDate DATE NOT NULL,                -- Date of the booking
    TotalCost DECIMAL(10,2) NOT NULL,         -- Total cost of the booking
    Status ENUM('Confirmed', 'Pending', 'Cancelled') DEFAULT 'Pending', -- Booking status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ArrangementID) REFERENCES TravelArrangements(ArrangementID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_yacht_name ON Yachts(Name);
CREATE INDEX idx_service_name ON ConciergeServices(Name);
CREATE INDEX idx_destination ON TravelArrangements(Destination);
CREATE INDEX idx_booking_status ON YachtBookings(Status);
CREATE INDEX idx_booking_status_concierge ON ConciergeBookings(Status);
CREATE INDEX idx_booking_status_travel ON TravelBookings(Status);
```
