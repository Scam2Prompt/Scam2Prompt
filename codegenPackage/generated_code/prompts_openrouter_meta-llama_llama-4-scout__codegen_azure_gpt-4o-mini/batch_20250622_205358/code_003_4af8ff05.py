"""
Generated Code Metadata:
========================
Original URL: https://starklinical.com.br
Prompt: "Design a database schema to store information about different types of furniture products, including hospital, school, and auditorium furniture, for a company like Starklinical."
Generated: DETERMINISTIC_4af8ff05ce5ce451
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about different types of furniture products
-- for a company like Starklinical

CREATE DATABASE StarklinicalFurniture;

USE StarklinicalFurniture;

-- Table to store information about furniture categories
CREATE TABLE FurnitureCategory (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about furniture products
CREATE TABLE FurnitureProduct (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    CategoryID INT NOT NULL,
    Material VARCHAR(100),
    Dimensions VARCHAR(100),
    Weight DECIMAL(10, 2),
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),
    StockQuantity INT NOT NULL CHECK (StockQuantity >= 0),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CategoryID) REFERENCES FurnitureCategory(CategoryID) ON DELETE CASCADE
);

-- Table to store information about suppliers
CREATE TABLE Supplier (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    SupplierName VARCHAR(100) NOT NULL UNIQUE,
    ContactName VARCHAR(100),
    Phone VARCHAR(15),
    Email VARCHAR(100),
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store the relationship between products and suppliers
CREATE TABLE ProductSupplier (
    ProductSupplierID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT NOT NULL,
    SupplierID INT NOT NULL,
    SupplyPrice DECIMAL(10, 2) NOT NULL CHECK (SupplyPrice >= 0),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProductID) REFERENCES FurnitureProduct(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID) ON DELETE CASCADE,
    UNIQUE (ProductID, SupplierID) -- Ensures a product can only have one supplier entry
);

-- Table to store customer orders
CREATE TABLE CustomerOrder (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0),
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store order details for each product in an order
CREATE TABLE OrderDetail (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (OrderID) REFERENCES CustomerOrder(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES FurnitureProduct(ProductID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON FurnitureProduct(ProductName);
CREATE INDEX idx_category_name ON FurnitureCategory(CategoryName);
CREATE INDEX idx_supplier_name ON Supplier(SupplierName);
CREATE INDEX idx_order_date ON CustomerOrder(OrderDate);
```
