"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Design a database schema in SQL for managing inventory of acrylic yarn products, based on the offerings of Ramji Acro.
Generated: DETERMINISTIC_94d1acd1397a40c8
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing inventory of acrylic yarn products

-- Create a database for the inventory management system
CREATE DATABASE IF NOT EXISTS RamjiAcroInventory;

-- Use the created database
USE RamjiAcroInventory;

-- Table to store information about yarn categories
CREATE TABLE IF NOT EXISTS YarnCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the yarn category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about yarn products
CREATE TABLE IF NOT EXISTS YarnProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the yarn product
    CategoryID INT NOT NULL,                      -- Foreign key referencing YarnCategories
    Color VARCHAR(50) NOT NULL,                  -- Color of the yarn
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the yarn product
    StockQuantity INT NOT NULL DEFAULT 0,        -- Quantity in stock
    Supplier VARCHAR(100),                        -- Supplier of the yarn product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES YarnCategories(CategoryID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store information about yarn suppliers
CREATE TABLE IF NOT EXISTS YarnSuppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL,           -- Name of the supplier
    ContactEmail VARCHAR(100),                     -- Contact email of the supplier
    PhoneNumber VARCHAR(15),                       -- Phone number of the supplier
    Address TEXT,                                  -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the supplier was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store inventory transactions (e.g., purchases, sales)
CREATE TABLE IF NOT EXISTS InventoryTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each transaction
    ProductID INT NOT NULL,                         -- Foreign key referencing YarnProducts
    TransactionType ENUM('Purchase', 'Sale') NOT NULL, -- Type of transaction
    Quantity INT NOT NULL,                          -- Quantity involved in the transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    FOREIGN KEY (ProductID) REFERENCES YarnProducts(ProductID) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes for performance optimization
CREATE INDEX idx_category_name ON YarnCategories(CategoryName);
CREATE INDEX idx_product_name ON YarnProducts(ProductName);
CREATE INDEX idx_supplier_name ON YarnSuppliers(SupplierName);
CREATE INDEX idx_transaction_date ON InventoryTransactions(TransactionDate);
```
