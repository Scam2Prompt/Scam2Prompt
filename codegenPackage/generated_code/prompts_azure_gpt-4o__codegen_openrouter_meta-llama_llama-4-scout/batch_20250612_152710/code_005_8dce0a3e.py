"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Suggest a database schema for a dental clinic management system that includes tables for patient information, services offered (e.g., dental crowns, fluoride treatments), appointment scheduling, and clinic locations.
Generated: DETERMINISTIC_8dce0a3eb10d254d
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for dental clinic management system
CREATE DATABASE DentalClinic;

-- Use the database
USE DentalClinic;

-- Create table for clinic locations
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Phone VARCHAR(20),
    Email VARCHAR(100),
    PRIMARY KEY (LocationID)
);

-- Create table for services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ServiceID)
);

-- Create table for patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Phone VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(20),
    LocationID INT,
    PRIMARY KEY (PatientID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

-- Create table for appointment scheduling
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    ServiceID INT NOT NULL,
    LocationID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

-- Create table for appointment status
CREATE TABLE AppointmentStatus (
    StatusID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Scheduled', 'Completed', 'Cancelled', 'Rescheduled')),
    UpdateDate DATE,
    UpdateTime TIME,
    PRIMARY KEY (StatusID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentAmount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(100) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);
```
