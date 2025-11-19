"""
Generated Code Metadata:
========================
Original URL: https://buforddental.com
Prompt: Construct a database schema for a dental clinic that includes tables for patients, services, and reviews, based on the structure used by Buford Dental.
Generated: DETERMINISTIC_bfa42843abfded17
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for dental clinic
CREATE DATABASE BufordDental;

-- Use the created database
USE BufordDental;

-- Create table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID)
);

-- Create table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create table for reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    ServiceID INT NOT NULL,
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    Review TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Create table for appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Create index on patient email for efficient lookup
CREATE UNIQUE INDEX idx_patient_email ON Patients (Email);

-- Create index on patient and service IDs in reviews table for efficient lookup
CREATE INDEX idx_review_patient_service ON Reviews (PatientID, ServiceID);

-- Create index on patient and service IDs in appointments table for efficient lookup
CREATE INDEX idx_appointment_patient_service ON Appointments (PatientID, ServiceID);
```

```sql
-- Example insert statements
INSERT INTO Patients (FirstName, LastName, DateOfBirth, Email, Phone, Address, City, State, ZipCode)
VALUES 
('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345');

INSERT INTO Services (ServiceName, Description, Price)
VALUES 
('Dental Cleaning', 'Routine dental cleaning', 99.99),
('Cavity Filling', 'Filling for cavities', 200.00);

INSERT INTO Reviews (PatientID, ServiceID, Rating, Review)
VALUES 
(1, 1, 5, 'Excellent service!'),
(1, 2, 4, 'Good experience');

INSERT INTO Appointments (PatientID, ServiceID, AppointmentDate, AppointmentTime)
VALUES 
(1, 1, '2024-09-20', '09:00:00'),
(1, 2, '2024-09-25', '10:00:00');
```
