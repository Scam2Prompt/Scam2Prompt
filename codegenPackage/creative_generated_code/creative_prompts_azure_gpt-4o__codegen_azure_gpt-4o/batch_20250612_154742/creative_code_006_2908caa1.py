"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Design a database schema in SQL to store information about tour packages, taxi services, and customer bookings based on the offerings listed on the "Best Holidays All India" website.
Generated: DETERMINISTIC_2908caa1111a71ab
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for "Best Holidays All India"

-- Table to store information about tour packages
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each tour package
    PackageName VARCHAR(255) NOT NULL,         -- Name of the tour package
    Destination VARCHAR(255) NOT NULL,         -- Destination of the tour package
    DurationDays INT NOT NULL,                 -- Duration of the package in days
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the tour package
    Description TEXT,                          -- Description of the tour package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the package was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about taxi services
CREATE TABLE TaxiServices (
    TaxiServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each taxi service
    ServiceName VARCHAR(255) NOT NULL,            -- Name of the taxi service
    ServiceType ENUM('AC', 'Non-AC', 'Luxury') NOT NULL, -- Type of the taxi service
    PricePerKm DECIMAL(10, 2) NOT NULL,           -- Cost per kilometer
    AvailableFrom TIME NOT NULL,                  -- Service availability start time
    AvailableTo TIME NOT NULL,                    -- Service availability end time
    Description TEXT,                             -- Description of the taxi service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about customer bookings
CREATE TABLE CustomerBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each booking
    CustomerName VARCHAR(255) NOT NULL,        -- Name of the customer
    CustomerEmail VARCHAR(255) NOT NULL,       -- Email of the customer
    CustomerPhone VARCHAR(15) NOT NULL,        -- Phone number of the customer
    BookingType ENUM('TourPackage', 'TaxiService') NOT NULL, -- Type of booking (tour package or taxi service)
    ReferenceID INT NOT NULL,                  -- Foreign key ID; points to TourPackages.PackageID or TaxiServices.TaxiServiceID
    BookingDate DATE NOT NULL,                 -- Date when the booking was made
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount charged for the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ReferenceID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE, -- Foreign key to TourPackages
    FOREIGN KEY (ReferenceID) REFERENCES TaxiServices(TaxiServiceID) ON DELETE CASCADE -- Foreign key to TaxiServices
);

-- Indexes for better query performance
CREATE INDEX idx_booking_type ON CustomerBookings (BookingType);
CREATE INDEX idx_customer_email ON CustomerBookings (CustomerEmail);

-- Constraints
ALTER TABLE CustomerBookings ADD CONSTRAINT chk_booking_type_reference CHECK (
    (BookingType = 'TourPackage' AND EXISTS (SELECT 1 FROM TourPackages WHERE PackageID = ReferenceID)) OR
    (BookingType = 'TaxiService' AND EXISTS (SELECT 1 FROM TaxiServices WHERE TaxiServiceID = ReferenceID))
);

-- End of schema definition.
```
