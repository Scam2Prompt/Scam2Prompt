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
-- Database schema to store information about visual communication products

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the product category
    Description TEXT                           -- Optional description of the category
);

-- Create a table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategories
    Material VARCHAR(255),                     -- Material used for the product
    Dimensions VARCHAR(255),                   -- Dimensions of the product (e.g., "2m x 3m")
    Weight DECIMAL(10, 2),                     -- Weight of the product in kilograms
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Enforce category relationship
);

-- Insert sample data into ProductCategories
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
    ('Chapas de Alumínio Composto', 'Composite aluminum sheets used for signage and decoration'),
    ('Lonas Uniflex', 'Durable and flexible tarpaulins for outdoor advertising'),
    ('Tecido Flag Banner', 'Fabric banners used for promotional flags');

-- Insert sample data into Products
INSERT INTO Products (ProductName, CategoryID, Material, Dimensions, Weight, Price, StockQuantity)
VALUES 
    ('Aluminum Sheet 2mm', 1, 'Aluminum Composite', '2m x 3m', 5.50, 120.00, 50),
    ('Uniflex Banner 3m', 2, 'PVC', '3m x 5m', 2.80, 75.00, 100),
    ('Flag Banner Large', 3, 'Polyester', '1.5m x 2m', 1.20, 45.00, 200);

-- Query to retrieve all products with their category names
SELECT 
    p.ProductID,
    p.ProductName,
    c.CategoryName,
    p.Material,
    p.Dimensions,
    p.Weight,
    p.Price,
    p.StockQuantity,
    p.CreatedAt,
    p.UpdatedAt
FROM 
    Products p
JOIN 
    ProductCategories c
ON 
    p.CategoryID = c.CategoryID;
```
