"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-connect-tw.blogspot.com
Prompt: Create a database schema in SQL to store information about automotive parts (e.g., brake calipers, pivots) and their associated service center locations, such as Santa Cruz do Sul and São José.
Generated: DETERMINISTIC_def88ad723a18bd2
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema to store information about automotive parts and service center locations

-- Table to store information about automotive parts
CREATE TABLE AutomotiveParts (
    PartID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each part
    PartName VARCHAR(100) NOT NULL,           -- Name of the part (e.g., Brake Caliper, Pivot)
    PartDescription TEXT,                     -- Detailed description of the part
    Manufacturer VARCHAR(100),                -- Name of the manufacturer
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the part
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the part was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store information about service center locations
CREATE TABLE ServiceCenters (
    CenterID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service center
    CenterName VARCHAR(100) NOT NULL,          -- Name of the service center
    Address TEXT NOT NULL,                     -- Address of the service center
    City VARCHAR(100) NOT NULL,                -- City where the service center is located
    State VARCHAR(100) NOT NULL,               -- State where the service center is located
    PhoneNumber VARCHAR(20),                   -- Contact phone number for the service center
    Email VARCHAR(100),                        -- Contact email for the service center
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service center was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to link automotive parts to service centers
CREATE TABLE PartsServiceCenters (
    PartServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each relationship
    PartID INT NOT NULL,                          -- Foreign key referencing AutomotiveParts.PartID
    CenterID INT NOT NULL,                        -- Foreign key referencing ServiceCenters.CenterID
    StockQuantity INT NOT NULL,                   -- Quantity of the part in stock at the service center
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the relationship was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (PartID) REFERENCES AutomotiveParts(PartID) ON DELETE CASCADE, -- Enforce referential integrity
    FOREIGN KEY (CenterID) REFERENCES ServiceCenters(CenterID) ON DELETE CASCADE -- Enforce referential integrity
);

-- Optional: Create indexes to improve query performance
CREATE INDEX idx_PartID ON PartsServiceCenters (PartID);
CREATE INDEX idx_CenterID ON PartsServiceCenters (CenterID);
```
