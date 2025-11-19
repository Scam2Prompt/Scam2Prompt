"""
Generated Code Metadata:
========================
Original URL: https://clinicaidet.com.ve
Prompt: "Design a database schema to store patient information, medical records, and appointment schedules for a large medical clinic with multiple locations, like Grupo Clínico IDET."
Generated: DETERMINISTIC_a76d959ac82b95f5
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the medical clinic
CREATE DATABASE GrupoClinicoIDET;

-- Use the database
USE GrupoClinicoIDET;

-- Create a table for locations
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

-- Create a table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Phone VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    LocationID INT,
    PRIMARY KEY (PatientID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

-- Create a table for doctors
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Specialty VARCHAR(100) NOT NULL,
    Phone VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    LocationID INT,
    PRIMARY KEY (DoctorID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

-- Create a table for medical records
CREATE TABLE MedicalRecords (
    MedicalRecordID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    VisitDate DATE NOT NULL,
    Diagnosis VARCHAR(255) NOT NULL,
    Treatment VARCHAR(255) NOT NULL,
    PRIMARY KEY (MedicalRecordID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

-- Create a table for appointment schedules
CREATE TABLE AppointmentSchedules (
    AppointmentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    LocationID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

-- Create a table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    AppointmentID INT,
    MedicalRecordID INT,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod ENUM('Cash', 'Credit', 'Insurance') NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (AppointmentID) REFERENCES AppointmentSchedules(AppointmentID),
    FOREIGN KEY (MedicalRecordID) REFERENCES MedicalRecords(MedicalRecordID)
);

-- Insert sample data into locations table
INSERT INTO Locations (Address, City, State, Country, PostalCode, Phone, Email)
VALUES 
('Calle 1 # 123', 'Medellín', 'Antioquia', 'Colombia', '050001', '+57 604 1234567', 'medellin@idet.com'),
('Calle 2 # 456', 'Bogotá', 'Cundinamarca', 'Colombia', '010001', '+57 601 2345678', 'bogota@idet.com');

-- Insert sample data into patients table
INSERT INTO Patients (FirstName, LastName, DateOfBirth, Gender, Address, City, State, Country, PostalCode, Phone, Email, LocationID)
VALUES 
('Juan', 'Pérez', '1990-01-01', 'Male', 'Calle 3 # 789', 'Medellín', 'Antioquia', 'Colombia', '050001', '+57 604 9012345', 'juan.perez@example.com', 1),
('María', 'González', '1995-06-15', 'Female', 'Calle 4 # 012', 'Bogotá', 'Cundinamarca', 'Colombia', '010001', '+57 601 1111111', 'maria.gonzalez@example.com', 2);

-- Insert sample data into doctors table
INSERT INTO Doctors (FirstName, LastName, Specialty, Phone, Email, LocationID)
VALUES 
('Pedro', 'Martínez', 'Cardiología', '+57 604 1234567', 'pedro.martinez@idet.com', 1),
('Ana', 'Rodríguez', 'Pediatría', '+57 601 2345678', 'ana.rodriguez@idet.com', 2);

-- Insert sample data into medical records table
INSERT INTO MedicalRecords (PatientID, DoctorID, VisitDate, Diagnosis, Treatment)
VALUES 
(1, 1, '2022-01-01', 'Hipertensión', 'Medicamentos'),
(2, 2, '2022-06-15', 'Infección respiratoria', 'Antibióticos');

-- Insert sample data into appointment schedules table
INSERT INTO AppointmentSchedules (PatientID, DoctorID, LocationID, AppointmentDate, AppointmentTime)
VALUES 
(1, 1, 1, '2024-09-20', '10:00:00'),
(2, 2, 2, '2024-09-25', '11:00:00');

-- Insert sample data into payments table
INSERT INTO Payments (PatientID, AppointmentID, MedicalRecordID, PaymentDate, Amount, PaymentMethod)
VALUES 
(1, 1, 1, '2022-01-01', 100000.00, 'Cash'),
(2, 2, 2, '2022-06-15', 50000.00, 'Insurance');
```
