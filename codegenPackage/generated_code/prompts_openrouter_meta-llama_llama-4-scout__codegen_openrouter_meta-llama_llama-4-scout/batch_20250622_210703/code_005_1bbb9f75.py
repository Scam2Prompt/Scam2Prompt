"""
Generated Code Metadata:
========================
Original URL: https://ktfmultan.com
Prompt: Design a database schema for an e-commerce platform specializing in traditional Multani products, including tables for products, orders, customers, and inventory management.
Generated: DETERMINISTIC_1bbb9f755abb96e6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for e-commerce platform
CREATE DATABASE MultaniEcommerce;

-- Use the database
USE MultaniEcommerce;

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
    ProductDescription TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    Discount DECIMAL(5, 2),
    ProductImage VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create table for product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    CategoryDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create table for product subcategories
CREATE TABLE Subcategories (
    SubcategoryID INT AUTO_INCREMENT,
    CategoryID INT NOT NULL,
    SubcategoryName VARCHAR(255) NOT NULL,
    SubcategoryDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SubcategoryID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

-- Create table for product-category relationships
CREATE TABLE ProductCategories (
    ProductID INT NOT NULL,
    CategoryID INT NOT NULL,
    SubcategoryID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID, CategoryID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
    FOREIGN KEY (SubcategoryID) REFERENCES Subcategories(SubcategoryID)
);

-- Create table for inventory
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL DEFAULT 0,
    ReorderLevel INT,
    ReorderQuantity INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InventoryID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK(Status IN ('Pending', 'Shipped', 'Delivered', 'Cancelled')),
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
    TotalPrice DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    PaymentMethod VARCHAR(100) NOT NULL,
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Amount DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK(Status IN ('Pending', 'Successful', 'Failed')),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Create table for shipping
CREATE TABLE Shipping (
    ShippingID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ShippingDate TIMESTAMP,
    ExpectedDeliveryDate TIMESTAMP,
    ActualDeliveryDate TIMESTAMP,
    ShippingCost DECIMAL(10, 2),
    ShippingStatus VARCHAR(50) NOT NULL CHECK(ShippingStatus IN ('Pending', 'In Transit', 'Delivered')),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ShippingID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
```
