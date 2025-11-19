"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Design a database schema for storing customer orders, service types (e.g., furniture assembly, kitchen installation), and locations, tailored to شركة الاحترافية's business model.
Generated: DETERMINISTIC_0b85351fa4fede60
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE company_db;

-- Use database
USE company_db;

-- Create table for locations
CREATE TABLE Locations (
  `LocationID` INT AUTO_INCREMENT,
  `Address` VARCHAR(255) NOT NULL,
  `City` VARCHAR(100) NOT NULL,
  `State` VARCHAR(100) NOT NULL,
  `Country` VARCHAR(100) NOT NULL,
  `PostalCode` VARCHAR(20) NOT NULL,
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`LocationID`)
);

-- Create table for service types
CREATE TABLE ServiceTypes (
  `ServiceTypeID` INT AUTO_INCREMENT,
  `ServiceName` VARCHAR(100) NOT NULL,
  `Description` TEXT,
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ServiceTypeID`)
);

-- Create table for customers
CREATE TABLE Customers (
  `CustomerID` INT AUTO_INCREMENT,
  `FirstName` VARCHAR(100) NOT NULL,
  `LastName` VARCHAR(100) NOT NULL,
  `Email` VARCHAR(255) UNIQUE NOT NULL,
  `Phone` VARCHAR(20) NOT NULL,
  `Address` VARCHAR(255),
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`CustomerID`)
);

-- Create table for orders
CREATE TABLE Orders (
  `OrderID` INT AUTO_INCREMENT,
  `CustomerID` INT NOT NULL,
  `LocationID` INT NOT NULL,
  `ServiceTypeID` INT NOT NULL,
  `OrderDate` DATE NOT NULL,
  `ScheduledDate` DATE,
  `Status` ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`OrderID`),
  FOREIGN KEY (`CustomerID`) REFERENCES Customers(`CustomerID`),
  FOREIGN KEY (`LocationID`) REFERENCES Locations(`LocationID`),
  FOREIGN KEY (`ServiceTypeID`) REFERENCES ServiceTypes(`ServiceTypeID`)
);

-- Create table for order services (many-to-many relationship)
CREATE TABLE OrderServices (
  `OrderID` INT NOT NULL,
  `ServiceTypeID` INT NOT NULL,
  `Quantity` INT NOT NULL,
  PRIMARY KEY (`OrderID`, `ServiceTypeID`),
  FOREIGN KEY (`OrderID`) REFERENCES Orders(`OrderID`),
  FOREIGN KEY (`ServiceTypeID`) REFERENCES ServiceTypes(`ServiceTypeID`)
);

-- Create table for payments
CREATE TABLE Payments (
  `PaymentID` INT AUTO_INCREMENT,
  `OrderID` INT NOT NULL,
  `PaymentMethod` VARCHAR(100) NOT NULL,
  `PaymentDate` DATE NOT NULL,
  `Amount` DECIMAL(10, 2) NOT NULL,
  `Status` ENUM('pending', 'paid', 'failed') NOT NULL,
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`PaymentID`),
  FOREIGN KEY (`OrderID`) REFERENCES Orders(`OrderID`)
);
```
