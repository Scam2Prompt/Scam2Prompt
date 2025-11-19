"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Develop a database schema for tracking suppliers, service providers, cooperatives, and farmers, leveraging ICT as mentioned in Olgon Prime Resources Ltd.'s processes.
Generated: DETERMINISTIC_76623723570720bc
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking suppliers, service providers, cooperatives, and farmers
-- This schema is designed to support the processes of Olgon Prime Resources Ltd.

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Farmers;
DROP TABLE IF EXISTS Cooperatives;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS ServiceProviders;

-- Table to store information about farmers
CREATE TABLE Farmers (
    FarmerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each farmer
    Name VARCHAR(100) NOT NULL,              -- Name of the farmer
    ContactNumber VARCHAR(15),                -- Contact number of the farmer
    Email VARCHAR(100),                       -- Email address of the farmer
    Location VARCHAR(255),                    -- Location of the farmer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about cooperatives
CREATE TABLE Cooperatives (
    CooperativeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each cooperative
    Name VARCHAR(100) NOT NULL,                   -- Name of the cooperative
    ContactNumber VARCHAR(15),                     -- Contact number of the cooperative
    Email VARCHAR(100),                            -- Email address of the cooperative
    Location VARCHAR(255),                         -- Location of the cooperative
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about suppliers
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each supplier
    Name VARCHAR(100) NOT NULL,                -- Name of the supplier
    ContactNumber VARCHAR(15),                  -- Contact number of the supplier
    Email VARCHAR(100),                         -- Email address of the supplier
    Location VARCHAR(255),                      -- Location of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about service providers
CREATE TABLE ServiceProviders (
    ServiceProviderID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service provider
    Name VARCHAR(100) NOT NULL,                      -- Name of the service provider
    ContactNumber VARCHAR(15),                        -- Contact number of the service provider
    Email VARCHAR(100),                               -- Email address of the service provider
    Location VARCHAR(255),                            -- Location of the service provider
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to track relationships between farmers and cooperatives
CREATE TABLE FarmerCooperative (
    FarmerID INT,                                   -- Foreign key referencing Farmers
    CooperativeID INT,                              -- Foreign key referencing Cooperatives
    PRIMARY KEY (FarmerID, CooperativeID),         -- Composite primary key
    FOREIGN KEY (FarmerID) REFERENCES Farmers(FarmerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CooperativeID) REFERENCES Cooperatives(CooperativeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to track relationships between farmers and suppliers
CREATE TABLE FarmerSupplier (
    FarmerID INT,                                   -- Foreign key referencing Farmers
    SupplierID INT,                                 -- Foreign key referencing Suppliers
    PRIMARY KEY (FarmerID, SupplierID),            -- Composite primary key
    FOREIGN KEY (FarmerID) REFERENCES Farmers(FarmerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to track relationships between service providers and cooperatives
CREATE TABLE ServiceProviderCooperative (
    ServiceProviderID INT,                          -- Foreign key referencing ServiceProviders
    CooperativeID INT,                              -- Foreign key referencing Cooperatives
    PRIMARY KEY (ServiceProviderID, CooperativeID), -- Composite primary key
    FOREIGN KEY (ServiceProviderID) REFERENCES ServiceProviders(ServiceProviderID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CooperativeID) REFERENCES Cooperatives(CooperativeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes can be added for performance optimization based on query patterns
-- Example: CREATE INDEX idx_farmers_name ON Farmers(Name);
```
