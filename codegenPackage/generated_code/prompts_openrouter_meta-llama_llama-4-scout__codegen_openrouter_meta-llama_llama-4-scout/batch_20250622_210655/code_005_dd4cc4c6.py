"""
Generated Code Metadata:
========================
Original URL: https://shishehbalkon.ir
Prompt: "Design a database schema for managing orders, customer information, and product catalogs for a company specializing in glass balconies and related services like Akbarzadeh."
Generated: DETERMINISTIC_dd4cc4c6dbc6a5bf
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE GlassBalconyDB;

-- Use database
USE GlassBalconyDB;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status ENUM('Pending', 'In Progress', 'Delivered', 'Cancelled') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for order items
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create table for order services
CREATE TABLE OrderServices (
    OrderServiceID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ServiceID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderServiceID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    PaymentMethod ENUM('Cash', 'Credit Card', 'Bank Transfer') NOT NULL,
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Amount DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
```

```sql
-- sample_data.sql

-- Insert sample data into customers table
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, PostalCode, Country)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'New York', 'NY', '10001', 'USA'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Park Ave', 'New York', 'NY', '10002', 'USA');

-- Insert sample data into products table
INSERT INTO Products (ProductName, Description, Price)
VALUES 
('Glass Balcony', 'High-quality glass balcony', 1000.00),
('Aluminum Railing', 'Durable aluminum railing', 500.00);

-- Insert sample data into orders table
INSERT INTO Orders (CustomerID, TotalCost, Status)
VALUES 
(1, 1500.00, 'Pending'),
(2, 2000.00, 'In Progress');

-- Insert sample data into order items table
INSERT INTO OrderItems (OrderID, ProductID, Quantity, UnitPrice)
VALUES 
(1, 1, 1, 1000.00),
(1, 2, 1, 500.00),
(2, 1, 2, 1000.00);

-- Insert sample data into services table
INSERT INTO Services (ServiceName, Description, Price)
VALUES 
('Installation', 'Professional installation service', 500.00),
('Maintenance', 'Regular maintenance service', 200.00);

-- Insert sample data into order services table
INSERT INTO OrderServices (OrderID, ServiceID, Quantity, UnitPrice)
VALUES 
(1, 1, 1, 500.00),
(2, 2, 1, 200.00);

-- Insert sample data into payments table
INSERT INTO Payments (OrderID, PaymentMethod, Amount)
VALUES 
(1, 'Credit Card', 1500.00),
(2, 'Bank Transfer', 2000.00);
```
