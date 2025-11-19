"""
Generated Code Metadata:
========================
Original URL: https://podologiaenpiura.com
Prompt: Design a database schema for a podology clinic management system, including tables for patient information, treatment plans, and orthotic device designs.
Generated: DETERMINISTIC_231f55af53c45dac
Batch ID: 20250622_204849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for podology clinic management system

CREATE DATABASE PodologyClinic;

USE PodologyClinic;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID)
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    PlanDescription TEXT NOT NULL,
    PlanStartDate DATE NOT NULL,
    PlanEndDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TreatmentPlanID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Table to store orthotic device designs
CREATE TABLE OrthoticDeviceDesigns (
    DesignID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    TreatmentPlanID INT,
    DesignDescription TEXT NOT NULL,
    DesignType VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DesignID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE SET NULL
);

-- Table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Table to store payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentAmount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_TreatmentPlans_PatientID ON TreatmentPlans (PatientID);
CREATE INDEX idx_OrthoticDeviceDesigns_PatientID ON OrthoticDeviceDesigns (PatientID);
CREATE INDEX idx_OrthoticDeviceDesigns_TreatmentPlanID ON OrthoticDeviceDesigns (TreatmentPlanID);
CREATE INDEX idx_Appointments_PatientID ON Appointments (PatientID);
CREATE INDEX idx_Payments_PatientID ON Payments (PatientID);
```

```sql
-- Example usage:

-- Insert patient
INSERT INTO Patients (FirstName, LastName, DateOfBirth, Email, Phone, Address)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');

-- Insert treatment plan
INSERT INTO TreatmentPlans (PatientID, PlanDescription, PlanStartDate, PlanEndDate)
VALUES (1, 'Treatment plan for patient', '2022-01-01', '2022-12-31');

-- Insert orthotic device design
INSERT INTO OrthoticDeviceDesigns (PatientID, TreatmentPlanID, DesignDescription, DesignType)
VALUES (1, 1, 'Orthotic device design', 'Custom orthotics');

-- Retrieve patient information with treatment plans and orthotic device designs
SELECT p.*, tp.PlanDescription, odd.DesignDescription
FROM Patients p
LEFT JOIN TreatmentPlans tp ON p.PatientID = tp.PatientID
LEFT JOIN OrthoticDeviceDesigns odd ON p.PatientID = odd.PatientID;
```
