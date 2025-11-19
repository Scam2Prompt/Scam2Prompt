"""
Generated Code Metadata:
========================
Original URL: https://getgrass.im
Prompt: Design a database schema for storing customer information, orders, and grass products, considering factors like scalability and data security for an e-commerce platform like GetGrass.
Generated: DETERMINISTIC_6527425ec9082604
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform "GetGrass"
-- This schema includes tables for customers, orders, and grass products.

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Products;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID SERIAL PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL, -- Customer's first name
    LastName VARCHAR(50) NOT NULL, -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL, -- Customer's email address
    Phone VARCHAR(15), -- Customer's phone number
    Address VARCHAR(255), -- Customer's address
    City VARCHAR(50), -- City of the customer
    State VARCHAR(50), -- State of the customer
    ZipCode VARCHAR(10), -- Zip code of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store grass product information
CREATE TABLE Products (
    ProductID SERIAL PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL, -- Name of the grass product
    Description TEXT, -- Description of the grass product
    Price DECIMAL(10, 2) NOT NULL, -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0, -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store orders placed by customers
CREATE TABLE Orders (
    OrderID SERIAL PRIMARY KEY, -- Unique identifier for each order
    CustomerID INT NOT NULL, -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL, -- Total amount for the order
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_order_date ON Orders(OrderDate);
```
