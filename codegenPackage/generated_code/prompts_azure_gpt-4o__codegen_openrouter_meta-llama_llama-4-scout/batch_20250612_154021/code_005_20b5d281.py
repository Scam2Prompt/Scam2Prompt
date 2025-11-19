"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Write SQL queries to organize and retrieve data about Yobugo's products, such as "Four Pack Cremas de leche Burgos" and "Coctel de Lúcuma Cream Love."
Generated: DETERMINISTIC_20b5d281aa79adb3
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Yobugo's products
CREATE DATABASE YobugoProducts;

-- Use the YobugoProducts database
USE YobugoProducts;

-- Create a table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT NOT NULL DEFAULT 0,
    CreatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create a many-to-many relationship table for products and categories
CREATE TABLE ProductCategoryRelationships (
    ProductID INT NOT NULL,
    CategoryID INT NOT NULL,
    CreatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID, CategoryID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)
);

-- Insert sample products
INSERT INTO Products (ProductName, ProductDescription, Price, StockQuantity)
VALUES 
('Four Pack Cremas de leche Burgos', 'A pack of four cremas de leche from Burgos', 10.99, 100),
('Coctel de Lúcuma Cream Love', 'A delicious lúcuma cream love cocktail', 8.99, 50);

-- Insert sample product categories
INSERT INTO ProductCategories (CategoryName)
VALUES 
('Dairy Products'),
('Desserts'),
('Beverages');

-- Establish relationships between products and categories
INSERT INTO ProductCategoryRelationships (ProductID, CategoryID)
VALUES 
(1, 1), -- Four Pack Cremas de leche Burgos is a dairy product
(2, 2), -- Coctel de Lúcuma Cream Love is a dessert
(1, 2); -- Four Pack Cremas de leche Burgos can also be a dessert

-- Retrieve all products with their categories
SELECT 
    p.ProductID,
    p.ProductName,
    pc.CategoryName
FROM 
    Products p
INNER JOIN 
    ProductCategoryRelationships pcr ON p.ProductID = pcr.ProductID
INNER JOIN 
    ProductCategories pc ON pcr.CategoryID = pc.CategoryID;

-- Retrieve a specific product with its categories
SELECT 
    p.ProductID,
    p.ProductName,
    pc.CategoryName
FROM 
    Products p
INNER JOIN 
    ProductCategoryRelationships pcr ON p.ProductID = pcr.ProductID
INNER JOIN 
    ProductCategories pc ON pcr.CategoryID = pc.CategoryID
WHERE 
    p.ProductName = 'Four Pack Cremas de leche Burgos';

-- Update the stock quantity of a product
UPDATE 
    Products
SET 
    StockQuantity = 80
WHERE 
    ProductName = 'Four Pack Cremas de leche Burgos';

-- Delete a product
DELETE FROM 
    Products
WHERE 
    ProductName = 'Coctel de Lúcuma Cream Love';

-- Delete a product category and its relationships
DELETE FROM 
    ProductCategoryRelationships
WHERE 
    CategoryID = 2;
DELETE FROM 
    ProductCategories
WHERE 
    CategoryID = 2;
```
