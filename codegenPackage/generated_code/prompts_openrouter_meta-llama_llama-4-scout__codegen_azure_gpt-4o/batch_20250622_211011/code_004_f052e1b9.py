"""
Generated Code Metadata:
========================
Original URL: https://celestia.homes
Prompt: Design a database schema to store information about properties for sale on the Costa del Sol, inspired by the types of properties and features listed on Celestia Homes.
Generated: DETERMINISTIC_f052e1b9f299da67
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about properties for sale on the Costa del Sol

-- Table to store property details
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Title VARCHAR(255) NOT NULL,               -- Title or name of the property
    Description TEXT,                          -- Detailed description of the property
    Price DECIMAL(15, 2) NOT NULL,             -- Price of the property
    Location VARCHAR(255) NOT NULL,            -- Location of the property (e.g., city, area)
    PropertyType VARCHAR(50) NOT NULL,         -- Type of property (e.g., apartment, villa, townhouse)
    Bedrooms INT NOT NULL,                     -- Number of bedrooms
    Bathrooms INT NOT NULL,                    -- Number of bathrooms
    SquareMeters INT,                          -- Size of the property in square meters
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store features of properties (e.g., pool, garden, sea view)
CREATE TABLE Features (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each feature
    Name VARCHAR(100) NOT NULL UNIQUE          -- Name of the feature (e.g., "Pool", "Garden", "Sea View")
);

-- Junction table to associate properties with features (many-to-many relationship)
CREATE TABLE PropertyFeatures (
    PropertyID INT NOT NULL,                   -- Foreign key referencing Properties table
    FeatureID INT NOT NULL,                    -- Foreign key referencing Features table
    PRIMARY KEY (PropertyID, FeatureID),       -- Composite primary key
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (FeatureID) REFERENCES Features(FeatureID) ON DELETE CASCADE      -- Cascade delete
);

-- Table to store images for properties
CREATE TABLE PropertyImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    PropertyID INT NOT NULL,                   -- Foreign key referencing Properties table
    ImageURL VARCHAR(2083) NOT NULL,           -- URL of the image
    AltText VARCHAR(255),                      -- Alternative text for the image
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store agents who manage the properties
CREATE TABLE Agents (
    AgentID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each agent
    Name VARCHAR(255) NOT NULL,                -- Name of the agent
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the agent
    PhoneNumber VARCHAR(20),                   -- Phone number of the agent
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the agent was added
);

-- Table to associate properties with agents (many-to-many relationship)
CREATE TABLE PropertyAgents (
    PropertyID INT NOT NULL,                   -- Foreign key referencing Properties table
    AgentID INT NOT NULL,                      -- Foreign key referencing Agents table
    PRIMARY KEY (PropertyID, AgentID),         -- Composite primary key
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID) ON DELETE CASCADE             -- Cascade delete
);

-- Table to store inquiries made by potential buyers
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each inquiry
    PropertyID INT NOT NULL,                   -- Foreign key referencing Properties table
    Name VARCHAR(255) NOT NULL,                -- Name of the person making the inquiry
    Email VARCHAR(255) NOT NULL,               -- Email address of the person making the inquiry
    PhoneNumber VARCHAR(20),                   -- Phone number of the person making the inquiry
    Message TEXT,                              -- Message or inquiry details
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the inquiry was made
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_properties_location ON Properties(Location); -- Index for location-based searches
CREATE INDEX idx_properties_price ON Properties(Price);       -- Index for price-based searches
CREATE INDEX idx_properties_type ON Properties(PropertyType); -- Index for property type-based searches
```
