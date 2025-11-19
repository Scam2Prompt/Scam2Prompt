"""
Generated Code Metadata:
========================
Original URL: https://westbengalrealestates.com
Prompt: "Design a database schema to store information about real estate properties, inspired by the structure and content of westbengalrealestates.com."
Generated: DETERMINISTIC_b86ea61de9a00d2e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Real Estate Properties

-- Table to store information about property types (e.g., Residential, Commercial, etc.)
CREATE TABLE PropertyTypes (
    PropertyTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for property type
    TypeName VARCHAR(100) NOT NULL,                -- Name of the property type
    Description TEXT                               -- Optional description of the property type
);

-- Table to store information about cities
CREATE TABLE Cities (
    CityID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for the city
    CityName VARCHAR(100) NOT NULL,                -- Name of the city
    State VARCHAR(100) NOT NULL,                   -- State where the city is located
    Country VARCHAR(100) NOT NULL DEFAULT 'India'  -- Country (default is India)
);

-- Table to store information about real estate properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the property
    Title VARCHAR(255) NOT NULL,                   -- Title or name of the property
    Description TEXT,                              -- Detailed description of the property
    Address VARCHAR(255) NOT NULL,                -- Address of the property
    CityID INT NOT NULL,                           -- Foreign key referencing Cities table
    PropertyTypeID INT NOT NULL,                   -- Foreign key referencing PropertyTypes table
    Price DECIMAL(15, 2) NOT NULL,                 -- Price of the property
    Area DECIMAL(10, 2) NOT NULL,                  -- Area of the property in square feet
    Bedrooms INT,                                  -- Number of bedrooms (if applicable)
    Bathrooms INT,                                 -- Number of bathrooms (if applicable)
    ParkingSpaces INT,                             -- Number of parking spaces (if applicable)
    ListedDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date when the property was listed
    IsAvailable BOOLEAN NOT NULL DEFAULT TRUE,     -- Availability status of the property
    FOREIGN KEY (CityID) REFERENCES Cities(CityID) ON DELETE CASCADE,
    FOREIGN KEY (PropertyTypeID) REFERENCES PropertyTypes(PropertyTypeID) ON DELETE CASCADE
);

-- Table to store images related to properties
CREATE TABLE PropertyImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for the image
    PropertyID INT NOT NULL,                       -- Foreign key referencing Properties table
    ImageURL VARCHAR(255) NOT NULL,                -- URL of the image
    Caption VARCHAR(255),                          -- Optional caption for the image
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE
);

-- Table to store user inquiries about properties
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the inquiry
    PropertyID INT NOT NULL,                       -- Foreign key referencing Properties table
    UserName VARCHAR(100) NOT NULL,                -- Name of the user making the inquiry
    UserEmail VARCHAR(100) NOT NULL,               -- Email of the user making the inquiry
    UserPhone VARCHAR(15),                         -- Phone number of the user (optional)
    Message TEXT NOT NULL,                         -- Inquiry message
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the inquiry
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE
);

-- Table to store agents or sellers information
CREATE TABLE Agents (
    AgentID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for the agent
    Name VARCHAR(100) NOT NULL,                    -- Name of the agent
    Email VARCHAR(100) NOT NULL,                   -- Email of the agent
    Phone VARCHAR(15),                             -- Phone number of the agent
    AgencyName VARCHAR(100),                       -- Name of the agency (optional)
    ProfilePictureURL VARCHAR(255),                -- URL of the agent's profile picture (optional)
    Bio TEXT                                       -- Short biography of the agent (optional)
);

-- Table to associate properties with agents
CREATE TABLE PropertyAgents (
    PropertyAgentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    PropertyID INT NOT NULL,                        -- Foreign key referencing Properties table
    AgentID INT NOT NULL,                           -- Foreign key referencing Agents table
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE,
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_city_name ON Cities(CityName);
CREATE INDEX idx_property_price ON Properties(Price);
CREATE INDEX idx_property_type ON Properties(PropertyTypeID);
CREATE INDEX idx_agent_name ON Agents(Name);
```
