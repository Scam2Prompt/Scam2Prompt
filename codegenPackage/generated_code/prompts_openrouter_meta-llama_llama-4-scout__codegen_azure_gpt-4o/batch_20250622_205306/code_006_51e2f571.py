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
-- Create a database for TAMS TRUCKS inventory management
CREATE DATABASE TAMS_TRUCKS_INVENTORY;

-- Use the newly created database
USE TAMS_TRUCKS_INVENTORY;

-- Create a table to store cargo information
CREATE TABLE Cargo (
    CargoID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each cargo item
    Name VARCHAR(255) NOT NULL,             -- Name of the cargo item
    Description TEXT,                       -- Description of the cargo item
    Quantity INT NOT NULL,                  -- Quantity of the cargo item
    Weight DECIMAL(10, 2),                  -- Weight of the cargo item in kilograms
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store equipment information
CREATE TABLE Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each equipment item
    Name VARCHAR(255) NOT NULL,                 -- Name of the equipment item
    Description TEXT,                           -- Description of the equipment item
    Quantity INT NOT NULL,                      -- Quantity of the equipment item
    Condition ENUM('New', 'Good', 'Fair', 'Poor') NOT NULL, -- Condition of the equipment
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to track transactions (e.g., additions, removals, updates)
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    ItemType ENUM('Cargo', 'Equipment') NOT NULL, -- Type of item involved in the transaction
    ItemID INT NOT NULL,                          -- ID of the item involved in the transaction
    Action ENUM('Add', 'Remove', 'Update') NOT NULL, -- Action performed on the item
    QuantityChange INT NOT NULL,                  -- Change in quantity (positive for addition, negative for removal)
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of the transaction
);

-- Insert sample data into Cargo table
INSERT INTO Cargo (Name, Description, Quantity, Weight)
VALUES 
('Steel Beams', 'Heavy-duty steel beams for construction', 50, 5000.00),
('Wooden Pallets', 'Standard wooden pallets for shipping', 200, 1500.00);

-- Insert sample data into Equipment table
INSERT INTO Equipment (Name, Description, Quantity, Condition)
VALUES 
('Forklift', 'Industrial forklift for lifting heavy cargo', 5, 'Good'),
('Hand Truck', 'Lightweight hand truck for small cargo', 20, 'New');

-- Query to retrieve all cargo items
SELECT * FROM Cargo;

-- Query to retrieve all equipment items
SELECT * FROM Equipment;

-- Query to log a transaction (example: adding 10 steel beams)
INSERT INTO Transactions (ItemType, ItemID, Action, QuantityChange)
VALUES ('Cargo', 1, 'Add', 10);

-- Query to update the quantity of an item in the Cargo table (example: adding 10 steel beams)
UPDATE Cargo
SET Quantity = Quantity + 10
WHERE CargoID = 1;

-- Query to retrieve all transactions
SELECT * FROM Transactions;

-- Error handling: Ensure foreign key constraints for Transactions table
ALTER TABLE Transactions
ADD CONSTRAINT FK_ItemID_Cargo FOREIGN KEY (ItemID) REFERENCES Cargo(CargoID)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Transactions
ADD CONSTRAINT FK_ItemID_Equipment FOREIGN KEY (ItemID) REFERENCES Equipment(EquipmentID)
ON DELETE CASCADE ON UPDATE CASCADE;

-- Ensure proper indexing for faster queries
CREATE INDEX idx_cargo_name ON Cargo(Name);
CREATE INDEX idx_equipment_name ON Equipment(Name);
CREATE INDEX idx_transactions_itemtype ON Transactions(ItemType);
```
