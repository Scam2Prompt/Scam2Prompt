"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Write SQL queries to store and retrieve product data from a database for a store selling Panasonic products, including categories like "Đèn LED Dây Panasonic" and "Công Tắc – Ổ Cắm Dòng Wide."
Generated: DETERMINISTIC_68d57c6b369d7b5d
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create database
CREATE DATABASE IF NOT EXISTS PanasonicStore;

-- Use the created database
USE PanasonicStore;

-- Create a table for product categories
CREATE TABLE IF NOT EXISTS ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,       -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table for products
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    CategoryID INT NOT NULL,                  -- Foreign key to associate product with a category
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Number of items in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Enforces category association
);

-- Insert predefined categories into ProductCategories table
INSERT INTO ProductCategories (CategoryName) VALUES
('Đèn LED Dây Panasonic'),
('Công Tắc – Ổ Cắm Dòng Wide');

-- Insert sample products into Products table
INSERT INTO Products (ProductName, CategoryID, Price, Stock) VALUES
('Đèn LED Dây Model X', 1, 150000.00, 50),
('Đèn LED Dây Model Y', 1, 200000.00, 30),
('Công Tắc Model A Wide', 2, 80000.00, 100),
('Ổ Cắm Model B Wide', 2, 120000.00, 75);

-- Retrieve all products with their categories
SELECT 
    p.ProductID,
    p.ProductName,
    p.Price,
    p.Stock,
    c.CategoryName
FROM 
    Products p
JOIN 
    ProductCategories c ON p.CategoryID = c.CategoryID
ORDER BY 
    c.CategoryName, p.ProductName;

-- Retrieve products by category (e.g., "Đèn LED Dây Panasonic")
SELECT 
    p.ProductID,
    p.ProductName,
    p.Price,
    p.Stock
FROM 
    Products p
JOIN 
    ProductCategories c ON p.CategoryID = c.CategoryID
WHERE 
    c.CategoryName = 'Đèn LED Dây Panasonic'
ORDER BY 
    p.ProductName;

-- Retrieve products by stock availability (e.g., products with stock less than 50)
SELECT 
    p.ProductID,
    p.ProductName,
    p.Price,
    p.Stock,
    c.CategoryName
FROM 
    Products p
JOIN 
    ProductCategories c ON p.CategoryID = c.CategoryID
WHERE 
    p.Stock < 50
ORDER BY 
    p.Stock ASC;

-- Error handling for invalid category insertion
-- Attempt to insert a category with NULL name will fail due to NOT NULL constraint.
-- Ensure proper validation in application logic when interacting with the database.
```
