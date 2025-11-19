"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: Create a database schema for managing multiple construction sites, including fields for site managers, associated trades, and award recognition, inspired by Westpoint Construction's Pride in the Job awards.
Generated: DETERMINISTIC_4bc423b0f32b015e
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing multiple construction sites
-- This schema includes tables for construction sites, site managers, trades, and award recognitions.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS AwardRecognition;
DROP TABLE IF EXISTS Trades;
DROP TABLE IF EXISTS SiteManagers;
DROP TABLE IF EXISTS ConstructionSites;

-- Table to store information about construction sites
CREATE TABLE ConstructionSites (
    SiteID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each construction site
    SiteName VARCHAR(255) NOT NULL,        -- Name of the construction site
    Location VARCHAR(255) NOT NULL,        -- Location of the construction site
    StartDate DATE NOT NULL,                -- Start date of the construction project
    EndDate DATE,                           -- End date of the construction project (nullable)
    ManagerID INT,                          -- Foreign key referencing SiteManagers
    FOREIGN KEY (ManagerID) REFERENCES SiteManagers(ManagerID) -- Establishing relationship with SiteManagers
);

-- Table to store information about site managers
CREATE TABLE SiteManagers (
    ManagerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each site manager
    FirstName VARCHAR(100) NOT NULL,          -- First name of the site manager
    LastName VARCHAR(100) NOT NULL,           -- Last name of the site manager
    PhoneNumber VARCHAR(15),                   -- Phone number of the site manager (nullable)
    Email VARCHAR(255) UNIQUE NOT NULL         -- Email address of the site manager (must be unique)
);

-- Table to store information about trades associated with construction sites
CREATE TABLE Trades (
    TradeID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each trade
    TradeName VARCHAR(100) NOT NULL,           -- Name of the trade (e.g., plumbing, electrical)
    Description TEXT                           -- Description of the trade (nullable)
);

-- Table to store award recognitions for construction sites
CREATE TABLE AwardRecognition (
    AwardID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each award
    SiteID INT,                                 -- Foreign key referencing ConstructionSites
    AwardName VARCHAR(255) NOT NULL,           -- Name of the award (e.g., Pride in the Job)
    AwardDate DATE NOT NULL,                    -- Date when the award was received
    FOREIGN KEY (SiteID) REFERENCES ConstructionSites(SiteID) -- Establishing relationship with ConstructionSites
);

-- Indexes for performance optimization
CREATE INDEX idx_site_manager ON ConstructionSites(ManagerID);
CREATE INDEX idx_trade_name ON Trades(TradeName);
CREATE INDEX idx_award_site ON AwardRecognition(SiteID);
```
