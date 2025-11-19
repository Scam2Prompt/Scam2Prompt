"""
Generated Code Metadata:
========================
Original URL: https://pacerealestatevt.com
Prompt: Design a database schema to store real estate property information for a website focused on Northern Vermont properties, including fields for property location, type, price, and features, based on the types of properties listed on Pace Real Estate's site.
Generated: DETERMINISTIC_c85f1d0bee885296
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing real estate property information
-- This schema is designed to store information about properties in Northern Vermont.

-- Table to store property information
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Title VARCHAR(255) NOT NULL,               -- Title or name of the property
    Description TEXT,                          -- Detailed description of the property
    Location VARCHAR(255) NOT NULL,            -- Location of the property (e.g., city, town, or address)
    Type ENUM('Residential', 'Commercial', 'Land', 'Rental') NOT NULL, -- Type of property
    Price DECIMAL(15, 2) NOT NULL,             -- Price of the property
    Bedrooms INT DEFAULT NULL,                 -- Number of bedrooms (if applicable)
    Bathrooms INT DEFAULT NULL,                -- Number of bathrooms (if applicable)
    SquareFeet INT DEFAULT NULL,               -- Size of the property in square feet (if applicable)
    Features JSON DEFAULT NULL,                -- JSON field to store additional features (e.g., "garage", "pool")
    ListedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the property was listed
    UpdatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated date
);

-- Table to store images associated with properties
CREATE TABLE PropertyImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    PropertyID INT NOT NULL,                   -- Foreign key referencing the Properties table
    ImageURL VARCHAR(2083) NOT NULL,           -- URL of the image
    AltText VARCHAR(255) DEFAULT NULL,         -- Alternative text for the image
    UploadedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the image was uploaded
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascade delete if property is removed
);

-- Table to store agents who manage properties
CREATE TABLE Agents (
    AgentID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each agent
    Name VARCHAR(255) NOT NULL,                -- Name of the agent
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the agent
    Phone VARCHAR(20) DEFAULT NULL,            -- Phone number of the agent
    ProfilePictureURL VARCHAR(2083) DEFAULT NULL, -- URL of the agent's profile picture
    CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date the agent was added
);

-- Table to associate agents with properties
CREATE TABLE PropertyAgents (
    PropertyID INT NOT NULL,                   -- Foreign key referencing the Properties table
    AgentID INT NOT NULL,                      -- Foreign key referencing the Agents table
    PRIMARY KEY (PropertyID, AgentID),         -- Composite primary key
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete if property is removed
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID) ON DELETE CASCADE -- Cascade delete if agent is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_location ON Properties(Location); -- Index for location-based searches
CREATE INDEX idx_price ON Properties(Price);       -- Index for price-based searches
CREATE INDEX idx_type ON Properties(Type);         -- Index for type-based searches
```
