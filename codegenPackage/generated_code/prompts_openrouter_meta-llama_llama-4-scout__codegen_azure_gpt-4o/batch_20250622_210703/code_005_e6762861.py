"""
Generated Code Metadata:
========================
Original URL: https://bigbearcustoms.shop
Prompt: Design a database schema to store information about motorcycle gear and accessories, including Alpinestars products, and write a SQL query to retrieve product details.
Generated: DETERMINISTIC_e676286188352477
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Motorcycle Gear and Accessories

-- Table to store product categories
CREATE TABLE ProductCategory (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., Jackets, Helmets, Gloves)
    Description TEXT                           -- Optional description of the category
);

-- Table to store product details
CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Brand VARCHAR(255) NOT NULL,               -- Brand of the product (e.g., Alpinestars)
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategory
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL,                        -- Quantity available in stock
    Description TEXT,                          -- Optional description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategory(CategoryID) -- Enforce category relationship
);

-- Table to store product accessories
CREATE TABLE ProductAccessory (
    AccessoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each accessory
    ProductID INT NOT NULL,                     -- Foreign key linking to Product
    AccessoryName VARCHAR(255) NOT NULL,        -- Name of the accessory
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the accessory
    Description TEXT,                           -- Optional description of the accessory
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the accessory was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) -- Enforce product relationship
);

-- SQL Query to retrieve product details, including category and accessories
SELECT 
    p.ProductID,
    p.ProductName,
    p.Brand,
    pc.CategoryName,
    p.Price AS ProductPrice,
    p.Stock,
    p.Description AS ProductDescription,
    pa.AccessoryName,
    pa.Price AS AccessoryPrice,
    pa.Description AS AccessoryDescription
FROM 
    Product p
JOIN 
    ProductCategory pc ON p.CategoryID = pc.CategoryID
LEFT JOIN 
    ProductAccessory pa ON p.ProductID = pa.ProductID
WHERE 
    p.Brand = 'Alpinestars'; -- Filter for Alpinestars products
```
