"""
Generated Code Metadata:
========================
Original URL: https://toys-kopitsa.com.ua
Prompt: Design a simple database schema to store information about soft toys, customers, and orders for an e-commerce platform similar to https://toys-kopitsa.com.ua, using a relational database management system like MySQL.
Generated: DETERMINISTIC_4dbf8659df937ae2
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform to manage soft toys, customers, and orders

-- Create a database
CREATE DATABASE IF NOT EXISTS SoftToysECommerce;
USE SoftToysECommerce;

-- Table to store information about soft toys
CREATE TABLE IF NOT EXISTS SoftToys (
    ToyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each toy
    Name VARCHAR(255) NOT NULL,           -- Name of the toy
    Description TEXT,                     -- Description of the toy
    Price DECIMAL(10, 2) NOT NULL,        -- Price of the toy
    Stock INT NOT NULL,                   -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the toy was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about customers
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- First name of the customer
    LastName VARCHAR(100) NOT NULL,            -- Last name of the customer
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the customer
    PhoneNumber VARCHAR(15),                   -- Phone number of the customer
    Address TEXT,                              -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about orders
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    CustomerID INT NOT NULL,                -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,    -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Table to store information about order items (toys in each order)
CREATE TABLE IF NOT EXISTS OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Foreign key referencing Orders table
    ToyID INT NOT NULL,                         -- Foreign key referencing SoftToys table
    Quantity INT NOT NULL,                      -- Quantity of the toy in the order
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the toy at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is deleted
    FOREIGN KEY (ToyID) REFERENCES SoftToys(ToyID) ON DELETE CASCADE -- Cascade delete if toy is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email); -- Index on customer email for faster lookups
CREATE INDEX idx_order_date ON Orders(OrderDate);    -- Index on order date for faster queries

-- Example error handling: Ensure all tables are created successfully
-- If any table creation fails, the script will stop execution
```
