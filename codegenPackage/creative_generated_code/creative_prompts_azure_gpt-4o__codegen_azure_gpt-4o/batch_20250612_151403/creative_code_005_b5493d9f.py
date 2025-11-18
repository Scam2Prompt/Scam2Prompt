"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Write SQL queries to manage a database of eco-friendly products, including categories like "reusable bags" and "customizable promotional items," inspired by Grupo ProBolsa's product catalog.
Generated: DETERMINISTIC_b5493d9f6364604d
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for eco-friendly products
CREATE DATABASE EcoFriendlyProducts;

-- Switch to the EcoFriendlyProducts database
USE EcoFriendlyProducts;

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,       -- Name of the category
    Description TEXT,                         -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the category was created
);

-- Create a table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    CategoryID INT NOT NULL,                  -- Foreign key to ProductCategories
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Stock quantity available
    EcoRating INT CHECK (EcoRating BETWEEN 1 AND 5), -- Eco-friendly rating (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Enforce category relationship
);

-- Insert sample data into ProductCategories
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
    ('Reusable Bags', 'Eco-friendly bags made from sustainable materials'),
    ('Customizable Promotional Items', 'Eco-friendly promotional items that can be customized');

-- Insert sample data into Products
INSERT INTO Products (ProductName, CategoryID, Price, Stock, EcoRating)
VALUES 
    ('Canvas Tote Bag', 1, 15.99, 100, 5),
    ('Recycled Plastic Bag', 1, 12.50, 200, 4),
    ('Eco-Friendly Pen', 2, 2.99, 500, 4),
    ('Customizable Notebook', 2, 9.99, 300, 5);

-- Query to fetch all categories
SELECT * FROM ProductCategories;

-- Query to fetch all products with their category name
SELECT 
    p.ProductID,
    p.ProductName,
    p.Price,
    p.Stock,
    p.EcoRating,
    c.CategoryName
FROM Products p
JOIN ProductCategories c ON p.CategoryID = c.CategoryID;

-- Query to fetch products with an eco-rating of 5
SELECT 
    ProductID,
    ProductName,
    Price,
    Stock,
    EcoRating
FROM Products
WHERE EcoRating = 5;

-- Query to update stock for a specific product
UPDATE Products
SET Stock = Stock - 10 -- Reduce stock by 10 units
WHERE ProductName = 'Canvas Tote Bag' AND Stock >= 10;

-- Error handling: Ensure stock is not negative
UPDATE Products
SET Stock = 0
WHERE Stock < 0;

-- Query to delete a category (cascade delete on related products)
-- Note: Foreign key constraints must be set up to cascade delete
DELETE FROM ProductCategories
WHERE CategoryName = 'Customizable Promotional Items';

-- Query to add a new eco-friendly product
INSERT INTO Products (ProductName, CategoryID, Price, Stock, EcoRating)
VALUES ('Bamboo Utensil Set', 1, 20.00, 150, 5);

-- Query to fetch products that are in stock
SELECT 
    ProductID,
    ProductName,
    Price,
    Stock
FROM Products
WHERE Stock > 0;

-- Query to list products sorted by eco-rating (highest first) and price (lowest first)
SELECT 
    ProductID,
    ProductName,
    Price,
    Stock,
    EcoRating
FROM Products
ORDER BY EcoRating DESC, Price ASC;
```
