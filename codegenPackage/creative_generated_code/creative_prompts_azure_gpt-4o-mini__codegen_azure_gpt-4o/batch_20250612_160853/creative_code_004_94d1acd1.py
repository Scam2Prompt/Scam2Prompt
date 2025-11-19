"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Design a database schema in SQL for managing inventory of acrylic yarn products, based on the offerings of Ramji Acro.
Generated: DETERMINISTIC_94d1acd1397a40c8
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Inventory of Acrylic Yarn Products
-- Based on Ramji Acro's offerings

-- Create a database (optional, depending on the environment)
CREATE DATABASE IF NOT EXISTS AcrylicYarnInventory;
USE AcrylicYarnInventory;

-- Table for storing information about yarn products
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the yarn product
    Description TEXT,                         -- Detailed description of the product
    Category VARCHAR(100),                    -- Category or type of yarn (e.g., dyed, raw, etc.)
    Color VARCHAR(50),                        -- Color of the yarn
    Weight DECIMAL(10, 2) DEFAULT 0.00,       -- Weight in grams
    UnitPrice DECIMAL(10, 2) NOT NULL,        -- Price per unit (e.g., per kilogram)
    Status ENUM('Active', 'Discontinued') DEFAULT 'Active', -- Product status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for storing inventory stock levels
CREATE TABLE IF NOT EXISTS Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each inventory record
    ProductID INT NOT NULL,                     -- Foreign key referencing Products table
    StockQuantity INT NOT NULL DEFAULT 0,       -- Quantity of the product in stock
    ReorderLevel INT NOT NULL DEFAULT 10,       -- Minimum stock level before reorder is triggered
    LastRestocked TIMESTAMP,                    -- Timestamp of last restocking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the inventory record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete on product removal
);

-- Table for managing supplier information
CREATE TABLE IF NOT EXISTS Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,        -- Name of the supplier
    ContactInfo TEXT,                          -- Contact details for the supplier
    Address TEXT,                              -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the supplier record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for tracking restocking transactions
CREATE TABLE IF NOT EXISTS RestockingTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    InventoryID INT NOT NULL,                     -- Foreign key referencing Inventory table
    SupplierID INT NOT NULL,                      -- Foreign key referencing Suppliers table
    RestockedQuantity INT NOT NULL,               -- Quantity of items restocked
    RestockedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of restocking
    TotalCost DECIMAL(10, 2) NOT NULL,            -- Total cost of restocking
    FOREIGN KEY (InventoryID) REFERENCES Inventory(InventoryID) ON DELETE CASCADE, -- Cascade delete on inventory removal
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Cascade delete on supplier removal
);

-- Table for tracking sales transactions
CREATE TABLE IF NOT EXISTS SalesTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    QuantitySold INT NOT NULL,                    -- Quantity of product sold
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of sale
    TotalRevenue DECIMAL(10, 2) NOT NULL,         -- Total revenue generated from the sale
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete on product removal
);

-- Example Indexes for Optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_supplier_name ON Suppliers(SupplierName);
CREATE INDEX idx_inventory_product ON Inventory(ProductID);

-- End of Schema
```
