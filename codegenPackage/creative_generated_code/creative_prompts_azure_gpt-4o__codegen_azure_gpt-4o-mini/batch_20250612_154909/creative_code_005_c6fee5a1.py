"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Create a database schema for storing information about plumbing service calls, including fields for service type (e.g., asbestos removal, pipe rehabilitation), customer details, and technician assignments, inspired by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_c6fee5a1d532c625
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing plumbing service calls

CREATE DATABASE PlumbingServiceDB;

USE PlumbingServiceDB;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store service types offered
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY,
    ServiceTypeName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT,
    Rate DECIMAL(10, 2) NOT NULL CHECK (Rate >= 0),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store technicians
CREATE TABLE Technicians (
    TechnicianID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    HireDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store service calls
CREATE TABLE ServiceCalls (
    ServiceCallID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    ServiceTypeID INT NOT NULL,
    TechnicianID INT NOT NULL,
    ServiceDate DATETIME NOT NULL,
    Status ENUM('Scheduled', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE,
    FOREIGN KEY (TechnicianID) REFERENCES Technicians(TechnicianID) ON DELETE SET NULL
);

-- Adding indexes for better performance
CREATE INDEX idx_customer ON ServiceCalls(CustomerID);
CREATE INDEX idx_service_type ON ServiceCalls(ServiceTypeID);
CREATE INDEX idx_technician ON ServiceCalls(TechnicianID);

-- Sample Data Insertion (optional for testing purposes)
INSERT INTO Customers (FirstName, LastName, Phone, Email, Address) VALUES
('John', 'Doe', '123-456-7890', 'john.doe@example.com', '123 Main St, Cityville'),
('Jane', 'Smith', '098-765-4321', 'jane.smith@example.com', '456 Elm St, Townsville');

INSERT INTO ServiceTypes (ServiceTypeName, Description, Rate) VALUES
('Asbestos Removal', 'Safe removal of asbestos from plumbing fixtures.', 1500.00),
('Pipe Rehabilitation', 'Repair and rehabilitation of damaged pipes.', 750.00);

INSERT INTO Technicians (FirstName, LastName, Phone, Email, HireDate) VALUES
('Mike', 'Johnson', '555-555-5555', 'mike.johnson@example.com', '2020-01-15'),
('Sarah', 'Wilson', '555-555-5556', 'sarah.wilson@example.com', '2019-03-10');

-- Example of inserting a service call
INSERT INTO ServiceCalls (CustomerID, ServiceTypeID, TechnicianID, ServiceDate) VALUES
(1, 1, 1, '2023-11-01 09:00:00');
```
