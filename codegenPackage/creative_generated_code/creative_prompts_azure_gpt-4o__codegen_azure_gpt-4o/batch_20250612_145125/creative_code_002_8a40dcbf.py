"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Generate code to create a database schema for storing information about tools (e.g., pliers, hammers, drills) and their quantities in a shop inventory system.
Generated: DETERMINISTIC_8a40dcbfdac4544e
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for a shop inventory system
-- that tracks tools and their quantities.

-- Use appropriate naming conventions and enforce data integrity.

CREATE DATABASE ShopInventory;

USE ShopInventory;

-- Table to store information about tools
CREATE TABLE Tools (
    ToolID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tool
    Name VARCHAR(100) NOT NULL,            -- Name of the tool
    Description TEXT,                      -- Optional text description of the tool
    Category VARCHAR(50),                  -- Category of the tool (e.g., Hand Tools, Power Tools)
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the tool
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the tool was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update to the tool
);

-- Table to track inventory quantities for each tool
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the inventory record
    ToolID INT NOT NULL,                        -- Foreign key referencing Tools table
    Quantity INT NOT NULL,                      -- Quantity of the tool in stock
    Location VARCHAR(100),                      -- Location of the tool in the shop (optional)
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    CONSTRAINT fk_ToolID FOREIGN KEY (ToolID) REFERENCES Tools(ToolID) ON DELETE CASCADE -- Foreign key relationship
);

-- Indexes to improve query performance
CREATE INDEX idx_ToolName ON Tools (Name);
CREATE INDEX idx_ToolCategory ON Tools (Category);
CREATE INDEX idx_InventoryToolID ON Inventory (ToolID);

-- Sample data insertion (optional, for testing purposes)
INSERT INTO Tools (Name, Description, Category, Price)
VALUES 
    ('Hammer', 'A durable claw hammer.', 'Hand Tools', 14.99),
    ('Drill', 'Cordless power drill with battery.', 'Power Tools', 79.99),
    ('Pliers', 'Needle-nose pliers.', 'Hand Tools', 9.99);

INSERT INTO Inventory (ToolID, Quantity, Location)
VALUES 
    (1, 25, 'Aisle 1'),
    (2, 10, 'Aisle 5'),
    (3, 40, 'Aisle 3');
```
