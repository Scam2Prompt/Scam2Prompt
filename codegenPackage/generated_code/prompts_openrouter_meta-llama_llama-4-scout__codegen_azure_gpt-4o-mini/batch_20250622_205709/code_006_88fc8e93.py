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
-- Database schema for storing information about agricultural products
-- including pesticides, herbicides, and fertilizers.

CREATE DATABASE AgriculturalProductsDB;

USE AgriculturalProductsDB;

-- Table to store product categories (e.g., Pesticides, Herbicides, Fertilizers)
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store agricultural products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    CategoryID INT NOT NULL,
    Manufacturer VARCHAR(255),
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT DEFAULT 0,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE
);

-- Table to store product specifications
CREATE TABLE ProductSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT NOT NULL,
    SpecificationName VARCHAR(100) NOT NULL,
    SpecificationValue VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT NOT NULL,
    ReviewerName VARCHAR(100) NOT NULL,
    Rating INT CHECK (Rating >= 1 AND Rating <= 5),
    ReviewText TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    SupplierName VARCHAR(255) NOT NULL UNIQUE,
    ContactPerson VARCHAR(100),
    Phone VARCHAR(15),
    Email VARCHAR(100),
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to link products with suppliers
CREATE TABLE ProductSuppliers (
    ProductSupplierID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT NOT NULL,
    SupplierID INT NOT NULL,
    SupplyPrice DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_supplier_name ON Suppliers(SupplierName);
```
