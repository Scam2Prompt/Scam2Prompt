"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Create a database schema for managing timber products, including categories like softwood, hardwood, and sawn timber, as described by Askar Trading International.
Generated: DETERMINISTIC_63c27bfee277f6b8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for managing timber products
CREATE DATABASE TimberProductsDB;

-- Use the created database
USE TimberProductsDB;

-- Create a table for timber product categories
CREATE TABLE TimberProductCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create a table for timber products
CREATE TABLE TimberProducts (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    CategoryID INT,
    Description TEXT,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    UnitOfMeasurement VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (CategoryID) REFERENCES TimberProductCategories(CategoryID)
);

-- Create a table for suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT,
    SupplierName VARCHAR(255) NOT NULL,
    ContactPerson VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SupplierID)
);

-- Create a table for product suppliers
CREATE TABLE ProductSuppliers (
    ProductID INT,
    SupplierID INT,
    SupplyPrice DECIMAL(10, 2) NOT NULL,
    LeadTime INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID, SupplierID),
    FOREIGN KEY (ProductID) REFERENCES TimberProducts(ProductID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create a table for inventory
CREATE TABLE Inventory (
    ProductID INT,
    Quantity INT NOT NULL DEFAULT 0,
    WarehouseLocation VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (ProductID) REFERENCES TimberProducts(ProductID)
);

-- Create a table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    OrderDate DATE NOT NULL,
    SupplierID INT,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK(Status IN ('Pending', 'Shipped', 'Delivered', 'Cancelled')),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create a table for order items
CREATE TABLE OrderItems (
    OrderID INT,
    ProductID INT,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES TimberProducts(ProductID)
);

-- Insert sample data into categories
INSERT INTO TimberProductCategories (CategoryName, Description)
VALUES 
('Softwood', 'Softwood timber products'),
('Hardwood', 'Hardwood timber products'),
('Sawn Timber', 'Sawn timber products');

-- Insert sample data into products
INSERT INTO TimberProducts (ProductName, CategoryID, Description, UnitPrice, UnitOfMeasurement)
VALUES 
('Pine Wood', 1, 'Softwood pine wood', 10.00, 'm3'),
('Oak Wood', 2, 'Hardwood oak wood', 20.00, 'm3'),
('Sawn Pine', 3, 'Sawn pine timber', 15.00, 'm2');

-- Insert sample data into suppliers
INSERT INTO Suppliers (SupplierName, ContactPerson, Email, Phone, Address)
VALUES 
('Askar Trading International', 'John Doe', 'john.doe@askartrading.com', '+1 123 456 7890', '123 Main St'),
('Timber Suppliers Inc.', 'Jane Smith', 'jane.smith@timbersuppliers.com', '+1 987 654 3210', '456 Elm St');

-- Insert sample data into product suppliers
INSERT INTO ProductSuppliers (ProductID, SupplierID, SupplyPrice, LeadTime)
VALUES 
(1, 1, 8.00, 7),
(2, 2, 18.00, 14),
(3, 1, 12.00, 10);

-- Insert sample data into inventory
INSERT INTO Inventory (ProductID, Quantity, WarehouseLocation)
VALUES 
(1, 100, 'Warehouse A'),
(2, 50, 'Warehouse B'),
(3, 200, 'Warehouse C');
```
