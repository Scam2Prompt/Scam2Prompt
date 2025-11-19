"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Create a database schema in SQL to manage client information for an NDIS provider, including tables for personal details, services availed (e.g., household tasks, travel assistance), and appointment scheduling.
Generated: DETERMINISTIC_056329dc44909096
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for NDIS provider
CREATE DATABASE NDIS_Provider;

-- Use the created database
USE NDIS_Provider;

-- Create table for client personal details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT,
    ServiceType VARCHAR(100) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceTypeID)
);

-- Create table for services availed by clients
CREATE TABLE ClientServices (
    ClientServiceID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceTypeID INT NOT NULL,
    ServiceDate DATE NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientServiceID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE
);

-- Create table for appointment scheduling
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    ServiceTypeID INT NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE
);

-- Create table for household tasks
CREATE TABLE HouseholdTasks (
    HouseholdTaskID INT AUTO_INCREMENT,
    ClientServiceID INT NOT NULL,
    TaskType VARCHAR(100) NOT NULL,
    TaskDate DATE NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (HouseholdTaskID),
    FOREIGN KEY (ClientServiceID) REFERENCES ClientServices(ClientServiceID) ON DELETE CASCADE
);

-- Create table for travel assistance
CREATE TABLE TravelAssistance (
    TravelAssistanceID INT AUTO_INCREMENT,
    ClientServiceID INT NOT NULL,
    TravelDate DATE NOT NULL,
    TravelTime TIME NOT NULL,
    Destination VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TravelAssistanceID),
    FOREIGN KEY (ClientServiceID) REFERENCES ClientServices(ClientServiceID) ON DELETE CASCADE
);

-- Insert sample data into ServiceTypes table
INSERT INTO ServiceTypes (ServiceType, Description)
VALUES 
('Household Tasks', 'Assistance with household chores'),
('Travel Assistance', 'Assistance with travel');

-- Create stored procedure to add new client
DELIMITER //
CREATE PROCEDURE AddClient(
    IN p_FirstName VARCHAR(255),
    IN p_LastName VARCHAR(255),
    IN p_DateOfBirth DATE,
    IN p_Address VARCHAR(255),
    IN p_Phone VARCHAR(20),
    IN p_Email VARCHAR(100)
)
BEGIN
    INSERT INTO Clients (FirstName, LastName, DateOfBirth, Address, Phone, Email)
    VALUES (p_FirstName, p_LastName, p_DateOfBirth, p_Address, p_Phone, p_Email);
END//
DELIMITER ;

-- Create stored procedure to schedule appointment
DELIMITER //
CREATE PROCEDURE ScheduleAppointment(
    IN p_ClientID INT,
    IN p_AppointmentDate DATE,
    IN p_AppointmentTime TIME,
    IN p_ServiceTypeID INT
)
BEGIN
    INSERT INTO Appointments (ClientID, AppointmentDate, AppointmentTime, ServiceTypeID)
    VALUES (p_ClientID, p_AppointmentDate, p_AppointmentTime, p_ServiceTypeID);
END//
DELIMITER ;
```
