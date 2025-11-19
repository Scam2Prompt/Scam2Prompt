"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Design a database schema to store product information, customer data, and order details for an e-commerce website like ebrasilbrazz, which sells various products, including equipment, supplies, and home decor items.
Generated: DETERMINISTIC_48b73e76ed86557a
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce website

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS OrderDetails;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Products;

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Description TEXT,                           -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                 -- Quantity available in stock
    Category VARCHAR(100),                      -- Category of the product (e.g., equipment, supplies, home decor)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store customer data
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    Phone VARCHAR(15),                         -- Customer's phone number
    Address VARCHAR(255),                       -- Customer's address
    City VARCHAR(100),                          -- Customer's city
    State VARCHAR(100),                         -- Customer's state
    ZipCode VARCHAR(10),                        -- Customer's zip code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store order details
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each order
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending',  -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store order details for each product in an order
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order detail
    OrderID INT NOT NULL,                           -- Foreign key referencing Orders
    ProductID INT NOT NULL,                         -- Foreign key referencing Products
    Quantity INT NOT NULL,                          -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
