"""
Generated Code Metadata:
========================
Original URL: https://meeytamsk-logjjiin.godaddysites.com
Prompt: Write a SQL query to design a database schema for storing and retrieving real estate listing data, including features like property descriptions, prices, and locations, inspired by the content on meeytamsk-logjjiin.
Generated: DETERMINISTIC_3a090f8a1bc96d50
Batch ID: 20250622_211907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for real estate listings
CREATE DATABASE RealEstateDB;

-- Use the newly created database
USE RealEstateDB;

-- Table to store property listings
CREATE TABLE PropertyListings (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Title VARCHAR(255) NOT NULL,               -- Title of the property listing
    Description TEXT NOT NULL,                  -- Detailed description of the property
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the property
    Location VARCHAR(255) NOT NULL,             -- Location of the property
    PropertyType ENUM('House', 'Apartment', 'Condo', 'Land') NOT NULL, -- Type of property
    Bedrooms INT DEFAULT 0,                     -- Number of bedrooms
    Bathrooms INT DEFAULT 0,                    -- Number of bathrooms
    SquareFeet INT DEFAULT 0,                   -- Size of the property in square feet
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the listing was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store property images
CREATE TABLE PropertyImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each image
    PropertyID INT NOT NULL,                     -- Foreign key referencing PropertyListings
    ImageURL VARCHAR(255) NOT NULL,             -- URL of the property image
    FOREIGN KEY (PropertyID) REFERENCES PropertyListings(PropertyID) ON DELETE CASCADE -- Ensures images are deleted if the property is deleted
);

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,       -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,         -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Unique email for the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);

-- Table to store user favorites
CREATE TABLE UserFavorites (
    FavoriteID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each favorite
    UserID INT NOT NULL,                         -- Foreign key referencing Users
    PropertyID INT NOT NULL,                     -- Foreign key referencing PropertyListings
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the favorite was added
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Ensures favorites are deleted if the user is deleted
    FOREIGN KEY (PropertyID) REFERENCES PropertyListings(PropertyID) ON DELETE CASCADE -- Ensures favorites are deleted if the property is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_property_location ON PropertyListings(Location);
CREATE INDEX idx_property_price ON PropertyListings(Price);
CREATE INDEX idx_user_email ON Users(Email);
```
