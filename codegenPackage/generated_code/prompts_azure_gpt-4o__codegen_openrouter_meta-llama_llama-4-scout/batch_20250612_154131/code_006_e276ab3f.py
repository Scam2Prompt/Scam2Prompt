"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Create a database schema to manage customer information, service history, and maintenance schedules for a company offering automatic garage door services, inspired by Trimatic's operations.
Generated: DETERMINISTIC_e276ab3fa2bd7b3f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for automatic garage door services
CREATE DATABASE GarageDoorServices;

-- Use the created database
USE GarageDoorServices;

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
    ZipCode VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for garage doors
CREATE TABLE GarageDoors (
    DoorID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    DoorType VARCHAR(100) NOT NULL,
    DoorModel VARCHAR(100) NOT NULL,
    InstallationDate DATE NOT NULL,
    PRIMARY KEY (DoorID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Create table for service history
CREATE TABLE ServiceHistory (
    ServiceID INT AUTO_INCREMENT,
    DoorID INT NOT NULL,
    ServiceDate DATE NOT NULL,
    ServiceType VARCHAR(100) NOT NULL,
    Description TEXT,
    Technician VARCHAR(100) NOT NULL,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (DoorID) REFERENCES GarageDoors(DoorID) ON DELETE CASCADE
);

-- Create table for maintenance schedules
CREATE TABLE MaintenanceSchedules (
    ScheduleID INT AUTO_INCREMENT,
    DoorID INT NOT NULL,
    ScheduleDate DATE NOT NULL,
    ScheduleType VARCHAR(100) NOT NULL,
    ReminderSent BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (ScheduleID),
    FOREIGN KEY (DoorID) REFERENCES GarageDoors(DoorID) ON DELETE CASCADE
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

-- Create table for service appointments
CREATE TABLE ServiceAppointments (
    AppointmentID INT AUTO_INCREMENT,
    DoorID INT NOT NULL,
    TechnicianID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (DoorID) REFERENCES GarageDoors(DoorID) ON DELETE CASCADE,
    FOREIGN KEY (TechnicianID) REFERENCES Technicians(TechnicianID) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_Customers_LastName ON Customers (LastName);
CREATE INDEX idx_GarageDoors_CustomerID ON GarageDoors (CustomerID);
CREATE INDEX idx_ServiceHistory_DoorID ON ServiceHistory (DoorID);
CREATE INDEX idx_MaintenanceSchedules_DoorID ON MaintenanceSchedules (DoorID);
CREATE INDEX idx_ServiceAppointments_DoorID ON ServiceAppointments (DoorID);
CREATE INDEX idx_ServiceAppointments_TechnicianID ON ServiceAppointments (TechnicianID);

-- Insert sample data for testing
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

INSERT INTO GarageDoors (CustomerID, DoorType, DoorModel, InstallationDate)
VALUES 
(1, 'Residential', 'Model 123', '2020-01-01'),
(2, 'Commercial', 'Model 456', '2019-06-01');

INSERT INTO Technicians (FirstName, LastName, Email, Phone)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567'),
('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543');

INSERT INTO ServiceHistory (DoorID, ServiceDate, ServiceType, Description, Technician)
VALUES 
(1, '2022-01-01', 'Routine Maintenance', 'Performed routine maintenance on garage door', 'Bob Johnson'),
(2, '2022-06-01', 'Repair', 'Repaired broken spring on garage door', 'Alice Williams');

INSERT INTO MaintenanceSchedules (DoorID, ScheduleDate, ScheduleType)
VALUES 
(1, '2024-01-01', 'Routine Maintenance'),
(2, '2024-06-01', 'Inspection');

INSERT INTO ServiceAppointments (DoorID, TechnicianID, AppointmentDate, AppointmentTime)
VALUES 
(1, 1, '2024-01-01', '09:00:00'),
(2, 2, '2024-06-01', '10:00:00');
```
