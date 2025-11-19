"""
Generated Code Metadata:
========================
Original URL: https://www.cymrepuestos.com.ar
Prompt: "Create a database schema for storing information about automotive spare parts, including product categories, brands, and supplier details, inspired by CYM Repuestos' product offerings."
Generated: DETERMINISTIC_2ed20f62577f434c
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about automotive spare parts

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "Engine Parts", "Brakes")
    Description TEXT                           -- Optional description of the category
);

-- Table to store brands
CREATE TABLE Brands (
    BrandID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each brand
    BrandName VARCHAR(255) NOT NULL,           -- Name of the brand (e.g., "Bosch", "Toyota")
    Country VARCHAR(100)                       -- Country of origin for the brand
);

-- Table to store supplier details
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,        -- Name of the supplier
    ContactName VARCHAR(255),                  -- Name of the contact person at the supplier
    Phone VARCHAR(50),                         -- Phone number of the supplier
    Email VARCHAR(255),                        -- Email address of the supplier
    Address TEXT                               -- Physical address of the supplier
);

-- Table to store spare parts information
CREATE TABLE SpareParts (
    PartID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each spare part
    PartName VARCHAR(255) NOT NULL,            -- Name of the spare part (e.g., "Brake Pad", "Oil Filter")
    CategoryID INT NOT NULL,                   -- Foreign key referencing ProductCategories
    BrandID INT NOT NULL,                      -- Foreign key referencing Brands
    SupplierID INT NOT NULL,                   -- Foreign key referencing Suppliers
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the spare part
    StockQuantity INT NOT NULL,                -- Quantity of the spare part in stock
    Description TEXT,                          -- Optional description of the spare part
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Foreign key constraints
ALTER TABLE SpareParts
ADD CONSTRAINT FK_SpareParts_Category FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE SpareParts
ADD CONSTRAINT FK_SpareParts_Brand FOREIGN KEY (BrandID) REFERENCES Brands(BrandID)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE SpareParts
ADD CONSTRAINT FK_SpareParts_Supplier FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
ON DELETE CASCADE ON UPDATE CASCADE;

-- Indexes for faster lookups
CREATE INDEX IDX_ProductCategories_CategoryName ON ProductCategories(CategoryName);
CREATE INDEX IDX_Brands_BrandName ON Brands(BrandName);
CREATE INDEX IDX_Suppliers_SupplierName ON Suppliers(SupplierName);
CREATE INDEX IDX_SpareParts_PartName ON SpareParts(PartName);
```
