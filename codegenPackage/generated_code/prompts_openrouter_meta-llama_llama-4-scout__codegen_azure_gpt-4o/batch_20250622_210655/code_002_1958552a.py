"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: "Generate a SQL database schema for managing Laotaigroup's business units, including construction projects, trading, and investment activities."
Generated: DETERMINISTIC_1958552a26ea0647
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Laotaigroup's Business Units Management
-- This schema includes tables for managing construction projects, trading activities, and investment activities.

-- Create a table for business units
CREATE TABLE BusinessUnits (
    UnitID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each business unit
    UnitName VARCHAR(255) NOT NULL,        -- Name of the business unit
    UnitType ENUM('Construction', 'Trading', 'Investment') NOT NULL, -- Type of business unit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the unit was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for construction projects
CREATE TABLE ConstructionProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    UnitID INT NOT NULL,                      -- Foreign key referencing BusinessUnits
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the construction project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    Budget DECIMAL(15, 2) NOT NULL,           -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UnitID) REFERENCES BusinessUnits(UnitID) ON DELETE CASCADE -- Cascade delete if the business unit is deleted
);

-- Create a table for trading activities
CREATE TABLE TradingActivities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each trading activity
    UnitID INT NOT NULL,                       -- Foreign key referencing BusinessUnits
    ActivityName VARCHAR(255) NOT NULL,        -- Name of the trading activity
    TradeDate DATE NOT NULL,                   -- Date of the trading activity
    Amount DECIMAL(15, 2) NOT NULL,            -- Amount involved in the trading activity
    Currency VARCHAR(10) NOT NULL,             -- Currency used in the trading activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the activity was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UnitID) REFERENCES BusinessUnits(UnitID) ON DELETE CASCADE -- Cascade delete if the business unit is deleted
);

-- Create a table for investment activities
CREATE TABLE InvestmentActivities (
    InvestmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each investment activity
    UnitID INT NOT NULL,                         -- Foreign key referencing BusinessUnits
    InvestmentName VARCHAR(255) NOT NULL,        -- Name of the investment activity
    InvestmentDate DATE NOT NULL,                -- Date of the investment activity
    Amount DECIMAL(15, 2) NOT NULL,              -- Amount invested
    ROI DECIMAL(5, 2),                           -- Return on investment (percentage)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the investment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UnitID) REFERENCES BusinessUnits(UnitID) ON DELETE CASCADE -- Cascade delete if the business unit is deleted
);

-- Create indexes for faster querying
CREATE INDEX idx_UnitType ON BusinessUnits(UnitType); -- Index on UnitType for filtering business units
CREATE INDEX idx_ProjectStatus ON ConstructionProjects(Status); -- Index on Status for filtering construction projects
CREATE INDEX idx_TradeDate ON TradingActivities(TradeDate); -- Index on TradeDate for filtering trading activities
CREATE INDEX idx_InvestmentDate ON InvestmentActivities(InvestmentDate); -- Index on InvestmentDate for filtering investment activities
```
