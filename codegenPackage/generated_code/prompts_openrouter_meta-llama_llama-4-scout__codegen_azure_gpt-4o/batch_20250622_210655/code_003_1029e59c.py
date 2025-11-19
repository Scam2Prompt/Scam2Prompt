"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: "Design a database schema for a real estate platform that includes tables for properties (with types like apartments, houses, offices), locations (cities, neighborhoods), and property features (number of bedrooms, bathrooms, parking spots), considering the services offered by Inmobiliaria Félix Trujillo Falla."
Generated: DETERMINISTIC_1029e59c48086193
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Real Estate Platform

-- Table: Locations
-- Stores information about cities and neighborhoods
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    City VARCHAR(100) NOT NULL,                -- Name of the city
    Neighborhood VARCHAR(100),                 -- Name of the neighborhood (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: PropertyTypes
-- Stores different types of properties (e.g., apartments, houses, offices)
CREATE TABLE PropertyTypes (
    PropertyTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property type
    TypeName VARCHAR(50) NOT NULL UNIQUE,          -- Name of the property type
    Description TEXT,                              -- Optional description of the property type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: Properties
-- Stores information about individual properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Title VARCHAR(255) NOT NULL,               -- Title or name of the property
    Description TEXT,                          -- Detailed description of the property
    Price DECIMAL(15, 2) NOT NULL,             -- Price of the property
    LocationID INT NOT NULL,                   -- Foreign key referencing Locations table
    PropertyTypeID INT NOT NULL,               -- Foreign key referencing PropertyTypes table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE, -- Cascade delete for location
    FOREIGN KEY (PropertyTypeID) REFERENCES PropertyTypes(PropertyTypeID) ON DELETE CASCADE -- Cascade delete for property type
);

-- Table: PropertyFeatures
-- Stores features of properties (e.g., number of bedrooms, bathrooms, parking spots)
CREATE TABLE PropertyFeatures (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feature
    PropertyID INT NOT NULL,                  -- Foreign key referencing Properties table
    Bedrooms INT DEFAULT 0,                   -- Number of bedrooms
    Bathrooms INT DEFAULT 0,                  -- Number of bathrooms
    ParkingSpots INT DEFAULT 0,               -- Number of parking spots
    SquareFootage DECIMAL(10, 2),             -- Size of the property in square footage
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascade delete for property
);

-- Table: Services
-- Stores services offered by the real estate agency
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL UNIQUE, -- Name of the service
    Description TEXT,                         -- Optional description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: PropertyServices
-- Maps properties to services offered
CREATE TABLE PropertyServices (
    PropertyServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each mapping
    PropertyID INT NOT NULL,                          -- Foreign key referencing Properties table
    ServiceID INT NOT NULL,                           -- Foreign key referencing Services table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for record creation
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete for property
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete for service
);

-- Indexes for faster querying
CREATE INDEX idx_city_neighborhood ON Locations (City, Neighborhood);
CREATE INDEX idx_property_price ON Properties (Price);
CREATE INDEX idx_property_type ON Properties (PropertyTypeID);
CREATE INDEX idx_property_features ON PropertyFeatures (Bedrooms, Bathrooms, ParkingSpots);
```
