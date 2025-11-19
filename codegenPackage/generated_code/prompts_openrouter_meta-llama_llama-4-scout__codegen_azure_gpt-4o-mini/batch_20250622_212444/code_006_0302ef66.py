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
-- Database schema for a construction supply company's product catalog

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store suppliers
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL,         -- Name of the supplier
    ContactName VARCHAR(100),                    -- Name of the contact person at the supplier
    Phone VARCHAR(15),                           -- Phone number of the supplier
    Email VARCHAR(100),                          -- Email address of the supplier
    Address VARCHAR(255),                        -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the supplier was last updated
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,        -- Quantity of the product in stock
    CategoryID INT,                               -- Foreign key referencing Categories
    SupplierID INT,                               -- Foreign key referencing Suppliers
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL, -- Ensures referential integrity
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE SET NULL  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_category_name ON Categories(CategoryName);
CREATE INDEX idx_supplier_name ON Suppliers(SupplierName);
```
