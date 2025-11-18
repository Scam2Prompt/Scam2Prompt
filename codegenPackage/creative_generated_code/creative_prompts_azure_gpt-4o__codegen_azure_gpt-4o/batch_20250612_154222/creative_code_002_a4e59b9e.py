"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Develop a database schema for storing information about appliance repair services, including appliance types, supported brands (e.g., Toshiba, Samsung, LG), and service history.
Generated: DETERMINISTIC_a4e59b9eb28ec21d
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Appliance Repair Services

-- Create a table for Appliance Types
CREATE TABLE ApplianceTypes (
    ApplianceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the appliance type
    TypeName VARCHAR(100) NOT NULL UNIQUE,          -- Name of the appliance type (e.g., Refrigerator, Washing Machine)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp for when the record was created
);

-- Create a table for Supported Brands
CREATE TABLE SupportedBrands (
    BrandID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for the brand
    BrandName VARCHAR(100) NOT NULL UNIQUE,         -- Name of the brand (e.g., Toshiba, Samsung, LG)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp for when the record was created
);

-- Create a table for Service History
CREATE TABLE ServiceHistory (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for the service record
    ApplianceTypeID INT NOT NULL,                   -- Foreign key referencing ApplianceTypes.ApplianceTypeID
    BrandID INT NOT NULL,                           -- Foreign key referencing SupportedBrands.BrandID
    CustomerName VARCHAR(100) NOT NULL,            -- Name of the customer
    CustomerContact VARCHAR(50),                   -- Contact information for the customer (e.g., phone or email)
    ServiceDate DATE NOT NULL,                      -- Date the service was performed
    ServiceDetails TEXT,                            -- Detailed description of the service performed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    CONSTRAINT FK_ServiceHistory_ApplianceType FOREIGN KEY (ApplianceTypeID) REFERENCES ApplianceTypes(ApplianceTypeID),
    CONSTRAINT FK_ServiceHistory_Brand FOREIGN KEY (BrandID) REFERENCES SupportedBrands(BrandID)
);

-- Add indexing for performance optimization
CREATE INDEX IDX_ServiceHistory_ServiceDate ON ServiceHistory(ServiceDate); -- Index for querying by service date
CREATE INDEX IDX_ServiceHistory_CustomerName ON ServiceHistory(CustomerName); -- Index for querying by customer name

-- Error Handling: Ensure strict foreign key constraints
SET FOREIGN_KEY_CHECKS = 1;
```
