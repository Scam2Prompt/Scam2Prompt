"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Generate a SQL database schema for storing information about menuiserie products, including tables for products, suppliers, and customers, with relationships between them."
Generated: DETERMINISTIC_ca6866e7ca39866f
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Menusierie Products

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store supplier information
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL,          -- Name of the supplier
    ContactName VARCHAR(50),                      -- Contact person's name
    Phone VARCHAR(15),                           -- Supplier's phone number
    Email VARCHAR(100) UNIQUE,                   -- Supplier's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the supplier was created
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL,                   -- Quantity of the product in stock
    SupplierID INT,                               -- Foreign key referencing Suppliers
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) -- Establishing relationship with Suppliers
);

-- Table to store orders placed by customers
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each order
    CustomerID INT,                               -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establishing relationship with Customers
);

-- Table to store items in each order
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each order item
    OrderID INT,                                  -- Foreign key referencing Orders
    ProductID INT,                                -- Foreign key referencing Products
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), -- Establishing relationship with Orders
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Establishing relationship with Products
);
```
