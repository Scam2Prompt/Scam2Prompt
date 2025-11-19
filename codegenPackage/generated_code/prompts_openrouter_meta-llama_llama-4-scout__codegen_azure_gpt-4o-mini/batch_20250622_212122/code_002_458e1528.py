"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Generate a SQL database schema for a wholesale kitchen supply store like Varejão das Louças that sells to restaurants and hotels.
Generated: DETERMINISTIC_458e1528e876aed6
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for a Wholesale Kitchen Supply Store

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Suppliers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Customer's name
    ContactPerson VARCHAR(100),                 -- Contact person's name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    Address VARCHAR(255),                       -- Customer's address
    City VARCHAR(50),                           -- City of the customer
    State VARCHAR(50),                          -- State of the customer
    ZipCode VARCHAR(10),                        -- Zip code of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store supplier information
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each supplier
    Name VARCHAR(100) NOT NULL,                 -- Supplier's name
    ContactPerson VARCHAR(100),                  -- Contact person's name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Supplier's email address
    Phone VARCHAR(15),                           -- Supplier's phone number
    Address VARCHAR(255),                        -- Supplier's address
    City VARCHAR(50),                            -- City of the supplier
    State VARCHAR(50),                           -- State of the supplier
    ZipCode VARCHAR(10),                         -- Zip code of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,                  -- Product name
    Description TEXT,                            -- Product description
    Price DECIMAL(10, 2) NOT NULL,               -- Product price
    StockQuantity INT NOT NULL DEFAULT 0,        -- Quantity in stock
    SupplierID INT,                              -- Foreign key referencing Suppliers
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE SET NULL -- Handle supplier deletion
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    CustomerID INT,                              -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Order date
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount of the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Handle customer deletion
);

-- Table to store items in each order
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order item
    OrderID INT,                                 -- Foreign key referencing Orders
    ProductID INT,                               -- Foreign key referencing Products
    Quantity INT NOT NULL,                       -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Handle order deletion
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Handle product deletion
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_supplier_email ON Suppliers(Email);
CREATE INDEX idx_product_name ON Products(Name);
CREATE INDEX idx_order_date ON Orders(OrderDate);
```
