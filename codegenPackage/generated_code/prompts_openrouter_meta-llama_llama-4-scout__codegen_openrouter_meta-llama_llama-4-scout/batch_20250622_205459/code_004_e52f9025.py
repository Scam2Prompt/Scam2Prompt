"""
Generated Code Metadata:
========================
Original URL: https://poocoinnex.weebly.com
Prompt: Write a SQL query to design a database schema for a barbershop management system, including tables for barbers, clients, appointments, and services offered, such as those provided by Southcorner Barbershop.
Generated: DETERMINISTIC_e52f9025e663a462
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for barbershop management system
CREATE DATABASE BarbershopManagement;

-- Use the database
USE BarbershopManagement;

-- Create table for barbers
CREATE TABLE Barbers (
    BarberID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    HireDate DATE,
    PRIMARY KEY (BarberID)
);

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    PRIMARY KEY (ClientID)
);

-- Create table for services offered
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
    ClientID INT NOT NULL,
    BarberID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (BarberID) REFERENCES Barbers(BarberID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create table for appointment history
CREATE TABLE AppointmentHistory (
    HistoryID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    ClientID INT NOT NULL,
    BarberID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    CompletionDate DATE,
    PRIMARY KEY (HistoryID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (BarberID) REFERENCES Barbers(BarberID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create indexes for faster queries
CREATE INDEX idx_appointments_clientid ON Appointments (ClientID);
CREATE INDEX idx_appointments_barberid ON Appointments (BarberID);
CREATE INDEX idx_appointments_serviceid ON Appointments (ServiceID);

-- Insert sample data
INSERT INTO Barbers (FirstName, LastName, Email, Phone, HireDate)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '2020-01-01'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '2020-06-01');

INSERT INTO Clients (FirstName, LastName, Email, Phone, Address)
VALUES 
('Sam', 'Smith', 'sam.smith@example.com', '555-123-4567', '123 Main St'),
('Emily', 'Johnson', 'emily.johnson@example.com', '555-987-6543', '456 Elm St');

INSERT INTO Services (ServiceName, Description, Price)
VALUES 
('Haircut', 'Standard haircut', 20.00),
('Shave', 'Straight razor shave', 30.00),
('Haircut and Shave', 'Combo of haircut and shave', 40.00);

INSERT INTO Appointments (ClientID, BarberID, ServiceID, AppointmentDate, AppointmentTime)
VALUES 
(1, 1, 1, '2024-09-20', '09:00:00'),
(2, 2, 2, '2024-09-21', '10:00:00');
```
