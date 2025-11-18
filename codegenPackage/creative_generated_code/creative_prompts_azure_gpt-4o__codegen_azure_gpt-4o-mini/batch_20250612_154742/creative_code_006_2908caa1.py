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
-- Create a schema for storing tour packages, taxi services, and customer bookings

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CustomerBookings;
DROP TABLE IF EXISTS TaxiServices;
DROP TABLE IF EXISTS TourPackages;

-- Create a table to store information about tour packages
CREATE TABLE TourPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each tour package
    PackageName VARCHAR(255) NOT NULL,       -- Name of the tour package
    Description TEXT NOT NULL,                -- Detailed description of the package
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the tour package
    Duration VARCHAR(50) NOT NULL,           -- Duration of the tour (e.g., '3 days', '1 week')
    Availability BOOLEAN DEFAULT TRUE,        -- Indicates if the package is available for bookings
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table to store information about taxi services
CREATE TABLE TaxiServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each taxi service
    ServiceName VARCHAR(255) NOT NULL,         -- Name of the taxi service provider
    VehicleType VARCHAR(100) NOT NULL,         -- Type of vehicle (e.g., 'Sedan', 'SUV')
    RatePerKm DECIMAL(10, 2) NOT NULL,         -- Rate charged per kilometer
    Availability BOOLEAN DEFAULT TRUE,          -- Indicates if the service is available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the service was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table to store customer bookings for tour packages and taxi services
CREATE TABLE CustomerBookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each booking
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer
    CustomerEmail VARCHAR(255) NOT NULL,          -- Email of the customer for contact
    CustomerPhone VARCHAR(15) NOT NULL,           -- Phone number of the customer
    PackageID INT,                                 -- The tour package being booked
    ServiceID INT,                                 -- The taxi service being booked
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the booking
    NumberOfPersons INT NOT NULL,                 -- Number of persons booked for the tour
    TotalCost DECIMAL(10, 2) NOT NULL,           -- Total cost of the booking
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE SET NULL, -- Foreign key reference to TourPackages
    FOREIGN KEY (ServiceID) REFERENCES TaxiServices(ServiceID) ON DELETE SET NULL  -- Foreign key reference to TaxiServices
);

-- Add appropriate indexes to improve query performance
CREATE INDEX idx_package_name ON TourPackages(PackageName);
CREATE INDEX idx_service_name ON TaxiServices(ServiceName);
CREATE INDEX idx_customer_email ON CustomerBookings(CustomerEmail);
```
