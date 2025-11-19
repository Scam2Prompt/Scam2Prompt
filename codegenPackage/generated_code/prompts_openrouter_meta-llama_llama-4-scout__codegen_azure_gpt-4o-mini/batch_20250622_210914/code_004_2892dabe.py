"""
Generated Code Metadata:
========================
Original URL: https://www.kff.org.kw
Prompt: "Design a basic database schema for storing information about agricultural products and their prices in Kuwait."
Generated: DETERMINISTIC_2892dabe5c50f819
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about agricultural products and their prices in Kuwait

-- Create a database for agricultural products
CREATE DATABASE IF NOT EXISTS AgricultureDB;

-- Use the created database
USE AgricultureDB;

-- Table to store information about agricultural products
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the agricultural product
    Category VARCHAR(100) NOT NULL,             -- Category of the product (e.g., fruits, vegetables)
    Description TEXT,                           -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store pricing information for products
CREATE TABLE IF NOT EXISTS ProductPrices (
    PriceID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each price entry
    ProductID INT NOT NULL,                     -- Foreign key referencing Products table
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    Currency VARCHAR(10) DEFAULT 'KWD',         -- Currency of the price (default is Kuwaiti Dinar)
    EffectiveDate DATE NOT NULL,                -- Date when the price becomes effective
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about suppliers
CREATE TABLE IF NOT EXISTS Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,         -- Name of the supplier
    ContactInfo VARCHAR(255),                    -- Contact information for the supplier
    Address VARCHAR(255),                        -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the supplier was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to link products with their suppliers
CREATE TABLE IF NOT EXISTS ProductSuppliers (
    ProductSupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product-supplier link
    ProductID INT NOT NULL,                          -- Foreign key referencing Products table
    SupplierID INT NOT NULL,                         -- Foreign key referencing Suppliers table
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_product_category ON Products(Category);
CREATE INDEX idx_supplier_name ON Suppliers(SupplierName);
```
