"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supplymarinebr.com.br
Prompt: Write code to create a database schema for managing maritime supply operations, including categories like food supplies, electrical equipment, tools, hygiene services, and personal protective equipment, as detailed by Supply Marine.
Generated: DETERMINISTIC_e4f2ce6aef05150e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing maritime supply operations
-- The schema includes tables to manage supplies, categories, suppliers, and transactions.

-- Create the 'SupplyMarine' database
CREATE DATABASE SupplyMarine;

-- Use the created database
USE SupplyMarine;

-- Create a table for Categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,        -- Name of the category (e.g., Food Supplies, Electrical Equipment)
    Description TEXT                           -- Optional description of the category
);

-- Create a table for Supplies
CREATE TABLE Supplies (
    SupplyID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each supply
    SupplyName VARCHAR(100) NOT NULL,         -- Name of the supply item
    CategoryID INT NOT NULL,                  -- Foreign key linking to Categories table
    Quantity INT NOT NULL CHECK (Quantity >= 0), -- Quantity available (must be non-negative)
    UnitPrice DECIMAL(10, 2) NOT NULL,        -- Price per unit
    SupplierID INT NOT NULL,                  -- Foreign key linking to Suppliers table
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Tracks updates
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID), -- Ensures valid category
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)   -- Ensures valid supplier
);

-- Create a table for Suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL,        -- Name of the supplier
    ContactInfo VARCHAR(255),                  -- Contact information for the supplier
    Address TEXT                               -- Address of the supplier
);

-- Create a table for Transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    SupplyID INT NOT NULL,                        -- Foreign key linking to Supplies table
    Quantity INT NOT NULL CHECK (Quantity > 0),   -- Quantity involved in the transaction
    TransactionType ENUM('IN', 'OUT') NOT NULL,   -- Type of transaction (IN for supply received, OUT for supply issued)
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of transaction
    Remarks TEXT,                                 -- Optional remarks for the transaction
    FOREIGN KEY (SupplyID) REFERENCES Supplies(SupplyID) -- Ensures valid supply item
);

-- Populate the Categories table with predefined values
INSERT INTO Categories (CategoryName, Description)
VALUES 
    ('Food Supplies', 'Items like provisions, packaged food, and perishables'),
    ('Electrical Equipment', 'Tools and materials for electrical maintenance'),
    ('Tools', 'General-purpose tools used onboard ships'),
    ('Hygiene Services', 'Items for sanitation and cleaning'),
    ('Personal Protective Equipment', 'Safety gear such as helmets, gloves, and vests');

-- Add a view to summarize stock levels by category
CREATE VIEW StockSummary AS
SELECT 
    c.CategoryName,
    SUM(s.Quantity) AS TotalQuantity,
    COUNT(s.SupplyID) AS ItemCount
FROM 
    Supplies s
INNER JOIN 
    Categories c ON s.CategoryID = c.CategoryID
GROUP BY 
    c.CategoryName;

-- Ensure the database schema is ready for production by committing the changes
COMMIT;
```
