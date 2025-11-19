"""
Generated Code Metadata:
========================
Original URL: https://tecnicos-whirlpool.com
Prompt: Create a SQL database schema to store information about Whirlpool appliance repair services, including customer details, appliance types, and service status.
Generated: DETERMINISTIC_ee3a90a42ae55c13
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Whirlpool appliance repair services
CREATE DATABASE WhirlpoolRepair;

-- Use the database
USE WhirlpoolRepair;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL,
    PRIMARY KEY (CustomerID)
);

-- Create table for appliance types
CREATE TABLE ApplianceTypes (
    ApplianceTypeID INT AUTO_INCREMENT,
    ApplianceType VARCHAR(100) NOT NULL,
    Description TEXT,
    PRIMARY KEY (ApplianceTypeID)
);

-- Create table for appliances
CREATE TABLE Appliances (
    ApplianceID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ApplianceTypeID INT NOT NULL,
    ModelNumber VARCHAR(100) NOT NULL,
    SerialNumber VARCHAR(100) NOT NULL,
    PurchaseDate DATE,
    PRIMARY KEY (ApplianceID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ApplianceTypeID) REFERENCES ApplianceTypes(ApplianceTypeID)
);

-- Create table for service status
CREATE TABLE ServiceStatus (
    ServiceStatusID INT AUTO_INCREMENT,
    ServiceStatus VARCHAR(100) NOT NULL,
    Description TEXT,
    PRIMARY KEY (ServiceStatusID)
);

-- Create table for repair services
CREATE TABLE RepairServices (
    ServiceID INT AUTO_INCREMENT,
    ApplianceID INT NOT NULL,
    ServiceDate DATE NOT NULL,
    ServiceStatusID INT NOT NULL,
    Description TEXT,
    Cost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (ApplianceID) REFERENCES Appliances(ApplianceID),
    FOREIGN KEY (ServiceStatusID) REFERENCES ServiceStatus(ServiceStatusID)
);

-- Create table for technicians
CREATE TABLE Technicians (
    TechnicianID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    PRIMARY KEY (TechnicianID)
);

-- Create table for service assignments
CREATE TABLE ServiceAssignments (
    ServiceAssignmentID INT AUTO_INCREMENT,
    ServiceID INT NOT NULL,
    TechnicianID INT NOT NULL,
    AssignmentDate DATE NOT NULL,
    PRIMARY KEY (ServiceAssignmentID),
    FOREIGN KEY (ServiceID) REFERENCES RepairServices(ServiceID),
    FOREIGN KEY (TechnicianID) REFERENCES Technicians(TechnicianID)
);

-- Insert some sample data
INSERT INTO ApplianceTypes (ApplianceType, Description)
VALUES 
('Washing Machine', 'Whirlpool washing machine'),
('Dryer', 'Whirlpool dryer'),
('Refrigerator', 'Whirlpool refrigerator'),
('Oven', 'Whirlpool oven');

INSERT INTO ServiceStatus (ServiceStatus, Description)
VALUES 
('Scheduled', 'Service scheduled'),
('In Progress', 'Service in progress'),
('Completed', 'Service completed'),
('Cancelled', 'Service cancelled');

INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');
```
