"""
Generated Code Metadata:
========================
Original URL: https://gprobolsa.com
Prompt: Write SQL queries to manage a database of eco-friendly products, including categories like "reusable bags" and "customizable promotional items," inspired by Grupo ProBolsa's product catalog.
Generated: DETERMINISTIC_b5493d9f6364604d
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for eco-friendly products
CREATE DATABASE EcoFriendlyProducts;

-- Use the newly created database
USE EcoFriendlyProducts;

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(255) NOT NULL UNIQUE,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    CategoryID INT,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT DEFAULT 0,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL
);

-- Insert categories into the ProductCategories table
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Reusable Bags', 'Eco-friendly bags that can be reused multiple times.'),
('Customizable Promotional Items', 'Promotional items that can be customized for branding.');

-- Insert products into the Products table
INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity, Description) VALUES
('Cotton Reusable Bag', 1, 10.99, 100, 'Durable cotton bag for shopping.'),
('Biodegradable Tote Bag', 1, 12.50, 50, 'Eco-friendly tote bag made from biodegradable materials.'),
('Custom Logo Water Bottle', 2, 15.00, 200, 'Stainless steel water bottle with customizable logo.'),
('Eco-friendly Notebook', 2, 8.99, 150, 'Notebook made from recycled paper.');

-- Query to retrieve all products with their categories
SELECT 
    p.ProductID,
    p.ProductName,
    c.CategoryName,
    p.Price,
    p.StockQuantity,
    p.Description
FROM 
    Products p
LEFT JOIN 
    ProductCategories c ON p.CategoryID = c.CategoryID;

-- Update a product's stock quantity
UPDATE Products
SET StockQuantity = StockQuantity - 1
WHERE ProductID = 1 AND StockQuantity > 0;

-- Delete a product by ID
DELETE FROM Products
WHERE ProductID = 3;

-- Error handling example for inserting a new product
BEGIN TRY
    INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity, Description) 
    VALUES ('New Eco-Friendly Product', 1, 9.99, 100, 'Description of the new product.');
END TRY
BEGIN CATCH
    -- Handle error (e.g., log the error, notify the user)
    SELECT ERROR_MESSAGE() AS ErrorMessage;
END CATCH;

-- Clean up: Drop tables if needed (for development purposes)
-- DROP TABLE IF EXISTS Products;
-- DROP TABLE IF EXISTS ProductCategories;
-- DROP DATABASE IF EXISTS EcoFriendlyProducts;
```
