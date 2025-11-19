"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Construct a database schema for a dental clinic that supports various treatments like chirurgia orale and igiene orale, reflecting the comprehensive services provided by Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_ed19c7e7b4dab480
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the dental clinic
CREATE DATABASE StudioDentistico;

-- Use the database
USE StudioDentistico;

-- Create a table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID)
);

-- Create a table for doctors
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Specialty VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DoctorID)
);

-- Create a table for treatments
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT,
    TreatmentName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TreatmentID)
);

-- Create a table for appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

-- Create a table for patient treatments
CREATE TABLE PatientTreatments (
    PatientTreatmentID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    TreatmentID INT NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientTreatmentID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID),
    FOREIGN KEY (TreatmentID) REFERENCES Treatments(TreatmentID)
);

-- Insert some sample data
INSERT INTO Patients (FirstName, LastName, DateOfBirth, Address, Phone, Email)
VALUES 
('John', 'Doe', '1990-01-01', 'Via Milano 1', '1234567890', 'john.doe@example.com'),
('Jane', 'Doe', '1995-06-01', 'Via Roma 2', '9876543210', 'jane.doe@example.com');

INSERT INTO Doctors (FirstName, LastName, Specialty, Phone, Email)
VALUES 
('Vira', 'Palazzo', 'Chirurgia Orale', '1111111111', 'vira.palazzo@example.com'),
('Luca', 'Bianchi', 'Igiene Orale', '2222222222', 'luca.bianchi@example.com');

INSERT INTO Treatments (TreatmentName, Description, Price)
VALUES 
('Chirurgia Orale', 'Interventi di chirurgia orale', 200.00),
('Igiene Orale', 'Pulizia e igiene dei denti', 100.00);

INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, AppointmentTime)
VALUES 
(1, 1, '2024-09-16', '10:00:00'),
(2, 2, '2024-09-17', '11:00:00');

INSERT INTO PatientTreatments (AppointmentID, TreatmentID, Description)
VALUES 
(1, 1, 'Intervento di chirurgia orale per estrazione dente'),
(2, 2, 'Pulizia e igiene dei denti');
```
