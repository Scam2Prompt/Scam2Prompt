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
-- SQL Database Schema for Inmobiliaria Nueva Ciudad

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Renters;
DROP TABLE IF EXISTS Owners;
DROP TABLE IF EXISTS Properties;

-- Table to store information about property owners
CREATE TABLE Owners (
    OwnerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each owner
    FirstName VARCHAR(50) NOT NULL,          -- Owner's first name
    LastName VARCHAR(50) NOT NULL,           -- Owner's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Owner's email address (must be unique)
    PhoneNumber VARCHAR(15),                  -- Owner's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about renters
CREATE TABLE Renters (
    RenterID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each renter
    FirstName VARCHAR(50) NOT NULL,           -- Renter's first name
    LastName VARCHAR(50) NOT NULL,            -- Renter's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Renter's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Renter's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about properties
CREATE TABLE Properties (
    PropertyID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each property
    OwnerID INT NOT NULL,                       -- Foreign key referencing the owner
    Address VARCHAR(255) NOT NULL,             -- Property address
    City VARCHAR(100) NOT NULL,                 -- City where the property is located
    State VARCHAR(100) NOT NULL,                -- State where the property is located
    ZipCode VARCHAR(10) NOT NULL,              -- Zip code of the property
    RentAmount DECIMAL(10, 2) NOT NULL,        -- Monthly rent amount
    Status ENUM('Available', 'Rented', 'Under Maintenance') DEFAULT 'Available',  -- Current status of the property
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID) ON DELETE CASCADE  -- Foreign key constraint
);

-- Table to manage rental agreements between properties and renters
CREATE TABLE RentalAgreements (
    AgreementID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each rental agreement
    PropertyID INT NOT NULL,                     -- Foreign key referencing the property
    RenterID INT NOT NULL,                       -- Foreign key referencing the renter
    StartDate DATE NOT NULL,                     -- Start date of the rental agreement
    EndDate DATE NOT NULL,                       -- End date of the rental agreement
    MonthlyRent DECIMAL(10, 2) NOT NULL,        -- Monthly rent amount agreed upon
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE,  -- Foreign key constraint
    FOREIGN KEY (RenterID) REFERENCES Renters(RenterID) ON DELETE CASCADE  -- Foreign key constraint
);
```
