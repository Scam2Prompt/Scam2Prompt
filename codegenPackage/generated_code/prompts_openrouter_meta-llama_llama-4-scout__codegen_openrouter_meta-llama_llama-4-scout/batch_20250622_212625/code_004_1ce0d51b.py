"""
Generated Code Metadata:
========================
Original URL: https://www.bronzetanning.co
Prompt: Create a SQL database schema to store information about spa clients, appointments, and services offered, including fields for client names, appointment dates, and services provided.
Generated: DETERMINISTIC_1ce0d51b9035e087
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the spa management system
CREATE DATABASE SpaManagement;

-- Use the SpaManagement database
USE SpaManagement;

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    PostalCode VARCHAR(20),
    PRIMARY KEY (ClientID)
);

-- Create a table to store service information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(100) NOT NULL,
    ServiceDescription TEXT,
    ServicePrice DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ServiceID)
);

-- Create a table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    ServiceID INT,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create a table to store appointment services (many-to-many relationship)
CREATE TABLE AppointmentServices (
    AppointmentID INT NOT NULL,
    ServiceID INT NOT NULL,
    PRIMARY KEY (AppointmentID, ServiceID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_ClientID ON Appointments (ClientID);
CREATE INDEX idx_ServiceID ON Appointments (ServiceID);
CREATE INDEX idx_Appointments_ClientID ON AppointmentServices (AppointmentID);
CREATE INDEX idx_Appointments_ServiceID ON AppointmentServices (ServiceID);

-- Example data insertion
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address, City, State, PostalCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

INSERT INTO Services (ServiceName, ServiceDescription, ServicePrice)
VALUES 
('Massage', 'Full body massage', 60.00),
('Facial', 'Customized facial treatment', 75.00),
('Manicure', 'Nail care and polish', 30.00);

INSERT INTO Appointments (ClientID, AppointmentDate, AppointmentTime, ServiceID)
VALUES 
(1, '2024-09-16', '09:00:00', 1),
(2, '2024-09-17', '10:00:00', 2);

INSERT INTO AppointmentServices (AppointmentID, ServiceID)
VALUES 
(1, 1),
(1, 3),
(2, 2);
```
