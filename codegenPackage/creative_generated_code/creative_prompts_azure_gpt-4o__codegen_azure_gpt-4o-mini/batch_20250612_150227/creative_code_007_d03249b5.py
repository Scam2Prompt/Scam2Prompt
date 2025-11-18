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
-- Database schema for tracking portfolio companies' growth and international expansion

-- Create a schema for Initia Capital
CREATE SCHEMA InitiaCapital;

-- Table to store portfolio companies
CREATE TABLE InitiaCapital.PortfolioCompanies (
    CompanyID SERIAL PRIMARY KEY,           -- Unique identifier for each company
    CompanyName VARCHAR(255) NOT NULL,     -- Name of the portfolio company
    FoundedYear INT CHECK (FoundedYear > 0), -- Year the company was founded
    Industry VARCHAR(100),                  -- Industry the company operates in
    HeadquartersLocation VARCHAR(255),      -- Location of the company's headquarters
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to track the growth metrics of portfolio companies
CREATE TABLE InitiaCapital.GrowthMetrics (
    MetricID SERIAL PRIMARY KEY,            -- Unique identifier for each growth metric
    CompanyID INT NOT NULL,                 -- Foreign key referencing portfolio companies
    Revenue DECIMAL(15, 2) CHECK (Revenue >= 0), -- Revenue growth metric
    EmployeesCount INT CHECK (EmployeesCount >= 0), -- Number of employees
    Year INT CHECK (Year > 0),              -- Year of the metric
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (CompanyID) REFERENCES InitiaCapital.PortfolioCompanies (CompanyID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to track international expansion efforts
CREATE TABLE InitiaCapital.InternationalExpansion (
    ExpansionID SERIAL PRIMARY KEY,         -- Unique identifier for each expansion effort
    CompanyID INT NOT NULL,                 -- Foreign key referencing portfolio companies
    Country VARCHAR(100) NOT NULL,          -- Country where the company is expanding
    ExpansionYear INT CHECK (ExpansionYear > 0), -- Year of expansion
    MarketEntryStrategy VARCHAR(255),       -- Strategy used for market entry
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (CompanyID) REFERENCES InitiaCapital.PortfolioCompanies (CompanyID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Example insertion of a portfolio company
INSERT INTO InitiaCapital.PortfolioCompanies (CompanyName, FoundedYear, Industry, HeadquartersLocation)
VALUES ('Tech Innovations Inc.', 2015, 'Technology', 'San Francisco, CA');

-- Example insertion of growth metrics for the portfolio company
INSERT INTO InitiaCapital.GrowthMetrics (CompanyID, Revenue, EmployeesCount, Year)
VALUES (1, 5000000.00, 50, 2023);

-- Example insertion of international expansion details
INSERT INTO InitiaCapital.InternationalExpansion (CompanyID, Country, ExpansionYear, MarketEntryStrategy)
VALUES (1, 'Germany', 2023, 'Joint Venture');
```
