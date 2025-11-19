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
-- Create a SQL database schema for car listings

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CarListings;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Locations;

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of user creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store location information
CREATE TABLE Locations (
    LocationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each location
    City VARCHAR(100) NOT NULL,                 -- City name
    State VARCHAR(100) NOT NULL,                -- State name
    Country VARCHAR(100) NOT NULL,              -- Country name
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of location creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store car listings
CREATE TABLE CarListings (
    CarID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each car listing
    UserID INT NOT NULL,                        -- Foreign key referencing the user who created the listing
    LocationID INT NOT NULL,                    -- Foreign key referencing the location of the car
    Make VARCHAR(50) NOT NULL,                  -- Car manufacturer
    Model VARCHAR(50) NOT NULL,                 -- Car model
    Year INT NOT NULL CHECK (Year > 1885),     -- Year of manufacture (must be greater than 1885)
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the car (must be non-negative)
    Description TEXT,                           -- Description of the car
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of listing creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Ensure user deletion cascades
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE  -- Ensure location deletion cascades
);

-- Indexes for performance optimization
CREATE INDEX idx_user ON CarListings(UserID);
CREATE INDEX idx_location ON CarListings(LocationID);
CREATE INDEX idx_year ON CarListings(Year);
```
