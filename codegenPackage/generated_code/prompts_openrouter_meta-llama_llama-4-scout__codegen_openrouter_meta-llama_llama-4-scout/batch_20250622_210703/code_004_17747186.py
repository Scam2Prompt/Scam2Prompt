"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Design a data model for a maritime supply company's database, including tables for customers, products, orders, and services such as provisioning and maintenance.
Generated: DETERMINISTIC_17747186629809b5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database
CREATE DATABASE MaritimeSupply;

-- Use database
USE MaritimeSupply;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    ContactName VARCHAR(255) NOT NULL,
    ContactTitle VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(100),
    Region VARCHAR(100),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    Phone VARCHAR(20),
    Fax VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    Description TEXT,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    UnitsInStock INT,
    UnitsOnOrder INT,
    ReorderLevel INT,
    Discontinued BOOLEAN DEFAULT FALSE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT,
    OrderDate DATE NOT NULL,
    RequiredDate DATE,
    ShippedDate DATE,
    ShipVia INT,
    Freight DECIMAL(10, 2),
    ShipName VARCHAR(255),
    ShipAddress VARCHAR(255),
    ShipCity VARCHAR(100),
    ShipRegion VARCHAR(100),
    ShipPostalCode VARCHAR(20),
    ShipCountry VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for order details
CREATE TABLE OrderDetails (
    OrderID INT,
    ProductID INT,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    Quantity INT NOT NULL,
    Discount DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create table for services (provisioning and maintenance)
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceType ENUM('provisioning', 'maintenance') NOT NULL,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create table for provisioning services
CREATE TABLE ProvisioningServices (
    ProvisioningServiceID INT AUTO_INCREMENT,
    OrderID INT,
    ServiceID INT,
    ServiceDate DATE NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProvisioningServiceID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create table for maintenance services
CREATE TABLE MaintenanceServices (
    MaintenanceServiceID INT AUTO_INCREMENT,
    OrderID INT,
    ServiceID INT,
    MaintenanceDate DATE NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MaintenanceServiceID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create indexes
CREATE INDEX idx_Customers_CompanyName ON Customers (CompanyName);
CREATE INDEX idx_Products_ProductName ON Products (ProductName);
CREATE INDEX idx_Orders_CustomerID ON Orders (CustomerID);
CREATE INDEX idx_OrderDetails_OrderID ON OrderDetails (OrderID);
CREATE INDEX idx_OrderDetails_ProductID ON OrderDetails (ProductID);
```

```sql
-- Example insert statements
INSERT INTO Customers (CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax, Email)
VALUES 
('ABC Shipping', 'John Doe', 'CEO', '123 Main St', 'New York', 'NY', '10001', 'USA', '123-456-7890', '123-456-7891', 'john.doe@example.com'),
('XYZ Marine', 'Jane Smith', 'Manager', '456 Park Ave', 'Los Angeles', 'CA', '90001', 'USA', '987-654-3210', '987-654-3211', 'jane.smith@example.com');

INSERT INTO Products (ProductName, Description, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
VALUES 
('Anchors', 'High-quality anchors for boats', 100.00, 100, 50, 20, FALSE),
('Ropes', 'Durable ropes for marine use', 50.00, 200, 100, 30, FALSE);

INSERT INTO Orders (CustomerID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry)
VALUES 
(1, '2022-01-01', '2022-01-15', '2022-01-10', 1, 100.00, 'ABC Shipping', '123 Main St', 'New York', 'NY', '10001', 'USA'),
(2, '2022-01-05', '2022-01-20', '2022-01-15', 2, 200.00, 'XYZ Marine', '456 Park Ave', 'Los Angeles', 'CA', '90001', 'USA');

INSERT INTO OrderDetails (OrderID, ProductID, UnitPrice, Quantity, Discount)
VALUES 
(1, 1, 100.00, 2, 0.00),
(1, 2, 50.00, 3, 0.00),
(2, 1, 100.00, 1, 0.00);

INSERT INTO Services (ServiceType, ServiceName, Description)
VALUES 
('provisioning', 'Food and Water Provisioning', 'Provisioning of food and water for vessels'),
('maintenance', 'Engine Maintenance', 'Regular maintenance of vessel engines');

INSERT INTO ProvisioningServices (OrderID, ServiceID, ServiceDate, Description)
VALUES 
(1, 1, '2022-01-05', 'Provisioning of food and water for vessel');

INSERT INTO MaintenanceServices (OrderID, ServiceID, MaintenanceDate, Description)
VALUES 
(2, 2, '2022-01-10', 'Regular maintenance of vessel engine');
```
