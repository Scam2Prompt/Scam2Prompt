"""
Generated Code Metadata:
========================
Original URL: https://mluce-ginza.net
Prompt: Generate a sample database schema for storing client information, treatment plans, and appointment schedules for a makeup salon with multiple services like M luce.
Generated: DETERMINISTIC_c486160f4f873434
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for makeup salon
CREATE DATABASE MakeupSalon;

-- Use the database
USE MakeupSalon;

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

-- Create table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10,2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create table for treatment plans
CREATE TABLE TreatmentPlans (
    PlanID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceID INT NOT NULL,
    PlanDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PlanID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create table for appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create table for M Luce services (example of a specific service)
CREATE TABLE MLuceServices (
    MLuceServiceID INT AUTO_INCREMENT,
    ServiceID INT NOT NULL,
    MLuceServiceName VARCHAR(255) NOT NULL,
    MLuceServiceDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MLuceServiceID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Insert sample data into services table
INSERT INTO Services (ServiceName, Description, Price)
VALUES 
('M Luce Facial', 'A customized facial treatment', 120.00),
('Makeup Application', 'Professional makeup application for special occasions', 75.00),
('Waxing', 'Eyebrow waxing and shaping', 30.00);

-- Insert sample data into clients table
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address)
VALUES 
('Jane', 'Doe', 'jane.doe@example.com', '123-456-7890', '123 Main St'),
('John', 'Smith', 'john.smith@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into treatment plans table
INSERT INTO TreatmentPlans (ClientID, ServiceID, PlanDescription)
VALUES 
(1, 1, 'Monthly facial treatments for skin rejuvenation'),
(2, 2, 'Makeup application for wedding');

-- Insert sample data into appointments table
INSERT INTO Appointments (ClientID, ServiceID, AppointmentDate, AppointmentTime)
VALUES 
(1, 1, '2024-09-20', '10:00:00'),
(2, 2, '2024-09-25', '14:00:00');

-- Insert sample data into M Luce services table
INSERT INTO MLuceServices (ServiceID, MLuceServiceName, MLuceServiceDescription)
VALUES 
(1, 'M Luce Facial Treatment', 'A customized facial treatment using M Luce products');
```
