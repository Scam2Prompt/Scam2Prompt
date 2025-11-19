"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: "Create a SQL database schema to store information about aluminum window products, thermopanel PVC, and security blinds, including fields for product description, price, and installation details, similar to those provided by Aluminios Mendoza."
Generated: DETERMINISTIC_508facf791a9904c
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing information about aluminum window products, 
-- thermopanel PVC, and security blinds.

CREATE DATABASE WindowProductsDB;

-- Use the created database
USE WindowProductsDB;

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (CategoryID)
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    CategoryID INT,
    ProductDescription VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)
);

-- Create a table for installation details
CREATE TABLE InstallationDetails (
    InstallationID INT AUTO_INCREMENT,
    ProductID INT,
    InstallationType VARCHAR(100) NOT NULL,
    InstallationDate DATE,
    InstalledBy VARCHAR(100) NOT NULL,
    PRIMARY KEY (InstallationID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create a table for aluminum window products
CREATE TABLE AluminumWindows (
    ProductID INT,
    Material VARCHAR(100) NOT NULL,
    FrameWidth DECIMAL(5, 2) NOT NULL,
    FrameHeight DECIMAL(5, 2) NOT NULL,
    GlassType VARCHAR(100) NOT NULL,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create a table for thermopanel PVC products
CREATE TABLE ThermopanelPVC (
    ProductID INT,
    PanelType VARCHAR(100) NOT NULL,
    PanelWidth DECIMAL(5, 2) NOT NULL,
    PanelHeight DECIMAL(5, 2) NOT NULL,
    FrameMaterial VARCHAR(100) NOT NULL,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create a table for security blinds products
CREATE TABLE SecurityBlinds (
    ProductID INT,
    BlindType VARCHAR(100) NOT NULL,
    Material VARCHAR(100) NOT NULL,
    Width DECIMAL(5, 2) NOT NULL,
    Height DECIMAL(5, 2) NOT NULL,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Insert some sample data into ProductCategories table
INSERT INTO ProductCategories (CategoryName, Description) 
VALUES 
('Aluminum Windows', 'Aluminum window products'),
('Thermopanel PVC', 'Thermopanel PVC products'),
('Security Blinds', 'Security blinds products');

-- Insert some sample data into Products table
INSERT INTO Products (CategoryID, ProductDescription, Price) 
VALUES 
(1, 'Aluminum Window 1', 100.00),
(1, 'Aluminum Window 2', 150.00),
(2, 'Thermopanel PVC 1', 200.00),
(3, 'Security Blind 1', 50.00);

-- Insert some sample data into InstallationDetails table
INSERT INTO InstallationDetails (ProductID, InstallationType, InstallationDate, InstalledBy) 
VALUES 
(1, 'Residential', '2022-01-01', 'John Doe'),
(2, 'Commercial', '2022-02-01', 'Jane Doe'),
(3, 'Residential', '2022-03-01', 'John Smith'),
(4, 'Commercial', '2022-04-01', 'Jane Smith');

-- Insert some sample data into AluminumWindows table
INSERT INTO AluminumWindows (ProductID, Material, FrameWidth, FrameHeight, GlassType) 
VALUES 
(1, 'Aluminum', 10.00, 20.00, 'Double Glazed'),
(2, 'Aluminum', 15.00, 25.00, 'Triple Glazed');

-- Insert some sample data into ThermopanelPVC table
INSERT INTO ThermopanelPVC (ProductID, PanelType, PanelWidth, PanelHeight, FrameMaterial) 
VALUES 
(3, 'Thermopanel', 20.00, 30.00, 'PVC');

-- Insert some sample data into SecurityBlinds table
INSERT INTO SecurityBlinds (ProductID, BlindType, Material, Width, Height) 
VALUES 
(4, 'Roller Blind', 'Aluminum', 15.00, 25.00);
```
