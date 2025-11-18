"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Develop a database schema to manage packaging product inventories and export destinations, inspired by Osku's wide portfolio and global distribution.
Generated: DETERMINISTIC_3bbaa902592bb883
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing packaging product inventories and export destinations

-- Create a table to store information about products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Description TEXT,                          -- Description of the product
    Category VARCHAR(100),                     -- Category of the product
    UnitPrice DECIMAL(10, 2) NOT NULL,         -- Price per unit of the product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity available in inventory
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store export destinations
CREATE TABLE ExportDestinations (
    DestinationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each destination
    Country VARCHAR(100) NOT NULL,                 -- Country name
    City VARCHAR(100) NOT NULL,                    -- City name
    Address TEXT NOT NULL,                         -- Address details
    ContactPerson VARCHAR(255),                   -- Name of the contact person at the destination
    ContactPhone VARCHAR(20),                     -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the destination entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store export records linking products to destinations
CREATE TABLE ExportRecords (
    ExportID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for the export record
    ProductID INT NOT NULL,                           -- Foreign key referencing the product
    DestinationID INT NOT NULL,                       -- Foreign key referencing the export destination
    ExportQuantity INT NOT NULL,                      -- Quantity of the product exported
    ExportDate DATE NOT NULL,                         -- Date of the export
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Cascade delete to maintain referential integrity
    FOREIGN KEY (DestinationID) REFERENCES ExportDestinations(DestinationID) ON DELETE CASCADE, -- Cascade delete to maintain referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP     -- Timestamp for when the export record was created
);

-- Create a table to store logs for monitoring activity (optional for production use)
CREATE TABLE ActivityLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for the log
    ActionType VARCHAR(100) NOT NULL,           -- Type of action performed (e.g., "INSERT", "UPDATE", "DELETE")
    TableName VARCHAR(100) NOT NULL,            -- Name of the table affected
    Description TEXT,                           -- Detailed information about the action
    ActionTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the action occurred
);

-- Ensure indexes for faster lookup on key columns (optional but recommended for performance)
CREATE INDEX idx_product_category ON Products(Category);
CREATE INDEX idx_destination_country_city ON ExportDestinations(Country, City);
CREATE INDEX idx_export_product_destination ON ExportRecords(ProductID, DestinationID);
```
