"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Write code to create a database schema for managing maritime supply operations, including categories like food supplies, electrical equipment, tools, hygiene services, and personal protective equipment, as detailed by Supply Marine.
Generated: DETERMINISTIC_e4f2ce6aef05150e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for managing maritime supply operations

-- Create database
CREATE DATABASE MaritimeSupplyDB;

-- Use database
USE MaritimeSupplyDB;

-- Create table for supply categories
CREATE TABLE SupplyCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (CategoryID)
);

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

-- Create table for supplies
CREATE TABLE Supplies (
    SupplyID INT AUTO_INCREMENT,
    SupplyName VARCHAR(255) NOT NULL,
    Description TEXT,
    CategoryID INT NOT NULL,
    SupplierID INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    UnitOfMeasurement VARCHAR(20) NOT NULL,
    PRIMARY KEY (SupplyID),
    FOREIGN KEY (CategoryID) REFERENCES SupplyCategories(CategoryID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create table for inventory
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT,
    SupplyID INT NOT NULL,
    Quantity INT NOT NULL DEFAULT 0,
    ReorderLevel INT NOT NULL DEFAULT 0,
    ReorderQuantity INT NOT NULL DEFAULT 0,
    PRIMARY KEY (InventoryID),
    FOREIGN KEY (SupplyID) REFERENCES Supplies(SupplyID)
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    SupplierID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Pending', 'Shipped', 'Received', 'Cancelled')),
    PRIMARY KEY (OrderID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create table for order items
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    SupplyID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (SupplyID) REFERENCES Supplies(SupplyID)
);

-- Insert supply categories
INSERT INTO SupplyCategories (CategoryName, Description)
VALUES 
('Food Supplies', 'Food and beverages for crew and passengers'),
('Electrical Equipment', 'Electrical equipment and components'),
('Tools', 'Hand tools and machinery'),
('Hygiene Services', 'Hygiene and cleaning services'),
('Personal Protective Equipment', 'Personal protective equipment and gear');

-- Insert sample suppliers
INSERT INTO Suppliers (SupplierName, Address, City, State, Country, PostalCode, Phone, Email)
VALUES 
('Supplier 1', '123 Main St', 'New York', 'NY', 'USA', '10001', '123-456-7890', 'supplier1@example.com'),
('Supplier 2', '456 Elm St', 'Los Angeles', 'CA', 'USA', '90001', '987-654-3210', 'supplier2@example.com');

-- Insert sample supplies
INSERT INTO Supplies (SupplyName, Description, CategoryID, SupplierID, UnitPrice, UnitOfMeasurement)
VALUES 
('Fresh Water', 'Bottled water for drinking', 1, 1, 1.00, 'liter'),
('Bread', 'Freshly baked bread', 1, 1, 2.00, 'loaf'),
('LED Light', 'Energy-efficient LED light', 2, 2, 50.00, 'unit'),
('Wrench', 'Adjustable wrench', 3, 2, 20.00, 'unit'),
('Mop', 'Microfiber mop', 4, 1, 10.00, 'unit'),
('Gloves', 'Latex gloves', 5, 2, 5.00, 'pair');

-- Insert sample inventory
INSERT INTO Inventory (SupplyID, Quantity, ReorderLevel, ReorderQuantity)
VALUES 
(1, 1000, 500, 200),
(2, 500, 200, 100),
(3, 50, 20, 10),
(4, 100, 50, 20),
(5, 200, 100, 50),
(6, 500, 200, 100);
```
