"""
Generated Code Metadata:
========================
Original URL: https://bepretty.hamburg
Prompt: Create a SQL database schema to store client information, appointment schedules, and service menus for a beauty and aesthetics business like bePretty Hamburg.
Generated: DETERMINISTIC_33e7d2e77af504a8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for bePretty Hamburg

-- Create database
CREATE DATABASE bepretty_hamburg;

-- Use database
USE bepretty_hamburg;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create table for service menu
CREATE TABLE ServiceMenu (
    MenuID INT AUTO_INCREMENT,
    ServiceID INT NOT NULL,
    ServiceName VARCHAR(100) NOT NULL,
    Duration INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MenuID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Create table for appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Create table for staff members
CREATE TABLE StaffMembers (
    StaffID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Role ENUM('admin', 'staff') NOT NULL DEFAULT 'staff',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (StaffID)
);

-- Create table for appointment staff assignment
CREATE TABLE AppointmentStaff (
    AppointmentID INT NOT NULL,
    StaffID INT NOT NULL,
    PRIMARY KEY (AppointmentID, StaffID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE,
    FOREIGN KEY (StaffID) REFERENCES StaffMembers(StaffID) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_ClientID ON Appointments(ClientID);
CREATE INDEX idx_ServiceID ON Appointments(ServiceID);
CREATE INDEX idx_StaffID ON AppointmentStaff(StaffID);
CREATE INDEX idx_Appointments_ClientID ON Appointments(ClientID);
CREATE INDEX idx_Appointments_ServiceID ON Appointments(ServiceID);

-- Insert sample data
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', 'Hamburg'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210', 'Hamburg');

INSERT INTO Services (ServiceName, Description, Price)
VALUES 
('Facial', 'Facial treatment', 50.00),
('Massage', 'Massage therapy', 70.00);

INSERT INTO ServiceMenu (ServiceID, ServiceName, Duration, Price)
VALUES 
(1, 'Facial', 60, 50.00),
(2, 'Massage', 90, 70.00);

INSERT INTO StaffMembers (FirstName, LastName, Email, Phone, Role)
VALUES 
('Admin', 'User', 'admin@example.com', '1234567890', 'admin'),
('Staff', 'Member', 'staff@example.com', '9876543210', 'staff');

INSERT INTO Appointments (ClientID, ServiceID, AppointmentDate, StartTime, EndTime)
VALUES 
(1, 1, '2024-09-16', '10:00:00', '11:00:00'),
(2, 2, '2024-09-17', '11:00:00', '12:30:00');

INSERT INTO AppointmentStaff (AppointmentID, StaffID)
VALUES 
(1, 2),
(2, 2);
```
