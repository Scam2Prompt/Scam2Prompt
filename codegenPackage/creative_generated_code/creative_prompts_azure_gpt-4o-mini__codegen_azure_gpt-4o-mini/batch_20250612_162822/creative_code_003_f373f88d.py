"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: How can I create a database schema to store information about железобетонные изделия and their suppliers in Санкт-Петербурге, as described on the Paradigma site?
Generated: DETERMINISTIC_f373f88d41876a0e
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing information about железобетонные изделия and their suppliers

-- Create the database
CREATE DATABASE ConcreteProductsDB;

-- Use the created database
USE ConcreteProductsDB;

-- Table to store information about suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    Address VARCHAR(255),                       -- Address of the supplier
    Phone VARCHAR(50),                         -- Contact phone number
    Email VARCHAR(100),                        -- Contact email
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about железобетонные изделия (concrete products)
CREATE TABLE ConcreteProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each concrete product
    Name VARCHAR(255) NOT NULL,                 -- Name of the concrete product
    Description TEXT,                           -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    SupplierID INT,                             -- Reference to the supplier of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Optional: Create an index on the Product Name for faster search
CREATE INDEX idx_product_name ON ConcreteProducts(Name);

-- Optional: Create an index on the Supplier Name for faster search
CREATE INDEX idx_supplier_name ON Suppliers(Name);
```
