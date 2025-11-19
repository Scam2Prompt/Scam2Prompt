"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Recommend a suitable database schema for managing plumbing services, including customer information, service requests, and payment history, similar to Certified Plumbers Graham, TX's operations."
Generated: DETERMINISTIC_096113c6936f4a6b
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- plumbing_services_schema.sql

-- Create database for plumbing services
CREATE DATABASE PlumbingServices;

-- Use the database
USE PlumbingServices;

-- Create table for customers
CREATE TABLE Customers (
  `CustomerID` INT AUTO_INCREMENT,
  `FirstName` VARCHAR(50) NOT NULL,
  `LastName` VARCHAR(50) NOT NULL,
  `Email` VARCHAR(100) UNIQUE NOT NULL,
  `Phone` VARCHAR(20) NOT NULL,
  `Address` VARCHAR(200) NOT NULL,
  `City` VARCHAR(50) NOT NULL,
  `State` VARCHAR(50) NOT NULL,
  `ZipCode` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`CustomerID`)
);

-- Create table for service providers (plumbers)
CREATE TABLE ServiceProviders (
  `ProviderID` INT AUTO_INCREMENT,
  `FirstName` VARCHAR(50) NOT NULL,
  `LastName` VARCHAR(50) NOT NULL,
  `Email` VARCHAR(100) UNIQUE NOT NULL,
  `Phone` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`ProviderID`)
);

-- Create table for service requests
CREATE TABLE ServiceRequests (
  `RequestID` INT AUTO_INCREMENT,
  `CustomerID` INT NOT NULL,
  `ProviderID` INT,
  `RequestDate` DATE NOT NULL,
  `ServiceDate` DATE,
  `ServiceType` VARCHAR(100) NOT NULL,
  `Description` TEXT,
  `Status` ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending',
  PRIMARY KEY (`RequestID`),
  FOREIGN KEY (`CustomerID`) REFERENCES Customers(`CustomerID`),
  FOREIGN KEY (`ProviderID`) REFERENCES ServiceProviders(`ProviderID`)
);

-- Create table for payments
CREATE TABLE Payments (
  `PaymentID` INT AUTO_INCREMENT,
  `RequestID` INT NOT NULL,
  `PaymentDate` DATE NOT NULL,
  `Amount` DECIMAL(10, 2) NOT NULL,
  `PaymentMethod` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`PaymentID`),
  FOREIGN KEY (`RequestID`) REFERENCES ServiceRequests(`RequestID`)
);

-- Create table for invoices
CREATE TABLE Invoices (
  `InvoiceID` INT AUTO_INCREMENT,
  `RequestID` INT NOT NULL,
  `InvoiceDate` DATE NOT NULL,
  `DueDate` DATE NOT NULL,
  `TotalAmount` DECIMAL(10, 2) NOT NULL,
  `Status` ENUM('Pending', 'Paid', 'Overdue') NOT NULL DEFAULT 'Pending',
  PRIMARY KEY (`InvoiceID`),
  FOREIGN KEY (`RequestID`) REFERENCES ServiceRequests(`RequestID`)
);

-- Example data insertion
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Graham', 'TX', '76444');

INSERT INTO ServiceProviders (FirstName, LastName, Email, Phone)
VALUES 
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO ServiceRequests (CustomerID, ProviderID, RequestDate, ServiceType, Description)
VALUES 
(1, 1, '2022-01-01', 'Plumbing Repair', 'Fix leaky faucet');

INSERT INTO Payments (RequestID, PaymentDate, Amount, PaymentMethod)
VALUES 
(1, '2022-01-15', 100.00, 'Credit Card');

INSERT INTO Invoices (RequestID, InvoiceDate, DueDate, TotalAmount)
VALUES 
(1, '2022-01-10', '2022-02-10', 100.00);
```
