"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laotaigroup.com
Prompt: Develop a database schema for managing real estate assets and rental services, inspired by the operations of Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_1be63a220719483b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing real estate assets and rental services for Lao Tai Trading - Investment Group

-- Create a database
CREATE DATABASE RealEstateManagement;

-- Use the created database
USE RealEstateManagement;

-- Table to store information about properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each property
    PropertyName VARCHAR(255) NOT NULL,         -- Name of the property
    PropertyType ENUM('Residential', 'Commercial', 'Industrial', 'Land') NOT NULL,  -- Type of property
    Address VARCHAR(255) NOT NULL,               -- Address of the property
    City VARCHAR(100) NOT NULL,                  -- City where the property is located
    State VARCHAR(100) NOT NULL,                 -- State where the property is located
    ZipCode VARCHAR(10) NOT NULL,                -- Zip code of the property location
    Price DECIMAL(15, 2) NOT NULL,               -- Price of the property
    Status ENUM('Available', 'Rented', 'Under Maintenance') DEFAULT 'Available', -- Current status of the property
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store tenant information
CREATE TABLE Tenants (
    TenantID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each tenant
    FirstName VARCHAR(100) NOT NULL,             -- Tenant's first name
    LastName VARCHAR(100) NOT NULL,              -- Tenant's last name
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Tenant's email address
    Phone VARCHAR(15) NOT NULL,                  -- Tenant's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the tenant was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to manage rental agreements
CREATE TABLE Rentals (
    RentalID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each rental agreement
    TenantID INT NOT NULL,                        -- Foreign key referencing the tenant
    PropertyID INT NOT NULL,                      -- Foreign key referencing the property
    StartDate DATE NOT NULL,                      -- Start date of the rental agreement
    EndDate DATE NOT NULL,                        -- End date of the rental agreement
    MonthlyRent DECIMAL(15, 2) NOT NULL,         -- Monthly rent amount
    SecurityDeposit DECIMAL(15, 2) NOT NULL,     -- Security deposit amount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the rental agreement was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID) ON DELETE CASCADE, -- Cascading delete on tenant removal
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascading delete on property removal
);

-- Table to store maintenance requests
CREATE TABLE MaintenanceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each maintenance request
    PropertyID INT NOT NULL,                      -- Foreign key referencing the property
    Description TEXT NOT NULL,                    -- Description of the maintenance issue
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the request was made
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Current status of the request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the request was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascading delete on property removal
);

-- Table to store payment records
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each payment record
    RentalID INT NOT NULL,                         -- Foreign key referencing the rental agreement
    Amount DECIMAL(15, 2) NOT NULL,               -- Amount of payment
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the payment was made
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the payment record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID) ON DELETE CASCADE -- Cascading delete on rental removal
);
```
