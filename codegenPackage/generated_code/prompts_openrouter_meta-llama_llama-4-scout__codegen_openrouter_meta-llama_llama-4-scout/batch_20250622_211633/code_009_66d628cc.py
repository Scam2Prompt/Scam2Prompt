"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: "Design a database schema for storing and managing industrial product information, including product categories, pricing, and supplier details."
Generated: DETERMINISTIC_66d628cc2ce147e1
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for industrial product information

-- Create database
CREATE DATABASE IndustrialProductDB;

-- Use database
USE IndustrialProductDB;

-- Create table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
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
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SupplierID)
);

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    Description TEXT,
    CategoryID INT NOT NULL,
    SupplierID INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create table for product pricing history
CREATE TABLE ProductPricingHistory (
    PricingHistoryID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    EffectiveDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PricingHistoryID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create indexes for foreign keys
CREATE INDEX idx_ProductCategories_CategoryID ON Products (CategoryID);
CREATE INDEX idx_Suppliers_SupplierID ON Products (SupplierID);
CREATE INDEX idx_Products_ProductID ON ProductPricingHistory (ProductID);

-- Insert sample data
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
('Electrical', 'Electrical products'),
('Mechanical', 'Mechanical products'),
('Chemical', 'Chemical products');

INSERT INTO Suppliers (SupplierName, Address, City, State, Country, PostalCode, Phone, Email)
VALUES 
('Supplier1', '123 Main St', 'New York', 'NY', 'USA', '10001', '123-456-7890', 'supplier1@example.com'),
('Supplier2', '456 Elm St', 'Chicago', 'IL', 'USA', '60601', '987-654-3210', 'supplier2@example.com');

INSERT INTO Products (ProductName, Description, CategoryID, SupplierID, Price)
VALUES 
('Product1', 'This is product 1', 1, 1, 10.99),
('Product2', 'This is product 2', 2, 2, 5.99),
('Product3', 'This is product 3', 3, 1, 7.99);

INSERT INTO ProductPricingHistory (ProductID, Price, EffectiveDate)
VALUES 
(1, 10.99, '2022-01-01'),
(1, 11.99, '2022-06-01'),
(2, 5.99, '2022-01-01'),
(3, 7.99, '2022-01-01');
```
