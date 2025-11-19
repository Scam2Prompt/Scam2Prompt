"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: "Design a database schema to store customer information, service requests, and appointment schedules for a plumbing and heating business like Flammedeauinc."
Generated: DETERMINISTIC_e43fbba985122e8c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Flammedeauinc

-- Create database
CREATE DATABASE FlammedeauincDB;

-- Use database
USE FlammedeauincDB;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for service requests
CREATE TABLE ServiceRequests (
    ServiceRequestID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    RequestType ENUM('plumbing', 'heating') NOT NULL,
    Description TEXT,
    Priority ENUM('low', 'medium', 'high') NOT NULL DEFAULT 'low',
    Status ENUM('open', 'in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'open',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceRequestID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Create table for appointment schedules
CREATE TABLE AppointmentSchedules (
    AppointmentID INT AUTO_INCREMENT,
    ServiceRequestID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    TechnicianID INT,
    Status ENUM('scheduled', 'rescheduled', 'cancelled', 'completed') NOT NULL DEFAULT 'scheduled',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ServiceRequestID) REFERENCES ServiceRequests(ServiceRequestID) ON DELETE CASCADE
);

-- Create table for technicians
CREATE TABLE Technicians (
    TechnicianID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TechnicianID)
);

-- Create index on CustomerID in ServiceRequests table
CREATE INDEX idx_CustomerID ON ServiceRequests (CustomerID);

-- Create index on ServiceRequestID in AppointmentSchedules table
CREATE INDEX idx_ServiceRequestID ON AppointmentSchedules (ServiceRequestID);

-- Example insert statements
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345');

INSERT INTO ServiceRequests (CustomerID, RequestType, Description, Priority)
VALUES (1, 'plumbing', 'Leaky faucet', 'low');

INSERT INTO Technicians (FirstName, LastName, Email, Phone)
VALUES ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO AppointmentSchedules (ServiceRequestID, AppointmentDate, AppointmentTime, TechnicianID)
VALUES (1, '2024-09-17', '09:00:00', 1);
```
