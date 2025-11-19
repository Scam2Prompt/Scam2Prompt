"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Write a SQL query to manage client orders for customized flip-flops and shoe soles, including tracking product types, quantities, and delivery status for clients like hoteles and eventos especiales.
Generated: DETERMINISTIC_4681cde182d8449f
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema to manage client orders for customized flip-flops and shoe soles

-- Create a table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    ClientName VARCHAR(255) NOT NULL,
    ClientType VARCHAR(100) NOT NULL,
    ContactPerson VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    PRIMARY KEY (ClientID)
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductType ENUM('flip-flops', 'shoe soles') NOT NULL,
    ProductDescription VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ProductID)
);

-- Create a table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    DeliveryStatus ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
    PRIMARY KEY (OrderID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Create a table for order items
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    PRIMARY KEY (OrderItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create a table for deliveries
CREATE TABLE Deliveries (
    DeliveryID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    DeliveryDate DATE,
    DeliveryStatus ENUM('pending', 'shipped', 'delivered') NOT NULL DEFAULT 'pending',
    PRIMARY KEY (DeliveryID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Insert sample data
INSERT INTO Clients (ClientName, ClientType, ContactPerson, Email, Phone, Address)
VALUES 
('Hoteles', 'hotel', 'John Doe', 'john.doe@hoteles.com', '123-456-7890', '123 Main St'),
('Eventos Especiales', 'event planner', 'Jane Smith', 'jane.smith@eventosespeciales.com', '987-654-3210', '456 Elm St');

INSERT INTO Products (ProductType, ProductDescription, Price)
VALUES 
('flip-flops', 'Customized flip-flops', 10.99),
('shoe soles', 'Customized shoe soles', 5.99);

INSERT INTO Orders (ClientID, OrderDate, TotalCost)
VALUES 
(1, '2022-01-01', 100.00),
(2, '2022-01-15', 50.00);

INSERT INTO OrderItems (OrderID, ProductID, Quantity)
VALUES 
(1, 1, 10),
(1, 2, 5),
(2, 1, 5);

INSERT INTO Deliveries (OrderID, DeliveryDate, DeliveryStatus)
VALUES 
(1, NULL, 'pending'),
(2, NULL, 'pending');

-- SQL queries to manage client orders

-- Get all orders for a client
SELECT * FROM Orders
WHERE ClientID = 1;

-- Get all order items for an order
SELECT * FROM OrderItems
WHERE OrderID = 1;

-- Update delivery status of an order
UPDATE Orders
SET DeliveryStatus = 'shipped'
WHERE OrderID = 1;

-- Update delivery status of a delivery
UPDATE Deliveries
SET DeliveryStatus = 'delivered', DeliveryDate = CURRENT_DATE
WHERE OrderID = 1;

-- Get total sales for a product
SELECT SUM(oi.Quantity * p.Price) AS TotalSales
FROM OrderItems oi
JOIN Products p ON oi.ProductID = p.ProductID
WHERE p.ProductID = 1;

-- Get all clients with pending deliveries
SELECT c.*
FROM Clients c
JOIN Orders o ON c.ClientID = o.ClientID
JOIN Deliveries d ON o.OrderID = d.OrderID
WHERE d.DeliveryStatus = 'pending';
```
