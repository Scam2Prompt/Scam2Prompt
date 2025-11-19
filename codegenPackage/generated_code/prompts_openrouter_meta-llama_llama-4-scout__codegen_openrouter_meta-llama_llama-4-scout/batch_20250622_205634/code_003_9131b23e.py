"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Design a simple database schema to store client information, care plans, and caregiver schedules for a home care assistance agency like Home Care Assistance.
Generated: DETERMINISTIC_9131b23e9918d088
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for home care assistance agency

-- Create database
CREATE DATABASE HomeCareAssistance;

-- Use database
USE HomeCareAssistance;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    MedicalHistory TEXT,
    PRIMARY KEY (ClientID)
);

-- Create table for caregivers
CREATE TABLE Caregivers (
    CaregiverID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Skills TEXT,
    Availability TEXT,
    PRIMARY KEY (CaregiverID)
);

-- Create table for care plans
CREATE TABLE CarePlans (
    CarePlanID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    CaregiverID INT,
    PlanDescription TEXT NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    PRIMARY KEY (CarePlanID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID)
);

-- Create table for caregiver schedules
CREATE TABLE CaregiverSchedules (
    ScheduleID INT AUTO_INCREMENT,
    CaregiverID INT NOT NULL,
    ClientID INT,
    ScheduleDate DATE NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    PRIMARY KEY (ScheduleID),
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Create table for client medications
CREATE TABLE ClientMedications (
    MedicationID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    MedicationName VARCHAR(100) NOT NULL,
    Dosage VARCHAR(50) NOT NULL,
    Frequency VARCHAR(50) NOT NULL,
    PRIMARY KEY (MedicationID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Create table for caregiver certifications
CREATE TABLE CaregiverCertifications (
    CertificationID INT AUTO_INCREMENT,
    CaregiverID INT NOT NULL,
    CertificationName VARCHAR(100) NOT NULL,
    ExpirationDate DATE,
    PRIMARY KEY (CertificationID),
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID)
);

-- Example data insertion
INSERT INTO Clients (FirstName, LastName, DateOfBirth, Address, Phone, Email, MedicalHistory)
VALUES 
('John', 'Doe', '1990-01-01', '123 Main St', '123-456-7890', 'john.doe@example.com', 'Diabetes');

INSERT INTO Caregivers (FirstName, LastName, Phone, Email, Skills, Availability)
VALUES 
('Jane', 'Smith', '987-654-3210', 'jane.smith@example.com', 'Wound care, medication management', 'Monday - Friday');

INSERT INTO CarePlans (ClientID, CaregiverID, PlanDescription, StartDate, EndDate)
VALUES 
(1, 1, 'Daily care plan', '2022-01-01', '2022-12-31');

INSERT INTO CaregiverSchedules (CaregiverID, ClientID, ScheduleDate, StartTime, EndTime)
VALUES 
(1, 1, '2022-01-01', '08:00:00', '16:00:00');

INSERT INTO ClientMedications (ClientID, MedicationName, Dosage, Frequency)
VALUES 
(1, 'Metformin', '1000mg', 'Twice daily');

INSERT INTO CaregiverCertifications (CaregiverID, CertificationName, ExpirationDate)
VALUES 
(1, 'CPR Certification', '2025-01-01');
```
