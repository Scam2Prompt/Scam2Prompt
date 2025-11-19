"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Design a database schema for an e-commerce platform that manages products, orders, and customers for a business like PureKana or skyMD, with SQL code for data insertion and querying.
Generated: DETERMINISTIC_3d2622c74a47fc95
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Customer's email address
    Phone VARCHAR(15),                        -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product
    Description TEXT,                          -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL DEFAULT 0,              -- Available stock for the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the product was created
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store items in each order
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Foreign key referencing Orders
    ProductID INT NOT NULL,                     -- Foreign key referencing Products
    Quantity INT NOT NULL,                      -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion

-- Inserting customers
INSERT INTO Customers (FirstName, LastName, Email, Phone) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321');

-- Inserting products
INSERT INTO Products (ProductName, Description, Price, Stock) VALUES
('CBD Oil', 'High-quality CBD oil for wellness.', 29.99, 100),
('Vitamins', 'Essential vitamins for daily health.', 19.99, 200);

-- Inserting an order
INSERT INTO Orders (CustomerID, TotalAmount) VALUES
(1, 49.98); -- Assuming customer with ID 1 is placing an order

-- Inserting order items
INSERT INTO OrderItems (OrderID, ProductID, Quantity, Price) VALUES
(1, 1, 1, 29.99), -- 1 unit of CBD Oil
(1, 2, 1, 19.99); -- 1 unit of Vitamins

-- Sample query to retrieve all orders with customer and product details
SELECT 
    o.OrderID,
    c.FirstName,
    c.LastName,
    p.ProductName,
    oi.Quantity,
    oi.Price,
    o.TotalAmount,
    o.OrderDate
FROM 
    Orders o
JOIN 
    Customers c ON o.CustomerID = c.CustomerID
JOIN 
    OrderItems oi ON o.OrderID = oi.OrderID
JOIN 
    Products p ON oi.ProductID = p.ProductID
ORDER BY 
    o.OrderDate DESC; -- Orders sorted by date
```
