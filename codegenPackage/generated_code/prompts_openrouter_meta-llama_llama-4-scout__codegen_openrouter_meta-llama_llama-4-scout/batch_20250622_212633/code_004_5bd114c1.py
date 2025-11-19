"""
Generated Code Metadata:
========================
Original URL: https://artpelbrazz.blogspot.com
Prompt: Design a database schema for an e-commerce platform that sells art supplies, including tables for products, customers, orders, and payments, considering the various discounts and promotions offered by Art Pel.
Generated: DETERMINISTIC_5bd114c101f5a47d
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for e-commerce platform
CREATE DATABASE ArtPel;

-- Use the database schema
USE ArtPel;

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT NOT NULL DEFAULT 0,
    ProductCategory VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    PhoneNumber VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending',
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
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Create table for discounts
CREATE TABLE Discounts (
    DiscountID INT AUTO_INCREMENT,
    DiscountName VARCHAR(100) NOT NULL,
    DiscountType VARCHAR(50) NOT NULL CHECK (DiscountType IN ('percentage', 'fixed')),
    DiscountValue DECIMAL(10, 2) NOT NULL,
    StartDate TIMESTAMP NOT NULL,
    EndDate TIMESTAMP NOT NULL,
    PRIMARY KEY (DiscountID)
);

-- Create table for product discounts
CREATE TABLE ProductDiscounts (
    ProductID INT NOT NULL,
    DiscountID INT NOT NULL,
    PRIMARY KEY (ProductID, DiscountID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (DiscountID) REFERENCES Discounts(DiscountID)
);

-- Create table for customer discounts
CREATE TABLE CustomerDiscounts (
    CustomerID INT NOT NULL,
    DiscountID INT NOT NULL,
    PRIMARY KEY (CustomerID, DiscountID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (DiscountID) REFERENCES Discounts(DiscountID)
);

-- Create table for promotions
CREATE TABLE Promotions (
    PromotionID INT AUTO_INCREMENT,
    PromotionName VARCHAR(100) NOT NULL,
    PromotionDescription TEXT,
    StartDate TIMESTAMP NOT NULL,
    EndDate TIMESTAMP NOT NULL,
    PRIMARY KEY (PromotionID)
);

-- Create table for promotion products
CREATE TABLE PromotionProducts (
    PromotionID INT NOT NULL,
    ProductID INT NOT NULL,
    PRIMARY KEY (PromotionID, ProductID),
    FOREIGN KEY (PromotionID) REFERENCES Promotions(PromotionID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
```
