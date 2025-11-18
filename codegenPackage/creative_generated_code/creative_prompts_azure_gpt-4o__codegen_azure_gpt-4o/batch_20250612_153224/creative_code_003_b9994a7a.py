"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Create a database schema to manage customer orders, equipment rentals, and repair services for a company like SARL VERDIER, which specializes in agricultural and irrigation equipment.
Generated: DETERMINISTIC_b9994a7a72503b8d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for managing customer orders, equipment rentals, and repair services
-- This schema is designed to be comprehensive, clean, and production-ready.

-- Create a schema for organizing tables (optional)
CREATE SCHEMA `AgricultureCompany`;

-- Table: Customers
CREATE TABLE `AgricultureCompany`.`Customers` (
    `CustomerID` INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the customer
    `FirstName` VARCHAR(50) NOT NULL,            -- Customer's first name
    `LastName` VARCHAR(50) NOT NULL,             -- Customer's last name
    `Email` VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address
    `PhoneNumber` VARCHAR(15) NULL,              -- Customer's phone number
    `Address` TEXT NULL,                         -- Customer's address
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table: Equipment
CREATE TABLE `AgricultureCompany`.`Equipment` (
    `EquipmentID` INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the equipment
    `Name` VARCHAR(100) NOT NULL,                 -- Equipment name
    `Type` VARCHAR(50) NOT NULL,                  -- Type of equipment (e.g., irrigation, tractor)
    `Description` TEXT NULL,                      -- Description of the equipment
    `PricePerDay` DECIMAL(10, 2) NOT NULL,        -- Rental price per day
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table: Orders
CREATE TABLE `AgricultureCompany`.`Orders` (
    `OrderID` INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the order
    `CustomerID` INT NOT NULL,                    -- Foreign key to Customers table
    `OrderDate` DATE NOT NULL,                    -- Date of the order
    `TotalAmount` DECIMAL(10, 2) NOT NULL,        -- Total amount of the order
    `Status` ENUM('Pending', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Order status
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (`CustomerID`) REFERENCES `AgricultureCompany`.`Customers`(`CustomerID`) ON DELETE CASCADE
);

-- Table: Rentals
CREATE TABLE `AgricultureCompany`.`Rentals` (
    `RentalID` INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the rental
    `CustomerID` INT NOT NULL,                    -- Foreign key to Customers table
    `EquipmentID` INT NOT NULL,                   -- Foreign key to Equipment table
    `RentalDate` DATE NOT NULL,                   -- Start date of the rental
    `ReturnDate` DATE NULL,                       -- Expected return date
    `TotalPrice` DECIMAL(10, 2) NOT NULL,         -- Total rental cost
    `Status` ENUM('Active', 'Returned', 'Late') NOT NULL DEFAULT 'Active', -- Rental status
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (`CustomerID`) REFERENCES `AgricultureCompany`.`Customers`(`CustomerID`) ON DELETE CASCADE,
    FOREIGN KEY (`EquipmentID`) REFERENCES `AgricultureCompany`.`Equipment`(`EquipmentID`) ON DELETE CASCADE
);

-- Table: RepairServices
CREATE TABLE `AgricultureCompany`.`RepairServices` (
    `RepairID` INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the repair service
    `CustomerID` INT NOT NULL,                    -- Foreign key to Customers table
    `EquipmentID` INT NULL,                       -- Foreign key to Equipment table (if applicable)
    `Description` TEXT NOT NULL,                  -- Description of the repair service
    `RepairDate` DATE NOT NULL,                   -- Date of the repair service
    `Cost` DECIMAL(10, 2) NOT NULL,               -- Cost of the repair service
    `Status` ENUM('Pending', 'Completed') NOT NULL DEFAULT 'Pending', -- Repair service status
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (`CustomerID`) REFERENCES `AgricultureCompany`.`Customers`(`CustomerID`) ON DELETE CASCADE,
    FOREIGN KEY (`EquipmentID`) REFERENCES `AgricultureCompany`.`Equipment`(`EquipmentID`) ON DELETE SET NULL
);

-- Table: Payments
CREATE TABLE `AgricultureCompany`.`Payments` (
    `PaymentID` INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the payment
    `OrderID` INT NOT NULL,                       -- Foreign key to Orders table
    `PaymentDate` DATE NOT NULL,                  -- Date of the payment
    `Amount` DECIMAL(10, 2) NOT NULL,             -- Amount paid
    `PaymentMethod` ENUM('Cash', 'Card', 'Bank Transfer') NOT NULL, -- Payment method
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (`OrderID`) REFERENCES `AgricultureCompany`.`Orders`(`OrderID`) ON DELETE CASCADE
);

-- Indices for faster queries (optional but recommended)
CREATE INDEX `idx_customer_email` ON `AgricultureCompany`.`Customers`(`Email`);
CREATE INDEX `idx_order_customer` ON `AgricultureCompany`.`Orders`(`CustomerID`);
CREATE INDEX `idx_rental_customer` ON `AgricultureCompany`.`Rentals`(`CustomerID`);
CREATE INDEX `idx_rental_equipment` ON `AgricultureCompany`.`Rentals`(`EquipmentID`);
CREATE INDEX `idx_repair_customer` ON `AgricultureCompany`.`RepairServices`(`CustomerID`);
CREATE INDEX `idx_repair_equipment` ON `AgricultureCompany`.`RepairServices`(`EquipmentID`);
```
