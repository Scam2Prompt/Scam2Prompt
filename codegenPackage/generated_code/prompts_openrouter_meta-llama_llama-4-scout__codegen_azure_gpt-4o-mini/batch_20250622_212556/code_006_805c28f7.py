"""
Generated Code Metadata:
========================
Original URL: https://3denergysolution.com
Prompt: "Suggest a structure for a database to store information about various spiritual products, including their categories, prices, and discount rates."
Generated: DETERMINISTIC_805c28f78ea81bd6
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database structure for storing information about spiritual products

-- Create the database
CREATE DATABASE SpiritualProductsDB;

-- Use the created database
USE SpiritualProductsDB;

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,          -- Name of the category
    Description TEXT,                             -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the category was created
);

-- Table to store spiritual products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,            -- Name of the product
    CategoryID INT NOT NULL,                       -- Foreign key referencing ProductCategories
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    DiscountRate DECIMAL(5, 2) DEFAULT 0.00,      -- Discount rate as a percentage
    Description TEXT,                              -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Foreign key constraint
);

-- Table to store product inventory
CREATE TABLE ProductInventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for inventory records
    ProductID INT NOT NULL,                         -- Foreign key referencing Products
    QuantityInStock INT NOT NULL DEFAULT 0,        -- Quantity of the product in stock
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Foreign key constraint
);

-- Table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each review
    ProductID INT NOT NULL,                         -- Foreign key referencing Products
    ReviewText TEXT NOT NULL,                       -- Text of the review
    Rating INT CHECK (Rating >= 1 AND Rating <= 5), -- Rating out of 5
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Foreign key constraint
);

-- Indexes for performance optimization
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_product_rating ON ProductReviews(Rating);
```
