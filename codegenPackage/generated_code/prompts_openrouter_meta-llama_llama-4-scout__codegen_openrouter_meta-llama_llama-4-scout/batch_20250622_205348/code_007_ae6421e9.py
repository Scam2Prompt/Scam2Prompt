"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: "Design a database schema to store product information for a metal distribution company, including details about materials, prices, and suppliers."
Generated: DETERMINISTIC_ae6421e9dd9dfa5e
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the metal distribution company
CREATE DATABASE MetalDistribution;

-- Use the MetalDistribution database
USE MetalDistribution;

-- Create a table to store material information
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT,
    MaterialName VARCHAR(255) NOT NULL,
    MaterialType VARCHAR(100) NOT NULL,
    Density DECIMAL(10, 2) NOT NULL,
    Unit VARCHAR(20) NOT NULL,
    PRIMARY KEY (MaterialID)
);

-- Create a table to store supplier information
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

-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    MaterialID INT NOT NULL,
    SupplierID INT NOT NULL,
    Description TEXT,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create a table to store price information
CREATE TABLE Prices (
    PriceID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    Price DECIMAL(15, 2) NOT NULL,
    Unit VARCHAR(20) NOT NULL,
    EffectiveDate DATE NOT NULL,
    ExpirationDate DATE,
    PRIMARY KEY (PriceID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create a table to store product inventory
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    Quantity DECIMAL(15, 2) NOT NULL,
    Unit VARCHAR(20) NOT NULL,
    Warehouse VARCHAR(100) NOT NULL,
    PRIMARY KEY (InventoryID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_Materials_MaterialID ON Materials (MaterialID);
CREATE INDEX idx_Suppliers_SupplierID ON Suppliers (SupplierID);
CREATE INDEX idx_Products_MaterialID ON Products (MaterialID);
CREATE INDEX idx_Products_SupplierID ON Products (SupplierID);
CREATE INDEX idx_Prices_ProductID ON Prices (ProductID);
CREATE INDEX idx_Inventory_ProductID ON Inventory (ProductID);

-- Insert sample data into the tables
INSERT INTO Materials (MaterialName, MaterialType, Density, Unit)
VALUES 
('Aluminum', 'Metal', 2.70, 'kg/m³'),
('Copper', 'Metal', 8.96, 'kg/m³'),
('Steel', 'Alloy', 7.85, 'kg/m³');

INSERT INTO Suppliers (SupplierName, Address, City, State, Country, PostalCode, Phone, Email)
VALUES 
('Supplier1', '123 Main St', 'New York', 'NY', 'USA', '10001', '123-456-7890', 'supplier1@example.com'),
('Supplier2', '456 Elm St', 'Chicago', 'IL', 'USA', '60601', '987-654-3210', 'supplier2@example.com');

INSERT INTO Products (ProductName, MaterialID, SupplierID, Description)
VALUES 
('Aluminum Sheet', 1, 1, 'A sheet of aluminum'),
('Copper Wire', 2, 2, 'A spool of copper wire'),
('Steel Beam', 3, 1, 'A steel beam');

INSERT INTO Prices (ProductID, Price, Unit, EffectiveDate)
VALUES 
(1, 10.99, 'kg', '2022-01-01'),
(2, 5.99, 'm', '2022-01-01'),
(3, 20.99, 'kg', '2022-01-01');

INSERT INTO Inventory (ProductID, Quantity, Unit, Warehouse)
VALUES 
(1, 1000.00, 'kg', 'Warehouse A'),
(2, 500.00, 'm', 'Warehouse B'),
(3, 2000.00, 'kg', 'Warehouse A');
```
