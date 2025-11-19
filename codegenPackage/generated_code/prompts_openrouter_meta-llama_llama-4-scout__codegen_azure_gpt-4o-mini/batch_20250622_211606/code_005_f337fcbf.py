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
-- Database schema for managing supply chain data

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS QualityControlMetrics;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Manufacturers;

-- Table for storing product information
CREATE TABLE Products (
    ProductID SERIAL PRIMARY KEY,          -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,    -- Name of the product
    ManufacturerID INT NOT NULL,           -- Foreign key referencing Manufacturers
    SupplierID INT NOT NULL,               -- Foreign key referencing Suppliers
    Category VARCHAR(100),                  -- Category of the product
    Price DECIMAL(10, 2) NOT NULL,        -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE
);

-- Table for storing manufacturer information
CREATE TABLE Manufacturers (
    ManufacturerID SERIAL PRIMARY KEY,     -- Unique identifier for each manufacturer
    ManufacturerName VARCHAR(255) NOT NULL, -- Name of the manufacturer
    ContactInfo VARCHAR(255),               -- Contact information for the manufacturer
    Address VARCHAR(255),                    -- Address of the manufacturer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the manufacturer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for storing supplier information
CREATE TABLE Suppliers (
    SupplierID SERIAL PRIMARY KEY,          -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,     -- Name of the supplier
    ContactInfo VARCHAR(255),                -- Contact information for the supplier
    Address VARCHAR(255),                     -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for storing quality control metrics
CREATE TABLE QualityControlMetrics (
    MetricID SERIAL PRIMARY KEY,            -- Unique identifier for each quality control metric
    ProductID INT NOT NULL,                 -- Foreign key referencing Products
    InspectionDate DATE NOT NULL,           -- Date of the quality inspection
    QualityScore INT CHECK (QualityScore BETWEEN 0 AND 100), -- Quality score (0-100)
    Comments TEXT,                          -- Additional comments regarding the inspection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the metric was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_supplier_name ON Suppliers(SupplierName);
CREATE INDEX idx_manufacturer_name ON Manufacturers(ManufacturerName);
CREATE INDEX idx_product_quality ON QualityControlMetrics(ProductID);
```
