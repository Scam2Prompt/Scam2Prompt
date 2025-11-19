"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: "Design a simple database schema to store information about packaging products, including product types (e.g., arándanos, uva mesa), and their export destinations."
Generated: DETERMINISTIC_a107a49b6d6bf9f9
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for packaging products

-- Create a database for packaging products
CREATE DATABASE PackagingProductsDB;

-- Use the created database
USE PackagingProductsDB;

-- Table to store product types
CREATE TABLE ProductTypes (
    ProductTypeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product type
    Name VARCHAR(100) NOT NULL,                     -- Name of the product type (e.g., arándanos, uva mesa)
    Description TEXT,                                -- Description of the product type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product type was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store export destinations
CREATE TABLE ExportDestinations (
    DestinationID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each export destination
    Country VARCHAR(100) NOT NULL,                   -- Name of the country for the export destination
    City VARCHAR(100),                                -- City of the export destination
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the destination was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store packaging products
CREATE TABLE PackagingProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each packaging product
    ProductTypeID INT NOT NULL,                       -- Foreign key referencing ProductTypes
    DestinationID INT NOT NULL,                       -- Foreign key referencing ExportDestinations
    Quantity INT NOT NULL,                            -- Quantity of the product being packaged
    PackagingDate DATE NOT NULL,                      -- Date when the product was packaged
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (ProductTypeID) REFERENCES ProductTypes(ProductTypeID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (DestinationID) REFERENCES ExportDestinations(DestinationID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion (optional)
INSERT INTO ProductTypes (Name, Description) VALUES 
('arándanos', 'Blueberries, a popular fruit for export.'),
('uva mesa', 'Table grapes, commonly exported fresh.');

INSERT INTO ExportDestinations (Country, City) VALUES 
('USA', 'New York'),
('Canada', 'Toronto');

INSERT INTO PackagingProducts (ProductTypeID, DestinationID, Quantity, PackagingDate) VALUES 
(1, 1, 1000, '2023-10-01'),
(2, 2, 500, '2023-10-02');

-- End of SQL script
```
