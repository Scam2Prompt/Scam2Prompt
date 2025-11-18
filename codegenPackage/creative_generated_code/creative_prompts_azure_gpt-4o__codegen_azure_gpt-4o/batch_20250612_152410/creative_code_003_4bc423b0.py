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
-- Database Schema for Managing Construction Sites with Relevant Details

-- Create a table for site managers
CREATE TABLE SiteManagers (
    ManagerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each manager
    FirstName VARCHAR(50) NOT NULL,           -- Manager's first name
    LastName VARCHAR(50) NOT NULL,            -- Manager's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Manager's email address
    Phone VARCHAR(15),                        -- Manager's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for construction sites
CREATE TABLE ConstructionSites (
    SiteID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each site
    SiteName VARCHAR(100) NOT NULL,         -- Name of the construction site
    Address VARCHAR(255) NOT NULL,          -- Address of the site
    StartDate DATE NOT NULL,                -- Project start date
    EndDate DATE,                           -- Project end date (nullable for ongoing projects)
    ManagerID INT NOT NULL,                 -- Foreign key referencing SiteManagers
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ManagerID) REFERENCES SiteManagers(ManagerID) -- Ensure referential integrity
);

-- Create a table for trades associated with construction sites
CREATE TABLE Trades (
    TradeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each trade
    TradeName VARCHAR(100) NOT NULL,        -- Name/description of the trade (e.g., "Electrician")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create an associative table to link trades to construction sites
CREATE TABLE SiteTrades (
    SiteTradeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    SiteID INT NOT NULL,                        -- Foreign key referencing ConstructionSites
    TradeID INT NOT NULL,                       -- Foreign key referencing Trades
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (SiteID) REFERENCES ConstructionSites(SiteID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TradeID) REFERENCES Trades(TradeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for award recognition (e.g., "Pride in the Job" awards)
CREATE TABLE Awards (
    AwardID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each award
    AwardName VARCHAR(100) NOT NULL,         -- Name of the award
    Description TEXT,                        -- Detailed description of the award
    AwardDate DATE NOT NULL,                 -- Date the award was given
    SiteID INT NOT NULL,                     -- Foreign key referencing ConstructionSites
    ManagerID INT,                           -- Optional foreign key referencing SiteManagers (if relevant)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (SiteID) REFERENCES ConstructionSites(SiteID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ManagerID) REFERENCES SiteManagers(ManagerID) ON DELETE SET NULL -- Ensure referential integrity
);

-- Add indexes where appropriate for faster queries
CREATE INDEX idx_site_manager ON ConstructionSites(ManagerID);
CREATE INDEX idx_site_trade ON SiteTrades(SiteID, TradeID);

-- End of database schema
```
