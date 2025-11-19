"""
Generated Code Metadata:
========================
Original URL: https://cmcbukittinggi.co.id
Prompt: Design a simple database schema to store information about computer products like those sold on Central Multi Computer.
Generated: DETERMINISTIC_b91c83de93480996
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about computer products

-- Create a database for the computer products
CREATE DATABASE ComputerProductsDB;

-- Use the created database
USE ComputerProductsDB;

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,        -- Quantity in stock
    CategoryID INT,                               -- Foreign key referencing ProductCategories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL -- Foreign key constraint
);

-- Table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each review
    ProductID INT,                                -- Foreign key referencing Products
    ReviewText TEXT NOT NULL,                     -- Text of the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating from 1 to 5
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,              -- Customer's first name
    LastName VARCHAR(100) NOT NULL,               -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,           -- Customer's email (must be unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each order
    CustomerID INT,                                -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,          -- Total amount for the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store order details (products in each order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each order detail
    OrderID INT,                                   -- Foreign key referencing Orders
    ProductID INT,                                 -- Foreign key referencing Products
    Quantity INT NOT NULL,                         -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Foreign key constraint
);
```
