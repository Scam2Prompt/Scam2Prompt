"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Generate a sample database schema for a uniform manufacturing company, including tables for customers, orders, products (e.g., school uniforms, work uniforms), and suppliers, inspired by Real Garment's business model.
Generated: DETERMINISTIC_55bf617c94684128
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for uniform manufacturing company
CREATE DATABASE UniformManufacturing;

-- Use the database schema
USE UniformManufacturing;

-- Create table for suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT,
    SupplierName VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PRIMARY KEY (SupplierID)
);

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription TEXT,
    ProductType ENUM('School Uniform', 'Work Uniform') NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    UnitStock INT NOT NULL DEFAULT 0,
    SupplierID INT,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    CustomerName VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PRIMARY KEY (CustomerID)
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending',
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for order details
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderDetailID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create trigger to update total cost of order when order details are inserted or updated
DELIMITER $$
CREATE TRIGGER UpdateOrderTotalCost
AFTER INSERT OR UPDATE ON OrderDetails
FOR EACH ROW
BEGIN
    DECLARE Total DECIMAL(10, 2);
    SET Total = (SELECT SUM(od.Quantity * od.UnitPrice) FROM OrderDetails od WHERE od.OrderID = NEW.OrderID);
    UPDATE Orders SET TotalCost = Total WHERE OrderID = NEW.OrderID;
END$$
DELIMITER ;

-- Create trigger to prevent deletion of products with existing order details
DELIMITER $$
CREATE TRIGGER PreventProductDeletion
BEFORE DELETE ON Products
FOR EACH ROW
BEGIN
    IF (SELECT COUNT(*) FROM OrderDetails WHERE ProductID = OLD.ProductID) > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete product with existing order details';
    END IF;
END$$
DELIMITER ;

-- Create trigger to prevent deletion of customers with existing orders
DELIMITER $$
CREATE TRIGGER PreventCustomerDeletion
BEFORE DELETE ON Customers
FOR EACH ROW
BEGIN
    IF (SELECT COUNT(*) FROM Orders WHERE CustomerID = OLD.CustomerID) > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete customer with existing orders';
    END IF;
END$$
DELIMITER ;

-- Create trigger to prevent deletion of suppliers with existing products
DELIMITER $$
CREATE TRIGGER PreventSupplierDeletion
BEFORE DELETE ON Suppliers
FOR EACH ROW
BEGIN
    IF (SELECT COUNT(*) FROM Products WHERE SupplierID = OLD.SupplierID) > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete supplier with existing products';
    END IF;
END$$
DELIMITER ;
```
