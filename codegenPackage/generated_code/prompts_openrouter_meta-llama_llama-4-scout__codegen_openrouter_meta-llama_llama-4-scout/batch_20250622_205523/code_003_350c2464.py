"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Create a SQL database schema for a cleaning services company, including tables for customers, services, and appointments, with constraints and relationships.
Generated: DETERMINISTIC_350c2464fbda70b6
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for cleaning services company
CREATE DATABASE CleaningServices;

-- Use the database schema
USE CleaningServices;

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

-- Create table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ServiceID)
);

-- Create table for appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentAmount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(100) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE
);

-- Create table for employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    PRIMARY KEY (EmployeeID)
);

-- Create table for appointment employees
CREATE TABLE AppointmentEmployees (
    AppointmentID INT NOT NULL,
    EmployeeID INT NOT NULL,
    PRIMARY KEY (AppointmentID, EmployeeID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Insert sample data into tables
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

INSERT INTO Services (ServiceName, Description, Price)
VALUES 
('House Cleaning', 'Basic house cleaning services', 100.00),
('Deep Cleaning', 'Deep cleaning services for larger homes', 200.00);

INSERT INTO Appointments (CustomerID, ServiceID, AppointmentDate, StartTime, EndTime)
VALUES 
(1, 1, '2024-09-17', '09:00:00', '11:00:00'),
(2, 2, '2024-09-18', '10:00:00', '13:00:00');

INSERT INTO Payments (AppointmentID, PaymentDate, PaymentAmount, PaymentMethod)
VALUES 
(1, '2024-09-17', 100.00, 'Cash'),
(2, '2024-09-18', 200.00, 'Credit Card');

INSERT INTO Employees (FirstName, LastName, Email, Phone)
VALUES 
('Bob', 'Smith', 'bob.smith@example.com', '555-123-4567'),
('Alice', 'Johnson', 'alice.johnson@example.com', '555-987-6543');

INSERT INTO AppointmentEmployees (AppointmentID, EmployeeID)
VALUES 
(1, 1),
(2, 2);
```
