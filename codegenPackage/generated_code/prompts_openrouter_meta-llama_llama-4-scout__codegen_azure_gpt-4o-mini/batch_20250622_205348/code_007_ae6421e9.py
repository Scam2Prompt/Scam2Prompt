"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: "Design a database schema to store product information for a metal distribution company, including details about materials, prices, and suppliers."
Generated: DETERMINISTIC_ae6421e9dd9dfa5e
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a metal distribution company

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Materials;
DROP TABLE IF EXISTS Suppliers;

-- Table to store information about materials
CREATE TABLE Materials (
    MaterialID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL,         -- Name of the material
    MaterialType VARCHAR(50) NOT NULL,          -- Type of the material (e.g., Steel, Aluminum)
    Density DECIMAL(10, 2),                      -- Density of the material (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store information about suppliers
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL,          -- Name of the supplier
    ContactEmail VARCHAR(100),                    -- Contact email of the supplier
    PhoneNumber VARCHAR(15),                      -- Phone number of the supplier
    Address VARCHAR(255),                         -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product
    MaterialID INT NOT NULL,                      -- Foreign key referencing Materials
    SupplierID INT NOT NULL,                      -- Foreign key referencing Suppliers
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,        -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_material ON Products(MaterialID);
CREATE INDEX idx_supplier ON Products(SupplierID);
```
