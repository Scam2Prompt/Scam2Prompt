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
-- Create a new database for Panasonic products
CREATE DATABASE PanasonicStore;

-- Use the PanasonicStore database
USE PanasonicStore;

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(255) NOT NULL UNIQUE,
    Description TEXT
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    CategoryID INT,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT DEFAULT 0,
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE
);

-- Insert categories into the ProductCategories table
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Đèn LED Dây Panasonic', 'High-quality LED strip lights from Panasonic.'),
('Công Tắc – Ổ Cắm Dòng Wide', 'Wide range of switches and sockets from Panasonic.');

-- Insert products into the Products table
INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity) VALUES
('Đèn LED Dây 5m', 1, 350000.00, 100),
('Công Tắc 2 Nút Panasonic', 2, 75000.00, 200),
('Công Tắc 1 Nút Panasonic', 2, 50000.00, 150);

-- Query to retrieve all products with their category names
SELECT 
    p.ProductID,
    p.ProductName,
    c.CategoryName,
    p.Price,
    p.StockQuantity
FROM 
    Products p
JOIN 
    ProductCategories c ON p.CategoryID = c.CategoryID
ORDER BY 
    p.ProductID;

-- Update a product's stock quantity (example: reduce stock)
UPDATE Products
SET StockQuantity = StockQuantity - 1
WHERE ProductID = 1 AND StockQuantity > 0;

-- Delete a product by its ID
DELETE FROM Products
WHERE ProductID = 2;

-- Handling errors for transactions (example)
START TRANSACTION;

-- An example transaction to insert a new product
BEGIN TRY
    INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity) 
    VALUES ('Đèn LED Dây 10m', 1, 650000.00, 50);
    COMMIT;  -- Commit the transaction if successful
END TRY
BEGIN CATCH
    ROLLBACK;  -- Rollback if there's an error
    -- Handle the error here (log it, raise an error, etc.)
END CATCH;

-- Query to retrieve products by a specific category
SELECT 
    p.ProductID,
    p.ProductName,
    p.Price,
    p.StockQuantity
FROM 
    Products p
WHERE 
    p.CategoryID = (SELECT CategoryID FROM ProductCategories WHERE CategoryName = 'Đèn LED Dây Panasonic');
```
