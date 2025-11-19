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
-- Database Schema for Supply Chain Management

-- Table: Products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    ManufacturerID INT NOT NULL,              -- Foreign key referencing Manufacturers table
    SupplierID INT NOT NULL,                  -- Foreign key referencing Suppliers table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each manufacturer
    Name VARCHAR(255) NOT NULL,                    -- Name of the manufacturer
    ContactInfo TEXT,                              -- Contact information for the manufacturer
    Address TEXT,                                  -- Address of the manufacturer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the manufacturer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactInfo TEXT,                          -- Contact information for the supplier
    Address TEXT,                              -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: QualityControlMetrics
CREATE TABLE QualityControlMetrics (
    MetricID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each quality control metric
    ProductID INT NOT NULL,                   -- Foreign key referencing Products table
    InspectionDate DATE NOT NULL,             -- Date of the quality inspection
    MetricName VARCHAR(255) NOT NULL,         -- Name of the quality metric
    MetricValue DECIMAL(10, 2) NOT NULL,      -- Value of the quality metric
    Status ENUM('Pass', 'Fail') NOT NULL,     -- Status of the quality check
    Notes TEXT,                               -- Additional notes about the inspection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the metric was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    CONSTRAINT FK_ProductID FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Foreign Key Constraints
ALTER TABLE Products
ADD CONSTRAINT FK_ManufacturerID FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE CASCADE;

ALTER TABLE Products
ADD CONSTRAINT FK_SupplierID FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE;

-- Indexes for faster queries
CREATE INDEX IDX_Products_ManufacturerID ON Products (ManufacturerID);
CREATE INDEX IDX_Products_SupplierID ON Products (SupplierID);
CREATE INDEX IDX_QualityControlMetrics_ProductID ON QualityControlMetrics (ProductID);
```
