"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Develop a simple database schema to store customer information, vehicle details, and service records for a windscreen repair and replacement company in Melbourne.
Generated: DETERMINISTIC_c203f5d5db628d84
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a windscreen repair and replacement company

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    City VARCHAR(50) NOT NULL,                 -- City where the customer resides
    State VARCHAR(50) NOT NULL,                -- State where the customer resides
    PostalCode VARCHAR(10),                    -- Postal code of the customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer record was created
);

-- Create a table to store vehicle details
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each vehicle
    CustomerID INT NOT NULL,                   -- Foreign key linking to the Customers table
    Make VARCHAR(50) NOT NULL,                 -- Vehicle's make (e.g., Toyota, Ford)
    Model VARCHAR(50) NOT NULL,                -- Vehicle's model (e.g., Corolla, Focus)
    Year INT NOT NULL,                         -- Year of manufacture
    RegistrationNumber VARCHAR(20) UNIQUE NOT NULL, -- Vehicle's registration number (must be unique)
    VIN VARCHAR(17) UNIQUE,                    -- Vehicle Identification Number (optional, must be unique)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Create a table to store service records
CREATE TABLE ServiceRecords (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service record
    VehicleID INT NOT NULL,                    -- Foreign key linking to the Vehicles table
    ServiceDate DATE NOT NULL,                 -- Date the service was performed
    ServiceType ENUM('Repair', 'Replacement') NOT NULL, -- Type of service performed
    Description TEXT,                          -- Detailed description of the service
    Cost DECIMAL(10, 2) NOT NULL,              -- Cost of the service
    TechnicianName VARCHAR(100),              -- Name of the technician who performed the service
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE -- Cascade delete if vehicle is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_vehicle_registration ON Vehicles(RegistrationNumber); -- Index for quick lookup by registration number
CREATE INDEX idx_service_date ON ServiceRecords(ServiceDate); -- Index for quick lookup by service date
```
