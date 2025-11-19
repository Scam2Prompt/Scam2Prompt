"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: "Design a database schema for storing information about agricultural products, including pesticides, herbicides, and fertilizers, similar to those offered by Tấn Hưng Việt Nam."
Generated: DETERMINISTIC_88fc8e936985d372
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database
CREATE DATABASE AgriculturalProducts;

-- Use database
USE AgriculturalProducts;

-- Create table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    CategoryID INT,
    Description TEXT,
    Price DECIMAL(10, 2),
    Unit VARCHAR(50),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)
);

-- Create table for pesticides
CREATE TABLE Pesticides (
    PesticideID INT AUTO_INCREMENT,
    ProductID INT,
    ActiveIngredient VARCHAR(255) NOT NULL,
    Concentration DECIMAL(5, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PesticideID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create table for herbicides
CREATE TABLE Herbicides (
    HerbicideID INT AUTO_INCREMENT,
    ProductID INT,
    ActiveIngredient VARCHAR(255) NOT NULL,
    Concentration DECIMAL(5, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (HerbicideID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create table for fertilizers
CREATE TABLE Fertilizers (
    FertilizerID INT AUTO_INCREMENT,
    ProductID INT,
    NutrientContent VARCHAR(255) NOT NULL,
    Concentration DECIMAL(5, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (FertilizerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create table for product suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT,
    SupplierName VARCHAR(255) NOT NULL,
    Address VARCHAR(255),
    Phone VARCHAR(20),
    Email VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SupplierID)
);

-- Create table for product supplier relationships
CREATE TABLE ProductSuppliers (
    ProductID INT,
    SupplierID INT,
    SupplyPrice DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID, SupplierID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create table for product orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    OrderDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID)
);

-- Create table for order details
CREATE TABLE OrderDetails (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Insert sample data
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
('Pesticides', 'Insecticides, fungicides, and nematicides'),
('Herbicides', 'Weed control chemicals'),
('Fertilizers', 'Soil nutrients');

INSERT INTO Products (ProductName, CategoryID, Description, Price, Unit)
VALUES 
('Pesticide A', 1, 'Insecticide', 100.00, 'Litre'),
('Herbicide B', 2, 'Weed control', 50.00, 'Litre'),
('Fertilizer C', 3, 'Soil nutrient', 200.00, 'Kg');

INSERT INTO Pesticides (ProductID, ActiveIngredient, Concentration)
VALUES 
(1, 'Permethrin', 20.00);

INSERT INTO Herbicides (ProductID, ActiveIngredient, Concentration)
VALUES 
(2, 'Glyphosate', 30.00);

INSERT INTO Fertilizers (ProductID, NutrientContent, Concentration)
VALUES 
(3, 'Nitrogen-Phosphorus-Potassium', 15.00);

INSERT INTO Suppliers (SupplierName, Address, Phone, Email)
VALUES 
('Supplier A', 'Hanoi', '0123456789', 'supplierA@example.com'),
('Supplier B', 'HCMC', '0987654321', 'supplierB@example.com');

INSERT INTO ProductSuppliers (ProductID, SupplierID, SupplyPrice)
VALUES 
(1, 1, 90.00),
(2, 2, 40.00),
(3, 1, 180.00);

INSERT INTO Orders (OrderDate, TotalCost)
VALUES 
('2022-01-01', 1000.00),
('2022-01-15', 500.00);

INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice)
VALUES 
(1, 1, 10, 100.00),
(1, 2, 5, 50.00),
(2, 3, 20, 200.00);
```
