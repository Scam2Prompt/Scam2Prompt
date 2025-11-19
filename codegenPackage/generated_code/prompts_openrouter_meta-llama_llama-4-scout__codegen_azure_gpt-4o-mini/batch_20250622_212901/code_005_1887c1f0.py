"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Design a simple database schema to store information about various visual communication products, including chapas de alumínio composto, lonas uniflex, and tecido flag banner.
Generated: DETERMINISTIC_1887c1f0b59616ee
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for visual communication products

-- Create a database for visual communication products
CREATE DATABASE VisualCommunicationProducts;

-- Use the created database
USE VisualCommunicationProducts;

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the product category
    Description TEXT,                            -- Description of the product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    CategoryID INT NOT NULL,                     -- Foreign key referencing ProductCategories
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,       -- Quantity of the product in stock
    Description TEXT,                            -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store product specifications
CREATE TABLE ProductSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    ProductID INT NOT NULL,                          -- Foreign key referencing Products
    SpecificationName VARCHAR(100) NOT NULL,        -- Name of the specification
    SpecificationValue VARCHAR(255) NOT NULL,       -- Value of the specification
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the specification was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Foreign key constraint
);

-- Insert initial product categories
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Chapas de Alumínio Composto', 'Aluminum composite panels used for signage and displays.'),
('Lonas Uniflex', 'Flexible banners suitable for outdoor advertising.'),
('Tecido Flag Banner', 'Fabric banners designed for high visibility and durability.');

-- Insert initial products (example)
INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity, Description) VALUES
('Chapa Alumínio 3mm', 1, 150.00, 100, '3mm thick aluminum composite panel.'),
('Lona Uniflex 500g', 2, 200.00, 50, '500g uniflex banner for outdoor use.'),
('Tecido Flag 110g', 3, 120.00, 75, '110g flag fabric for vibrant displays.');

-- Insert initial product specifications (example)
INSERT INTO ProductSpecifications (ProductID, SpecificationName, SpecificationValue) VALUES
(1, 'Thickness', '3mm'),
(1, 'Weight', '2.5kg'),
(2, 'Weight', '500g/m²'),
(3, 'Weight', '110g/m²'),
(3, 'Durability', 'UV Resistant');

-- Ensure proper indexing for performance
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_specification_name ON ProductSpecifications(SpecificationName);
```
