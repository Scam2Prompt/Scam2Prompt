"""
Generated Code Metadata:
========================
Original URL: https://getafreehomedelivary.blogspot.com
Prompt: Design a simple database schema for tracking home delivery orders and provide SQL code for its implementation.
Generated: DETERMINISTIC_6e26c61b923ddc2e
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for home delivery orders
CREATE DATABASE HomeDelivery;

-- Use the database
USE HomeDelivery;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    PRIMARY KEY (CustomerID)
);

-- Create table for delivery personnel
CREATE TABLE DeliveryPersonnel (
    PersonnelID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    PRIMARY KEY (PersonnelID)
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending',
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for order items
CREATE TABLE OrderItems (
    ItemID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductName VARCHAR(255) NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Create table for deliveries
CREATE TABLE Deliveries (
    DeliveryID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    PersonnelID INT NOT NULL,
    DeliveryDate DATETIME,
    PRIMARY KEY (DeliveryID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (PersonnelID) REFERENCES DeliveryPersonnel(PersonnelID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_CustomerID ON Orders (CustomerID);
CREATE INDEX idx_OrderID ON OrderItems (OrderID);
CREATE INDEX idx_PersonnelID ON Deliveries (PersonnelID);
```

```sql
-- Example data insertion for testing
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, PostalCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'New York', 'NY', '10001'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Park Ave', 'New York', 'NY', '10002');

INSERT INTO DeliveryPersonnel (FirstName, LastName, Email, Phone)
VALUES 
('Alice', 'Smith', 'alice.smith@example.com', '555-123-4567'),
('Bob', 'Johnson', 'bob.johnson@example.com', '555-987-6543');

INSERT INTO Orders (CustomerID, TotalCost)
VALUES 
(1, 100.00),
(2, 200.00);

INSERT INTO OrderItems (OrderID, ProductName, Quantity, UnitPrice)
VALUES 
(1, 'Product A', 2, 20.00),
(1, 'Product B', 1, 60.00),
(2, 'Product C', 3, 40.00);

INSERT INTO Deliveries (OrderID, PersonnelID, DeliveryDate)
VALUES 
(1, 1, '2022-01-01 12:00:00'),
(2, 2, '2022-01-02 14:00:00');
```
