"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dunhill-servicedapartments.com
Prompt: Recommend a database schema for storing apartment details (e.g., location, price, bedrooms, bathrooms) and user preferences for a serviced apartment booking platform similar to Dunhill Serviced Apartments.
Generated: DETERMINISTIC_3ee4cf9302b13cb3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing apartment details and user preferences
-- This schema is designed for a serviced apartment booking platform.

-- Table to store apartment details
CREATE TABLE Apartments (
    ApartmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each apartment
    Name VARCHAR(255) NOT NULL,                 -- Name of the apartment
    Address TEXT NOT NULL,                      -- Full address of the apartment
    City VARCHAR(100) NOT NULL,                 -- City where the apartment is located
    State VARCHAR(100) NOT NULL,                -- State where the apartment is located
    Country VARCHAR(100) NOT NULL,              -- Country where the apartment is located
    PricePerNight DECIMAL(10, 2) NOT NULL,      -- Price per night for the apartment
    Bedrooms INT NOT NULL,                      -- Number of bedrooms in the apartment
    Bathrooms INT NOT NULL,                     -- Number of bathrooms in the apartment
    Amenities JSON,                             -- List of amenities (e.g., wifi, parking, etc.) in JSON format
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store user preferences
CREATE TABLE UserPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each preference record
    UserID INT NOT NULL,                         -- Foreign key linking to the user table (assume a Users table exists)
    MaxPrice DECIMAL(10, 2),                     -- Maximum price user is willing to pay per night
    MinBedrooms INT,                             -- Minimum number of bedrooms user prefers
    MinBathrooms INT,                            -- Minimum number of bathrooms user prefers
    DesiredCity VARCHAR(100),                   -- Desired city for the apartment
    DesiredAmenities JSON,                       -- Desired amenities in JSON format
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Link to Users table
);

-- Indexes for efficient querying
CREATE INDEX idx_apartments_city ON Apartments (City); -- Index for fast lookups by city
CREATE INDEX idx_apartments_price ON Apartments (PricePerNight); -- Index for sorting/filtering by price
CREATE INDEX idx_user_preferences_user ON UserPreferences (UserID); -- Index for fast lookups by user

-- Example of error handling:
-- Ensure JSON format is valid for Amenities and DesiredAmenities fields
-- In production, additional constraints and checks can be added based on application requirements.
```
