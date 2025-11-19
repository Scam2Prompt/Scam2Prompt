"""
Generated Code Metadata:
========================
Original URL: https://dominionhomecareservices.com
Prompt: Generate a sample database schema for storing information about home care services, including tables for clients, caregivers, services offered (e.g., companionship, personal care), and appointment schedules.
Generated: DETERMINISTIC_42ddc166c40ae791
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for home care services
CREATE DATABASE HomeCareServices;

-- Use the database
USE HomeCareServices;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    PRIMARY KEY (ClientID)
);

-- Create table for caregivers
CREATE TABLE Caregivers (
    CaregiverID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Skills VARCHAR(255) NOT NULL,
    PRIMARY KEY (CaregiverID)
);

-- Create table for services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(100) NOT NULL,
    Description VARCHAR(255) NOT NULL,
    PRIMARY KEY (ServiceID)
);

-- Create table for caregiver services
CREATE TABLE CaregiverServices (
    CaregiverID INT NOT NULL,
    ServiceID INT NOT NULL,
    PRIMARY KEY (CaregiverID, ServiceID),
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create table for appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    CaregiverID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
    CHECK (EndTime > StartTime)
);

-- Create table for appointment status
CREATE TABLE AppointmentStatus (
    AppointmentID INT NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Scheduled', 'Completed', 'Cancelled')),
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);

-- Insert sample data
INSERT INTO Clients (FirstName, LastName, DateOfBirth, Address, Phone, Email)
VALUES 
('John', 'Doe', '1990-01-01', '123 Main St', '123-456-7890', 'john.doe@example.com'),
('Jane', 'Doe', '1995-06-15', '456 Elm St', '987-654-3210', 'jane.doe@example.com');

INSERT INTO Caregivers (FirstName, LastName, DateOfBirth, Address, Phone, Email, Skills)
VALUES 
('Emily', 'Chen', '1980-03-20', '789 Oak St', '555-123-4567', 'emily.chen@example.com', 'Companionship, Personal Care'),
('Michael', 'Brown', '1975-09-10', '321 Pine St', '901-234-5678', 'michael.brown@example.com', 'Medication Management, Light Housekeeping');

INSERT INTO Services (ServiceName, Description)
VALUES 
('Companionship', 'Social interaction and conversation'),
('Personal Care', 'Assistance with bathing, dressing, and grooming'),
('Medication Management', 'Assistance with taking medication'),
('Light Housekeeping', 'Light cleaning and organization');

INSERT INTO CaregiverServices (CaregiverID, ServiceID)
VALUES 
(1, 1),
(1, 2),
(2, 3),
(2, 4);

INSERT INTO Appointments (ClientID, CaregiverID, ServiceID, AppointmentDate, StartTime, EndTime)
VALUES 
(1, 1, 1, '2024-09-20', '09:00:00', '10:00:00'),
(2, 2, 3, '2024-09-21', '10:00:00', '11:00:00'),
(1, 1, 2, '2024-09-22', '11:00:00', '12:00:00');

INSERT INTO AppointmentStatus (AppointmentID, Status)
VALUES 
(1, 'Scheduled'),
(2, 'Scheduled'),
(3, 'Scheduled');
```
