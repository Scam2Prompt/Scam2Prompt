"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: "Design a database schema for storing product information, including details about rocadeiras Toyama TBC33X and motores diesel Toyama TDE130EXP."
Generated: DETERMINISTIC_24cb989a6d071927
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing product information

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the product category
    Description TEXT                             -- Description of the product category
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product
    CategoryID INT NOT NULL,                      -- Foreign key referencing ProductCategories
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,        -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Foreign key constraint
);

-- Insert product categories
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Rocadeiras', 'Machines for cutting grass and vegetation.'),
('Motores Diesel', 'Diesel engines for various applications.');

-- Insert specific products
INSERT INTO Products (ProductName, CategoryID, Description, Price, StockQuantity) VALUES
('Rocadeira Toyama TBC33X', 1, 'A powerful grass cutting machine ideal for large areas.', 1200.00, 10),
('Motor Diesel Toyama TDE130EXP', 2, 'A reliable diesel engine suitable for various machinery.', 2500.00, 5);

-- Query to retrieve all products with their categories
SELECT p.ProductID, p.ProductName, c.CategoryName, p.Description, p.Price, p.StockQuantity
FROM Products p
JOIN ProductCategories c ON p.CategoryID = c.CategoryID;

-- Error handling can be implemented in application code when executing these SQL statements.
```
