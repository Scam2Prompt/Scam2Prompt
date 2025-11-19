"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Create a SQL database schema for storing information about properties, owners, and renters, as used by Inmobiliaria Nueva Ciudad for their property management services.
Generated: DETERMINISTIC_bbb0e7245f33bf0f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Property Management System
-- Database: InmobiliariaNuevaCiudad

-- Create the database
CREATE DATABASE InmobiliariaNuevaCiudad;

-- Use the database
USE InmobiliariaNuevaCiudad;

-- Table: Owners
CREATE TABLE Owners (
    OwnerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each owner
    FirstName VARCHAR(50) NOT NULL,         -- Owner's first name
    LastName VARCHAR(50) NOT NULL,          -- Owner's last name
    Email VARCHAR(100) UNIQUE NOT NULL,     -- Owner's email address
    PhoneNumber VARCHAR(15),                -- Owner's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table: Properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    OwnerID INT NOT NULL,                      -- Foreign key referencing Owners table
    Address VARCHAR(255) NOT NULL,             -- Property address
    City VARCHAR(100) NOT NULL,                -- City where the property is located
    State VARCHAR(100) NOT NULL,               -- State where the property is located
    ZipCode VARCHAR(10) NOT NULL,              -- Zip code of the property
    PropertyType ENUM('Apartment', 'House', 'Condo', 'Commercial') NOT NULL, -- Type of property
    NumberOfRooms INT NOT NULL,                -- Number of rooms in the property
    RentPrice DECIMAL(10, 2) NOT NULL,         -- Monthly rent price
    IsAvailable BOOLEAN DEFAULT TRUE,         -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID) ON DELETE CASCADE -- Cascade delete if owner is removed
);

-- Table: Renters
CREATE TABLE Renters (
    RenterID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each renter
    FirstName VARCHAR(50) NOT NULL,          -- Renter's first name
    LastName VARCHAR(50) NOT NULL,           -- Renter's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Renter's email address
    PhoneNumber VARCHAR(15),                 -- Renter's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table: Rentals
CREATE TABLE Rentals (
    RentalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each rental
    PropertyID INT NOT NULL,                 -- Foreign key referencing Properties table
    RenterID INT NOT NULL,                   -- Foreign key referencing Renters table
    StartDate DATE NOT NULL,                 -- Rental start date
    EndDate DATE,                            -- Rental end date (nullable for ongoing rentals)
    MonthlyRent DECIMAL(10, 2) NOT NULL,     -- Monthly rent amount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete if property is removed
    FOREIGN KEY (RenterID) REFERENCES Renters(RenterID) ON DELETE CASCADE -- Cascade delete if renter is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_owner_email ON Owners(Email);
CREATE INDEX idx_property_address ON Properties(Address);
CREATE INDEX idx_renter_email ON Renters(Email);

-- End of schema definition
```
