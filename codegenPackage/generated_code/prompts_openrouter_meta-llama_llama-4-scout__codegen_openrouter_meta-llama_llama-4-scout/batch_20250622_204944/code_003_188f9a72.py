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
-- Create a database for party supplies
CREATE DATABASE PartySupplies;

-- Use the PartySupplies database
USE PartySupplies;

-- Create a table for product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    CategoryID INT,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT NOT NULL DEFAULT 0,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Create a table for product price history
CREATE TABLE ProductPriceHistory (
    PriceHistoryID INT AUTO_INCREMENT,
    ProductID INT,
    Price DECIMAL(10, 2) NOT NULL,
    EffectiveDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PriceHistoryID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Insert some sample categories
INSERT INTO Categories (CategoryName, Description)
VALUES 
('Bolas', 'Party balls and inflatables'),
('Biscoitos', 'Cookies and biscuits'),
('Salgados', 'Savory snacks');

-- Insert some sample products
INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity)
VALUES 
('Red Party Ball', 1, 5.99, 100),
('Chocolate Chip Cookie', 2, 2.99, 50),
('Spicy Potato Chips', 3, 3.99, 200);

-- Insert some sample price history
INSERT INTO ProductPriceHistory (ProductID, Price, EffectiveDate)
VALUES 
(1, 5.99, '2022-01-01'),
(1, 6.49, '2023-01-01'),
(2, 2.99, '2022-01-01'),
(3, 3.99, '2022-01-01'),
(3, 4.49, '2023-06-01');
```
