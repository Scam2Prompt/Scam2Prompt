"""
Generated Code Metadata:
========================
Original URL: https://www.navkarfurniture.com
Prompt: Design a database schema for an online furniture store like Navkar Furniture, including tables for products, customers, and orders.
Generated: DETERMINISTIC_a5179a54f49b4349
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online furniture store

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Products;

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                           -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                 -- Quantity available in stock
    Category VARCHAR(100),                      -- Category of the product (e.g., chair, table)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,             -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,         -- Customer's email address (must be unique)
    Phone VARCHAR(15),                          -- Customer's phone number
    Address VARCHAR(255) NOT NULL,              -- Customer's shipping address
    City VARCHAR(100) NOT NULL,                 -- City of the customer
    State VARCHAR(100) NOT NULL,                -- State of the customer
    ZipCode VARCHAR(10) NOT NULL,               -- Zip code of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store order information
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store order items (products in each order)
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order item
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);
```
