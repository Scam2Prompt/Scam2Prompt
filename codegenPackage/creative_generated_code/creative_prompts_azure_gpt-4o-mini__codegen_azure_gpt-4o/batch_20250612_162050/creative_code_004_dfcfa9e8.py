"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaarabella.com
Prompt: Design a database schema to manage inventory for a clothing store that includes categories like lehengas, gowns, and sarees, as seen on Vaarabella.
Generated: DETERMINISTIC_dfcfa9e8eee7e8a4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Clothing Store Inventory Management

-- Table: Categories
-- Purpose: Stores different categories of clothing (e.g., lehengas, gowns, sarees).
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL UNIQUE,         -- Name of the category (e.g., lehenga, gown)
    Description TEXT                           -- Optional description about the category
);

-- Table: Products
-- Purpose: Stores individual clothing items with details.
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product (e.g., "Red Bridal Lehenga")
    CategoryID INT NOT NULL,                  -- Foreign key linking to Categories table
    SKU VARCHAR(100) UNIQUE NOT NULL,         -- Stock Keeping Unit for unique product identification
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Quantity INT NOT NULL DEFAULT 0,          -- Available quantity in inventory
    Description TEXT,                         -- Optional detailed description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Table: Suppliers
-- Purpose: Stores information about suppliers providing inventory.
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactEmail VARCHAR(255),                 -- Supplier's contact email
    ContactPhone VARCHAR(20),                  -- Supplier's contact phone number
    Address TEXT                               -- Full address of the supplier
);

-- Table: ProductSuppliers
-- Purpose: Establishes a many-to-many relationship between products and suppliers.
CREATE TABLE ProductSuppliers (
    ProductID INT NOT NULL,                   -- Foreign key referencing Products table
    SupplierID INT NOT NULL,                  -- Foreign key referencing Suppliers table
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of acquiring the product from the supplier
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE,
    PRIMARY KEY (ProductID, SupplierID)       -- Composite primary key for uniqueness
);

-- Table: InventoryLogs
-- Purpose: Tracks changes in inventory levels over time.
CREATE TABLE InventoryLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each log entry
    ProductID INT NOT NULL,                   -- Foreign key referencing Products table
    ChangeType ENUM('INCREASE', 'DECREASE') NOT NULL, -- Type of change (increase or decrease)
    QuantityChange INT NOT NULL,              -- Number of units added or removed
    ChangeReason TEXT,                        -- Optional reason for the inventory change
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the change
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Indexes for faster search and querying
CREATE INDEX IDX_Products_CategoryID ON Products(CategoryID); -- Index on CategoryID for Products table
CREATE INDEX IDX_ProductSuppliers_ProductID ON ProductSuppliers(ProductID); -- Index on ProductID for ProductSuppliers table
CREATE INDEX IDX_InventoryLogs_ProductID ON InventoryLogs(ProductID); -- Index on ProductID for InventoryLogs table
```
