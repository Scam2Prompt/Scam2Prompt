"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Design a simple database schema to store client information and appointment schedules for a reflexology clinic like Red Horse Reflexology, and provide SQL code for creating the necessary tables.
Generated: DETERMINISTIC_f884bfb10e6bbc6a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the reflexology clinic
CREATE DATABASE RedHorseReflexology;

-- Use the created database
USE RedHorseReflexology;

-- Create a table to store client information
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
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create a table to store practitioners information
CREATE TABLE Practitioners (
    PractitionerID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PractitionerID)
);

-- Create a table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    PractitionerID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    Description VARCHAR(200),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (PractitionerID) REFERENCES Practitioners(PractitionerID) ON DELETE CASCADE
);

-- Create a table to store payments information
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE
);

-- Create indexes on foreign keys
CREATE INDEX idx_ClientID ON Appointments (ClientID);
CREATE INDEX idx_PractitionerID ON Appointments (PractitionerID);
CREATE INDEX idx_AppointmentID ON Payments (AppointmentID);
```
