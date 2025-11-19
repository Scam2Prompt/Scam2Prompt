"""
Generated Code Metadata:
========================
Original URL: https://homemerce.com
Prompt: "Design a simple database schema to store information about different types of coving products, including their dimensions, materials, and prices, as seen on Homemerce."
Generated: DETERMINISTIC_d9c7037d7bb29081
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing information about coving products

-- Create a database named 'CovingProductsDB'
CREATE DATABASE CovingProductsDB;

-- Use the created database
USE CovingProductsDB;

-- Table to store information about different types of coving products
CREATE TABLE CovingProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the coving product
    Dimensions VARCHAR(100) NOT NULL,          -- Dimensions of the product (e.g., "2m x 10cm")
    Material VARCHAR(100) NOT NULL,             -- Material of the product (e.g., "PVC", "Wood")
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category (e.g., "Coving", "Cornice")
    Description TEXT                             -- Description of the category
);

-- Table to link products to categories (Many-to-Many relationship)
CREATE TABLE ProductCategories (
    ProductID INT,                               -- Foreign key referencing CovingProducts
    CategoryID INT,                              -- Foreign key referencing Categories
    PRIMARY KEY (ProductID, CategoryID),        -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES CovingProducts(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion for Categories
INSERT INTO Categories (CategoryName, Description) VALUES
('Coving', 'Decorative molding used to cover the joint between walls and ceilings.'),
('Cornice', 'A decorative molding that crowns a building or furniture.');

-- Sample data insertion for CovingProducts
INSERT INTO CovingProducts (ProductName, Dimensions, Material, Price) VALUES
('Classic Coving', '2m x 10cm', 'PVC', 15.99),
('Modern Cornice', '3m x 15cm', 'Wood', 29.99);

-- Sample data insertion for ProductCategories
INSERT INTO ProductCategories (ProductID, CategoryID) VALUES
(1, 1),  -- Linking 'Classic Coving' to 'Coving' category
(2, 2);  -- Linking 'Modern Cornice' to 'Cornice' category

-- Query to retrieve all products with their categories
SELECT p.ProductID, p.ProductName, p.Dimensions, p.Material, p.Price, c.CategoryName
FROM CovingProducts p
JOIN ProductCategories pc ON p.ProductID = pc.ProductID
JOIN Categories c ON pc.CategoryID = c.CategoryID;
```
