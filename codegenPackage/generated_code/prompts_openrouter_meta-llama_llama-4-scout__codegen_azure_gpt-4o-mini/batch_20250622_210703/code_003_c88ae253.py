"""
Generated Code Metadata:
========================
Original URL: https://chedanthe.dk
Prompt: "Create a SQL database schema to manage furniture inventory, including tables for products, prices, and customer orders, suitable for an e-commerce platform like Chedanthe."
Generated: DETERMINISTIC_c88ae2539c994354
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Furniture Inventory Management

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CustomerOrders;
DROP TABLE IF EXISTS Prices;
DROP TABLE IF EXISTS Products;

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Description TEXT,                           -- Description of the product
    Category VARCHAR(100),                      -- Category of the product (e.g., chair, table)
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store pricing information for products
CREATE TABLE Prices (
    PriceID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each price entry
    ProductID INT NOT NULL,                     -- Foreign key referencing Products
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    EffectiveDate DATE NOT NULL,                -- Date when the price becomes effective
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer orders
CREATE TABLE CustomerOrders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each order
    CustomerName VARCHAR(255) NOT NULL,        -- Name of the customer
    CustomerEmail VARCHAR(255) NOT NULL,       -- Email of the customer
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store order details, linking products to customer orders
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                          -- Foreign key referencing CustomerOrders
    ProductID INT NOT NULL,                        -- Foreign key referencing Products
    Quantity INT NOT NULL,                         -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES CustomerOrders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_order_date ON CustomerOrders(OrderDate);
CREATE INDEX idx_product_id ON Prices(ProductID);
```
