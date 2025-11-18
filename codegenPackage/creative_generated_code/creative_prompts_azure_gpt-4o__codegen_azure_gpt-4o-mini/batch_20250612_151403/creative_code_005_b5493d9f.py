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
-- SQL script to manage a database of eco-friendly products

-- Step 1: Create a database for eco-friendly products
CREATE DATABASE EcoFriendlyProducts;

-- Step 2: Use the newly created database
USE EcoFriendlyProducts;

-- Step 3: Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the product category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the category was created
);

-- Step 4: Create a table for eco-friendly products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    CategoryID INT,                              -- Foreign key to the ProductCategories table
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    Stock INT DEFAULT 0,                         -- Stock quantity of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Ensures referential integrity
);

-- Step 5: Insert sample categories into the ProductCategories table
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Reusable Bags', 'Eco-friendly bags that can be reused multiple times.'),
('Customizable Promotional Items', 'Promotional items that can be customized for branding.');

-- Step 6: Insert sample products into the Products table
INSERT INTO Products (ProductName, CategoryID, Price, Stock) VALUES
('Organic Cotton Tote Bag', 1, 15.99, 100),
('Eco-Friendly Jute Bag', 1, 12.49, 50),
('Custom Printed Water Bottle', 2, 9.99, 200),
('Biodegradable Phone Case', 2, 14.99, 150);

-- Step 7: Query to retrieve all products with their categories
SELECT 
    p.ProductID,
    p.ProductName,
    c.CategoryName,
    p.Price,
    p.Stock
FROM 
    Products p
JOIN 
    ProductCategories c ON p.CategoryID = c.CategoryID;

-- Step 8: Update a product's stock
UPDATE Products
SET Stock = Stock - 1
WHERE ProductID = 1;  -- Example: reducing stock for the product with ID 1

-- Step 9: Error handling using a transaction
START TRANSACTION;

BEGIN TRY
    -- Example operation that might cause an error
    INSERT INTO Products (ProductName, CategoryID, Price, Stock) VALUES
    ('Non-Toxic Lunch Box', 1, 19.99, 30);
    
    COMMIT;  -- Commit transaction if no errors occurred
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;  -- Rollback transaction if any error occurred
        -- Log the error or handle it accordingly
END TRY;
```
