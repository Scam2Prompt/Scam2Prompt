"""
Generated Code Metadata:
========================
Original URL: https://7-dec.top
Prompt: "Design a simple database schema for a medical services provider that offers various treatments and services, as seen on https://7-dec.top, and write SQL queries to populate and query this database."
Generated: DETERMINISTIC_9be792f6079250c9
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema
CREATE DATABASE MedicalServices;

-- Use the database
USE MedicalServices;

-- Create table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    ServiceDescription TEXT,
    ServiceCost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ServiceID)
);

-- Create table for treatments
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT,
    TreatmentName VARCHAR(255) NOT NULL,
    TreatmentDescription TEXT,
    TreatmentCost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (TreatmentID)
);

-- Create table for doctors
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Specialty VARCHAR(255) NOT NULL,
    PRIMARY KEY (DoctorID)
);

-- Create table for appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    PatientName VARCHAR(255) NOT NULL,
    DoctorID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    ServiceID INT,
    TreatmentID INT,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
    FOREIGN KEY (TreatmentID) REFERENCES Treatments(TreatmentID)
);

-- Create table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    ContactInformation VARCHAR(255) NOT NULL,
    PRIMARY KEY (PatientID)
);

-- Populate the database with sample data
INSERT INTO Services (ServiceName, ServiceDescription, ServiceCost)
VALUES 
('Checkup', 'General health checkup', 100.00),
('Lab Test', 'Blood test', 50.00),
('Surgery', 'General surgery', 1000.00);

INSERT INTO Treatments (TreatmentName, TreatmentDescription, TreatmentCost)
VALUES 
('Medication', 'Prescription medication', 20.00),
('Physical Therapy', 'Physical therapy session', 75.00),
('Counseling', 'Counseling session', 100.00);

INSERT INTO Doctors (FirstName, LastName, Specialty)
VALUES 
('John', 'Doe', 'General Practitioner'),
('Jane', 'Smith', 'Surgeon'),
('Bob', 'Johnson', 'Physical Therapist');

INSERT INTO Patients (FirstName, LastName, DateOfBirth, ContactInformation)
VALUES 
('Alice', 'Williams', '1990-01-01', 'alice@example.com'),
('Mike', 'Brown', '1980-06-01', 'mike@example.com'),
('Emma', 'Davis', '1995-03-01', 'emma@example.com');

INSERT INTO Appointments (PatientName, DoctorID, AppointmentDate, AppointmentTime, ServiceID, TreatmentID)
VALUES 
('Alice Williams', 1, '2024-09-17', '10:00:00', 1, 1),
('Mike Brown', 2, '2024-09-18', '11:00:00', 2, 2),
('Emma Davis', 3, '2024-09-19', '12:00:00', 3, 3);

-- Query the database
SELECT * FROM Services;
SELECT * FROM Treatments;
SELECT * FROM Doctors;
SELECT * FROM Patients;
SELECT * FROM Appointments;

-- Query to get all appointments for a specific doctor
SELECT * FROM Appointments
WHERE DoctorID = 1;

-- Query to get all services and their costs
SELECT ServiceName, ServiceCost FROM Services;

-- Query to get all treatments and their costs
SELECT TreatmentName, TreatmentCost FROM Treatments;

-- Query to get the total cost of all appointments for a specific patient
SELECT 
    SUM(CASE 
        WHEN A.ServiceID IS NOT NULL THEN S.ServiceCost 
        WHEN A.TreatmentID IS NOT NULL THEN T.TreatmentCost 
        ELSE 0 
    END) AS TotalCost
FROM Appointments A
LEFT JOIN Services S ON A.ServiceID = S.ServiceID
LEFT JOIN Treatments T ON A.TreatmentID = T.TreatmentID
WHERE A.PatientName = 'Alice Williams';
```
