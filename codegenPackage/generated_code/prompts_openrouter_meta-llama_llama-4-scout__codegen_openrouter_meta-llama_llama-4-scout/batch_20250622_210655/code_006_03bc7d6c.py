"""
Generated Code Metadata:
========================
Original URL: https://learnatcheap.com
Prompt: "Design a database schema for storing course information, customer details, and order history for an e-commerce platform like LearningAtCheap.com."
Generated: DETERMINISTIC_03bc7d6cdc7b5706
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for LearningAtCheap.com

-- Create database
CREATE DATABASE LearningAtCheap;

-- Use database
USE LearningAtCheap;

-- Create table for courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT,
    CourseName VARCHAR(255) NOT NULL,
    CourseDescription TEXT,
    CoursePrice DECIMAL(10, 2) NOT NULL,
    CourseDuration INT,
    CourseLevel VARCHAR(50),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CourseID)
);

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    PostalCode VARCHAR(10),
    Country VARCHAR(50),
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
    Status VARCHAR(50) NOT NULL,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for order items
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    CourseID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_CustomerID ON Orders (CustomerID);
CREATE INDEX idx_OrderID ON OrderItems (OrderID);
CREATE INDEX idx_CourseID ON OrderItems (CourseID);
CREATE INDEX idx_PaymentID ON Payments (PaymentID);
```

```sql
-- Example data insertion for testing
INSERT INTO Courses (CourseName, CourseDescription, CoursePrice, CourseDuration, CourseLevel)
VALUES 
('Introduction to Python', 'Learn the basics of Python programming', 19.99, 3, 'Beginner'),
('Advanced Java', 'Master the art of Java programming', 49.99, 6, 'Advanced');

INSERT INTO Customers (FirstName, LastName, Email, PasswordHash, Address, City, State, PostalCode, Country, PhoneNumber)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'password_hash', '123 Main St', 'New York', 'NY', '10001', 'USA', '123-456-7890'),
('Jane', 'Doe', 'jane.doe@example.com', 'password_hash', '456 Park Ave', 'Los Angeles', 'CA', '90001', 'USA', '987-654-3210');

INSERT INTO Orders (CustomerID, TotalCost, Status)
VALUES 
(1, 19.99, 'Completed'),
(2, 49.99, 'Pending');

INSERT INTO OrderItems (OrderID, CourseID, Quantity, UnitPrice)
VALUES 
(1, 1, 1, 19.99),
(2, 2, 1, 49.99);

INSERT INTO Payments (OrderID, PaymentMethod, Amount)
VALUES 
(1, 'Credit Card', 19.99),
(2, 'PayPal', 49.99);
```
