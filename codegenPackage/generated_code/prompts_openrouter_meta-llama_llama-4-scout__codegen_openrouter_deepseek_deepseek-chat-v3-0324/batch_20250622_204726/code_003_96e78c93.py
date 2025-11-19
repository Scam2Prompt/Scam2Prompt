"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Develop a basic SQL database schema to store patient data, appointment schedules, and medical records for a gastroenterology clinic that offers services such as endocrinologia, motilidade digestiva, and proctologia.
Generated: DETERMINISTIC_96e78c93bc4e5fc3
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a gastroenterology clinic management system

-- Create database
CREATE DATABASE GastroenterologyClinic;
USE GastroenterologyClinic;

-- Patients table
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    insurance_provider VARCHAR(50),
    insurance_number VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%' OR email IS NULL)
);

-- Doctors table
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization ENUM('Endocrinologia', 'Motilidade Digestiva', 'Proctologia', 'Gastroenterologia Geral') NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_doctor_email CHECK (email LIKE '%@%.%')
);

-- Appointments table
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    service_type ENUM('Consultation', 'Endoscopy', 'Colonoscopy', 'Motility Study', 'Other Procedure') NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No Show') DEFAULT 'Scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id) ON DELETE CASCADE,
    CONSTRAINT unique_appointment UNIQUE (doctor_id, appointment_date, appointment_time)
);

-- Medical records table
CREATE TABLE MedicalRecords (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    visit_date DATE NOT NULL,
    diagnosis TEXT,
    treatment TEXT,
    prescription TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id) ON DELETE CASCADE
);

-- Procedures table
CREATE TABLE Procedures (
    procedure_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INT NOT NULL,
    category ENUM('Endocrinologia', 'Motilidade Digestiva', 'Proctologia') NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Appointment procedures junction table
CREATE TABLE AppointmentProcedures (
    appointment_id INT NOT NULL,
    procedure_id INT NOT NULL,
    notes TEXT,
    PRIMARY KEY (appointment_id, procedure_id),
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id) ON DELETE CASCADE,
    FOREIGN KEY (procedure_id) REFERENCES Procedures(procedure_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_patient_name ON Patients(last_name, first_name);
CREATE INDEX idx_doctor_specialization ON Doctors(specialization);
CREATE INDEX idx_appointment_date ON Appointments(appointment_date);
CREATE INDEX idx_medical_record_patient ON MedicalRecords(patient_id);
```
