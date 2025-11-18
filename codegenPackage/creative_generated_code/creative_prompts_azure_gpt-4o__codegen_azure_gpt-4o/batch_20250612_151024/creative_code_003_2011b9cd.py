"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jinlinghospital.com
Prompt: Create a database schema using SQL to manage Jinling Hospital's specialized medical consultations, including tables for departments (e.g., cardiology, neurology, hepatology), doctors, patients, and appointment details.
Generated: DETERMINISTIC_2011b9cd72d6bba0
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Jinling Hospital Database Schema

-- Table for storing information about hospital departments
CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the department
    Name VARCHAR(100) NOT NULL,                  -- Name of the department (e.g., Cardiology, Neurology)
    Description TEXT                             -- Optional description of the department
);

-- Table for storing doctor information
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the doctor
    FullName VARCHAR(100) NOT NULL,              -- Full name of the doctor
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Email address for contact (unique constraint)
    PhoneNumber VARCHAR(15),                     -- Optional phone number for contact
    Specialty VARCHAR(100) NOT NULL,             -- Primary area of expertise (e.g., Cardiology)
    DepartmentID INT NOT NULL,                   -- Foreign key linking doctor to a department
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) 
        ON DELETE CASCADE                        -- Deletes doctor records if the department is deleted
);

-- Table for storing patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the patient
    FullName VARCHAR(100) NOT NULL,              -- Full name of the patient
    DateOfBirth DATE NOT NULL,                   -- Date of birth for age calculations
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the patient
    Email VARCHAR(100),                          -- Optional email for contact
    PhoneNumber VARCHAR(15),                     -- Optional phone number for contact
    Address TEXT                                 -- Optional address for contact
);

-- Table for storing appointment details
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the appointment
    AppointmentDate DATETIME NOT NULL,               -- Date and time of the appointment
    ReasonForVisit TEXT,                             -- Reason for the medical consultation
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    PatientID INT NOT NULL,                          -- Foreign key linking appointment to a patient
    DoctorID INT NOT NULL,                           -- Foreign key linking appointment to a doctor
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) 
        ON DELETE CASCADE,                           -- Deletes appointment records if the patient is deleted
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) 
        ON DELETE SET NULL                           -- Sets doctor field to NULL if the doctor is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_department_name ON Departments(Name);
CREATE INDEX idx_doctor_name ON Doctors(FullName);
CREATE INDEX idx_patient_name ON Patients(FullName);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
