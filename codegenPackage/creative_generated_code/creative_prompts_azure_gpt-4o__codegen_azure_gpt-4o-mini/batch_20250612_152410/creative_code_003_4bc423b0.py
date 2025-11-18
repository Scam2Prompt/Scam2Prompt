"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westpoint-construction.co.uk
Prompt: Create a database schema for managing multiple construction sites, including fields for site managers, associated trades, and award recognition, inspired by Westpoint Construction's Pride in the Job awards.
Generated: DETERMINISTIC_4bc423b0f32b015e
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing multiple construction sites

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS SiteManagers CASCADE;
DROP TABLE IF EXISTS Trades CASCADE;
DROP TABLE IF EXISTS ConstructionSites CASCADE;
DROP TABLE IF EXISTS Awards CASCADE;

-- Table to store information about site managers
CREATE TABLE SiteManagers (
    ManagerID SERIAL PRIMARY KEY,        -- Unique identifier for each site manager
    FirstName VARCHAR(50) NOT NULL,     -- First name of the site manager
    LastName VARCHAR(50) NOT NULL,      -- Last name of the site manager
    Phone VARCHAR(15),                   -- Contact number of the site manager
    Email VARCHAR(100) UNIQUE,           -- Email address (must be unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about different trades
CREATE TABLE Trades (
    TradeID SERIAL PRIMARY KEY,          -- Unique identifier for each trade
    TradeName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the trade (must be unique)
    Description TEXT,                    -- Description of the trade
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about construction sites
CREATE TABLE ConstructionSites (
    SiteID SERIAL PRIMARY KEY,           -- Unique identifier for each construction site
    SiteName VARCHAR(100) NOT NULL,      -- Name of the construction site
    Location VARCHAR(255) NOT NULL,      -- Physical address of the site
    ManagerID INT REFERENCES SiteManagers(ManagerID) ON DELETE SET NULL,  -- Foreign key reference to site managers
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store award recognitions related to construction sites
CREATE TABLE Awards (
    AwardID SERIAL PRIMARY KEY,           -- Unique identifier for each award
    SiteID INT REFERENCES ConstructionSites(SiteID) ON DELETE CASCADE,  -- Foreign key reference to construction sites
    AwardName VARCHAR(100) NOT NULL,      -- Name of the award
    AwardYear INT NOT NULL CHECK (AwardYear > 2000),  -- Year when the award was received, must be after 2000
    Description TEXT,                     -- Description of the award
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Optional: Create indexes for better performance on frequently queried columns
CREATE INDEX idx_site_name ON ConstructionSites (SiteName);
CREATE INDEX idx_manager_email ON SiteManagers (Email);
CREATE INDEX idx_trade_name ON Trades (TradeName);
```
