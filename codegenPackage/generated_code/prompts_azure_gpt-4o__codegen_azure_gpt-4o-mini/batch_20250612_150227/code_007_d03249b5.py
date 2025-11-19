"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Develop a database schema for tracking portfolio companies' growth and international expansion, considering Initia Capital's operational support and strategic guidance.
Generated: DETERMINISTIC_d03249b528142a73
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking portfolio companies' growth and international expansion

-- Create a table to store information about portfolio companies
CREATE TABLE PortfolioCompanies (
    CompanyID SERIAL PRIMARY KEY, -- Unique identifier for each company
    CompanyName VARCHAR(255) NOT NULL, -- Name of the company
    Industry VARCHAR(100), -- Industry sector of the company
    FoundedDate DATE, -- Date the company was founded
    HeadquartersLocation VARCHAR(255), -- Location of the company's headquarters
    WebsiteURL VARCHAR(255), -- Company's website URL
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to track growth metrics for each company
CREATE TABLE GrowthMetrics (
    MetricID SERIAL PRIMARY KEY, -- Unique identifier for each growth metric record
    CompanyID INT NOT NULL, -- Foreign key referencing the portfolio company
    Year INT NOT NULL, -- Year of the growth metric
    Revenue DECIMAL(15, 2), -- Revenue for the year
    EmployeeCount INT, -- Number of employees
    MarketShare DECIMAL(5, 2), -- Market share percentage
    FOREIGN KEY (CompanyID) REFERENCES PortfolioCompanies(CompanyID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to track international expansions
CREATE TABLE InternationalExpansions (
    ExpansionID SERIAL PRIMARY KEY, -- Unique identifier for each expansion record
    CompanyID INT NOT NULL, -- Foreign key referencing the portfolio company
    Country VARCHAR(100) NOT NULL, -- Country where the expansion occurs
    City VARCHAR(100), -- City of the new location
    ExpansionDate DATE NOT NULL, -- Date of the expansion
    Description TEXT, -- Description of the expansion
    FOREIGN KEY (CompanyID) REFERENCES PortfolioCompanies(CompanyID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store operational support and strategic guidance provided by Initia Capital
CREATE TABLE OperationalSupport (
    SupportID SERIAL PRIMARY KEY, -- Unique identifier for each support record
    CompanyID INT NOT NULL, -- Foreign key referencing the portfolio company
    SupportType VARCHAR(100) NOT NULL, -- Type of support (e.g., financial, strategic, operational)
    Description TEXT, -- Description of the support provided
    SupportDate DATE NOT NULL, -- Date when the support was provided
    FOREIGN KEY (CompanyID) REFERENCES PortfolioCompanies(CompanyID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to log any errors that occur during operations
CREATE TABLE ErrorLogs (
    ErrorID SERIAL PRIMARY KEY, -- Unique identifier for each error log
    ErrorMessage TEXT NOT NULL, -- Description of the error
    ErrorDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the error occurred
    CompanyID INT, -- Optional foreign key referencing the portfolio company
    FOREIGN KEY (CompanyID) REFERENCES PortfolioCompanies(CompanyID) ON DELETE SET NULL -- Allows for null if not related to a company
);
```
