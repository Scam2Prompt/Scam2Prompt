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
-- Create a database schema for an e-commerce platform
-- Database name: EcommercePlatform

-- Use the database
CREATE DATABASE IF NOT EXISTS EcommercePlatform;
USE EcommercePlatform;

-- Table: Categories
-- Stores product categories such as "گیفت کارت اپل," "گیفت کارت ایکس باکس," etc.
CREATE TABLE IF NOT EXISTS Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL UNIQUE,          -- Name of the category
    Description TEXT DEFAULT NULL,              -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table: Products
-- Stores products and assigns each product to a category
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                     -- Name of the product
    Description TEXT DEFAULT NULL,                  -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,                  -- Price of the product
    Quantity INT DEFAULT 0,                         -- Available quantity of the product
    CategoryID INT NOT NULL,                        -- Foreign key referencing Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    CONSTRAINT FK_CategoryID FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Table: Orders
-- Stores order details
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each order
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer placing the order
    CustomerEmail VARCHAR(255) NOT NULL,          -- Email of the customer
    TotalAmount DECIMAL(10, 2) NOT NULL,          -- Total amount for the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    Status ENUM('Pending', 'Processing', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table: OrderItems
-- Stores individual items within an order
CREATE TABLE IF NOT EXISTS OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each order item
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,                -- Price per unit of the product
    CONSTRAINT FK_OrderID FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    CONSTRAINT FK_ProductID FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Indexes for performance optimization
-- Add an index to improve lookup speed for Products based on CategoryID
CREATE INDEX IDX_CategoryID ON Products(CategoryID);

-- Add an index to improve lookup speed for OrderItems based on OrderID
CREATE INDEX IDX_OrderID ON OrderItems(OrderID);

-- Add an index to improve lookup speed for OrderItems based on ProductID
CREATE INDEX IDX_ProductID ON OrderItems(ProductID);
```
