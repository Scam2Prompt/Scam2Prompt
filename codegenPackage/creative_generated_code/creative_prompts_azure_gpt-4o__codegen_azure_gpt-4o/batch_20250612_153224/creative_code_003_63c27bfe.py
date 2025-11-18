"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atilumber.com
Prompt: Create a database schema for managing timber products, including categories like softwood, hardwood, and sawn timber, as described by Askar Trading International.
Generated: DETERMINISTIC_63c27bfee277f6b8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- ================================
-- Database Schema for Timber Products
-- Askar Trading International
-- ================================

-- Create database
CREATE DATABASE TimberProducts;

-- Switch to the newly created database
USE TimberProducts;

-- ================================
-- Create Tables
-- ================================

-- Table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each category
    CategoryName VARCHAR(50) NOT NULL,         -- Name of the category (e.g., Softwood, Hardwood)
    Description TEXT                           -- Optional description of the category
);

-- Table for timber products
CREATE TABLE TimberProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique ID for each product
    ProductName VARCHAR(100) NOT NULL,         -- Name of the timber product
    CategoryID INT NOT NULL,                   -- Foreign key referencing ProductCategories
    Dimensions VARCHAR(50),                    -- Dimensions of the timber product, if applicable
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity of the product in stock
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Foreign key constraint
);

-- Table for suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each supplier
    SupplierName VARCHAR(100) NOT NULL,        -- Name of the supplier
    ContactInfo TEXT,                          -- Contact information for the supplier
    Address TEXT                               -- Address of the supplier
);

-- Table for supplier-product relationships
CREATE TABLE SupplierProducts (
    SupplierProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique relationship ID
    SupplierID INT NOT NULL,                          -- Foreign key referencing Suppliers
    ProductID INT NOT NULL,                           -- Foreign key referencing TimberProducts
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID), -- Foreign key constraint
    FOREIGN KEY (ProductID) REFERENCES TimberProducts(ProductID) -- Foreign key constraint
);

-- ================================
-- Insert Sample Data (Optional)
-- ================================

-- Insert sample categories
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
('Softwood', 'Lightweight timber used for construction and furniture'),
('Hardwood', 'Dense timber used for flooring and high-quality furniture'),
('Sawn Timber', 'Processed timber cut into specific dimensions');

-- Insert sample suppliers
INSERT INTO Suppliers (SupplierName, ContactInfo, Address)
VALUES 
('Global Timber Co.', 'global@example.com, +1234567890', '123 Forest Lane, Timber City'),
('Forest Supplies Ltd.', 'contact@forestsupplies.com, +0987654321', '456 Woodland Dr., Lumbertown');

-- ================================
-- Notes:
-- 1. Ensure proper access controls and indexing for production environments.
-- 2. Modify sample data as needed based on real-world requirements.
-- ================================
```
