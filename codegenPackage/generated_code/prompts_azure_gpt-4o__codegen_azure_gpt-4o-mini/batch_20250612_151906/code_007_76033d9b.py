"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Create a database schema for managing procurement data, including categories like safety items, studs, bolts, and compressors, based on Cedar International Inc.'s offerings.
Generated: DETERMINISTIC_76033d9bde0102d5
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing procurement data for Cedar International Inc.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Purchases;

-- Table to store supplier information
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,         -- Name of the supplier
    ContactEmail VARCHAR(255),                   -- Email contact for the supplier
    PhoneNumber VARCHAR(20),                     -- Phone number of the supplier
    Address VARCHAR(255),                        -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the supplier was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,   -- Name of the category (e.g., safety items, studs)
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    CategoryID INT NOT NULL,                     -- Foreign key referencing Categories
    SupplierID INT NOT NULL,                     -- Foreign key referencing Suppliers
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,        -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store purchase orders
CREATE TABLE Purchases (
    PurchaseID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each purchase
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    Quantity INT NOT NULL,                        -- Quantity purchased
    PurchaseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the purchase
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the purchase
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the purchase was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (optional, for initial setup)
INSERT INTO Categories (CategoryName, Description) VALUES
('Safety Items', 'Items related to safety equipment'),
('Studs', 'Fasteners used in construction'),
('Bolts', 'Heavy-duty fasteners'),
('Compressors', 'Devices for compressing air');

INSERT INTO Suppliers (SupplierName, ContactEmail, PhoneNumber, Address) VALUES
('Supplier A', 'contact@suppliera.com', '123-456-7890', '123 Supplier St, City, Country'),
('Supplier B', 'contact@supplierb.com', '098-765-4321', '456 Supplier Ave, City, Country');

INSERT INTO Products (ProductName, CategoryID, SupplierID, Price, StockQuantity) VALUES
('Safety Helmet', 1, 1, 25.00, 100),
('Hex Bolt', 2, 2, 0.50, 500),
('Air Compressor', 4, 1, 150.00, 30);
```
