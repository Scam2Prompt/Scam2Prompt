"""
Generated Code Metadata:
========================
Original URL: https://promodinamic.com
Prompt: "Design a database schema for storing information about promotional products, printing methods, and customer orders for a company like Promodinamic."
Generated: DETERMINISTIC_924ec4cb061aebf3
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Promodinamic
CREATE DATABASE Promodinamic;

-- Use Promodinamic database
USE Promodinamic;

-- Create table for promotional products
CREATE TABLE Products (
  ProductID INT AUTO_INCREMENT,
  ProductName VARCHAR(255) NOT NULL,
  ProductDescription TEXT,
  UnitPrice DECIMAL(10, 2) NOT NULL,
  UnitStock INT NOT NULL DEFAULT 0,
  PRIMARY KEY (ProductID)
);

-- Create table for printing methods
CREATE TABLE PrintingMethods (
  PrintingMethodID INT AUTO_INCREMENT,
  PrintingMethodName VARCHAR(255) NOT NULL,
  PrintingMethodDescription TEXT,
  PRIMARY KEY (PrintingMethodID)
);

-- Create table for product printing methods
CREATE TABLE ProductPrintingMethods (
  ProductID INT NOT NULL,
  PrintingMethodID INT NOT NULL,
  PRIMARY KEY (ProductID, PrintingMethodID),
  FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
  FOREIGN KEY (PrintingMethodID) REFERENCES PrintingMethods(PrintingMethodID)
);

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
  PRIMARY KEY (CustomerID)
);

-- Create table for orders
CREATE TABLE Orders (
  OrderID INT AUTO_INCREMENT,
  CustomerID INT NOT NULL,
  OrderDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  TotalCost DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
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
  PrintingMethodID INT,
  PRIMARY KEY (OrderItemID),
  FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
  FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
  FOREIGN KEY (PrintingMethodID) REFERENCES PrintingMethods(PrintingMethodID)
);

-- Create table for payments
CREATE TABLE Payments (
  PaymentID INT AUTO_INCREMENT,
  OrderID INT NOT NULL,
  PaymentDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PaymentAmount DECIMAL(10, 2) NOT NULL,
  PaymentMethod VARCHAR(100) NOT NULL,
  PRIMARY KEY (PaymentID),
  FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Create indexes for faster queries
CREATE INDEX idx_Products_ProductName ON Products (ProductName);
CREATE INDEX idx_Orders_CustomerID ON Orders (CustomerID);
CREATE INDEX idx_OrderItems_OrderID ON OrderItems (OrderID);
CREATE INDEX idx_OrderItems_ProductID ON OrderItems (ProductID);
```

```sql
-- sample_data.sql

-- Insert sample data into Products table
INSERT INTO Products (ProductName, ProductDescription, UnitPrice, UnitStock)
VALUES
  ('T-Shirt', 'A high-quality T-shirt', 10.99, 100),
  ('Mug', 'A ceramic coffee mug', 5.99, 50),
  ('Pen', 'A ballpoint pen', 1.99, 200);

-- Insert sample data into PrintingMethods table
INSERT INTO PrintingMethods (PrintingMethodName, PrintingMethodDescription)
VALUES
  ('Screen Printing', 'A popular method for printing on fabrics'),
  ('Pad Printing', 'A versatile method for printing on various materials'),
  ('Digital Printing', 'A modern method for printing on paper and cardstock');

-- Insert sample data into ProductPrintingMethods table
INSERT INTO ProductPrintingMethods (ProductID, PrintingMethodID)
VALUES
  (1, 1),
  (1, 2),
  (2, 2),
  (2, 3),
  (3, 1),
  (3, 3);

-- Insert sample data into Customers table
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, PostalCode, Country)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345', 'USA'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890', 'USA');

-- Insert sample data into Orders table
INSERT INTO Orders (CustomerID, TotalCost)
VALUES
  (1, 21.98),
  (2, 11.98);

-- Insert sample data into OrderItems table
INSERT INTO OrderItems (OrderID, ProductID, Quantity, UnitPrice, PrintingMethodID)
VALUES
  (1, 1, 2, 10.99, 1),
  (1, 2, 1, 5.99, 2),
  (2, 3, 1, 1.99, 3);

-- Insert sample data into Payments table
INSERT INTO Payments (OrderID, PaymentAmount, PaymentMethod)
VALUES
  (1, 21.98, 'Credit Card'),
  (2, 11.98, 'Cash');
```
