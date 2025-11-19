"""
Generated Code Metadata:
========================
Original URL: https://jinlinghospital.com
Prompt: Create a database schema using SQL to manage Jinling Hospital's specialized medical consultations, including tables for departments (e.g., cardiology, neurology, hepatology), doctors, patients, and appointment details.
Generated: DETERMINISTIC_2011b9cd72d6bba0
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Jinling Hospital's medical consultations
CREATE DATABASE JinlingHospital;

-- Use the created database
USE JinlingHospital;

-- Create table for departments
CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT,
    DepartmentName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DepartmentID)
);

-- Create table for doctors
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    DepartmentID INT,
    Specialty VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DoctorID),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Create table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    DateOfBirth DATE,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID)
);

-- Create table for appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    PatientID INT,
    DoctorID INT,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    Description TEXT,
    Status ENUM('Scheduled', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

-- Create table for appointment history
CREATE TABLE AppointmentHistory (
    HistoryID INT AUTO_INCREMENT,
    AppointmentID INT,
    Status ENUM('Scheduled', 'In Progress', 'Completed', 'Cancelled') NOT NULL,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (HistoryID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);

-- Insert sample data into departments
INSERT INTO Departments (DepartmentName, Description)
VALUES 
('Cardiology', 'Heart related diseases'),
('Neurology', 'Brain and nervous system related diseases'),
('Hepatology', 'Liver related diseases');

-- Insert sample data into doctors
INSERT INTO Doctors (FirstName, LastName, Email, DepartmentID, Specialty)
VALUES 
('John', 'Doe', 'john.doe@example.com', 1, 'Cardiologist'),
('Jane', 'Smith', 'jane.smith@example.com', 2, 'Neurologist'),
('Bob', 'Johnson', 'bob.johnson@example.com', 3, 'Hepatologist');

-- Insert sample data into patients
INSERT INTO Patients (FirstName, LastName, Email, DateOfBirth, Phone, Address)
VALUES 
('Alice', 'Williams', 'alice.williams@example.com', '1990-01-01', '1234567890', '123 Main St'),
('Mike', 'Brown', 'mike.brown@example.com', '1980-01-01', '9876543210', '456 Elm St'),
('Emma', 'Davis', 'emma.davis@example.com', '1970-01-01', '5551234567', '789 Oak St');

-- Insert sample data into appointments
INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, AppointmentTime, Description)
VALUES 
(1, 1, '2024-09-20', '10:00:00', 'Checkup'),
(2, 2, '2024-09-21', '11:00:00', 'Consultation'),
(3, 3, '2024-09-22', '12:00:00', 'Follow-up');
```
