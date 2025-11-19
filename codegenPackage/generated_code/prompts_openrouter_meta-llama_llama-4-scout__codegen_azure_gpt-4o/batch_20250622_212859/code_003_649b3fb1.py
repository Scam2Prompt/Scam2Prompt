"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: "Design a database schema for storing information about transmission line accessories, such as fittings and clamps, manufactured by Swamiji Transmission Pvt. Ltd., and write a SQL query to retrieve product details."
Generated: DETERMINISTIC_649b3fb1c8ebbf1e
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Transmission Line Accessories

-- Create a table to store information about manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the manufacturer
    Name VARCHAR(255) NOT NULL,                   -- Name of the manufacturer
    Address TEXT,                                 -- Address of the manufacturer
    ContactNumber VARCHAR(15),                   -- Contact number of the manufacturer
    Email VARCHAR(255),                          -- Email address of the manufacturer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Insert manufacturer details for Swamiji Transmission Pvt. Ltd.
INSERT INTO Manufacturers (Name, Address, ContactNumber, Email)
VALUES ('Swamiji Transmission Pvt. Ltd.', '123 Industrial Area, City, Country', '1234567890', 'info@swamijitransmission.com');

-- Create a table to store information about transmission line accessories
CREATE TABLE Accessories (
    AccessoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for the accessory
    ManufacturerID INT NOT NULL,                 -- Foreign key linking to the manufacturer
    Name VARCHAR(255) NOT NULL,                  -- Name of the accessory
    Type VARCHAR(255) NOT NULL,                  -- Type/category of the accessory (e.g., fitting, clamp)
    Material VARCHAR(255),                       -- Material used for the accessory
    Weight DECIMAL(10, 2),                       -- Weight of the accessory in kilograms
    Dimensions VARCHAR(255),                     -- Dimensions of the accessory
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the accessory
    Stock INT NOT NULL,                          -- Number of items in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) -- Foreign key constraint
);

-- Insert sample accessory details
INSERT INTO Accessories (ManufacturerID, Name, Type, Material, Weight, Dimensions, Price, Stock)
VALUES 
(1, 'Clamp A', 'Clamp', 'Aluminum', 1.5, '10x5x3 cm', 25.50, 100),
(1, 'Fitting B', 'Fitting', 'Steel', 2.0, '15x10x5 cm', 40.00, 50),
(1, 'Clamp C', 'Clamp', 'Copper', 1.8, '12x6x4 cm', 30.75, 75);

-- SQL Query to retrieve product details
-- This query retrieves all accessories manufactured by Swamiji Transmission Pvt. Ltd.
SELECT 
    a.AccessoryID,
    a.Name AS AccessoryName,
    a.Type AS AccessoryType,
    a.Material,
    a.Weight,
    a.Dimensions,
    a.Price,
    a.Stock,
    m.Name AS ManufacturerName,
    m.Address AS ManufacturerAddress,
    m.ContactNumber AS ManufacturerContact,
    m.Email AS ManufacturerEmail
FROM 
    Accessories a
JOIN 
    Manufacturers m
ON 
    a.ManufacturerID = m.ManufacturerID
WHERE 
    m.Name = 'Swamiji Transmission Pvt. Ltd.';
```
