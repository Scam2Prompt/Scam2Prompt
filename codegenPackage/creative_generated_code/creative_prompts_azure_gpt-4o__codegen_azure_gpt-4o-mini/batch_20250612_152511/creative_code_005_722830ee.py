"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Create a database schema for an e-commerce platform that categorizes products like "گیفت کارت اپل," "گیفت کارت ایکس باکس," and "جم کلش رویال," ensuring efficient product management.
Generated: DETERMINISTIC_722830eeda4bd432
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an e-commerce platform

-- Drop existing tables if they exist (for re-running the script)
DROP TABLE IF EXISTS ProductCategories;
DROP TABLE IF EXISTS Products;

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,         -- Name of the category
    Description TEXT,                            -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the category was last updated
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    Description TEXT,                            -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    Stock INT NOT NULL DEFAULT 0,                -- Stock quantity of the product
    CategoryID INT,                              -- Foreign key for the product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)  -- Establishing a relationship with the ProductCategories table
);

-- Sample data insertion for product categories
INSERT INTO ProductCategories (CategoryName, Description) VALUES 
    ('گیفت کارت اپل', 'Apple Gift Card'),
    ('گیفت کارت ایکس باکس', 'Xbox Gift Card'),
    ('جم کلش رویال', 'Clash Royale Gems');

-- Sample data insertion for products
INSERT INTO Products (ProductName, Description, Price, Stock, CategoryID) VALUES 
    ('Apple Gift Card 50$', 'iTunes and App Store Gift Card', 50.00, 100, 1),
    ('Xbox Gift Card 50$', 'Xbox Live Gift Card', 50.00, 200, 2),
    ('Clash Royale Gems 1000', '1000 Gems for Clash Royale', 10.00, 300, 3);
```
