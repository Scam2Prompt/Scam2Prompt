"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Design a database schema for storing property listings and their associated details, suitable for a real estate platform like Presval, and write SQL queries to retrieve specific data.
Generated: DETERMINISTIC_410a37801a5b242a
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Property Listings

-- Table to store property listings
CREATE TABLE Property (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Title VARCHAR(255) NOT NULL,               -- Title of the property listing
    Description TEXT,                          -- Detailed description of the property
    Price DECIMAL(15, 2) NOT NULL,             -- Price of the property
    PropertyType ENUM('Apartment', 'House', 'Condo', 'Land', 'Commercial') NOT NULL, -- Type of property
    Address VARCHAR(255) NOT NULL,             -- Address of the property
    City VARCHAR(100) NOT NULL,                -- City where the property is located
    State VARCHAR(100) NOT NULL,               -- State where the property is located
    ZipCode VARCHAR(20),                       -- Zip code of the property location
    Bedrooms INT NOT NULL,                     -- Number of bedrooms
    Bathrooms INT NOT NULL,                    -- Number of bathrooms
    SquareFeet INT,                            -- Size of the property in square feet
    ListedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the property was listed
    IsAvailable BOOLEAN DEFAULT TRUE           -- Availability status of the property
);

-- Table to store property images
CREATE TABLE PropertyImage (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    PropertyID INT NOT NULL,                   -- Foreign key referencing Property table
    ImageURL VARCHAR(255) NOT NULL,            -- URL of the image
    IsPrimary BOOLEAN DEFAULT FALSE,           -- Indicates if the image is the primary image
    FOREIGN KEY (PropertyID) REFERENCES Property(PropertyID) ON DELETE CASCADE
);

-- Table to store property features
CREATE TABLE PropertyFeature (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each feature
    PropertyID INT NOT NULL,                   -- Foreign key referencing Property table
    FeatureName VARCHAR(100) NOT NULL,         -- Name of the feature (e.g., "Swimming Pool", "Garage")
    FOREIGN KEY (PropertyID) REFERENCES Property(PropertyID) ON DELETE CASCADE
);

-- Table to store agents who manage properties
CREATE TABLE Agent (
    AgentID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each agent
    Name VARCHAR(100) NOT NULL,                -- Name of the agent
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Email of the agent
    Phone VARCHAR(20),                         -- Phone number of the agent
    AgencyName VARCHAR(100)                    -- Name of the agency the agent belongs to
);

-- Table to associate agents with properties
CREATE TABLE PropertyAgent (
    PropertyID INT NOT NULL,                   -- Foreign key referencing Property table
    AgentID INT NOT NULL,                      -- Foreign key referencing Agent table
    FOREIGN KEY (PropertyID) REFERENCES Property(PropertyID) ON DELETE CASCADE,
    FOREIGN KEY (AgentID) REFERENCES Agent(AgentID) ON DELETE CASCADE,
    PRIMARY KEY (PropertyID, AgentID)          -- Composite primary key
);

-- Queries to retrieve specific data

-- 1. Retrieve all available properties in a specific city
SELECT * 
FROM Property
WHERE City = 'San Francisco' AND IsAvailable = TRUE;

-- 2. Retrieve all properties managed by a specific agent
SELECT p.*
FROM Property p
JOIN PropertyAgent pa ON p.PropertyID = pa.PropertyID
JOIN Agent a ON pa.AgentID = a.AgentID
WHERE a.Name = 'John Doe';

-- 3. Retrieve all features of a specific property
SELECT pf.FeatureName
FROM PropertyFeature pf
WHERE pf.PropertyID = 101; -- Replace 101 with the desired PropertyID

-- 4. Retrieve the primary image of a specific property
SELECT pi.ImageURL
FROM PropertyImage pi
WHERE pi.PropertyID = 101 AND pi.IsPrimary = TRUE; -- Replace 101 with the desired PropertyID

-- 5. Retrieve all properties within a specific price range
SELECT *
FROM Property
WHERE Price BETWEEN 500000 AND 1000000; -- Replace with desired price range

-- 6. Retrieve the total number of properties listed in each city
SELECT City, COUNT(*) AS TotalProperties
FROM Property
GROUP BY City;

-- 7. Retrieve all properties with a specific feature (e.g., "Swimming Pool")
SELECT p.*
FROM Property p
JOIN PropertyFeature pf ON p.PropertyID = pf.PropertyID
WHERE pf.FeatureName = 'Swimming Pool';
```
