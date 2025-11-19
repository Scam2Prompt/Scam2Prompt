"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Generate a sample database schema for a uniform manufacturing company, including tables for customers, orders, products (e.g., school uniforms, work uniforms), and suppliers, inspired by Real Garment's business model.
Generated: DETERMINISTIC_55bf617c94684128
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample Database Schema for a Uniform Manufacturing Company

-- Drop existing tables if they exist (for re-creation during development)
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Suppliers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    ProductType ENUM('School Uniform', 'Work Uniform') NOT NULL, -- Type of uniform
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    SupplierID INT,                              -- Foreign key referencing Suppliers
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) -- Establishing foreign key relationship
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

-- Table to store order information
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each order
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') NOT NULL, -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establishing foreign key relationship
);

-- Sample data insertion (for testing purposes)
INSERT INTO Suppliers (SupplierName, ContactName, Phone, Email) VALUES
('Uniform Supplies Co.', 'John Doe', '123-456-7890', 'contact@uniformsupplies.com'),
('Quality Fabrics Inc.', 'Jane Smith', '098-765-4321', 'info@qualityfabrics.com');

INSERT INTO Products (ProductName, ProductType, Price, SupplierID) VALUES
('School Blazer', 'School Uniform', 49.99, 1),
('Work Shirt', 'Work Uniform', 29.99, 2);

INSERT INTO Customers (FirstName, LastName, Email, Phone) VALUES
('Alice', 'Johnson', 'alice.johnson@example.com', '555-1234'),
('Bob', 'Smith', 'bob.smith@example.com', '555-5678');

INSERT INTO Orders (CustomerID, TotalAmount, Status) VALUES
(1, 79.98, 'Pending'),
(2, 29.99, 'Shipped');
```
