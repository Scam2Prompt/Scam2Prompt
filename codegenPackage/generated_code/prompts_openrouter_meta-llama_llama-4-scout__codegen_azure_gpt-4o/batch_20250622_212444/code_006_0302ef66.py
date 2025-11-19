"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: "Design a database schema for a construction supply company's product catalog, including tables for products, categories, and suppliers, using a SQL-like syntax."
Generated: DETERMINISTIC_0302ef667ff1d669
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Construction Supply Company's Product Catalog

-- Table: Categories
-- This table stores the categories of products.
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category
    Description TEXT                           -- Optional description of the category
);

-- Table: Suppliers
-- This table stores information about suppliers.
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactName VARCHAR(255),                  -- Name of the contact person
    Phone VARCHAR(50),                         -- Phone number of the supplier
    Email VARCHAR(255),                        -- Email address of the supplier
    Address TEXT                               -- Address of the supplier
);

-- Table: Products
-- This table stores information about products.
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                -- Quantity of the product in stock
    CategoryID INT NOT NULL,                   -- Foreign key referencing Categories table
    SupplierID INT NOT NULL,                   -- Foreign key referencing Suppliers table
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE, -- Cascade delete for category
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE SET NULL  -- Set supplier to NULL on delete
);

-- Indexes for faster lookups
CREATE INDEX idx_category_id ON Products(CategoryID); -- Index for CategoryID in Products table
CREATE INDEX idx_supplier_id ON Products(SupplierID); -- Index for SupplierID in Products table
```
