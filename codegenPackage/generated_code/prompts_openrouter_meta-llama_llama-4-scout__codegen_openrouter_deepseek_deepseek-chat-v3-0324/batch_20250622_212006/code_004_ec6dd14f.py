"""
Generated Code Metadata:
========================
Original URL: https://draisabelanobre.com.br
Prompt: "Generate a SQL database schema to store information about patients, procedures, and appointments for a facial harmonization clinic like Dra. Isabela Nobre's."
Generated: DETERMINISTIC_ec6dd14fe0626da0
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Facial Harmonization Clinic Database
-- Supports patient records, procedures, and appointment tracking

-- Enable strict mode for better data integrity
SET sql_mode = 'STRICT_TRANS_TABLES';

-- Create the database
CREATE DATABASE IF NOT EXISTS facial_harmonization_clinic;
USE facial_harmonization_clinic;

-- Patients table stores basic patient information
CREATE TABLE IF NOT EXISTS patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    cpf VARCHAR(14) UNIQUE COMMENT 'Brazilian CPF with formatting',
    rg VARCHAR(20) COMMENT 'Brazilian RG',
    health_insurance VARCHAR(100),
    insurance_number VARCHAR(50),
    allergies TEXT,
    medical_history TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_patient_name (last_name, first_name),
    INDEX idx_patient_cpf (cpf)
) ENGINE=InnoDB;

-- Procedures table stores available treatments
CREATE TABLE IF NOT EXISTS procedures (
    procedure_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_procedure_name (name)
) ENGINE=InnoDB;

-- Doctors table stores information about practitioners
CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_doctor_name (last_name, first_name)
) ENGINE=InnoDB;

-- Appointments table tracks patient visits
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    procedure_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No-show') DEFAULT 'Scheduled',
    notes TEXT,
    price DECIMAL(10, 2) COMMENT 'Final price including any adjustments',
    payment_status ENUM('Pending', 'Paid', 'Partial', 'Cancelled') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE,
    FOREIGN KEY (procedure_id) REFERENCES procedures(procedure_id) ON DELETE CASCADE,
    INDEX idx_appointment_date (appointment_date),
    INDEX idx_appointment_patient (patient_id),
    INDEX idx_appointment_doctor (doctor_id),
    CONSTRAINT chk_appointment_time CHECK (start_time < end_time)
) ENGINE=InnoDB;

-- Patient procedures table tracks procedures performed on patients
CREATE TABLE IF NOT EXISTS patient_procedures (
    patient_procedure_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    procedure_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_id INT COMMENT 'Optional link to appointment',
    procedure_date DATE NOT NULL,
    notes TEXT,
    before_photos TEXT COMMENT 'Comma-separated file paths',
    after_photos TEXT COMMENT 'Comma-separated file paths',
    complications TEXT,
    follow_up_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (procedure_id) REFERENCES procedures(procedure_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL,
    INDEX idx_patient_procedure_date (procedure_date)
) ENGINE=InnoDB;

-- Payments table tracks financial transactions
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT,
    patient_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('Cash', 'Credit Card', 'Debit Card', 'Bank Transfer', 'PIX', 'Other') NOT NULL,
    transaction_id VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    INDEX idx_payment_patient (patient_id),
    INDEX idx_payment_date (payment_date)
) ENGINE=InnoDB;

-- Consultation notes table for doctor's observations
CREATE TABLE IF NOT EXISTS consultation_notes (
    note_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_id INT COMMENT 'Optional link to appointment',
    note_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL,
    INDEX idx_consultation_patient (patient_id),
    INDEX idx_consultation_date (note_date)
) ENGINE=InnoDB;

-- Create a view for upcoming appointments
CREATE VIEW upcoming_appointments AS
SELECT 
    a.appointment_id,
    CONCAT(p.first_name, ' ', p.last_name) AS patient_name,
    CONCAT(d.first_name, ' ', d.last_name) AS doctor_name,
    pr.name AS procedure_name,
    a.appointment_date,
    a.start_time,
    a.end_time,
    a.status
FROM 
    appointments a
JOIN 
    patients p ON a.patient_id = p.patient_id
JOIN 
    doctors d ON a.doctor_id = d.doctor_id
JOIN 
    procedures pr ON a.procedure_id = pr.procedure_id
WHERE 
    a.appointment_date >= CURDATE()
ORDER BY 
    a.appointment_date, a.start_time;
```
