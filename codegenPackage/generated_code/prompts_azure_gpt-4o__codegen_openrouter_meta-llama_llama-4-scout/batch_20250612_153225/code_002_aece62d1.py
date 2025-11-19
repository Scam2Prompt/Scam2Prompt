"""
Generated Code Metadata:
========================
Original URL: https://rentalcarelena.it
Prompt: Generate code to create a database schema for a car rental service that includes tables for vehicle details (e.g., type, fuel, capacity), customer information, and booking records.
Generated: DETERMINISTIC_aece62d1910a8f4c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for car rental service
CREATE DATABASE CarRentalService;

-- Use the CarRentalService database
USE CarRentalService;

-- Create table for vehicle types
CREATE TABLE VehicleTypes (
    VehicleTypeID INT AUTO_INCREMENT,
    VehicleTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VehicleTypeID)
);

-- Create table for fuel types
CREATE TABLE FuelTypes (
    FuelTypeID INT AUTO_INCREMENT,
    FuelTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (FuelTypeID)
);

-- Create table for vehicles
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT,
    VehicleTypeID INT NOT NULL,
    FuelTypeID INT NOT NULL,
    LicensePlate VARCHAR(20) NOT NULL,
    Capacity INT NOT NULL,
    RentalRate DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VehicleID),
    FOREIGN KEY (VehicleTypeID) REFERENCES VehicleTypes(VehicleTypeID),
    FOREIGN KEY (FuelTypeID) REFERENCES FuelTypes(FuelTypeID)
);

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT,
    VehicleID INT NOT NULL,
    CustomerID INT NOT NULL,
    BookingDate DATE NOT NULL,
    ReturnDate DATE,
    RentalStatus ENUM('pending', 'rented', 'returned', 'cancelled') DEFAULT 'pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    BookingID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod ENUM('cash', 'credit', 'debit') NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
);

-- Insert sample data into VehicleTypes table
INSERT INTO VehicleTypes (VehicleTypeName, Description)
VALUES 
('Sedan', 'A standard 4-door sedan'),
('SUV', 'A sport utility vehicle'),
('Truck', 'A large vehicle for hauling goods');

-- Insert sample data into FuelTypes table
INSERT INTO FuelTypes (FuelTypeName, Description)
VALUES 
('Gasoline', 'A refined product derived from crude oil'),
('Diesel', 'A refined product derived from crude oil'),
('Electric', 'A battery-powered electric vehicle');

-- Insert sample data into Vehicles table
INSERT INTO Vehicles (VehicleTypeID, FuelTypeID, LicensePlate, Capacity, RentalRate)
VALUES 
(1, 1, 'ABC123', 5, 40.00),
(2, 2, 'XYZ789', 7, 60.00),
(3, 3, 'DEF456', 3, 30.00);

-- Insert sample data into Customers table
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into Bookings table
INSERT INTO Bookings (VehicleID, CustomerID, BookingDate, ReturnDate)
VALUES 
(1, 1, '2024-09-01', '2024-09-08'),
(2, 2, '2024-09-15', '2024-09-22');

-- Insert sample data into Payments table
INSERT INTO Payments (BookingID, PaymentDate, Amount, PaymentMethod)
VALUES 
(1, '2024-09-01', 200.00, 'credit'),
(2, '2024-09-15', 300.00, 'debit');
```
