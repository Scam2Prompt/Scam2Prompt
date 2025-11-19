"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Generate a SQL database schema to store information about different types of tires (e.g., Continental EcoContact5, Michelin Primacy 3) and wheels (e.g., OZ Ego Wheels, DOTZ Shift Wheels) offered by a company.
Generated: DETERMINISTIC_b672a53ad6b19c77
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Tire and Wheel Information

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Tires;
DROP TABLE IF EXISTS Wheels;

-- Table to store information about different types of tires
CREATE TABLE Tires (
    TireID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each tire
    Brand VARCHAR(50) NOT NULL,             -- Brand name of the tire
    Model VARCHAR(50) NOT NULL,             -- Model name of the tire
    Width INT NOT NULL,                      -- Width of the tire in mm
    AspectRatio INT NOT NULL,                -- Aspect ratio of the tire
    Diameter INT NOT NULL,                   -- Diameter of the tire in inches
    Type ENUM('Summer', 'Winter', 'All-Season') NOT NULL,  -- Type of tire
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the tire
    StockQuantity INT DEFAULT 0,            -- Quantity in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about different types of wheels
CREATE TABLE Wheels (
    WheelID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each wheel
    Brand VARCHAR(50) NOT NULL,              -- Brand name of the wheel
    Model VARCHAR(50) NOT NULL,              -- Model name of the wheel
    Diameter INT NOT NULL,                   -- Diameter of the wheel in inches
    Width INT NOT NULL,                      -- Width of the wheel in mm
    Material ENUM('Aluminum', 'Steel', 'Carbon Fiber') NOT NULL,  -- Material of the wheel
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the wheel
    StockQuantity INT DEFAULT 0,            -- Quantity in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Example of inserting data into the Tires table
INSERT INTO Tires (Brand, Model, Width, AspectRatio, Diameter, Type, Price, StockQuantity)
VALUES 
('Continental', 'EcoContact5', 205, 55, 16, 'Summer', 89.99, 100),
('Michelin', 'Primacy 3', 225, 45, 17, 'All-Season', 109.99, 50);

-- Example of inserting data into the Wheels table
INSERT INTO Wheels (Brand, Model, Diameter, Width, Material, Price, StockQuantity)
VALUES 
('OZ', 'Ego Wheels', 18, 8, 'Aluminum', 199.99, 30),
('DOTZ', 'Shift Wheels', 17, 7.5, 'Steel', 149.99, 20);
```
