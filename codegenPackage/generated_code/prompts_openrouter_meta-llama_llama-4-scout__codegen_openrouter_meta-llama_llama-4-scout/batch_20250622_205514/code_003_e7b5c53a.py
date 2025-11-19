"""
Generated Code Metadata:
========================
Original URL: https://payidarsaglik.com
Prompt: Design a database schema to store patient information, medical records, and home healthcare services provided by a company like Payidar Evde Sağlık Hizmetleri.
Generated: DETERMINISTIC_e7b5c53aea9a3036
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- database_schema.sql

-- Create database
CREATE DATABASE Payidar_Evde_Saglik_Hizmetleri;

-- Use database
USE Payidar_Evde_Saglik_Hizmetleri;

-- Create table for patients
CREATE TABLE Patients (
  PatientID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  DateOfBirth DATE NOT NULL,
  Gender ENUM('Male', 'Female', 'Other') NOT NULL,
  Address VARCHAR(255) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Email VARCHAR(100) UNIQUE,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (PatientID)
);

-- Create table for medical records
CREATE TABLE MedicalRecords (
  MedicalRecordID INT AUTO_INCREMENT,
  PatientID INT NOT NULL,
  MedicalHistory TEXT,
  Allergies TEXT,
  CurrentMedications TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (MedicalRecordID),
  FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Create table for healthcare services
CREATE TABLE HealthcareServices (
  ServiceID INT AUTO_INCREMENT,
  ServiceName VARCHAR(255) NOT NULL,
  ServiceDescription TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ServiceID)
);

-- Create table for healthcare service providers
CREATE TABLE HealthcareProviders (
  ProviderID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Specialty VARCHAR(255) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Email VARCHAR(100) UNIQUE,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ProviderID)
);

-- Create table for patient healthcare services
CREATE TABLE PatientHealthcareServices (
  PatientServiceID INT AUTO_INCREMENT,
  PatientID INT NOT NULL,
  ServiceID INT NOT NULL,
  ProviderID INT NOT NULL,
  ServiceDate DATE NOT NULL,
  ServiceTime TIME NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (PatientServiceID),
  FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
  FOREIGN KEY (ServiceID) REFERENCES HealthcareServices(ServiceID) ON DELETE CASCADE,
  FOREIGN KEY (ProviderID) REFERENCES HealthcareProviders(ProviderID) ON DELETE CASCADE
);

-- Create table for service visits
CREATE TABLE ServiceVisits (
  VisitID INT AUTO_INCREMENT,
  PatientServiceID INT NOT NULL,
  VisitDate DATE NOT NULL,
  VisitTime TIME NOT NULL,
  VisitNotes TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (VisitID),
  FOREIGN KEY (PatientServiceID) REFERENCES PatientHealthcareServices(PatientServiceID) ON DELETE CASCADE
);

-- Create indexes
CREATE INDEX idx_Patients_LastName ON Patients (LastName);
CREATE INDEX idx_Patients_Phone ON Patients (Phone);
CREATE INDEX idx_MedicalRecords_PatientID ON MedicalRecords (PatientID);
CREATE INDEX idx_PatientHealthcareServices_PatientID ON PatientHealthcareServices (PatientID);
CREATE INDEX idx_PatientHealthcareServices_ServiceID ON PatientHealthcareServices (ServiceID);
CREATE INDEX idx_ServiceVisits_PatientServiceID ON ServiceVisits (PatientServiceID);
```

```sql
-- sample_data.sql

-- Insert sample data into Patients table
INSERT INTO Patients (FirstName, LastName, DateOfBirth, Gender, Address, Phone, Email)
VALUES 
('John', 'Doe', '1990-01-01', 'Male', '123 Main St', '123-456-7890', 'john.doe@example.com'),
('Jane', 'Doe', '1995-06-01', 'Female', '456 Elm St', '987-654-3210', 'jane.doe@example.com');

-- Insert sample data into MedicalRecords table
INSERT INTO MedicalRecords (PatientID, MedicalHistory, Allergies, CurrentMedications)
VALUES 
(1, 'Hypertension', 'Penicillin', 'Lisinopril'),
(2, 'Diabetes', 'None', 'Metformin');

-- Insert sample data into HealthcareServices table
INSERT INTO HealthcareServices (ServiceName, ServiceDescription)
VALUES 
('Nursing Care', 'Skilled nursing care provided in the home'),
('Physical Therapy', 'Physical therapy services provided in the home');

-- Insert sample data into HealthcareProviders table
INSERT INTO HealthcareProviders (FirstName, LastName, Specialty, Phone, Email)
VALUES 
('Bob', 'Smith', 'Nurse', '555-123-4567', 'bob.smith@example.com'),
('Alice', 'Johnson', 'Physical Therapist', '555-987-6543', 'alice.johnson@example.com');

-- Insert sample data into PatientHealthcareServices table
INSERT INTO PatientHealthcareServices (PatientID, ServiceID, ProviderID, ServiceDate, ServiceTime)
VALUES 
(1, 1, 1, '2022-01-01', '09:00:00'),
(2, 2, 2, '2022-06-01', '10:00:00');

-- Insert sample data into ServiceVisits table
INSERT INTO ServiceVisits (PatientServiceID, VisitDate, VisitTime, VisitNotes)
VALUES 
(1, '2022-01-01', '09:00:00', 'Patient received nursing care'),
(2, '2022-06-01', '10:00:00', 'Patient received physical therapy');
```
