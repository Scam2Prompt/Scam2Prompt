"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Generate a SQL query to retrieve a list of products and their corresponding prices for a maritime supply company that offers electrical equipment, tools, and personal protective equipment.
Generated: DETERMINISTIC_cc03d357cc21e8b4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve a list of products and their corresponding prices for a maritime supply company

-- Define the database schema
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    ProductCategory VARCHAR(100) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Description TEXT
);

-- Insert sample data
INSERT INTO Products (ProductID, ProductName, ProductCategory, Price, Description)
VALUES
(1, 'Marine Grade Electrical Outlet', 'Electrical Equipment', 25.00, 'Water-resistant outlet for marine use'),
(2, 'Insulated Screwdriver', 'Tools', 15.00, 'Insulated screwdriver for electrical work'),
(3, 'Life Jacket', 'Personal Protective Equipment', 50.00, 'Type I life jacket for marine use'),
(4, 'Circuit Breaker', 'Electrical Equipment', 30.00, 'Marine grade circuit breaker'),
(5, 'Wrench Set', 'Tools', 40.00, 'Set of combination wrenches'),
(6, 'Safety Glasses', 'Personal Protective Equipment', 10.00, 'Protective eyewear for marine work');

-- SQL query to retrieve a list of products and their corresponding prices
SELECT 
    p.ProductID,
    p.ProductName,
    p.ProductCategory,
    p.Price
FROM 
    Products p
ORDER BY 
    p.ProductCategory, 
    p.ProductName;

-- Error handling example: Check if the Products table exists
SELECT 
    name 
FROM 
    sqlite_master 
WHERE 
    type='table' AND name='Products';

-- Retrieve products with prices greater than a specified amount
CREATE OR REPLACE FUNCTION GetProductsByPrice(minPrice DECIMAL(10, 2))
RETURNS TABLE (
    ProductID INT,
    ProductName VARCHAR(255),
    ProductCategory VARCHAR(100),
    Price DECIMAL(10, 2)
) AS $$
BEGIN
    RETURN QUERY 
    SELECT 
        p.ProductID,
        p.ProductName,
        p.ProductCategory,
        p.Price
    FROM 
        Products p
    WHERE 
        p.Price > minPrice
    ORDER BY 
        p.ProductCategory, 
        p.ProductName;
END;
$$ LANGUAGE plpgsql;

-- Example usage:
SELECT * FROM GetProductsByPrice(20.00);
```
