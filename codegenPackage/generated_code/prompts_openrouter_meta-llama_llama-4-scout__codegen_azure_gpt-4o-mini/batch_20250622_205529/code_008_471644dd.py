"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Create a SQL database schema to store product information for an e-commerce website like Jurunense Home Center."
Generated: DETERMINISTIC_471644ddf07644d6
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for an e-commerce website

-- Create the database
CREATE DATABASE JurunenseHomeCenter;

-- Use the created database
USE JurunenseHomeCenter;

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,         -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product, must be non-negative
    StockQuantity INT NOT NULL CHECK (StockQuantity >= 0), -- Quantity in stock, must be non-negative
    CategoryID INT,                               -- Foreign key to ProductCategories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Establish foreign key relationship
);

-- Table to store customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,              -- Customer's first name
    LastName VARCHAR(100) NOT NULL,                -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,            -- Customer's email, must be unique
    PasswordHash VARCHAR(255) NOT NULL,            -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each order
    CustomerID INT,                                -- Foreign key to Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0), -- Total amount of the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establish foreign key relationship
);

-- Table to store order items
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order item
    OrderID INT,                                   -- Foreign key to Orders
    ProductID INT,                                 -- Foreign key to Products
    Quantity INT NOT NULL CHECK (Quantity > 0),    -- Quantity of the product ordered, must be positive
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), -- Establish foreign key relationship
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Establish foreign key relationship
);

-- Table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each review
    ProductID INT,                                 -- Foreign key to Products
    CustomerID INT,                                -- Foreign key to Customers
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating from 1 to 5
    ReviewText TEXT,                               -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID), -- Establish foreign key relationship
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establish foreign key relationship
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_customer_email ON Customers(Email);
```
