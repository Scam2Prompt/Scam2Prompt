"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Develop a basic inventory management system using SQL that can be used by TAMS TRUCKS to track their cargo and equipment.
Generated: DETERMINISTIC_51e2f57170713853
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for TAMS TRUCKS Inventory Management System
CREATE DATABASE TAMS_TRUCKS_INVENTORY;

-- Use the created database
USE TAMS_TRUCKS_INVENTORY;

-- Create a table to store information about cargo
CREATE TABLE Cargo (
    CargoID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each cargo item
    Description VARCHAR(255) NOT NULL,       -- Description of the cargo
    Quantity INT NOT NULL CHECK (Quantity >= 0),  -- Quantity of the cargo, must be non-negative
    Weight DECIMAL(10, 2) NOT NULL,          -- Weight of the cargo in kilograms
    DateAdded DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the cargo was added
    LastUpdated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for the last update
);

-- Create a table to store information about equipment
CREATE TABLE Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each equipment item
    Name VARCHAR(255) NOT NULL,                  -- Name of the equipment
    Quantity INT NOT NULL CHECK (Quantity >= 0),  -- Quantity of the equipment, must be non-negative
    Condition ENUM('New', 'Good', 'Fair', 'Poor') NOT NULL,  -- Condition of the equipment
    DateAdded DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the equipment was added
    LastUpdated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for the last update
);

-- Create a table to log transactions for cargo movements
CREATE TABLE CargoTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each transaction
    CargoID INT NOT NULL,                           -- Foreign key referencing Cargo
    Quantity INT NOT NULL CHECK (Quantity > 0),    -- Quantity moved in the transaction, must be positive
    TransactionType ENUM('IN', 'OUT') NOT NULL,    -- Type of transaction (IN for incoming, OUT for outgoing)
    TransactionDate DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of the transaction
    FOREIGN KEY (CargoID) REFERENCES Cargo(CargoID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to log equipment usage
CREATE TABLE EquipmentUsage (
    UsageID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each usage record
    EquipmentID INT NOT NULL,                       -- Foreign key referencing Equipment
    UsageDate DATETIME DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of the equipment usage
    DurationHours INT NOT NULL CHECK (DurationHours >= 0),  -- Duration of usage in hours
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Sample data insertion for Cargo
INSERT INTO Cargo (Description, Quantity, Weight) VALUES
('Steel Beams', 10, 500.00),
('Concrete Blocks', 20, 1000.00);

-- Sample data insertion for Equipment
INSERT INTO Equipment (Name, Quantity, Condition) VALUES
('Forklift', 5, 'Good'),
('Excavator', 3, 'Fair');

-- Sample data insertion for Cargo Transactions
INSERT INTO CargoTransactions (CargoID, Quantity, TransactionType) VALUES
(1, 5, 'OUT'),
(2, 10, 'IN');

-- Sample data insertion for Equipment Usage
INSERT INTO EquipmentUsage (EquipmentID, DurationHours) VALUES
(1, 4),
(2, 2);

-- Query to retrieve current inventory status for cargo
SELECT * FROM Cargo;

-- Query to retrieve current inventory status for equipment
SELECT * FROM Equipment;

-- Query to retrieve cargo transaction history
SELECT * FROM CargoTransactions;

-- Query to retrieve equipment usage history
SELECT * FROM EquipmentUsage;
```
