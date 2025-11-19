"""
Generated Code Metadata:
========================
Original URL: https://panchsheelbank.com
Prompt: Create a database schema for managing safe deposit locker allocations, inspired by the services offered by Panchsheel Mercantile Co-op. Bank Ltd.
Generated: DETERMINISTIC_c426045e9e12ce4c
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for safe deposit locker allocations

-- Create database
CREATE DATABASE SafeDepositLockerDB;

-- Use database
USE SafeDepositLockerDB;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for locker sizes
CREATE TABLE LockerSizes (
    LockerSizeID INT AUTO_INCREMENT,
    Size VARCHAR(50) NOT NULL,
    Description VARCHAR(255),
    Rent DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (LockerSizeID)
);

-- Create table for safe deposit lockers
CREATE TABLE SafeDepositLockers (
    LockerID INT AUTO_INCREMENT,
    LockerSizeID INT NOT NULL,
    LockerNumber VARCHAR(50) NOT NULL,
    IsAllocated BOOLEAN DEFAULT FALSE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (LockerID),
    FOREIGN KEY (LockerSizeID) REFERENCES LockerSizes(LockerSizeID)
);

-- Create table for locker allocations
CREATE TABLE LockerAllocations (
    AllocationID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    LockerID INT NOT NULL,
    AllocationDate DATE NOT NULL,
    ExpirationDate DATE,
    RentPaid DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AllocationID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (LockerID) REFERENCES SafeDepositLockers(LockerID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    AllocationID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (AllocationID) REFERENCES LockerAllocations(AllocationID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_Customers_Email ON Customers (Email);
CREATE INDEX idx_LockerAllocations_CustomerID ON LockerAllocations (CustomerID);
CREATE INDEX idx_LockerAllocations_LockerID ON LockerAllocations (LockerID);
CREATE INDEX idx_Payments_AllocationID ON Payments (AllocationID);

-- Insert sample data
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210', '456 Elm St');

INSERT INTO LockerSizes (Size, Description, Rent)
VALUES 
('Small', 'Small locker', 10.00),
('Medium', 'Medium locker', 20.00),
('Large', 'Large locker', 30.00);

INSERT INTO SafeDepositLockers (LockerSizeID, LockerNumber, IsAllocated)
VALUES 
(1, 'LKR-001', FALSE),
(2, 'LKR-002', FALSE),
(3, 'LKR-003', FALSE);

INSERT INTO LockerAllocations (CustomerID, LockerID, AllocationDate, ExpirationDate, RentPaid)
VALUES 
(1, 1, '2022-01-01', '2023-01-01', 120.00),
(2, 2, '2022-02-01', '2023-02-01', 240.00);

INSERT INTO Payments (AllocationID, PaymentDate, Amount, PaymentMethod)
VALUES 
(1, '2022-01-01', 10.00, 'Cash'),
(1, '2022-02-01', 10.00, 'Cash'),
(2, '2022-02-01', 20.00, 'Card');
```
