"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Develop a database schema for tracking asset finance deals across multiple industries, including fields for asset types like amusement rides, commercial mortgages, and plant equipment, as mentioned on Rhino Asset Finance.
Generated: DETERMINISTIC_d175970df52e618f
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking asset finance deals across multiple industries.

-- Create a table for industries.
CREATE TABLE Industries (
    IndustryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each industry
    IndustryName VARCHAR(255) NOT NULL,        -- Name of the industry (e.g., Amusement, Commercial Mortgages, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for asset types.
CREATE TABLE AssetTypes (
    AssetTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each asset type
    AssetTypeName VARCHAR(255) NOT NULL,        -- Name of the asset type (e.g., Amusement Rides, Plant Equipment, etc.)
    IndustryID INT NOT NULL,                    -- Foreign key linking to the Industries table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (IndustryID) REFERENCES Industries(IndustryID) ON DELETE CASCADE -- Cascade delete to remove asset types if an industry is deleted
);

-- Create a table for finance deals.
CREATE TABLE FinanceDeals (
    DealID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each finance deal
    AssetTypeID INT NOT NULL,                  -- Foreign key linking to the AssetTypes table
    DealAmount DECIMAL(18, 2) NOT NULL,        -- The financial amount of the deal
    DealDate DATE NOT NULL,                    -- The date of the deal
    CustomerName VARCHAR(255) NOT NULL,        -- Name of the customer associated with the deal
    CustomerContact VARCHAR(255),             -- Contact information of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (AssetTypeID) REFERENCES AssetTypes(AssetTypeID) ON DELETE CASCADE -- Cascade delete to remove deals if an asset type is deleted
);

-- Optional: Indexes for faster lookup and search optimization.
CREATE INDEX idx_IndustryName ON Industries(IndustryName);
CREATE INDEX idx_AssetTypeName ON AssetTypes(AssetTypeName);
CREATE INDEX idx_DealDate ON FinanceDeals(DealDate);
CREATE INDEX idx_CustomerName ON FinanceDeals(CustomerName);

-- End of database schema.
```
