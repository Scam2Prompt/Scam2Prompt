"""
Generated Code Metadata:
========================
Original URL: https://www.trendsetterzs.com
Prompt: Design a database schema for managing supply chain data, including tables for products, manufacturers, suppliers, and quality control metrics, inspired by Trendsetters' supply chain management services.
Generated: DETERMINISTIC_f337fcbfa4ad5b65
Batch ID: 20250622_211606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for supply chain management

CREATE DATABASE SupplyChainManagement;

USE SupplyChainManagement;

-- Create table for manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ManufacturerID)
);

-- Create table for suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    ManufacturerID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SupplierID),
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID)
);

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    SKU VARCHAR(100) UNIQUE NOT NULL,
    ManufacturerID INT,
    SupplierID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create table for quality control metrics
CREATE TABLE QualityControlMetrics (
    MetricID INT AUTO_INCREMENT,
    ProductID INT,
    MetricName VARCHAR(100) NOT NULL,
    MetricValue DECIMAL(10, 2) NOT NULL,
    Unit VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MetricID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create table for quality control test results
CREATE TABLE QualityControlTestResults (
    TestResultID INT AUTO_INCREMENT,
    ProductID INT,
    TestDate DATE NOT NULL,
    Passed BOOLEAN NOT NULL,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TestResultID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create indexes for foreign keys
CREATE INDEX idx_Suppliers_ManufacturerID ON Suppliers (ManufacturerID);
CREATE INDEX idx_Products_ManufacturerID ON Products (ManufacturerID);
CREATE INDEX idx_Products_SupplierID ON Products (SupplierID);
CREATE INDEX idx_QualityControlMetrics_ProductID ON QualityControlMetrics (ProductID);
CREATE INDEX idx_QualityControlTestResults_ProductID ON QualityControlTestResults (ProductID);

-- Insert sample data
INSERT INTO Manufacturers (Name, Address, City, State, Country, PostalCode, Phone, Email)
VALUES 
('Manufacturer1', '123 Main St', 'New York', 'NY', 'USA', '10001', '123-456-7890', 'manufacturer1@example.com'),
('Manufacturer2', '456 Elm St', 'Chicago', 'IL', 'USA', '60611', '987-654-3210', 'manufacturer2@example.com');

INSERT INTO Suppliers (Name, Address, City, State, Country, PostalCode, Phone, Email, ManufacturerID)
VALUES 
('Supplier1', '789 Oak St', 'Los Angeles', 'CA', 'USA', '90001', '555-123-4567', 'supplier1@example.com', 1),
('Supplier2', '321 Pine St', 'Houston', 'TX', 'USA', '77001', '901-234-5678', 'supplier2@example.com', 2);

INSERT INTO Products (Name, Description, SKU, ManufacturerID, SupplierID)
VALUES 
('Product1', 'This is product 1', 'ABC123', 1, 1),
('Product2', 'This is product 2', 'DEF456', 2, 2);

INSERT INTO QualityControlMetrics (ProductID, MetricName, MetricValue, Unit)
VALUES 
(1, 'Weight', 10.00, 'lbs'),
(1, 'Length', 20.00, 'in'),
(2, 'Width', 15.00, 'in');

INSERT INTO QualityControlTestResults (ProductID, TestDate, Passed, Notes)
VALUES 
(1, '2022-01-01', TRUE, 'Passed quality control test'),
(2, '2022-02-01', FALSE, 'Failed quality control test');
```
