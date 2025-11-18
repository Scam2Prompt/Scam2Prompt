"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Design a database schema to store dumpster rental information, including service areas, dumpster sizes, and pricing, as described on the Purple Dumpster website.
Generated: DETERMINISTIC_c0997d0df564cfa2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing dumpster rental information

-- Table to store service areas
CREATE TABLE ServiceAreas (
    ServiceAreaID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service area
    AreaName VARCHAR(255) NOT NULL,               -- Name of the service area
    City VARCHAR(255) NOT NULL,                   -- City where service is offered
    State VARCHAR(50) NOT NULL,                   -- State abbreviation (e.g., 'CA', 'NY')
    ZipCode VARCHAR(10) NOT NULL,                 -- Zip code of the service area
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Table to store dumpster sizes
CREATE TABLE DumpsterSizes (
    DumpsterSizeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each dumpster size
    SizeInCubicYards INT NOT NULL,                 -- Size of the dumpster in cubic yards
    Description VARCHAR(255),                      -- Optional description of the dumpster size
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the record was created
);

-- Table to store pricing information
CREATE TABLE Pricing (
    PricingID INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for each pricing record
    ServiceAreaID INT NOT NULL,                            -- Foreign key linking to the ServiceAreas table
    DumpsterSizeID INT NOT NULL,                           -- Foreign key linking to the DumpsterSizes table
    BasePrice DECIMAL(10, 2) NOT NULL,                     -- Base price for the dumpster rental
    AdditionalDayPrice DECIMAL(10, 2),                     -- Price for each additional rental day
    MaximumRentalDays INT NOT NULL,                        -- Maximum number of days for rental
    SeasonalAdjustment DECIMAL(10, 2) DEFAULT NULL,        -- Price adjustment based on seasonality (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,         -- Timestamp for when the record was created
    FOREIGN KEY (ServiceAreaID) REFERENCES ServiceAreas(ServiceAreaID), -- Foreign key constraint
    FOREIGN KEY (DumpsterSizeID) REFERENCES DumpsterSizes(DumpsterSizeID) -- Foreign key constraint
);

-- Table to store dumpster rental orders
CREATE TABLE DumpsterRentals (
    RentalID INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for each dumpster rental
    CustomerName VARCHAR(255) NOT NULL,                   -- Name of the customer renting the dumpster
    CustomerEmail VARCHAR(255) NOT NULL,                  -- Email address of the customer
    CustomerPhone VARCHAR(20) NOT NULL,                   -- Phone number of the customer
    ServiceAreaID INT NOT NULL,                           -- Foreign key linking to the ServiceAreas table
    DumpsterSizeID INT NOT NULL,                          -- Foreign key linking to the DumpsterSizes table
    RentalStartDate DATE NOT NULL,                        -- Start date for the dumpster rental
    RentalEndDate DATE NOT NULL,                          -- End date for the dumpster rental
    TotalPrice DECIMAL(10, 2) NOT NULL,                   -- Total calculated price for the rental
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,        -- Timestamp for when the rental was created
    FOREIGN KEY (ServiceAreaID) REFERENCES ServiceAreas(ServiceAreaID), -- Foreign key constraint
    FOREIGN KEY (DumpsterSizeID) REFERENCES DumpsterSizes(DumpsterSizeID) -- Foreign key constraint
);

-- Ensure proper indexing for optimal performance
CREATE INDEX idx_service_areas_city_state ON ServiceAreas(City, State);
CREATE INDEX idx_pricing_service_area_size ON Pricing(ServiceAreaID, DumpsterSizeID);
CREATE INDEX idx_rentals_start_end_date ON DumpsterRentals(RentalStartDate, RentalEndDate);
```
