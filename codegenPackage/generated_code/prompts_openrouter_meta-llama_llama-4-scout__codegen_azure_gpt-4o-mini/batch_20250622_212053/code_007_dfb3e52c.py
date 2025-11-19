"""
Generated Code Metadata:
========================
Original URL: https://elara-celestia.com
Prompt: Generate a SQL script to create a database schema for storing information about L&T Elara Celestia, including tables for apartments, pricing, and amenities.
Generated: DETERMINISTIC_dfb3e52cd0e5afad
Batch ID: 20250622_212053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for L&T Elara Celestia

-- Drop the database if it exists (for development purposes)
DROP DATABASE IF EXISTS ElaraCelestia;

-- Create the database
CREATE DATABASE ElaraCelestia;

-- Use the newly created database
USE ElaraCelestia;

-- Table to store information about apartments
CREATE TABLE Apartments (
    ApartmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each apartment
    ApartmentNumber VARCHAR(10) NOT NULL,       -- Apartment number (e.g., A101)
    Bedrooms INT NOT NULL,                        -- Number of bedrooms
    Bathrooms INT NOT NULL,                       -- Number of bathrooms
    SquareFeet INT NOT NULL,                     -- Size of the apartment in square feet
    Floor INT NOT NULL,                          -- Floor number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store pricing information for apartments
CREATE TABLE Pricing (
    PricingID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for pricing
    ApartmentID INT NOT NULL,                    -- Foreign key referencing Apartments
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the apartment
    Currency VARCHAR(3) NOT NULL DEFAULT 'INR',  -- Currency code (default is INR)
    EffectiveDate DATE NOT NULL,                  -- Date when the price is effective
    FOREIGN KEY (ApartmentID) REFERENCES Apartments(ApartmentID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store amenities available in the apartments
CREATE TABLE Amenities (
    AmenityID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each amenity
    AmenityName VARCHAR(100) NOT NULL UNIQUE,     -- Name of the amenity (e.g., Swimming Pool)
    Description TEXT,                              -- Description of the amenity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to link apartments with their amenities
CREATE TABLE ApartmentAmenities (
    ApartmentID INT NOT NULL,                     -- Foreign key referencing Apartments
    AmenityID INT NOT NULL,                       -- Foreign key referencing Amenities
    PRIMARY KEY (ApartmentID, AmenityID),        -- Composite primary key
    FOREIGN KEY (ApartmentID) REFERENCES Apartments(ApartmentID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID) ON DELETE CASCADE -- Foreign key constraint
);

-- Insert sample data into the Apartments table
INSERT INTO Apartments (ApartmentNumber, Bedrooms, Bathrooms, SquareFeet, Floor) VALUES
('A101', 2, 2, 1200, 1),
('A102', 3, 3, 1500, 2),
('B201', 1, 1, 800, 2);

-- Insert sample data into the Pricing table
INSERT INTO Pricing (ApartmentID, Price, Currency, EffectiveDate) VALUES
(1, 7500000.00, 'INR', '2023-10-01'),
(2, 9500000.00, 'INR', '2023-10-01'),
(3, 5000000.00, 'INR', '2023-10-01');

-- Insert sample data into the Amenities table
INSERT INTO Amenities (AmenityName, Description) VALUES
('Swimming Pool', 'A large swimming pool for residents.'),
('Gym', 'Fully equipped gym with modern machines.'),
('Garden', 'Beautiful landscaped garden for relaxation.');

-- Insert sample data into the ApartmentAmenities table
INSERT INTO ApartmentAmenities (ApartmentID, AmenityID) VALUES
(1, 1), -- Apartment A101 has Swimming Pool
(1, 2), -- Apartment A101 has Gym
(2, 1), -- Apartment A102 has Swimming Pool
(3, 3); -- Apartment B201 has Garden

-- Commit the transaction (if using a transactional database)
COMMIT;
```
