"""
Generated Code Metadata:
========================
Original URL: https://arrendamosjv.com
Prompt: Design a database schema to store information about properties, clients, and rental contracts for a real estate company like Arrendamos J V SAS, using a relational database management system like MySQL.
Generated: DETERMINISTIC_6a4e0a979adc9345
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for real estate company
CREATE DATABASE ArrendamosJV;

-- Use database
USE ArrendamosJV;

-- Create table for clients
CREATE TABLE Clients (
  ClientID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  Phone VARCHAR(20),
  Address VARCHAR(255),
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ClientID)
);

-- Create table for properties
CREATE TABLE Properties (
  PropertyID INT AUTO_INCREMENT,
  Address VARCHAR(255) NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  Country VARCHAR(100) NOT NULL,
  PostalCode VARCHAR(20) NOT NULL,
  Type ENUM('Residential', 'Commercial') NOT NULL,
  Rent DECIMAL(10, 2) NOT NULL,
  UtilitiesIncluded BOOLEAN DEFAULT FALSE,
  ParkingAvailable BOOLEAN DEFAULT FALSE,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (PropertyID)
);

-- Create table for rental contracts
CREATE TABLE RentalContracts (
  ContractID INT AUTO_INCREMENT,
  ClientID INT NOT NULL,
  PropertyID INT NOT NULL,
  LeaseStartDate DATE NOT NULL,
  LeaseEndDate DATE NOT NULL,
  Rent DECIMAL(10, 2) NOT NULL,
  SecurityDeposit DECIMAL(10, 2) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ContractID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
  FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE Payments (
  PaymentID INT AUTO_INCREMENT,
  ContractID INT NOT NULL,
  PaymentDate DATE NOT NULL,
  Amount DECIMAL(10, 2) NOT NULL,
  PaymentMethod ENUM('Cash', 'Bank Transfer', 'Credit Card') NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (PaymentID),
  FOREIGN KEY (ContractID) REFERENCES RentalContracts(ContractID) ON DELETE CASCADE
);

-- Create table for property amenities
CREATE TABLE PropertyAmenities (
  AmenityID INT AUTO_INCREMENT,
  PropertyID INT NOT NULL,
  Amenity ENUM('Pool', 'Gym', 'Parking', 'WiFi', 'Furnished') NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (AmenityID),
  FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_ClientID ON RentalContracts (ClientID);
CREATE INDEX idx_PropertyID ON RentalContracts (PropertyID);
CREATE INDEX idx_ContractID ON Payments (ContractID);
CREATE INDEX idx_PropertyID ON PropertyAmenities (PropertyID);
```
