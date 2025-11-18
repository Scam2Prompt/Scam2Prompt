"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Create an SQL database schema to store product information for a plastic manufacturing company, including categories like "Indoor and Outdoor Planters," "Shelves," and "Plastic Furniture," as described on the Samba Plastic Industries website.
Generated: DETERMINISTIC_fbb1d39f55421a05
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for storing product information for a plastic manufacturing company

-- DROP the database if it exists, then create a new one
DROP DATABASE IF EXISTS PlasticManufacturingDB;
CREATE DATABASE PlasticManufacturingDB;

-- Use the newly created database
USE PlasticManufacturingDB;

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the product category (e.g., Indoor and Outdoor Planters, Shelves, etc.)
    Description TEXT                           -- Optional description of the category
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategories
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                -- Quantity of the product in stock
    ProductDescription TEXT,                   -- Optional description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Insert sample category data
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
    ('Indoor and Outdoor Planters', 'Planters that can enhance your indoor and outdoor spaces'),
    ('Shelves', 'Durable shelves made of quality plastic materials'),
    ('Plastic Furniture', 'Comfortable and lightweight furniture made from plastic');

-- Insert sample product data
INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity, ProductDescription)
VALUES
    ('Round Planter', 1, 19.95, 150, 'A classic round planter suitable for flowers and small plants'),
    ('Square Planter', 1, 24.50, 120, 'Perfect for medium-sized plants and shrubs'),
    ('Wall Shelf', 2, 35.00, 80, 'Compact wall-mounted shelf for home or office'),
    ('Plastic Chair', 3, 49.99, 60, 'Ergonomic design for maximum comfort'),
    ('Plastic Table', 3, 89.99, 40, 'Lightweight yet sturdy table suitable for indoor and outdoor use');

-- Query to check the inserted data (optional, for testing purposes)
SELECT * FROM ProductCategories;
SELECT * FROM Products;

-- Ensure proper indexing for faster queries
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_category_id ON Products(CategoryID);
```
