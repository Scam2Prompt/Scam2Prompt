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
-- SQL schema for storing products and prices for a distributor of party supplies

-- Create the database
CREATE DATABASE PartySuppliesDistributor;

-- Use the newly created database
USE PartySuppliesDistributor;

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "Bolas", "Biscoitos", "Salgados")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    CategoryID INT NOT NULL,                  -- Foreign key linking to the Categories table
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    StockQuantity INT DEFAULT 0,              -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store price history for products
CREATE TABLE PriceHistory (
    PriceHistoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each price history record
    ProductID INT NOT NULL,                        -- Foreign key linking to the Products table
    OldPrice DECIMAL(10, 2) NOT NULL,              -- Previous price of the product
    NewPrice DECIMAL(10, 2) NOT NULL,              -- Updated price of the product
    ChangeDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the price change occurred
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Insert sample categories
INSERT INTO Categories (CategoryName) VALUES 
('Bolas'), 
('Biscoitos'), 
('Salgados');

-- Example of inserting a product
INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity) VALUES 
('Chocolate Cake', 1, 25.99, 10), 
('Butter Cookies', 2, 15.49, 50), 
('Cheese Puffs', 3, 8.99, 100);

-- Query to verify the schema and sample data
SELECT * FROM Categories;
SELECT * FROM Products;
SELECT * FROM PriceHistory;
```
