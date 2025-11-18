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
-- Database schema for storing tool inventory
CREATE DATABASE IF NOT EXISTS ToolInventory;

USE ToolInventory;

-- Table to store tool categories (e.g., Hand Tools, Power Tools)
CREATE TABLE IF NOT EXISTS ToolCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store tools with their quantities
CREATE TABLE IF NOT EXISTS Tools (
    ToolID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tool
    ToolName VARCHAR(100) NOT NULL, -- Name of the tool
    CategoryID INT, -- Foreign key to ToolCategories
    Quantity INT NOT NULL DEFAULT 0, -- Quantity of the tool in stock
    Price DECIMAL(10, 2) NOT NULL DEFAULT 0.00, -- Price of the tool
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ToolCategories(CategoryID) ON DELETE SET NULL -- Establishing foreign key relationship
);

-- Example insert statements
INSERT INTO ToolCategories (CategoryName) VALUES ('Hand Tools'), ('Power Tools'), ('Gardening Tools');

INSERT INTO Tools (ToolName, CategoryID, Quantity, Price) VALUES 
('Pliers', 1, 50, 12.99),
('Hammer', 1, 75, 10.50),
('Drill', 2, 30, 99.99),
('Wrench', 1, 40, 8.75),
('Lawn Mower', 3, 20, 299.99);

-- Index for faster querying of tools by their names
CREATE INDEX idx_tool_name ON Tools (ToolName);
```
