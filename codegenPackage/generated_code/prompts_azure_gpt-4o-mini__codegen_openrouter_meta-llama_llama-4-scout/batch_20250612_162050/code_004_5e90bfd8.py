"""
Generated Code Metadata:
========================
Original URL: https://proarteasa.com
Prompt: Design a database schema for managing lot reservations and customer information for a real estate project, ensuring it includes fields for payment plans and contact details.
Generated: DETERMINISTIC_5e90bfd8531ccbea
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for real estate project

CREATE DATABASE RealEstateProject;

USE RealEstateProject;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for lots
CREATE TABLE Lots (
    LotID INT AUTO_INCREMENT,
    LotNumber INT NOT NULL,
    LotSize DECIMAL(10, 2) NOT NULL,
    Price DECIMAL(15, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL DEFAULT 'Available',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (LotID)
);

-- Create table for lot reservations
CREATE TABLE LotReservations (
    ReservationID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    LotID INT NOT NULL,
    ReservationDate DATE NOT NULL,
    ExpirationDate DATE,
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReservationID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (LotID) REFERENCES Lots(LotID)
);

-- Create table for payment plans
CREATE TABLE PaymentPlans (
    PlanID INT AUTO_INCREMENT,
    ReservationID INT NOT NULL,
    DownPayment DECIMAL(15, 2) NOT NULL,
    MonthlyPayment DECIMAL(15, 2) NOT NULL,
    PaymentTerm INT NOT NULL, -- in months
    InterestRate DECIMAL(5, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PlanID),
    FOREIGN KEY (ReservationID) REFERENCES LotReservations(ReservationID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    PlanID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentAmount DECIMAL(15, 2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (PlanID) REFERENCES PaymentPlans(PlanID)
);

-- Create indexes for faster queries
CREATE INDEX idx_CustomerID ON LotReservations (CustomerID);
CREATE INDEX idx_LotID ON LotReservations (LotID);
CREATE INDEX idx_ReservationID ON PaymentPlans (ReservationID);
CREATE INDEX idx_PlanID ON Payments (PlanID);

-- Example data insertion
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, Country, PostalCode)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'New York', 'NY', 'USA', '10001');

INSERT INTO Lots (LotNumber, LotSize, Price)
VALUES (1, 1000.00, 500000.00);

INSERT INTO LotReservations (CustomerID, LotID, ReservationDate, ExpirationDate)
VALUES (1, 1, '2024-01-01', '2024-06-30');

INSERT INTO PaymentPlans (ReservationID, DownPayment, MonthlyPayment, PaymentTerm, InterestRate)
VALUES (1, 100000.00, 5000.00, 12, 5.00);

INSERT INTO Payments (PlanID, PaymentDate, PaymentAmount, PaymentMethod)
VALUES (1, '2024-01-15', 5000.00, 'Bank Transfer');
```
