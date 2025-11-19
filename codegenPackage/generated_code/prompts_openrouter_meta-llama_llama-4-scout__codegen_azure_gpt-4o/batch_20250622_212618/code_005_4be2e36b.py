"""
Generated Code Metadata:
========================
Original URL: https://jiosell.com
Prompt: "Design a database schema to store product information from various online shops, including Jiosell, and implement efficient querying mechanisms."
Generated: DETERMINISTIC_4be2e36bdac5e31a
Batch ID: 20250622_212618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema to store product information from various online shops

-- Table to store shop information
CREATE TABLE Shops (
    ShopID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shop
    ShopName VARCHAR(255) NOT NULL,        -- Name of the shop
    ShopURL VARCHAR(2083),                 -- URL of the shop
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Description TEXT,                         -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    CurrencyCode CHAR(3) NOT NULL,            -- Currency code (e.g., USD, INR)
    Stock INT NOT NULL,                       -- Number of items in stock
    ShopID INT NOT NULL,                      -- Foreign key referencing Shops table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ShopID) REFERENCES Shops(ShopID) ON DELETE CASCADE -- Cascade delete if shop is removed
);

-- Indexes for efficient querying
CREATE INDEX idx_shop_id ON Products(ShopID); -- Index for ShopID in Products table
CREATE INDEX idx_product_name ON Products(ProductName); -- Index for ProductName in Products table

-- Query to fetch all products from a specific shop
-- Replace 'Jiosell' with the desired shop name
SELECT 
    p.ProductID, 
    p.ProductName, 
    p.Description, 
    p.Price, 
    p.CurrencyCode, 
    p.Stock, 
    s.ShopName 
FROM 
    Products p
JOIN 
    Shops s 
ON 
    p.ShopID = s.ShopID
WHERE 
    s.ShopName = 'Jiosell';

-- Query to fetch products within a specific price range
-- Replace 10.00 and 50.00 with desired price range
SELECT 
    ProductID, 
    ProductName, 
    Price, 
    CurrencyCode, 
    Stock 
FROM 
    Products
WHERE 
    Price BETWEEN 10.00 AND 50.00;

-- Query to fetch products that are out of stock
SELECT 
    ProductID, 
    ProductName, 
    Stock 
FROM 
    Products
WHERE 
    Stock = 0;

-- Query to fetch the total number of products per shop
SELECT 
    s.ShopName, 
    COUNT(p.ProductID) AS TotalProducts 
FROM 
    Shops s
LEFT JOIN 
    Products p 
ON 
    s.ShopID = p.ShopID
GROUP BY 
    s.ShopName;
```
