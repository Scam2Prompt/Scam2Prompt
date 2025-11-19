"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Suggest a database schema for a dental clinic management system that includes tables for patient information, services offered (e.g., dental crowns, fluoride treatments), appointment scheduling, and clinic locations.
Generated: DETERMINISTIC_8dce0a3eb10d254d
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Dental Clinic Management System

-- Patients table to store patient information
CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    insurance_provider VARCHAR(100),
    insurance_policy_number VARCHAR(50),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_visit_date DATETIME,
    medical_history TEXT,
    allergies TEXT,
    CONSTRAINT unique_email UNIQUE (email)
);

-- Clinic locations table
CREATE TABLE clinic_locations (
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    location_name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    operating_hours TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Dentists/Staff table
CREATE TABLE dentists (
    dentist_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    location_id INT,
    CONSTRAINT fk_dentist_location FOREIGN KEY (location_id) 
        REFERENCES clinic_locations(location_id) ON DELETE SET NULL,
    CONSTRAINT unique_dentist_email UNIQUE (email)
);

-- Dental services table
CREATE TABLE services (
    service_id INT PRIMARY KEY AUTO_INCREMENT,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INT NOT NULL,
    base_cost DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    category ENUM('Preventive', 'Restorative', 'Cosmetic', 'Orthodontic', 'Periodontal', 'Endodontic', 'Prosthodontic') NOT NULL
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    dentist_id INT NOT NULL,
    location_id INT NOT NULL,
    service_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No-Show') DEFAULT 'Scheduled',
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_appointment_patient FOREIGN KEY (patient_id) 
        REFERENCES patients(patient_id) ON DELETE CASCADE,
    CONSTRAINT fk_appointment_dentist FOREIGN KEY (dentist_id) 
        REFERENCES dentists(dentist_id) ON DELETE CASCADE,
    CONSTRAINT fk_appointment_location FOREIGN KEY (location_id) 
        REFERENCES clinic_locations(location_id) ON DELETE CASCADE,
    CONSTRAINT fk_appointment_service FOREIGN KEY (service_id) 
        REFERENCES services(service_id) ON DELETE CASCADE
);

-- Treatment records table
CREATE TABLE treatments (
    treatment_id INT PRIMARY KEY AUTO_INCREMENT,
    appointment_id INT NOT NULL,
    service_id INT NOT NULL,
    teeth_involved VARCHAR(50),
    notes TEXT,
    cost DECIMAL(10, 2) NOT NULL,
    payment_status ENUM('Pending', 'Partial', 'Paid') DEFAULT 'Pending',
    treatment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_treatment_appointment FOREIGN KEY (appointment_id) 
        REFERENCES appointments(appointment_id) ON DELETE CASCADE,
    CONSTRAINT fk_treatment_service FOREIGN KEY (service_id) 
        REFERENCES services(service_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    treatment_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Cash', 'Credit Card', 'Debit Card', 'Insurance', 'Check') NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    transaction_reference VARCHAR(100),
    notes TEXT,
    CONSTRAINT fk_payment_treatment FOREIGN KEY (treatment_id) 
        REFERENCES treatments(treatment_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_patient_name ON patients(last_name, first_name);
CREATE INDEX idx_appointment_date ON appointments(appointment_date, start_time);
CREATE INDEX idx_dentist_name ON dentists(last_name, first_name);
CREATE INDEX idx_service_name ON services(service_name);
```
