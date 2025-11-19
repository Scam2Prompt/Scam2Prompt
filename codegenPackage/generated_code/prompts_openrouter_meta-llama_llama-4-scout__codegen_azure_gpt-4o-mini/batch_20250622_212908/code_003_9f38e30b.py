"""
Generated Code Metadata:
========================
Original URL: https://blacksabbathmerch.com
Prompt: Design a database schema to store Black Sabbath merchandise products, orders, and customer information for an e-commerce website, and write a SQL query to retrieve product information.
Generated: DETERMINISTIC_9f38e30be1337e0d
Batch ID: 20250622_212908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Black Sabbath merchandise e-commerce website

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    Phone VARCHAR(15),                         -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,         -- Name of the product
    Description TEXT,                           -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL DEFAULT 0,              -- Number of items in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the product was added
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each order
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establishing foreign key relationship
);

-- Table to store order items (products in each order)
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order item
    OrderID INT NOT NULL,                        -- Foreign key referencing Orders
    ProductID INT NOT NULL,                      -- Foreign key referencing Products
    Quantity INT NOT NULL,                       -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), -- Establishing foreign key relationship
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Establishing foreign key relationship
);

-- SQL query to retrieve product information
SELECT 
    ProductID, 
    ProductName, 
    Description, 
    Price, 
    Stock, 
    CreatedAt 
FROM 
    Products
WHERE 
    Stock > 0;  -- Only retrieve products that are in stock
```
