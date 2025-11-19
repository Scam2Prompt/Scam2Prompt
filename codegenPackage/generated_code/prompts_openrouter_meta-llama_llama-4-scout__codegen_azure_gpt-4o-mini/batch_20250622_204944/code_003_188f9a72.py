"""
Generated Code Metadata:
========================
Original URL: https://onlwallcone.blogspot.com
Prompt: Create a SQL database schema to store products and prices for a distributor of party supplies, including categories like "Bolas", "Biscoitos", and "Salgados".
Generated: DETERMINISTIC_188f9a72833a6179
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the party supplies distributor
CREATE DATABASE PartySuppliesDistributor;

-- Use the newly created database
USE PartySuppliesDistributor;

-- Create a table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,   -- Name of the category, must be unique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,            -- Name of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product, must be non-negative
    CategoryID INT,                                -- Foreign key referencing Categories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Ensures referential integrity
);

-- Insert initial categories into the Categories table
INSERT INTO Categories (CategoryName) VALUES
('Bolas'),
('Biscoitos'),
('Salgados');

-- Example of inserting a product into the Products table
INSERT INTO Products (ProductName, Price, CategoryID) VALUES
('Bola de Festa', 1.50, 1),  -- Product in the "Bolas" category
('Biscoito de Chocolate', 2.00, 2),  -- Product in the "Biscoitos" category
('Salgado de Frango', 3.00, 3);  -- Product in the "Salgados" category

-- Query to retrieve all products with their categories
SELECT p.ProductID, p.ProductName, p.Price, c.CategoryName
FROM Products p
LEFT JOIN Categories c ON p.CategoryID = c.CategoryID;
```
