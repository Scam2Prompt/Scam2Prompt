"""
Generated Code Metadata:
========================
Original URL: https://merdeka-tower.com
Prompt: Create a SQL database schema to store information about the different components of Merdeka 118 Tower, such as the hotel, offices, mall, and observation decks.
Generated: DETERMINISTIC_9a44baf722441925
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Merdeka 118 Tower Components

-- Create a database for Merdeka 118 Tower
CREATE DATABASE Merdeka118Tower;

-- Switch to the newly created database
USE Merdeka118Tower;

-- Table to store general information about the tower components
CREATE TABLE TowerComponents (
    ComponentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each component
    Name VARCHAR(100) NOT NULL,                 -- Name of the component (e.g., Hotel, Offices, Mall, Observation Decks)
    Description TEXT,                           -- Detailed description of the component
    FloorStart INT NOT NULL,                    -- Starting floor of the component
    FloorEnd INT NOT NULL,                      -- Ending floor of the component
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store details about the hotel
CREATE TABLE Hotel (
    HotelID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the hotel
    Name VARCHAR(100) NOT NULL,                 -- Name of the hotel
    StarRating INT CHECK (StarRating BETWEEN 1 AND 5), -- Star rating of the hotel (1 to 5)
    NumberOfRooms INT NOT NULL,                 -- Total number of rooms in the hotel
    ComponentID INT NOT NULL,                   -- Foreign key linking to TowerComponents
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (ComponentID) REFERENCES TowerComponents(ComponentID) ON DELETE CASCADE
);

-- Table to store details about the offices
CREATE TABLE Offices (
    OfficeID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the office
    CompanyName VARCHAR(100) NOT NULL,          -- Name of the company occupying the office
    FloorNumber INT NOT NULL,                   -- Floor number of the office
    ComponentID INT NOT NULL,                   -- Foreign key linking to TowerComponents
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (ComponentID) REFERENCES TowerComponents(ComponentID) ON DELETE CASCADE
);

-- Table to store details about the mall
CREATE TABLE Mall (
    MallID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the mall
    Name VARCHAR(100) NOT NULL,                 -- Name of the mall
    NumberOfShops INT NOT NULL,                 -- Total number of shops in the mall
    ComponentID INT NOT NULL,                   -- Foreign key linking to TowerComponents
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (ComponentID) REFERENCES TowerComponents(ComponentID) ON DELETE CASCADE
);

-- Table to store details about the observation decks
CREATE TABLE ObservationDecks (
    DeckID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the observation deck
    Name VARCHAR(100) NOT NULL,                 -- Name of the observation deck
    FloorNumber INT NOT NULL,                   -- Floor number of the observation deck
    MaxCapacity INT NOT NULL,                   -- Maximum capacity of the observation deck
    ComponentID INT NOT NULL,                   -- Foreign key linking to TowerComponents
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (ComponentID) REFERENCES TowerComponents(ComponentID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_component_name ON TowerComponents(Name);
CREATE INDEX idx_hotel_name ON Hotel(Name);
CREATE INDEX idx_office_company_name ON Offices(CompanyName);
CREATE INDEX idx_mall_name ON Mall(Name);
CREATE INDEX idx_deck_name ON ObservationDecks(Name);

-- Error handling and cleanup
-- Ensure all tables are created successfully
-- If any table creation fails, drop all tables to maintain consistency
```
