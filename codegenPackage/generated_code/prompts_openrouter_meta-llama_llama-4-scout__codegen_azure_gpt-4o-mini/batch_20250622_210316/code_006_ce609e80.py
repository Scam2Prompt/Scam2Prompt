"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Design a database schema for storing information about Suzuki motorcycles, heavy bikes, and cars sold by Suzuki Capital Motors.
Generated: DETERMINISTIC_ce609e80a3430627
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Suzuki Capital Motors

-- Create a database for Suzuki Capital Motors
CREATE DATABASE SuzukiCapitalMotors;

-- Use the created database
USE SuzukiCapitalMotors;

-- Table to store information about motorcycles
CREATE TABLE Motorcycles (
    MotorcycleID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each motorcycle
    Model VARCHAR(100) NOT NULL,                   -- Model name of the motorcycle
    Year INT NOT NULL,                             -- Year of manufacture
    EngineCapacity DECIMAL(5,2) NOT NULL,         -- Engine capacity in liters
    Color VARCHAR(50),                             -- Color of the motorcycle
    Price DECIMAL(10,2) NOT NULL,                  -- Price of the motorcycle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about heavy bikes
CREATE TABLE HeavyBikes (
    HeavyBikeID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each heavy bike
    Model VARCHAR(100) NOT NULL,                   -- Model name of the heavy bike
    Year INT NOT NULL,                             -- Year of manufacture
    EngineCapacity DECIMAL(5,2) NOT NULL,         -- Engine capacity in liters
    Color VARCHAR(50),                             -- Color of the heavy bike
    Price DECIMAL(10,2) NOT NULL,                  -- Price of the heavy bike
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about cars
CREATE TABLE Cars (
    CarID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each car
    Model VARCHAR(100) NOT NULL,                   -- Model name of the car
    Year INT NOT NULL,                             -- Year of manufacture
    EngineCapacity DECIMAL(5,2) NOT NULL,         -- Engine capacity in liters
    Color VARCHAR(50),                             -- Color of the car
    Price DECIMAL(10,2) NOT NULL,                  -- Price of the car
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about sales transactions
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each sale
    VehicleType ENUM('Motorcycle', 'HeavyBike', 'Car') NOT NULL, -- Type of vehicle sold
    VehicleID INT NOT NULL,                        -- ID of the sold vehicle
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of the sale
    SalePrice DECIMAL(10,2) NOT NULL,              -- Sale price of the vehicle
    CustomerName VARCHAR(100) NOT NULL,            -- Name of the customer
    CustomerContact VARCHAR(50),                    -- Contact information of the customer
    FOREIGN KEY (VehicleID) REFERENCES (
        SELECT MotorcycleID FROM Motorcycles UNION
        SELECT HeavyBikeID FROM HeavyBikes UNION
        SELECT CarID FROM Cars
    ) ON DELETE CASCADE -- Ensures that if a vehicle is deleted, the sale record is also deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_motorcycle_model ON Motorcycles(Model);
CREATE INDEX idx_heavybike_model ON HeavyBikes(Model);
CREATE INDEX idx_car_model ON Cars(Model);
CREATE INDEX idx_sales_vehicle ON Sales(VehicleID);
```
