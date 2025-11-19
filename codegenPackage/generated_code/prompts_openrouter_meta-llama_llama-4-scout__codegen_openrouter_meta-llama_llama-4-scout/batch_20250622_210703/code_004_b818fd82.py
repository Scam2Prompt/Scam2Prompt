"""
Generated Code Metadata:
========================
Original URL: https://yummydelivery.com.ve
Prompt: Design a database schema for a food delivery platform like Yummy Delivery, including tables for products, orders, customers, and delivery information.
Generated: DETERMINISTIC_b818fd826b2ea0f7
Batch ID: 20250622_210703
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/burger.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/pizza.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- Create database for Yummy Delivery
CREATE DATABASE YummyDelivery;

-- Use YummyDelivery database
USE YummyDelivery;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Country VARCHAR(100) NOT NULL,
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
    ImageURL VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create table for restaurants or stores
CREATE TABLE Restaurants (
    RestaurantID INT AUTO_INCREMENT,
    RestaurantName VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (RestaurantID)
);

-- Create table for order items or menu items
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT,
    OrderID INT,
    ProductID INT,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderItemID),
    FOREIGN KEY (OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) ON DELETE CASCADE
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT,
    RestaurantID INT,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status ENUM('Pending', 'Preparing', 'OutForDelivery', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (RestaurantID) ON DELETE CASCADE
);

-- Create table for delivery information
CREATE TABLE DeliveryInformation (
    DeliveryID INT AUTO_INCREMENT,
    OrderID INT,
    DeliveryDate TIMESTAMP,
    DeliveryTime TIMESTAMP,
    DeliveryStatus ENUM('Pending', 'EnRoute', 'Delivered') NOT NULL DEFAULT 'Pending',
    DeliveryPersonName VARCHAR(255),
    DeliveryPersonContact VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DeliveryID),
    FOREIGN KEY (OrderID) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    OrderID INT,
    PaymentMethod ENUM('Cash', 'Card', 'Online') NOT NULL,
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Amount DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (OrderID) ON DELETE CASCADE
);

-- Insert sample data into tables
INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, Address, City, State, PostalCode, Country)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St', 'New York', 'NY', '10001', 'USA'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210', '456 Park Ave', 'New York', 'NY', '10002', 'USA');

INSERT INTO Restaurants (RestaurantName, Address, City, State, PostalCode, Country)
VALUES 
('Pizza Hut', '789 Broadway', 'New York', 'NY', '10003', 'USA'),
('Burger King', '321 Fifth Ave', 'New York', 'NY', '10004', 'USA');

INSERT INTO Products (ProductName, Description, Price, ImageURL)
VALUES 
('Cheese Pizza', 'A delicious cheese pizza', 14.99, 'https://example.com/pizza.jpg'),
('Whopper Burger', 'A juicy whopper burger', 10.99, 'https://example.com/burger.jpg');

INSERT INTO Orders (CustomerID, RestaurantID, TotalCost, Status)
VALUES 
(1, 1, 14.99, 'Pending'),
(2, 2, 10.99, 'Pending');

INSERT INTO OrderItems (OrderID, ProductID, Quantity, UnitPrice)
VALUES 
(1, 1, 1, 14.99),
(2, 2, 1, 10.99);

INSERT INTO DeliveryInformation (OrderID, DeliveryDate, DeliveryTime, DeliveryStatus)
VALUES 
(1, NULL, NULL, 'Pending'),
(2, NULL, NULL, 'Pending');

INSERT INTO Payments (OrderID, PaymentMethod, Amount)
VALUES 
(1, 'Card', 14.99),
(2, 'Cash', 10.99);
```
