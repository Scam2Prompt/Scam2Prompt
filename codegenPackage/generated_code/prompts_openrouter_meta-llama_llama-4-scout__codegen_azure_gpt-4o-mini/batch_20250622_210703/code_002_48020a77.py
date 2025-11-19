"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: "Generate a construction plan for a healthcare center using SQL and database management principles."
Generated: DETERMINISTIC_48020a77fe5b2e45
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for a Healthcare Center

-- Drop existing database if it exists
DROP DATABASE IF EXISTS HealthcareCenter;

-- Create a new database for the healthcare center
CREATE DATABASE HealthcareCenter;

-- Use the newly created database
USE HealthcareCenter;

-- Create a table for storing information about patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                   -- Patient's phone number
    Email VARCHAR(100),                        -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table for storing information about healthcare providers
CREATE TABLE Providers (
    ProviderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each provider
    FirstName VARCHAR(50) NOT NULL,            -- Provider's first name
    LastName VARCHAR(50) NOT NULL,             -- Provider's last name
    Specialty VARCHAR(100) NOT NULL,           -- Provider's specialty
    PhoneNumber VARCHAR(15),                    -- Provider's phone number
    Email VARCHAR(100),                         -- Provider's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table for storing appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients
    ProviderID INT NOT NULL,                      -- Foreign key referencing Providers
    AppointmentDate DATETIME NOT NULL,           -- Date and time of the appointment
    Reason VARCHAR(255),                          -- Reason for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ProviderID) REFERENCES Providers(ProviderID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for storing medical records
CREATE TABLE MedicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each medical record
    PatientID INT NOT NULL,                      -- Foreign key referencing Patients
    ProviderID INT NOT NULL,                     -- Foreign key referencing Providers
    RecordDate DATE NOT NULL,                    -- Date of the medical record
    Diagnosis VARCHAR(255),                      -- Diagnosis information
    Treatment VARCHAR(255),                      -- Treatment information
    Notes TEXT,                                  -- Additional notes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ProviderID) REFERENCES Providers(ProviderID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for storing billing information
CREATE TABLE Billing (
    BillID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each bill
    PatientID INT NOT NULL,                      -- Foreign key referencing Patients
    Amount DECIMAL(10, 2) NOT NULL,             -- Amount to be billed
    BillDate DATE NOT NULL,                      -- Date of the bill
    Status ENUM('Paid', 'Unpaid', 'Pending') DEFAULT 'Unpaid', -- Billing status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Insert sample data into Patients table
INSERT INTO Patients (FirstName, LastName, DateOfBirth, Gender, PhoneNumber, Email)
VALUES 
('John', 'Doe', '1980-01-01', 'Male', '123-456-7890', 'john.doe@example.com'),
('Jane', 'Smith', '1990-02-02', 'Female', '098-765-4321', 'jane.smith@example.com');

-- Insert sample data into Providers table
INSERT INTO Providers (FirstName, LastName, Specialty, PhoneNumber, Email)
VALUES 
('Dr. Alice', 'Johnson', 'Cardiology', '555-123-4567', 'alice.johnson@healthcare.com'),
('Dr. Bob', 'Williams', 'Pediatrics', '555-987-6543', 'bob.williams@healthcare.com');

-- Insert sample data into Appointments table
INSERT INTO Appointments (PatientID, ProviderID, AppointmentDate, Reason)
VALUES 
(1, 1, '2023-10-15 10:00:00', 'Routine Checkup'),
(2, 2, '2023-10-16 11:00:00', 'Vaccination');

-- Insert sample data into MedicalRecords table
INSERT INTO MedicalRecords (PatientID, ProviderID, RecordDate, Diagnosis, Treatment, Notes)
VALUES 
(1, 1, '2023-10-15', 'Hypertension', 'Lifestyle changes', 'Follow up in 3 months.'),
(2, 2, '2023-10-16', 'Routine Vaccination', 'Administered vaccine', 'No adverse reactions.');

-- Insert sample data into Billing table
INSERT INTO Billing (PatientID, Amount, BillDate, Status)
VALUES 
(1, 150.00, '2023-10-15', 'Unpaid'),
(2, 75.00, '2023-10-16', 'Paid');

-- Query to retrieve all appointments for a specific patient
SELECT 
    a.AppointmentID, 
    p.FirstName AS PatientFirstName, 
    p.LastName AS PatientLastName, 
    pr.FirstName AS ProviderFirstName, 
    pr.LastName AS ProviderLastName, 
    a.AppointmentDate, 
    a.Reason, 
    a.Status
FROM 
    Appointments a
JOIN 
    Patients p ON a.PatientID = p.PatientID
JOIN 
    Providers pr ON a.ProviderID = pr.ProviderID
WHERE 
    p.PatientID = 1; -- Change this ID to query for different patients

-- Note: Ensure to handle any potential errors during data insertion and querying in your application logic.
```
