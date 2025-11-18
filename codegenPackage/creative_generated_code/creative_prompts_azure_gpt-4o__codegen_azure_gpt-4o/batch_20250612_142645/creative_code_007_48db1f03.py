"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: Recommend a database schema for managing inventory in an e-commerce platform selling laminated, reflective, and decorative glass products, and provide SQL queries for basic operations.
Generated: DETERMINISTIC_48db1f030bfdbbbf
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for the Inventory Management System

-- Table to store categories of products
CREATE TABLE ProductCategory (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL,                -- Name of the category (e.g., Laminated, Reflective)
    Description TEXT                           -- Description of the category
);

-- Table to store products
CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,                -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategory
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL DEFAULT 0,              -- Quantity of product available in inventory
    Description TEXT,                          -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (CategoryID) REFERENCES ProductCategory(CategoryID) -- Ensures category exists
);

-- Table to track stock transactions (e.g., sales, restocking)
CREATE TABLE StockTransaction (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each transaction
    ProductID INT NOT NULL,                           -- Foreign key linking to Product
    Quantity INT NOT NULL,                            -- Quantity involved in the transaction
    TransactionType ENUM('SALE', 'RESTOCK') NOT NULL, -- Type of transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of transaction
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) -- Ensures product exists
);

-- Basic SQL Queries for Operations

-- 1. Add a new product category
INSERT INTO ProductCategory (Name, Description) 
VALUES ('Laminated Glass', 'Durable and shatter-resistant glass ideal for safety applications.');

-- 2. Add a new product
INSERT INTO Product (Name, CategoryID, Price, Stock, Description) 
VALUES ('Decorative Glass Panel', 3, 150.00, 50, 'Beautifully designed panel for interior decoration.');

-- 3. Update stock for a product (e.g., restocking)
UPDATE Product 
SET Stock = Stock + 20, UpdatedAt = CURRENT_TIMESTAMP 
WHERE ProductID = 1;

-- 4. Record a stock transaction (e.g., sale)
INSERT INTO StockTransaction (ProductID, Quantity, TransactionType) 
VALUES (1, -5, 'SALE');

-- 5. Fetch all products and their categories
SELECT 
    P.ProductID, 
    P.Name AS ProductName, 
    C.Name AS CategoryName, 
    P.Price, 
    P.Stock, 
    P.Description 
FROM Product P
JOIN ProductCategory C ON P.CategoryID = C.CategoryID;

-- 6. Fetch stock transactions for a specific product
SELECT 
    T.TransactionID, 
    T.ProductID, 
    T.Quantity, 
    T.TransactionType, 
    T.TransactionDate 
FROM StockTransaction T
WHERE T.ProductID = 1;

-- 7. Delete a product (with cascade deletion for related stock transactions)
DELETE FROM Product WHERE ProductID = 1;
```
