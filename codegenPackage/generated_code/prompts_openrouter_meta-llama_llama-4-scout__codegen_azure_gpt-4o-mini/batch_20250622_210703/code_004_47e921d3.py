"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: "Design a database schema to store property information for a real estate company like Dominguez Parra."
Generated: DETERMINISTIC_47e921d3433cdb6c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a real estate company to store property information

-- Create a table to store property types (e.g., Residential, Commercial, etc.)
CREATE TABLE PropertyTypes (
    PropertyTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each property type
    TypeName VARCHAR(50) NOT NULL,                -- Name of the property type
    Description TEXT,                              -- Description of the property type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store properties
CREATE TABLE Properties (
    PropertyID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each property
    PropertyTypeID INT NOT NULL,                   -- Foreign key referencing PropertyTypes
    Address VARCHAR(255) NOT NULL,                 -- Address of the property
    City VARCHAR(100) NOT NULL,                    -- City where the property is located
    State VARCHAR(100) NOT NULL,                   -- State where the property is located
    ZipCode VARCHAR(10) NOT NULL,                  -- Zip code of the property
    Price DECIMAL(15, 2) NOT NULL,                 -- Price of the property
    Bedrooms INT NOT NULL,                          -- Number of bedrooms
    Bathrooms INT NOT NULL,                         -- Number of bathrooms
    SquareFeet INT NOT NULL,                        -- Size of the property in square feet
    Description TEXT,                              -- Description of the property
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (PropertyTypeID) REFERENCES PropertyTypes(PropertyTypeID) -- Foreign key constraint
);

-- Create a table to store agents
CREATE TABLE Agents (
    AgentID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each agent
    FirstName VARCHAR(100) NOT NULL,                -- Agent's first name
    LastName VARCHAR(100) NOT NULL,                 -- Agent's last name
    Email VARCHAR(100) NOT NULL UNIQUE,             -- Agent's email address (must be unique)
    Phone VARCHAR(15),                              -- Agent's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store property listings
CREATE TABLE PropertyListings (
    ListingID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each listing
    PropertyID INT NOT NULL,                        -- Foreign key referencing Properties
    AgentID INT NOT NULL,                           -- Foreign key referencing Agents
    ListingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the property was listed
    Status ENUM('Active', 'Pending', 'Sold') NOT NULL, -- Status of the listing
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID), -- Foreign key constraint
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID) -- Foreign key constraint
);

-- Create a table to store property images
CREATE TABLE PropertyImages (
    ImageID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each image
    PropertyID INT NOT NULL,                        -- Foreign key referencing Properties
    ImageURL VARCHAR(255) NOT NULL,                 -- URL of the property image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) -- Foreign key constraint
);
```
