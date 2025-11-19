"""
Generated Code Metadata:
========================
Original URL: https://eferroeacobrza.blogspot.com
Prompt: "Write a SQL query to manage orders and customers for a company that distributes iron and steel products, including services like dobradeira de calhas and guilhotina."
Generated: DETERMINISTIC_0f515401711c6c8a
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
<<<<<<< HEAD
-- Create a database for the company
CREATE DATABASE IronSteelDistribution;

-- Use the newly created database
USE IronSteelDistribution;

-- Create a table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
=======
-- Create a database schema for managing orders and customers
-- This schema is designed for a company distributing iron and steel products, including services like dobradeira de calhas and guilhotina.

-- Create the Customers table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    Name VARCHAR(255) NOT NULL,                -- Customer's name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address
    Phone VARCHAR(20),                         -- Customer's phone number
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

<<<<<<< HEAD
-- Create a table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key linking to the Customers table
    ProductName VARCHAR(100) NOT NULL,         -- Name of the product or service ordered
    Quantity INT NOT NULL,                     -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product or service
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Enforce relationship with Customers table
);

-- Insert sample data into Customers table
INSERT INTO Customers (Name, Email, PhoneNumber, Address)
VALUES 
('John Doe', 'john.doe@example.com', '123-456-7890', '123 Steel St, Iron City'),
('Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Alloy Ave, Metal Town');

-- Insert sample data into Orders table
INSERT INTO Orders (CustomerID, ProductName, Quantity, Price, Status)
VALUES 
(1, 'Iron Rods', 100, 500.00, 'Completed'),
(1, 'Dobradeira de Calhas', 1, 1500.00, 'Pending'),
(2, 'Guilhotina', 1, 2500.00, 'Completed');

-- Query to retrieve all orders along with customer details
SELECT 
    o.OrderID,
    o.ProductName,
    o.Quantity,
    o.Price,
    o.OrderDate,
    o.Status,
    c.Name AS CustomerName,
    c.Email AS CustomerEmail,
    c.PhoneNumber AS CustomerPhone,
    c.Address AS CustomerAddress
FROM 
    Orders o
JOIN 
    Customers c
ON 
    o.CustomerID = c.CustomerID
ORDER BY 
    o.OrderDate DESC;

-- Query to calculate total revenue from completed orders
SELECT 
    SUM(Price) AS TotalRevenue
FROM 
    Orders
WHERE 
    Status = 'Completed';

-- Query to list all pending orders
SELECT 
    OrderID,
    ProductName,
    Quantity,
    Price,
    OrderDate,
    Status
FROM 
    Orders
WHERE 
    Status = 'Pending'
ORDER BY 
    OrderDate ASC;

-- Error handling: Ensure foreign key constraints are respected
-- Example: Attempting to insert an order with a non-existent CustomerID will fail
=======
-- Create the Products table to store product and service information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product/service
    Name VARCHAR(255) NOT NULL,               -- Name of the product/service
    Description TEXT,                         -- Description of the product/service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product/service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the product/service was added
);

-- Create the Orders table to store order information
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each order
    CustomerID INT NOT NULL,                  -- Foreign key referencing the Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    Status VARCHAR(50) DEFAULT 'Pending',     -- Status of the order (e.g., Pending, Completed, Cancelled)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Enforce relationship with Customers table
);

-- Create the OrderDetails table to store details of each order
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing the Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing the Products table
    Quantity INT NOT NULL,                        -- Quantity of the product/service ordered
    Subtotal DECIMAL(10, 2) NOT NULL,             -- Subtotal for the product/service (Price * Quantity)
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), -- Enforce relationship with Orders table
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Enforce relationship with Products table
);

-- Example query to insert a new customer
INSERT INTO Customers (Name, Email, Phone, Address)
VALUES ('John Doe', 'john.doe@example.com', '123-456-7890', '123 Steel Street, Industrial City');

-- Example query to insert a new product/service
INSERT INTO Products (Name, Description, Price)
VALUES ('Dobradeira de Calhas', 'High-quality gutter bending service', 150.00);

-- Example query to create a new order
INSERT INTO Orders (CustomerID, TotalAmount, Status)
VALUES (1, 300.00, 'Pending');

-- Example query to add order details
INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Subtotal)
VALUES (1, 1, 2, 300.00);

-- Example query to retrieve all orders with customer and product details
SELECT 
    o.OrderID,
    c.Name AS CustomerName,
    p.Name AS ProductName,
    od.Quantity,
    od.Subtotal,
    o.TotalAmount,
    o.Status,
    o.OrderDate
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
ORDER BY o.OrderDate DESC;

-- Example query to update the status of an order
UPDATE Orders
SET Status = 'Completed'
WHERE OrderID = 1;

-- Example query to delete a customer (with cascading delete for related orders and order details)
DELETE FROM Customers
WHERE CustomerID = 1;
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
```
