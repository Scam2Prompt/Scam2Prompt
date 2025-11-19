"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Write a database schema for storing product details, including categories, sizes, and warranty information, based on the diverse product offerings mentioned on the TDKCO website.
Generated: DETERMINISTIC_fa77c24f81ab91a6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing product details, including categories, sizes, and warranty information

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the category was last updated
);

-- Create a table for product sizes
CREATE TABLE ProductSizes (
    SizeID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each size
    SizeName VARCHAR(50) NOT NULL UNIQUE,        -- Name of the size (e.g., S, M, L, XL)
    Description TEXT,                            -- Description of the size
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the size was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the size was last updated
);

-- Create a table for warranty information
CREATE TABLE WarrantyInformation (
    WarrantyID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each warranty
    WarrantyPeriod VARCHAR(50) NOT NULL,         -- Duration of the warranty (e.g., "1 year", "2 years")
    WarrantyDetails TEXT,                         -- Additional details about the warranty
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the warranty was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the warranty was last updated
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product, must be non-negative
    CategoryID INT,                               -- Foreign key referencing ProductCategories
    SizeID INT,                                   -- Foreign key referencing ProductSizes
    WarrantyID INT,                               -- Foreign key referencing WarrantyInformation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL,  -- Handle category deletion
    FOREIGN KEY (SizeID) REFERENCES ProductSizes(SizeID) ON DELETE SET NULL,  -- Handle size deletion
    FOREIGN KEY (WarrantyID) REFERENCES WarrantyInformation(WarrantyID) ON DELETE SET NULL  -- Handle warranty deletion
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_category ON Products(CategoryID);
CREATE INDEX idx_size ON Products(SizeID);
CREATE INDEX idx_warranty ON Products(WarrantyID);
```
