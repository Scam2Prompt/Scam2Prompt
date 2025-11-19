"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: "Design a database schema to store information about various air conditioning systems, including their specifications and prices, similar to those listed on frigoterm.ro."
Generated: DETERMINISTIC_76db6eff4a9e177a
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about air conditioning systems

CREATE DATABASE AirConditioningDB;

USE AirConditioningDB;

-- Table to store manufacturers of air conditioning systems
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Country VARCHAR(100),
    Website VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store categories of air conditioning systems (e.g., Split, Portable, Central)
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store air conditioning systems
CREATE TABLE AirConditioners (
    AirConditionerID INT AUTO_INCREMENT PRIMARY KEY,
    ManufacturerID INT NOT NULL,
    CategoryID INT NOT NULL,
    Model VARCHAR(100) NOT NULL,
    Specifications JSON NOT NULL, -- Store specifications in JSON format
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Ensure price is non-negative
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE CASCADE,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Table to store customer reviews for air conditioning systems
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    AirConditionerID INT NOT NULL,
    CustomerName VARCHAR(100) NOT NULL,
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating must be between 1 and 5
    Comment TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AirConditionerID) REFERENCES AirConditioners(AirConditionerID) ON DELETE CASCADE
);

-- Table to store warranty information for air conditioning systems
CREATE TABLE Warranties (
    WarrantyID INT AUTO_INCREMENT PRIMARY KEY,
    AirConditionerID INT NOT NULL,
    DurationMonths INT NOT NULL CHECK (DurationMonths > 0), -- Warranty duration must be positive
    Details TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AirConditionerID) REFERENCES AirConditioners(AirConditionerID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_manufacturer ON AirConditioners(ManufacturerID);
CREATE INDEX idx_category ON AirConditioners(CategoryID);
CREATE INDEX idx_air_conditioner ON Reviews(AirConditionerID);
```
