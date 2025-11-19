"""
Generated Code Metadata:
========================
Original URL: https://shopeewise.com
Prompt: Design a simple database schema to store product information (e.g., product name, price, quantity) for an e-commerce platform like ShopeeWise.
Generated: DETERMINISTIC_36df0112b2bf01c8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a simple database schema for storing product information

-- Drop the table if it already exists to avoid conflicts during creation
DROP TABLE IF EXISTS Products;

-- Create a table named 'Products' to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product, cannot be null
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product, must be non-negative
    Quantity INT NOT NULL CHECK (Quantity >= 0),  -- Quantity of the product in stock, must be non-negative
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Index on ProductName for faster search queries
CREATE INDEX idx_product_name ON Products(ProductName);

-- Sample data insertion for testing purposes
INSERT INTO Products (ProductName, Price, Quantity) VALUES
('Sample Product 1', 19.99, 100),
('Sample Product 2', 29.99, 50),
('Sample Product 3', 9.99, 200);

-- Query to retrieve all products
SELECT * FROM Products;

-- Query to update a product's price and quantity
-- Example: Update the price and quantity of 'Sample Product 1'
UPDATE Products
SET Price = 17.99, Quantity = 90
WHERE ProductName = 'Sample Product 1';

-- Query to delete a product by ProductID
-- Example: Delete the product with ProductID = 1
DELETE FROM Products
WHERE ProductID = 1;
```
