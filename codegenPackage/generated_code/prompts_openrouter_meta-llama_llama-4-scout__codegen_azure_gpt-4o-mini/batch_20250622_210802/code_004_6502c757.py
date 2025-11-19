"""
Generated Code Metadata:
========================
Original URL: https://trykart.in
Prompt: Design a database schema for an e-commerce platform like Trykart, which can store product information, customer details, and order history.
Generated: DETERMINISTIC_6502c757fd3dd298
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email address (unique)
    PasswordHash VARCHAR(255) NOT NULL,         -- Hashed password for security
    PhoneNumber VARCHAR(15),                     -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    Description TEXT,                            -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,       -- Quantity available in stock
    Category VARCHAR(50),                        -- Category of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store items in each order
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order item
    OrderID INT NOT NULL,                        -- Foreign key referencing Orders
    ProductID INT NOT NULL,                      -- Foreign key referencing Products
    Quantity INT NOT NULL,                       -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_order_customer ON Orders(CustomerID);
```
