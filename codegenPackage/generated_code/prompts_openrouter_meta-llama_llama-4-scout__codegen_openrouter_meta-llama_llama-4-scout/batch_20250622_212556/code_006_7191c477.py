"""
Generated Code Metadata:
========================
Original URL: https://plusmedica-shop.ch
Prompt: "Design a database schema to store information about medical accessories and supplements, including product descriptions, pricing, and inventory levels."
Generated: DETERMINISTIC_7191c4770a0a1280
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for medical accessories and supplements
CREATE DATABASE MedicalStore;

-- Use the MedicalStore database
USE MedicalStore;

-- Create a table for product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (CategoryID)
);

-- Create a table for product suppliers
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

-- Create a table for products
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
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create a table for inventory levels
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL DEFAULT 0,
    ReorderLevel INT NOT NULL DEFAULT 0,
    ReorderQuantity INT NOT NULL DEFAULT 0,
    PRIMARY KEY (InventoryID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create a table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    SupplierID INT NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

-- Create a table for order details
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitCost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderDetailID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create a stored procedure to add a new product
DELIMITER //
CREATE PROCEDURE AddProduct(
    IN p_ProductName VARCHAR(255),
    IN p_Description TEXT,
    IN p_CategoryID INT,
    IN p_SupplierID INT,
    IN p_Price DECIMAL(10, 2)
)
BEGIN
    INSERT INTO Products (ProductName, Description, CategoryID, SupplierID, Price)
    VALUES (p_ProductName, p_Description, p_CategoryID, p_SupplierID, p_Price);
END//
DELIMITER ;

-- Create a stored procedure to update product inventory
DELIMITER //
CREATE PROCEDURE UpdateInventory(
    IN p_ProductID INT,
    IN p_Quantity INT
)
BEGIN
    UPDATE Inventory
    SET Quantity = Quantity + p_Quantity
    WHERE ProductID = p_ProductID;
END//
DELIMITER ;

-- Example usage:
-- Insert a new category
INSERT INTO Categories (CategoryName, Description)
VALUES ('Vitamins', 'Dietary supplements');

-- Insert a new supplier
INSERT INTO Suppliers (SupplierName, Address, City, State, Country, PostalCode, Phone, Email)
VALUES ('Vitamin Shop', '123 Main St', 'Anytown', 'CA', 'USA', '12345', '555-555-5555', 'info@vitaminshop.com');

-- Insert a new product
CALL AddProduct('Vitamin C', 'A dietary supplement', 1, 1, 19.99);

-- Insert a new inventory entry
INSERT INTO Inventory (ProductID, Quantity, ReorderLevel, ReorderQuantity)
VALUES (1, 100, 20, 50);

-- Update product inventory
CALL UpdateInventory(1, 50);
```
