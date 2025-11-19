"""
Generated Code Metadata:
========================
Original URL: https://arrendamosjv.com
Prompt: Design a database schema to store information about properties, clients, and rental contracts for a real estate company like Arrendamos J V SAS, using a relational database management system like MySQL.
Generated: DETERMINISTIC_6a4e0a979adc9345
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Real Estate Company: Arrendamos J V SAS

-- Create a database
CREATE DATABASE RealEstateCompany;
USE RealEstateCompany;

-- Table to store information about properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Address VARCHAR(255) NOT NULL,             -- Full address of the property
    City VARCHAR(100) NOT NULL,                -- City where the property is located
    State VARCHAR(100) NOT NULL,               -- State where the property is located
    ZipCode VARCHAR(20) NOT NULL,              -- Zip code of the property
    Type ENUM('Apartment', 'House', 'Commercial', 'Land') NOT NULL, -- Type of property
    Bedrooms INT NOT NULL,                     -- Number of bedrooms
    Bathrooms INT NOT NULL,                    -- Number of bathrooms
    SquareFeet INT NOT NULL,                   -- Size of the property in square feet
    RentPrice DECIMAL(10, 2) NOT NULL,         -- Monthly rent price
    AvailabilityStatus ENUM('Available', 'Rented') NOT NULL DEFAULT 'Available', -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,           -- First name of the client
    LastName VARCHAR(100) NOT NULL,            -- Last name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the client
    PhoneNumber VARCHAR(20) NOT NULL,          -- Phone number of the client
    Address VARCHAR(255),                      -- Address of the client
    City VARCHAR(100),                         -- City of the client
    State VARCHAR(100),                        -- State of the client
    ZipCode VARCHAR(20),                       -- Zip code of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table to store information about rental contracts
CREATE TABLE RentalContracts (
    ContractID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each contract
    PropertyID INT NOT NULL,                   -- Foreign key referencing Properties table
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    StartDate DATE NOT NULL,                   -- Start date of the rental contract
    EndDate DATE NOT NULL,                     -- End date of the rental contract
    MonthlyRent DECIMAL(10, 2) NOT NULL,       -- Monthly rent amount
    SecurityDeposit DECIMAL(10, 2) NOT NULL,   -- Security deposit amount
    PaymentStatus ENUM('Paid', 'Pending', 'Overdue') NOT NULL DEFAULT 'Pending', -- Payment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the contract was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimization
CREATE INDEX idx_properties_city ON Properties (City);
CREATE INDEX idx_clients_email ON Clients (Email);
CREATE INDEX idx_rentalcontracts_paymentstatus ON RentalContracts (PaymentStatus);

-- Error handling: Ensure foreign key constraints are enforced
SET FOREIGN_KEY_CHECKS = 1;
```
