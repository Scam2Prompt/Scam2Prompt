"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: "Generate a sample database schema for storing client information, horse details, and appointment schedules for an equine care provider like Martin Godwin."
Generated: DETERMINISTIC_e670879136b35fd7
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for equine care provider

-- Create database
CREATE DATABASE EquineCare;

-- Use database
USE EquineCare;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(200) NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    PostalCode VARCHAR(10) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for horses
CREATE TABLE Horses (
    HorseID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    HorseName VARCHAR(50) NOT NULL,
    Breed VARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Sex VARCHAR(10) NOT NULL CHECK (Sex IN ('Male', 'Female', 'Gelding')),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (HorseID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create table for veterinarians
CREATE TABLE Veterinarians (
    VeterinarianID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VeterinarianID)
);

-- Create table for appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    HorseID INT NOT NULL,
    VeterinarianID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    Description VARCHAR(200) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (HorseID) REFERENCES Horses(HorseID) ON DELETE CASCADE,
    FOREIGN KEY (VeterinarianID) REFERENCES Veterinarians(VeterinarianID) ON DELETE CASCADE
);

-- Create table for services provided
CREATE TABLE ServicesProvided (
    ServiceID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    ServiceName VARCHAR(50) NOT NULL,
    ServiceCost DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE
);

-- Create table for payments
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

-- Insert sample data
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address, City, State, PostalCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

INSERT INTO Horses (ClientID, HorseName, Breed, Age, Sex)
VALUES 
(1, 'Max', 'Quarter Horse', 10, 'Male'),
(1, 'Luna', 'Thoroughbred', 5, 'Female'),
(2, 'Buddy', 'Appaloosa', 15, 'Gelding');

INSERT INTO Veterinarians (FirstName, LastName, Email, Phone)
VALUES 
('Martin', 'Godwin', 'martin.godwin@example.com', '555-123-4567'),
('Emily', 'Chen', 'emily.chen@example.com', '555-901-2345');

INSERT INTO Appointments (ClientID, HorseID, VeterinarianID, AppointmentDate, AppointmentTime, Description)
VALUES 
(1, 1, 1, '2024-09-20', '09:00:00', 'Routine checkup'),
(1, 2, 2, '2024-09-22', '10:00:00', 'Vaccinations'),
(2, 3, 1, '2024-09-25', '11:00:00', 'Dental care');

INSERT INTO ServicesProvided (AppointmentID, ServiceName, ServiceCost)
VALUES 
(1, 'Exam', 50.00),
(1, 'Blood work', 20.00),
(2, 'Vaccinations', 100.00),
(3, 'Dental care', 75.00);

INSERT INTO Payments (AppointmentID, PaymentDate, PaymentAmount, PaymentMethod)
VALUES 
(1, '2024-09-20', 70.00, 'Cash'),
(2, '2024-09-22', 100.00, 'Credit card'),
(3, '2024-09-25', 75.00, 'Check');
```
