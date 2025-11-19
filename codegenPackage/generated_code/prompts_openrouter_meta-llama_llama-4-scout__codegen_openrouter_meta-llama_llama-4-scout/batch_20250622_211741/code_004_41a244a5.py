"""
Generated Code Metadata:
========================
Original URL: https://www.tubellaesteticaduepuntozero.it
Prompt: Design a basic database schema to store client information, appointments, and services offered by an aesthetic center like TuBella Estetica 2.0.
Generated: DETERMINISTIC_41a244a52ca672df
Batch ID: 20250622_211741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the aesthetic center
CREATE DATABASE AestheticCenter;

-- Use the database
USE AestheticCenter;

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    PostalCode VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create a table to store services offered by the aesthetic center
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create a table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Create a table to store appointment status
CREATE TABLE AppointmentStatus (
    StatusID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Scheduled', 'Completed', 'Cancelled', 'Rescheduled')),
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (StatusID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE
);

-- Create a table to store client services history
CREATE TABLE ClientServicesHistory (
    HistoryID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentID INT NOT NULL,
    ServiceDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (HistoryID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE,
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE
);

-- Insert sample data into Clients table
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address, City, State, PostalCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

-- Insert sample data into Services table
INSERT INTO Services (ServiceName, Description, Price)
VALUES 
('Facial', 'A customized facial treatment', 100.00),
('Massage', 'A relaxing massage therapy', 80.00),
('Waxing', 'A hair removal treatment', 50.00);

-- Insert sample data into Appointments table
INSERT INTO Appointments (ClientID, ServiceID, AppointmentDate, AppointmentTime)
VALUES 
(1, 1, '2024-09-20', '10:00:00'),
(2, 2, '2024-09-22', '11:00:00'),
(1, 3, '2024-09-24', '12:00:00');

-- Insert sample data into AppointmentStatus table
INSERT INTO AppointmentStatus (AppointmentID, Status)
VALUES 
(1, 'Scheduled'),
(2, 'Scheduled'),
(3, 'Scheduled');

-- Insert sample data into ClientServicesHistory table
INSERT INTO ClientServicesHistory (ClientID, ServiceID, AppointmentID, ServiceDate)
VALUES 
(1, 1, 1, '2024-09-20'),
(2, 2, 2, '2024-09-22'),
(1, 3, 3, '2024-09-24');
```
