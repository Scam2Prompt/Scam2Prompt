"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.hu
Prompt: Develop a database schema for tracking portfolio companies' growth and international expansion, considering Initia Capital's operational support and strategic guidance.
Generated: DETERMINISTIC_d03249b528142a73
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Tracking Portfolio Companies' Growth and International Expansion

-- Create a table for storing portfolio companies' details
CREATE TABLE PortfolioCompanies (
    CompanyID SERIAL PRIMARY KEY,                 -- Unique identifier for each portfolio company
    CompanyName VARCHAR(255) NOT NULL,           -- Name of the portfolio company
    Industry VARCHAR(100),                       -- Industry the company operates in
    FoundedYear INT CHECK (FoundedYear > 0),     -- Year the company was founded
    Headquarters VARCHAR(255),                  -- Headquarters location of the company
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create a table for tracking growth metrics of portfolio companies
CREATE TABLE GrowthMetrics (
    MetricID SERIAL PRIMARY KEY,                 -- Unique identifier for each growth metric entry
    CompanyID INT NOT NULL,                      -- Foreign key to PortfolioCompanies
    MetricName VARCHAR(100) NOT NULL,           -- Name of the metric (e.g., revenue, user growth)
    MetricValue DECIMAL(18, 4) NOT NULL,        -- Numeric value of the metric
    MetricDate DATE NOT NULL,                   -- Date the metric was recorded
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (CompanyID) REFERENCES PortfolioCompanies(CompanyID) ON DELETE CASCADE
);

-- Create a table for tracking international expansion details
CREATE TABLE InternationalExpansion (
    ExpansionID SERIAL PRIMARY KEY,             -- Unique identifier for each expansion entry
    CompanyID INT NOT NULL,                      -- Foreign key to PortfolioCompanies
    Country VARCHAR(100) NOT NULL,              -- Country where expansion occurred
    EntryDate DATE NOT NULL,                    -- Date the company entered the country
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('In Progress', 'Completed', 'Paused')), -- Status of the expansion
    Notes TEXT,                                 -- Additional notes about the expansion
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (CompanyID) REFERENCES PortfolioCompanies(CompanyID) ON DELETE CASCADE
);

-- Create a table to log operational support and strategic guidance provided by Initia Capital
CREATE TABLE OperationalSupportLogs (
    SupportID SERIAL PRIMARY KEY,               -- Unique identifier for each support log
    CompanyID INT NOT NULL,                      -- Foreign key to PortfolioCompanies
    SupportType VARCHAR(100) NOT NULL,          -- Type of support provided (e.g., funding, mentorship)
    Description TEXT,                           -- Detailed description of the support provided
    SupportDate DATE NOT NULL,                  -- Date the support was provided
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (CompanyID) REFERENCES PortfolioCompanies(CompanyID) ON DELETE CASCADE
);

-- Create triggers to update UpdatedAt fields automatically on data modification
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.UpdatedAt = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Attach the trigger function to relevant tables
CREATE TRIGGER set_updated_at_companies
BEFORE UPDATE ON PortfolioCompanies
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER set_updated_at_growth_metrics
BEFORE UPDATE ON GrowthMetrics
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER set_updated_at_international_expansion
BEFORE UPDATE ON InternationalExpansion
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER set_updated_at_support_logs
BEFORE UPDATE ON OperationalSupportLogs
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();
```
