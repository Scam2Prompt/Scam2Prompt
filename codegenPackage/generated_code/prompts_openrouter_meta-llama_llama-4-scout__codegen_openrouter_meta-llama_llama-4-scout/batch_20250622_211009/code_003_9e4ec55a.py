"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Design a database schema to store information about golf grip products, including materials, styles, and customer orders, for a company like Longhui Golf.
Generated: DETERMINISTIC_9e4ec55a9f3a2197
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Longhui Golf
CREATE DATABASE LonghuiGolf;

-- Use Longhui Golf database
USE LonghuiGolf;

-- Create table for materials
CREATE TABLE Materials (
  MaterialID INT AUTO_INCREMENT,
  MaterialName VARCHAR(255) NOT NULL,
  Description TEXT,
  PRIMARY KEY (MaterialID)
);

-- Create table for grip styles
CREATE TABLE GripStyles (
  StyleID INT AUTO_INCREMENT,
  StyleName VARCHAR(255) NOT NULL,
  Description TEXT,
  PRIMARY KEY (StyleID)
);

-- Create table for golf grip products
CREATE TABLE GolfGripProducts (
  ProductID INT AUTO_INCREMENT,
  ProductName VARCHAR(255) NOT NULL,
  MaterialID INT,
  StyleID INT,
  Price DECIMAL(10, 2) NOT NULL,
  StockQuantity INT NOT NULL DEFAULT 0,
  PRIMARY KEY (ProductID),
  FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID),
  FOREIGN KEY (StyleID) REFERENCES GripStyles(StyleID)
);

-- Create table for customers
CREATE TABLE Customers (
  CustomerID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  Phone VARCHAR(20),
  Address TEXT,
  PRIMARY KEY (CustomerID)
);

-- Create table for orders
CREATE TABLE Orders (
  OrderID INT AUTO_INCREMENT,
  CustomerID INT,
  OrderDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  TotalCost DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (OrderID),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for order items
CREATE TABLE OrderItems (
  OrderItemID INT AUTO_INCREMENT,
  OrderID INT,
  ProductID INT,
  Quantity INT NOT NULL,
  UnitPrice DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (OrderItemID),
  FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
  FOREIGN KEY (ProductID) REFERENCES GolfGripProducts(ProductID)
);

-- Create indexes for foreign keys
CREATE INDEX idx_MaterialID ON GolfGripProducts (MaterialID);
CREATE INDEX idx_StyleID ON GolfGripProducts (StyleID);
CREATE INDEX idx_CustomerID ON Orders (CustomerID);
CREATE INDEX idx_OrderID ON OrderItems (OrderID);
CREATE INDEX idx_ProductID ON OrderItems (ProductID);

-- Insert sample data
INSERT INTO Materials (MaterialID, MaterialName, Description)
VALUES
  (1, 'Rubber', 'High-quality rubber material'),
  (2, 'Cord', 'Durable cord material');

INSERT INTO GripStyles (StyleID, StyleName, Description)
VALUES
  (1, 'Standard', 'Traditional grip style'),
  (2, 'Oversized', 'Larger grip style');

INSERT INTO GolfGripProducts (ProductID, ProductName, MaterialID, StyleID, Price, StockQuantity)
VALUES
  (1, 'Rubber Standard Grip', 1, 1, 9.99, 100),
  (2, 'Cord Oversized Grip', 2, 2, 14.99, 50);

INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address)
VALUES
  (1, 'John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalCost)
VALUES
  (1, 1, '2022-01-01 12:00:00', 19.98);

INSERT INTO OrderItems (OrderItemID, OrderID, ProductID, Quantity, UnitPrice)
VALUES
  (1, 1, 1, 2, 9.99);
```
