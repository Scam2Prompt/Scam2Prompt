"""
Generated Code Metadata:
========================
Original URL: https://www.autocuyo.com.ar
Prompt: Create a SQL database schema to store car listings and related information for a website like Autocuyo, including tables for users, cars, and locations.
Generated: DETERMINISTIC_bc3cd277ad1139b0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for a car listing website

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store car information
CREATE TABLE Cars (
    CarID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each car
    UserID INT NOT NULL,                  -- Foreign key referencing the user who listed the car
    Make VARCHAR(50) NOT NULL,            -- Car manufacturer (e.g., Toyota, Ford)
    Model VARCHAR(50) NOT NULL,           -- Car model (e.g., Corolla, Mustang)
    Year INT NOT NULL,                    -- Year of manufacture
    Price DECIMAL(10, 2) NOT NULL,        -- Price of the car
    Mileage INT NOT NULL,                 -- Mileage of the car in kilometers
    Description TEXT,                     -- Additional details about the car
    LocationID INT NOT NULL,              -- Foreign key referencing the location of the car
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the car listing was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE SET NULL -- Set location to NULL if deleted
);

-- Table to store location information
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    City VARCHAR(100) NOT NULL,                -- City name
    State VARCHAR(100) NOT NULL,               -- State or region name
    Country VARCHAR(100) NOT NULL,             -- Country name
    PostalCode VARCHAR(20),                    -- Postal code (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the location was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users (Email); -- Index for quick lookup of users by email
CREATE INDEX idx_car_price ON Cars (Price);   -- Index for quick lookup of cars by price
CREATE INDEX idx_location_city ON Locations (City); -- Index for quick lookup of locations by city

-- Error handling and constraints
-- Ensure that the year of the car is reasonable
ALTER TABLE Cars ADD CONSTRAINT chk_year CHECK (Year >= 1886 AND Year <= YEAR(CURRENT_DATE));

-- Ensure that the price is positive
ALTER TABLE Cars ADD CONSTRAINT chk_price CHECK (Price > 0);

-- Ensure that the mileage is non-negative
ALTER TABLE Cars ADD CONSTRAINT chk_mileage CHECK (Mileage >= 0);
```
