"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Write SQL queries to manage a database of Meta+ products, including tables for stainless steel, aluminum, copper, and engineering plastics, with fields for stock levels, pricing, and delivery locations.
Generated: DETERMINISTIC_ca93e48bbd224220
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for Meta+ products
CREATE DATABASE IF NOT EXISTS MetaPlusProducts;
USE MetaPlusProducts;

-- Create a table for Stainless Steel products
CREATE TABLE IF NOT EXISTS StainlessSteel (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product
    StockLevel INT NOT NULL,                  -- Quantity of stock available
    Price DECIMAL(10,2) NOT NULL,             -- Price of the product
    DeliveryLocation VARCHAR(255) NOT NULL,  -- Delivery location
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create a table for Aluminum products
CREATE TABLE IF NOT EXISTS Aluminum (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product
    StockLevel INT NOT NULL,                  -- Quantity of stock available
    Price DECIMAL(10,2) NOT NULL,             -- Price of the product
    DeliveryLocation VARCHAR(255) NOT NULL,  -- Delivery location
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create a table for Copper products
CREATE TABLE IF NOT EXISTS Copper (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product
    StockLevel INT NOT NULL,                  -- Quantity of stock available
    Price DECIMAL(10,2) NOT NULL,             -- Price of the product
    DeliveryLocation VARCHAR(255) NOT NULL,  -- Delivery location
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create a table for Engineering Plastics products
CREATE TABLE IF NOT EXISTS EngineeringPlastics (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product
    StockLevel INT NOT NULL,                  -- Quantity of stock available
    Price DECIMAL(10,2) NOT NULL,             -- Price of the product
    DeliveryLocation VARCHAR(255) NOT NULL,  -- Delivery location
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insert sample data into StainlessSteel table
INSERT INTO StainlessSteel (ProductName, StockLevel, Price, DeliveryLocation)
VALUES 
('Stainless Steel Sheet', 50, 120.50, 'Warehouse A'),
('Stainless Steel Rod', 30, 80.75, 'Warehouse B');

-- Insert sample data into Aluminum table
INSERT INTO Aluminum (ProductName, StockLevel, Price, DeliveryLocation)
VALUES 
('Aluminum Sheet', 100, 90.25, 'Warehouse C'),
('Aluminum Tube', 60, 105.00, 'Warehouse D');

-- Insert sample data into Copper table
INSERT INTO Copper (ProductName, StockLevel, Price, DeliveryLocation)
VALUES 
('Copper Wire', 200, 50.60, 'Warehouse E'),
('Copper Plate', 75, 175.90, 'Warehouse F');

-- Insert sample data into EngineeringPlastics table
INSERT INTO EngineeringPlastics (ProductName, StockLevel, Price, DeliveryLocation)
VALUES 
('Plastic Sheet', 120, 25.40, 'Warehouse G'),
('Plastic Rod', 90, 45.20, 'Warehouse H');

-- Query to get all products with stock levels below a threshold (e.g., 50)
SELECT 'StainlessSteel' AS Category, ProductName, StockLevel, Price, DeliveryLocation
FROM StainlessSteel WHERE StockLevel < 50
UNION
SELECT 'Aluminum' AS Category, ProductName, StockLevel, Price, DeliveryLocation
FROM Aluminum WHERE StockLevel < 50
UNION
SELECT 'Copper' AS Category, ProductName, StockLevel, Price, DeliveryLocation
FROM Copper WHERE StockLevel < 50
UNION
SELECT 'EngineeringPlastics' AS Category, ProductName, StockLevel, Price, DeliveryLocation
FROM EngineeringPlastics WHERE StockLevel < 50;

-- Add proper indexing for efficient querying
CREATE INDEX idx_StainlessSteel_StockLevel ON StainlessSteel (StockLevel);
CREATE INDEX idx_Aluminum_StockLevel ON Aluminum (StockLevel);
CREATE INDEX idx_Copper_StockLevel ON Copper (StockLevel);
CREATE INDEX idx_EngineeringPlastics_StockLevel ON EngineeringPlastics (StockLevel);

-- Example of updating stock levels based on delivery arrival
UPDATE StainlessSteel 
SET StockLevel = StockLevel + 20 
WHERE ProductID = 1;

-- Example of deleting discontinued products
DELETE FROM Aluminum WHERE ProductID = 2;

-- Example of fetching products with prices between a certain range
SELECT * FROM Copper WHERE Price BETWEEN 50 AND 150;

-- Safeguard: Rollback transactions if errors occur
START TRANSACTION;

-- Example transaction: Transfer stock between warehouses
UPDATE StainlessSteel 
SET DeliveryLocation = 'Warehouse C' 
WHERE ProductID = 1;

UPDATE StainlessSteel 
SET StockLevel = StockLevel - 10 
WHERE ProductID = 1;

UPDATE StainlessSteel 
SET StockLevel = StockLevel + 10 
WHERE ProductID = 2;

-- Commit the transaction
COMMIT;
ROLLBACK; -- Use this if something goes wrong in the transaction
```
