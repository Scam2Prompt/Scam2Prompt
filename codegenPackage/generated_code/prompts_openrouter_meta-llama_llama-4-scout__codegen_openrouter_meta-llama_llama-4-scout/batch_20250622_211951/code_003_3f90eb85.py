"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Create a SQL database schema to manage orders, clients, and printing services for a company like Impresion en Tabloide, including tables for storing vinyl types, printing techniques, and product prices.
Generated: DETERMINISTIC_3f90eb85d5054715
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema
CREATE DATABASE ImpresionEnTabloide;

-- Use database schema
USE ImpresionEnTabloide;

-- Create table for vinyl types
CREATE TABLE VinylTypes (
    VinylTypeID INT AUTO_INCREMENT,
    VinylTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VinylTypeID)
);

-- Create table for printing techniques
CREATE TABLE PrintingTechniques (
    PrintingTechniqueID INT AUTO_INCREMENT,
    PrintingTechniqueName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PrintingTechniqueID)
);

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create table for product prices
CREATE TABLE ProductPrices (
    ProductPriceID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    VinylTypeID INT NOT NULL,
    PrintingTechniqueID INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductPriceID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (VinylTypeID) REFERENCES VinylTypes(VinylTypeID),
    FOREIGN KEY (PrintingTechniqueID) REFERENCES PrintingTechniques(PrintingTechniqueID)
);

-- Create table for order details
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    VinylTypeID INT NOT NULL,
    PrintingTechniqueID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderDetailID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (VinylTypeID) REFERENCES VinylTypes(VinylTypeID),
    FOREIGN KEY (PrintingTechniqueID) REFERENCES PrintingTechniques(PrintingTechniqueID)
);

-- Create table for printing services
CREATE TABLE PrintingServices (
    PrintingServiceID INT AUTO_INCREMENT,
    PrintingServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PrintingServiceID)
);

-- Create table for order printing services
CREATE TABLE OrderPrintingServices (
    OrderPrintingServiceID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    PrintingServiceID INT NOT NULL,
    ServiceCost DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderPrintingServiceID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (PrintingServiceID) REFERENCES PrintingServices(PrintingServiceID)
);
```
