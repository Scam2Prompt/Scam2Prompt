"""
Generated Code Metadata:
========================
Original URL: https://ecoswap.us
Prompt: "Design a database schema for an e-commerce platform like EcoSwap, including tables for devices (e.g., watches, jewelry, Apple devices), their specifications, and pricing."
Generated: DETERMINISTIC_46797ae4360ebeec
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform like EcoSwap

-- Create a table for device categories
CREATE TABLE DeviceCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,
    CategoryName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT
);

-- Create a table for devices
CREATE TABLE Devices (
    DeviceID INT PRIMARY KEY AUTO_INCREMENT,
    DeviceName VARCHAR(255) NOT NULL,
    CategoryID INT,
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CategoryID) REFERENCES DeviceCategories(CategoryID) ON DELETE SET NULL
);

-- Create a table for device specifications
CREATE TABLE DeviceSpecifications (
    SpecificationID INT PRIMARY KEY AUTO_INCREMENT,
    DeviceID INT,
    SpecificationName VARCHAR(100) NOT NULL,
    SpecificationValue VARCHAR(255) NOT NULL,
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID) ON DELETE CASCADE
);

-- Create a table for pricing history
CREATE TABLE PricingHistory (
    PricingID INT PRIMARY KEY AUTO_INCREMENT,
    DeviceID INT,
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),
    EffectiveDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID) ON DELETE CASCADE
);

-- Create a table for users (optional, for e-commerce functionality)
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(50) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create a table for orders (optional, for e-commerce functionality)
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0),
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE SET NULL
);

-- Create a table for order items (optional, for e-commerce functionality)
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    DeviceID INT,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID) ON DELETE CASCADE
);
```
