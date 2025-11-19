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
-- SQL Schema for storing product information related to aluminum windows, thermopanel PVC, and security blinds.

-- Create a database named 'ProductCatalog'
CREATE DATABASE ProductCatalog;

-- Use the newly created database
USE ProductCatalog;

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,        -- Name of the product category (e.g., Aluminum Windows, Thermopanel PVC, Security Blinds)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the category was created
);

-- Table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategories
    ProductName VARCHAR(150) NOT NULL,         -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    InstallationDetails TEXT,                  -- Information about installation requirements/details
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Enforce relationship with ProductCategories
);

-- Table to store installation details for products
CREATE TABLE InstallationDetails (
    InstallationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for installation details
    ProductID INT NOT NULL,                        -- Foreign key linking to Products
    InstallationCost DECIMAL(10, 2) NOT NULL,      -- Cost of installation
    EstimatedTime VARCHAR(50),                     -- Estimated time for installation (e.g., "2 hours")
    Notes TEXT,                                    -- Additional notes about installation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the installation details were created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Enforce relationship with Products
);

-- Insert sample categories
INSERT INTO ProductCategories (CategoryName) VALUES 
('Aluminum Windows'),
('Thermopanel PVC'),
('Security Blinds');

-- Example of inserting sample products
INSERT INTO Products (CategoryID, ProductName, Description, Price, InstallationDetails) VALUES 
(1, 'Sliding Aluminum Window', 'Durable sliding aluminum window with tempered glass.', 250.00, 'Requires professional installation.'),
(2, 'Thermopanel PVC Door', 'Energy-efficient PVC door with thermopanel technology.', 300.00, 'Installation includes sealing and alignment.'),
(3, 'Security Blind Model X', 'High-security blind with reinforced materials.', 150.00, 'Installation requires drilling and mounting.');

-- Example of inserting installation details
INSERT INTO InstallationDetails (ProductID, InstallationCost, EstimatedTime, Notes) VALUES 
(1, 50.00, '3 hours', 'Ensure proper alignment during installation.'),
(2, 75.00, '4 hours', 'Includes sealing and weatherproofing.'),
(3, 40.00, '2 hours', 'Requires specialized tools for mounting.');

-- Query to verify the schema and data
SELECT * FROM ProductCategories;
SELECT * FROM Products;
SELECT * FROM InstallationDetails;
```
