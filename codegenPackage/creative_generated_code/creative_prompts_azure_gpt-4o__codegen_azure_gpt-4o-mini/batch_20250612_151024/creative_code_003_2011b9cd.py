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
-- Database schema creation for Jinling Hospital's specialized medical consultations

-- Creating the main database
CREATE DATABASE JinlingHospital;

-- Switching to the newly created database
USE JinlingHospital;

-- Table to store information about departments
CREATE TABLE Departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each department
    name VARCHAR(100) NOT NULL UNIQUE,             -- Name of the department
    description TEXT,                               -- Description of the department's specialties
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the department was added
);

-- Table to store information about doctors
CREATE TABLE Doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each doctor
    name VARCHAR(100) NOT NULL,                     -- Doctor's name
    specialty VARCHAR(100) NOT NULL,                -- Specialty (e.g., Cardiology, Neurology)
    department_id INT,                              -- Foreign key linking to Departments table
    contact_number VARCHAR(15),                     -- Contact number of the doctor
    email VARCHAR(100) UNIQUE,                      -- Email of the doctor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the doctor was added
    FOREIGN KEY (department_id) REFERENCES Departments(department_id) -- Foreign key constraint
);

-- Table to store information about patients
CREATE TABLE Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each patient
    name VARCHAR(100) NOT NULL,                     -- Patient's name
    date_of_birth DATE NOT NULL,                    -- Patient's date of birth
    contact_number VARCHAR(15),                     -- Contact number of the patient
    email VARCHAR(100) UNIQUE,                      -- Email of the patient
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp for when the patient was added
);

-- Table to store appointment details
CREATE TABLE Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    patient_id INT,                                  -- Foreign key linking to Patients table
    doctor_id INT,                                   -- Foreign key linking to Doctors table
    appointment_date DATETIME NOT NULL,              -- Date and time of the appointment
    status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Scheduled', -- Status of the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the appointment was scheduled
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id), -- Foreign key constraint
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)    -- Foreign key constraint
);

-- Index creation for better performance
CREATE INDEX idx_doctor_department ON Doctors(department_id);
CREATE INDEX idx_patient_appointment ON Appointments(patient_id);
CREATE INDEX idx_doctor_appointment ON Appointments(doctor_id);
```
