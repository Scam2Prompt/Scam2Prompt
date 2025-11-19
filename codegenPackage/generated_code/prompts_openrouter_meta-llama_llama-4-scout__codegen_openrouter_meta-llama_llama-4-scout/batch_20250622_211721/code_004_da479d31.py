"""
Generated Code Metadata:
========================
Original URL: https://smart-medicalservices.com
Prompt: Design a database schema for a medical services company like Smart Medical Services, including tables for patients, services, appointments, and healthcare providers.
Generated: DETERMINISTIC_da479d314ca2472b
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Smart Medical Services
CREATE DATABASE SmartMedicalServices;

-- Use the database
USE SmartMedicalServices;

-- Create a table for healthcare providers
CREATE TABLE HealthcareProviders (
    ProviderID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Specialty VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProviderID)
);

-- Create a table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    DateOfBirth DATE,
    MedicalHistory TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID)
);

-- Create a table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    Cost DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create a table for appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    ProviderID INT NOT NULL,
    ServiceID INT,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    Status VARCHAR(50) NOT NULL DEFAULT 'Scheduled',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (ProviderID) REFERENCES HealthcareProviders(ProviderID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE SET NULL
);

-- Create a table for appointment reminders
CREATE TABLE AppointmentReminders (
    ReminderID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    ReminderDate DATE NOT NULL,
    ReminderTime TIME NOT NULL,
    Sent BOOLEAN NOT NULL DEFAULT FALSE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReminderID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE
);

-- Create a table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_appointments_patient_id ON Appointments (PatientID);
CREATE INDEX idx_appointments_provider_id ON Appointments (ProviderID);
CREATE INDEX idx_appointments_service_id ON Appointments (ServiceID);
CREATE INDEX idx_appointment_reminders_appointment_id ON AppointmentReminders (AppointmentID);
CREATE INDEX idx_payments_appointment_id ON Payments (AppointmentID);
```
