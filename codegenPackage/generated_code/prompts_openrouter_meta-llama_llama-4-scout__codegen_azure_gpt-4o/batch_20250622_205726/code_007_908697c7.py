"""
Generated Code Metadata:
========================
Original URL: https://trumflation.com
Prompt: "Develop a basic SQL database schema to store and query economic data related to trumflation analysis."
Generated: DETERMINISTIC_908697c743dc8623
Batch ID: 20250622_205726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for storing and querying economic data related to "trumflation" analysis

-- Create a table to store information about economic indicators
CREATE TABLE EconomicIndicators (
    IndicatorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each economic indicator
    Name VARCHAR(255) NOT NULL,                 -- Name of the economic indicator (e.g., CPI, GDP, etc.)
    Description TEXT,                           -- Description of the indicator
    Unit VARCHAR(50),                           -- Unit of measurement (e.g., percentage, dollars, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store economic data points
CREATE TABLE EconomicData (
    DataID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each data point
    IndicatorID INT NOT NULL,                  -- Foreign key referencing EconomicIndicators
    DataDate DATE NOT NULL,                    -- Date of the data point
    Value DECIMAL(15, 4) NOT NULL,             -- Value of the economic indicator on the given date
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (IndicatorID) REFERENCES EconomicIndicators(IndicatorID) ON DELETE CASCADE -- Ensure data integrity
);

-- Create a table to store metadata about data sources
CREATE TABLE DataSources (
    SourceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each data source
    Name VARCHAR(255) NOT NULL,                -- Name of the data source (e.g., Bureau of Labor Statistics)
    Website VARCHAR(255),                      -- Website URL of the data source
    ContactEmail VARCHAR(255),                 -- Contact email for the data source
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to associate data points with their sources
CREATE TABLE DataPointSources (
    DataPointSourceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    DataID INT NOT NULL,                              -- Foreign key referencing EconomicData
    SourceID INT NOT NULL,                            -- Foreign key referencing DataSources
    FOREIGN KEY (DataID) REFERENCES EconomicData(DataID) ON DELETE CASCADE, -- Ensure data integrity
    FOREIGN KEY (SourceID) REFERENCES DataSources(SourceID) ON DELETE CASCADE -- Ensure data integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_indicator_date ON EconomicData (IndicatorID, DataDate); -- Index for querying data by indicator and date
CREATE INDEX idx_source_name ON DataSources (Name);                      -- Index for querying data sources by name

-- Example queries for analysis
-- Query to retrieve all data points for a specific economic indicator
-- SELECT * FROM EconomicData WHERE IndicatorID = ? ORDER BY DataDate;

-- Query to retrieve the latest value of a specific economic indicator
-- SELECT * FROM EconomicData WHERE IndicatorID = ? ORDER BY DataDate DESC LIMIT 1;

-- Query to retrieve all indicators and their descriptions
-- SELECT * FROM EconomicIndicators;

-- Query to retrieve all data sources
-- SELECT * FROM DataSources;
```
