"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: Design a database schema for managing client information and appointment scheduling for an equine care service, taking cues from the organizational structure of Martin Godwin Equine Services.
Generated: DETERMINISTIC_d5ab1b53594d67ff
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the equine care service
CREATE DATABASE EquineCareService;

-- Use the database
USE EquineCareService;

-- Create a table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    ZipCode VARCHAR(10),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create a table for horses
CREATE TABLE Horses (
    HorseID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    HorseName VARCHAR(100) NOT NULL,
    Breed VARCHAR(50),
    Age INT,
    Sex VARCHAR(10),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (HorseID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create a table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create a table for veterinarians
CREATE TABLE Veterinarians (
    VeterinarianID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VeterinarianID)
);

-- Create a table for appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    HorseID INT,
    VeterinarianID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (HorseID) REFERENCES Horses(HorseID) ON DELETE SET NULL,
    FOREIGN KEY (VeterinarianID) REFERENCES Veterinarians(VeterinarianID) ON DELETE RESTRICT,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE RESTRICT
);

-- Create a table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentAmount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_ClientID ON Appointments(ClientID);
CREATE INDEX idx_HorseID ON Appointments(HorseID);
CREATE INDEX idx_VeterinarianID ON Appointments(VeterinarianID);
CREATE INDEX idx_ServiceID ON Appointments(ServiceID);
CREATE INDEX idx_AppointmentDate ON Appointments(AppointmentDate);
```

```sql
-- Example data insertion
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

INSERT INTO Horses (ClientID, HorseName, Breed, Age, Sex)
VALUES 
(1, 'Max', 'Quarter Horse', 10, 'Male'),
(1, 'Luna', 'Thoroughbred', 5, 'Female'),
(2, 'Buddy', 'Arabian', 15, 'Male');

INSERT INTO Services (ServiceName, Description, Price)
VALUES 
('Vaccination', 'Annual vaccination for horses', 50.00),
('Dental Care', 'Routine dental care for horses', 75.00),
('Hoof Trimming', 'Regular hoof trimming for horses', 30.00);

INSERT INTO Veterinarians (FirstName, LastName, Email, Phone)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567'),
('Alice', 'Williams', 'alice.williams@example.com', '555-901-2345');

INSERT INTO Appointments (ClientID, HorseID, VeterinarianID, ServiceID, AppointmentDate, AppointmentTime, Description)
VALUES 
(1, 1, 1, 1, '2024-09-20', '09:00:00', 'Annual vaccination'),
(1, 2, 1, 2, '2024-09-22', '10:00:00', 'Dental care'),
(2, 3, 2, 3, '2024-09-25', '11:00:00', 'Hoof trimming');

INSERT INTO Payments (AppointmentID, PaymentDate, PaymentAmount, PaymentMethod)
VALUES 
(1, '2024-09-20', 50.00, 'Cash'),
(2, '2024-09-22', 75.00, 'Credit Card'),
(3, '2024-09-25', 30.00, 'Check');
```
