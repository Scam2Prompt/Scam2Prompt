"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Develop a simple database schema to manage refrigerated vehicle rentals, customer information, and delivery records for a company like Refrigerator Transport in Dubai.
Generated: DETERMINISTIC_0e675601d1fd6e27
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing refrigerated vehicle rentals, customer information, and delivery records

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(100) NOT NULL,            -- Customer's full name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15) NOT NULL,          -- Customer's phone number
    Address TEXT NOT NULL,                     -- Customer's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer record was created
);

-- Create a table to store refrigerated vehicle information
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each vehicle
    LicensePlate VARCHAR(20) NOT NULL UNIQUE,  -- Vehicle's license plate number (must be unique)
    Model VARCHAR(50) NOT NULL,                -- Vehicle model
    CapacityInCubicMeters DECIMAL(10, 2) NOT NULL, -- Vehicle's storage capacity in cubic meters
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status of the vehicle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the vehicle record was created
);

-- Create a table to store rental information
CREATE TABLE Rentals (
    RentalID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each rental
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    VehicleID INT NOT NULL,                    -- Foreign key referencing Vehicles table
    RentalStartDate DATE NOT NULL,             -- Start date of the rental
    RentalEndDate DATE NOT NULL,               -- End date of the rental
    TotalCost DECIMAL(10, 2) NOT NULL,         -- Total cost of the rental
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the rental record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE SET NULL    -- Set vehicle to NULL if removed
);

-- Create a table to store delivery records
CREATE TABLE Deliveries (
    DeliveryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each delivery
    RentalID INT NOT NULL,                     -- Foreign key referencing Rentals table
    DeliveryDate DATE NOT NULL,                -- Date of the delivery
    DeliveryAddress TEXT NOT NULL,             -- Address where the delivery is made
    DeliveryStatus ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the delivery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the delivery record was created
    FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID) ON DELETE CASCADE -- Cascade delete if rental is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup of customers by email
CREATE INDEX idx_vehicle_availability ON Vehicles(IsAvailable); -- Index for quick lookup of available vehicles
CREATE INDEX idx_rental_dates ON Rentals(RentalStartDate, RentalEndDate); -- Index for querying rentals by date range
CREATE INDEX idx_delivery_status ON Deliveries(DeliveryStatus); -- Index for querying deliveries by status
```
