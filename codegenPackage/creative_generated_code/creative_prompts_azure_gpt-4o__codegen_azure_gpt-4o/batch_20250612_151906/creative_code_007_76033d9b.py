"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Create a database schema for managing procurement data, including categories like safety items, studs, bolts, and compressors, based on Cedar International Inc.'s offerings.
Generated: DETERMINISTIC_76033d9bde0102d5
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Procurement Data

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,          -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    CategoryID INT NOT NULL,                     -- Foreign key linking to ProductCategories
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL,                  -- Quantity available in stock
    Description TEXT,                            -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Cascade delete to maintain referential integrity
);

-- Create a table for procurement records
CREATE TABLE Procurements (
    ProcurementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each procurement record
    ProductID INT NOT NULL,                       -- Foreign key linking to Products
    Quantity INT NOT NULL,                        -- Quantity of product procured
    ProcurementDate DATE NOT NULL,                -- Date of procurement
    SupplierName VARCHAR(255) NOT NULL,           -- Name of the supplier
    TotalCost DECIMAL(12, 2),                     -- Total cost of the procurement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the procurement record was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete to maintain referential integrity
);

-- Create a table for suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,           -- Name of the supplier
    ContactInfo TEXT,                             -- Contact information for the supplier
    Address TEXT,                                 -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the supplier was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a junction table for product-supplier relationships
CREATE TABLE ProductSuppliers (
    ProductID INT NOT NULL,                       -- Foreign key linking to Products
    SupplierID INT NOT NULL,                      -- Foreign key linking to Suppliers
    PRIMARY KEY (ProductID, SupplierID),          -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,  -- Cascade delete for ProductID
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Cascade delete for SupplierID
);

-- Indexes for optimized queries
CREATE INDEX idx_category_name ON ProductCategories(CategoryName); -- Index for fast category lookup
CREATE INDEX idx_product_name ON Products(ProductName);           -- Index for fast product lookup
CREATE INDEX idx_supplier_name ON Suppliers(SupplierName);        -- Index for fast supplier lookup
```
