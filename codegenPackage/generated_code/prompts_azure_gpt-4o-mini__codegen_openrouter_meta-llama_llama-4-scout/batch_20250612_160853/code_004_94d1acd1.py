"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Design a database schema in SQL for managing inventory of acrylic yarn products, based on the offerings of Ramji Acro.
Generated: DETERMINISTIC_94d1acd1397a40c8
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for managing inventory of acrylic yarn products
CREATE DATABASE RamjiAcroInventory;

-- Use the created database
USE RamjiAcroInventory;

-- Create a table for yarn categories
CREATE TABLE YarnCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create a table for yarn brands
CREATE TABLE YarnBrands (
    BrandID INT AUTO_INCREMENT,
    BrandName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (BrandID)
);

-- Create a table for yarn products
CREATE TABLE YarnProducts (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    CategoryID INT,
    BrandID INT,
    Weight VARCHAR(50),
    FiberContent VARCHAR(100) NOT NULL,
    Color VARCHAR(100),
    SkeinLength DECIMAL(10, 2),
    SkeinWeight DECIMAL(10, 2),
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT DEFAULT 0,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (CategoryID) REFERENCES YarnCategories(CategoryID),
    FOREIGN KEY (BrandID) REFERENCES YarnBrands(BrandID)
);

-- Create a table for yarn product variants
CREATE TABLE YarnProductVariants (
    VariantID INT AUTO_INCREMENT,
    ProductID INT,
    Color VARCHAR(100),
    SkeinLength DECIMAL(10, 2),
    SkeinWeight DECIMAL(10, 2),
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT DEFAULT 0,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VariantID),
    FOREIGN KEY (ProductID) REFERENCES YarnProducts(ProductID)
);

-- Create a table for inventory transactions
CREATE TABLE InventoryTransactions (
    TransactionID INT AUTO_INCREMENT,
    ProductID INT,
    VariantID INT,
    TransactionType ENUM('IN', 'OUT') NOT NULL,
    Quantity INT NOT NULL,
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (TransactionID),
    FOREIGN KEY (ProductID) REFERENCES YarnProducts(ProductID),
    FOREIGN KEY (VariantID) REFERENCES YarnProductVariants(VariantID)
);

-- Create a table for suppliers
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

-- Create a table for purchase orders
CREATE TABLE PurchaseOrders (
    OrderID INT AUTO_INCREMENT,
    SupplierID INT,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status ENUM('PENDING', 'SHIPPED', 'RECEIVED') DEFAULT 'PENDING',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create a table for purchase order items
CREATE TABLE PurchaseOrderItems (
    OrderItemID INT AUTO_INCREMENT,
    OrderID INT,
    ProductID INT,
    VariantID INT,
    Quantity INT NOT NULL,
    UnitCost DECIMAL(10, 2) NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderItemID),
    FOREIGN KEY (OrderID) REFERENCES PurchaseOrders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES YarnProducts(ProductID),
    FOREIGN KEY (VariantID) REFERENCES YarnProductVariants(VariantID)
);

-- Insert some sample data
INSERT INTO YarnCategories (CategoryName, Description)
VALUES 
('Acrylic Yarns', 'High-quality acrylic yarns for knitting and crochet'),
('Blended Yarns', 'Acrylic yarns blended with other fibers');

INSERT INTO YarnBrands (BrandName, Description)
VALUES 
('Ramji Acro', 'Ramji Acro acrylic yarns');

INSERT INTO YarnProducts (ProductName, CategoryID, BrandID, FiberContent, Price, StockQuantity)
VALUES 
('Ramji Acro 100% Acrylic Yarn', 1, 1, '100% Acrylic', 5.99, 100),
('Ramji Acro Blended Yarn', 2, 1, '80% Acrylic, 20% Wool', 7.99, 50);

INSERT INTO YarnProductVariants (ProductID, Color, SkeinLength, SkeinWeight, Price, StockQuantity)
VALUES 
(1, 'Red', 300, 100, 5.99, 50),
(1, 'Blue', 300, 100, 5.99, 30),
(2, 'Green', 250, 80, 7.99, 20);

INSERT INTO Suppliers (SupplierName, Address, Phone, Email)
VALUES 
('Acrylic Yarn Suppliers', '123 Main St', '123-456-7890', 'info@acrylicyarnsuppliers.com');

INSERT INTO PurchaseOrders (SupplierID, OrderDate, TotalCost)
VALUES 
(1, '2022-01-01', 1000.00);

INSERT INTO PurchaseOrderItems (OrderID, ProductID, VariantID, Quantity, UnitCost, TotalCost)
VALUES 
(1, 1, 1, 50, 5.99, 299.50),
(1, 2, 3, 20, 7.99, 159.80);
```
