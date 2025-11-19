"""
Generated Code Metadata:
========================
Original URL: https://tidhholding.com
Prompt: Design a simple database schema to store information about TIDH Holding's investments, including fields for project name, location, and type of investment.
Generated: DETERMINISTIC_4dea3b39cd5e8c00
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for TIDH Holding's investments

-- Create a table to store investment information
CREATE TABLE Investments (
    InvestmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each investment
    ProjectName VARCHAR(255) NOT NULL,           -- Name of the investment project
    Location VARCHAR(255) NOT NULL,              -- Location of the investment project
    InvestmentType VARCHAR(100) NOT NULL,        -- Type of investment (e.g., Real Estate, Technology, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Add an index to optimize queries on frequently searched fields
CREATE INDEX idx_project_name ON Investments (ProjectName);
CREATE INDEX idx_location ON Investments (Location);
CREATE INDEX idx_investment_type ON Investments (InvestmentType);

-- Example of inserting data into the table
-- INSERT INTO Investments (ProjectName, Location, InvestmentType)
-- VALUES ('Green Energy Plant', 'California, USA', 'Renewable Energy');

-- Example of querying data from the table
-- SELECT * FROM Investments WHERE InvestmentType = 'Technology';

-- Example of updating data in the table
-- UPDATE Investments SET Location = 'New York, USA' WHERE InvestmentID = 1;

-- Example of deleting data from the table
-- DELETE FROM Investments WHERE InvestmentID = 1;

-- Ensure proper error handling in application code when interacting with this schema.
```
