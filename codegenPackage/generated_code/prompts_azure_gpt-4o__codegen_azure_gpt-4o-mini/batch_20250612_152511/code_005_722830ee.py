"""
Generated Code Metadata:
========================
Original URL: https://irgift.info
Prompt: Create a database schema for an e-commerce platform that categorizes products like "گیفت کارت اپل," "گیفت کارت ایکس باکس," and "جم کلش رویال," ensuring efficient product management.
Generated: DETERMINISTIC_722830eeda4bd432
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ProductCategories;
DROP TABLE IF EXISTS Products;

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category, must be unique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the category was last updated
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,  -- Name of the product
    Description TEXT,  -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product, must be non-negative
    StockQuantity INT NOT NULL CHECK (StockQuantity >= 0),  -- Quantity available in stock, must be non-negative
    CategoryID INT,  -- Foreign key referencing the ProductCategories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL  -- Ensures referential integrity
);

-- Insert initial categories into ProductCategories
INSERT INTO ProductCategories (CategoryName) VALUES
('گیفت کارت اپل'),
('گیفت کارت ایکس باکس'),
('جم کلش رویال');

-- Example of inserting a product into Products
INSERT INTO Products (ProductName, Description, Price, StockQuantity, CategoryID) VALUES
('Apple Gift Card', 'Gift card for Apple services.', 50.00, 100, 1),
('Xbox Gift Card', 'Gift card for Xbox services.', 50.00, 150, 2),
('Clash Royale Gems', 'In-game currency for Clash Royale.', 10.00, 200, 3);

-- Query to retrieve all products with their categories
SELECT p.ProductID, p.ProductName, p.Description, p.Price, p.StockQuantity, c.CategoryName
FROM Products p
LEFT JOIN ProductCategories c ON p.CategoryID = c.CategoryID;
```
