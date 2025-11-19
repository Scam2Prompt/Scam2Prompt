"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Design a simple database schema for storing information about stainless steel clean tube products, including material, specification, and application industry.
Generated: DETERMINISTIC_1265f0d39ed805ee
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for stainless steel clean tube products
CREATE DATABASE IF NOT EXISTS StainlessSteelProducts;

-- Use the created database
USE StainlessSteelProducts;

-- Table to store information about materials
CREATE TABLE IF NOT EXISTS Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL,         -- Name of the material
    Description TEXT,                            -- Description of the material
    UNIQUE (MaterialName)                        -- Ensure material names are unique
);

-- Table to store specifications of the products
CREATE TABLE IF NOT EXISTS Specifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each specification
    MaterialID INT NOT NULL,                         -- Foreign key referencing Materials
    SpecificationName VARCHAR(100) NOT NULL,        -- Name of the specification
    Value VARCHAR(100),                              -- Value of the specification
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE,  -- Ensure referential integrity
    UNIQUE (MaterialID, SpecificationName)          -- Ensure unique specifications per material
);

-- Table to store application industries
CREATE TABLE IF NOT EXISTS Industries (
    IndustryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each industry
    IndustryName VARCHAR(100) NOT NULL,         -- Name of the industry
    Description TEXT,                            -- Description of the industry
    UNIQUE (IndustryName)                        -- Ensure industry names are unique
);

-- Table to store products
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    MaterialID INT NOT NULL,                     -- Foreign key referencing Materials
    SpecificationID INT NOT NULL,                -- Foreign key referencing Specifications
    IndustryID INT NOT NULL,                     -- Foreign key referencing Industries
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,       -- Quantity in stock
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (SpecificationID) REFERENCES Specifications(SpecificationID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (IndustryID) REFERENCES Industries(IndustryID) ON DELETE CASCADE,  -- Ensure referential integrity
    UNIQUE (ProductName)                         -- Ensure product names are unique
);

-- Sample data insertion (for demonstration purposes)
INSERT INTO Materials (MaterialName, Description) VALUES
('304 Stainless Steel', 'A versatile stainless steel with good corrosion resistance.'),
('316 Stainless Steel', 'A higher corrosion resistance stainless steel, ideal for marine applications.');

INSERT INTO Specifications (MaterialID, SpecificationName, Value) VALUES
(1, 'Thickness', '1.5mm'),
(1, 'Diameter', '25mm'),
(2, 'Thickness', '2.0mm'),
(2, 'Diameter', '30mm');

INSERT INTO Industries (IndustryName, Description) VALUES
('Food Processing', 'Industry focused on the processing of food products.'),
('Pharmaceutical', 'Industry involved in the production of medications.');

INSERT INTO Products (MaterialID, SpecificationID, IndustryID, ProductName, Price, StockQuantity) VALUES
(1, 1, 1, '304 Clean Tube', 50.00, 100),
(2, 3, 2, '316 Clean Tube', 75.00, 50);
```
