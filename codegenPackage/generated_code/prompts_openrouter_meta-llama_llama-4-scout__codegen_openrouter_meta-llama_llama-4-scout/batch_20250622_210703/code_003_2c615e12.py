"""
Generated Code Metadata:
========================
Original URL: https://andesboardmaker.com
Prompt: Design a database schema for an online store that sells skateboarding equipment, including boards, hardware, and apparel, with columns for product descriptions, prices, and inventory levels.
Generated: DETERMINISTIC_2c615e1246fe2700
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for online skate store
CREATE DATABASE SkateStore;

-- Use the SkateStore database
USE SkateStore;

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription TEXT,
    ProductType ENUM('board', 'hardware', 'apparel') NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    InventoryLevel INT NOT NULL DEFAULT 0,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create table for boards
CREATE TABLE Boards (
    BoardID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    BoardType ENUM('complete', 'deck', 'truck') NOT NULL,
    Wheelbase DECIMAL(5, 2),
    Width DECIMAL(5, 2),
    Length DECIMAL(5, 2),
    Material VARCHAR(255),
    PRIMARY KEY (BoardID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create table for hardware
CREATE TABLE Hardware (
    HardwareID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    HardwareType ENUM('wheel', 'bearing', 'bolt') NOT NULL,
    Size DECIMAL(5, 2),
    Material VARCHAR(255),
    PRIMARY KEY (HardwareID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create table for apparel
CREATE TABLE Apparel (
    ApparelID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    ApparelType ENUM('shirt', 'pant', 'shoe') NOT NULL,
    Size ENUM('XS', 'S', 'M', 'L', 'XL') NOT NULL,
    Material VARCHAR(255),
    PRIMARY KEY (ApparelID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerName VARCHAR(255) NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalCost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderID)
);

-- Create table for order items
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    PRIMARY KEY (OrderItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_boards_productid ON Boards(ProductID);
CREATE INDEX idx_hardware_productid ON Hardware(ProductID);
CREATE INDEX idx_apparel_productid ON Apparel(ProductID);
CREATE INDEX idx_orderitems_orderid ON OrderItems(OrderID);
CREATE INDEX idx_orderitems_productid ON OrderItems(ProductID);

-- Insert sample data
INSERT INTO Products (ProductName, ProductDescription, ProductType, Price, InventoryLevel)
VALUES 
('Skateboard Deck', 'A wooden skateboard deck', 'board', 50.00, 10),
('Truck', 'A skateboard truck', 'hardware', 20.00, 20),
('T-Shirt', 'A skateboarding t-shirt', 'apparel', 15.00, 15);

INSERT INTO Boards (ProductID, BoardType, Wheelbase, Width, Length, Material)
VALUES 
(1, 'deck', 14.5, 10.0, 30.0, 'Maple Wood');

INSERT INTO Hardware (ProductID, HardwareType, Size, Material)
VALUES 
(2, 'truck', 125.0, 'Aluminum');

INSERT INTO Apparel (ProductID, ApparelType, Size, Material)
VALUES 
(3, 'shirt', 'M', 'Cotton');

INSERT INTO Orders (CustomerName, TotalCost)
VALUES 
('John Doe', 100.00);

INSERT INTO OrderItems (OrderID, ProductID, Quantity)
VALUES 
(1, 1, 1),
(1, 2, 2);
```
