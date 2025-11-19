"""
Generated Code Metadata:
========================
Original URL: https://www.panasonics.com.vn
Prompt: Write SQL queries to store and retrieve product data from a database for a store selling Panasonic products, including categories like "Đèn LED Dây Panasonic" and "Công Tắc – Ổ Cắm Dòng Wide."
Generated: DETERMINISTIC_68d57c6b369d7b5d
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for store
CREATE DATABASE PanasonicStore;

-- Use database
USE PanasonicStore;

-- Create table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName NVARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName NVARCHAR(255) NOT NULL,
    CategoryID INT,
    Price DECIMAL(18, 2) NOT NULL,
    StockQuantity INT NOT NULL DEFAULT 0,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)
);

-- Insert sample product categories
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
('Đèn LED Dây Panasonic', 'Đèn LED dây Panasonic chất lượng cao'),
('Công Tắc – Ổ Cắm Dòng Wide', 'Công tắc và ổ cắm dòng Wide của Panasonic');

-- Insert sample products
INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity, Description)
VALUES 
('Đèn LED Dây Panasonic 5m', 1, 250000.00, 100, 'Đèn LED dây Panasonic 5m'),
('Công Tắc Đơn Panasonic', 2, 50000.00, 50, 'Công tắc đơn Panasonic dòng Wide'),
('Ổ Cắm 3 Lỗ Panasonic', 2, 80000.00, 75, 'Ổ cắm 3 lỗ Panasonic dòng Wide');

-- Retrieve all products
SELECT 
    p.ProductID,
    p.ProductName,
    pc.CategoryName,
    p.Price,
    p.StockQuantity,
    p.Description
FROM 
    Products p
INNER JOIN 
    ProductCategories pc ON p.CategoryID = pc.CategoryID;

-- Retrieve product by ID
SELECT 
    p.ProductID,
    p.ProductName,
    pc.CategoryName,
    p.Price,
    p.StockQuantity,
    p.Description
FROM 
    Products p
INNER JOIN 
    ProductCategories pc ON p.CategoryID = pc.CategoryID
WHERE 
    p.ProductID = ?;

-- Update product
UPDATE 
    Products
SET 
    ProductName = ?,
    CategoryID = ?,
    Price = ?,
    StockQuantity = ?,
    Description = ?
WHERE 
    ProductID = ?;

-- Delete product
DELETE FROM 
    Products
WHERE 
    ProductID = ?;
```
