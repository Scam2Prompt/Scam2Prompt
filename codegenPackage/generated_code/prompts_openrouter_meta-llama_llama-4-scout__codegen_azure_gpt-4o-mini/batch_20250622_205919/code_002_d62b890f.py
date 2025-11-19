"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: "Generate a SQL query to manage inventory of nuts and bolts for a hardware store like APN Hardware, including product categories and pricing."
Generated: DETERMINISTIC_d62b890f7686956c
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to manage inventory of nuts and bolts for APN Hardware

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the product category
    Description TEXT                             -- Description of the category
);

-- Create a table to store products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product
    CategoryID INT,                               -- Foreign key referencing ProductCategories
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product, must be non-negative
    StockQuantity INT NOT NULL CHECK (StockQuantity >= 0),  -- Quantity in stock, must be non-negative
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)  -- Establish foreign key relationship
);

-- Insert sample product categories
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Nuts', 'Various types of nuts for hardware applications'),
('Bolts', 'Different sizes and types of bolts for construction');

-- Insert sample products
INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity) VALUES
('Hex Nut', 1, 0.05, 100),  -- Hex nut under Nuts category
('Carriage Bolt', 2, 0.15, 200);  -- Carriage bolt under Bolts category

-- Query to retrieve all products with their categories and pricing
SELECT 
    p.ProductID,
    p.ProductName,
    pc.CategoryName,
    p.Price,
    p.StockQuantity,
    p.CreatedAt,
    p.UpdatedAt
FROM 
    Products p
JOIN 
    ProductCategories pc ON p.CategoryID = pc.CategoryID
ORDER BY 
    pc.CategoryName, p.ProductName;  -- Order by category and product name

-- Error handling: Ensure that the operations are wrapped in a transaction
START TRANSACTION;

-- Example of updating a product's stock quantity
UPDATE Products
SET StockQuantity = StockQuantity - 1
WHERE ProductID = 1 AND StockQuantity > 0;  -- Ensure stock is available

-- Commit the transaction if successful
COMMIT;

-- Rollback in case of an error
ROLLBACK;
```
