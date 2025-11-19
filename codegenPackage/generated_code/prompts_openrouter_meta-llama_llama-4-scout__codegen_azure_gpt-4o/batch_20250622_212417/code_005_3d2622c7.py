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
-- Database Schema for an E-commerce Platform

-- Create a table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was created
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,               -- Product name
    Description TEXT,                         -- Product description
    Price DECIMAL(10, 2) NOT NULL,            -- Product price
    Stock INT NOT NULL,                       -- Quantity of product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the product was created
);

-- Create a table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each order
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    Status VARCHAR(50) DEFAULT 'Pending',     -- Status of the order (e.g., Pending, Shipped, Delivered)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establish relationship with Customers table
);

-- Create a table for order details (products in each order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    Quantity INT NOT NULL,                        -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), -- Establish relationship with Orders table
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Establish relationship with Products table
);

-- Insert sample data into Customers table
INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm Street'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Oak Avenue');

-- Insert sample data into Products table
INSERT INTO Products (Name, Description, Price, Stock)
VALUES 
('CBD Oil', 'Premium CBD oil for wellness', 49.99, 100),
('CBD Gummies', 'Delicious CBD-infused gummies', 29.99, 200);

-- Insert sample data into Orders table
INSERT INTO Orders (CustomerID, TotalAmount, Status)
VALUES 
(1, 79.98, 'Pending'),
(2, 49.99, 'Shipped');

-- Insert sample data into OrderDetails table
INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Price)
VALUES 
(1, 1, 1, 49.99),
(1, 2, 1, 29.99),
(2, 1, 1, 49.99);

-- Query to retrieve all customers
SELECT * FROM Customers;

-- Query to retrieve all products
SELECT * FROM Products;

-- Query to retrieve all orders with customer details
SELECT 
    Orders.OrderID,
    Customers.FirstName,
    Customers.LastName,
    Orders.OrderDate,
    Orders.TotalAmount,
    Orders.Status
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- Query to retrieve order details for a specific order
SELECT 
    OrderDetails.OrderID,
    Products.Name AS ProductName,
    OrderDetails.Quantity,
    OrderDetails.Price
FROM OrderDetails
JOIN Products ON OrderDetails.ProductID = Products.ProductID
WHERE OrderDetails.OrderID = 1;

-- Query to check stock levels for all products
SELECT 
    ProductID,
    Name,
    Stock
FROM Products
WHERE Stock < 50; -- Example condition to find low-stock products
```
