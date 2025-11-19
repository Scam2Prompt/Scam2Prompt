"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Describe how to create a database schema for managing health records in a SUS-based healthcare system, including tables for patients, health professionals, and services.
Generated: DETERMINISTIC_79540de79ff6728e
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for managing health records
CREATE DATABASE healthcare_system;

-- Use the created database
USE healthcare_system;

-- Create a table for patients
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('M', 'F', 'O') NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (patient_id)
);

-- Create a table for health professionals
CREATE TABLE health_professionals (
    professional_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    role ENUM('MEDIC', 'NURSE', 'TECHNICIAN') NOT NULL,
    crm VARCHAR(20) UNIQUE NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (professional_id)
);

-- Create a table for services
CREATE TABLE services (
    service_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (service_id)
);

-- Create a table for patient services
CREATE TABLE patient_services (
    patient_service_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    service_id INT NOT NULL,
    professional_id INT NOT NULL,
    service_date DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (patient_service_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    FOREIGN KEY (professional_id) REFERENCES health_professionals(professional_id)
);

-- Create a table for patient health records
CREATE TABLE patient_health_records (
    record_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    professional_id INT NOT NULL,
    record_date DATE NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (record_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (professional_id) REFERENCES health_professionals(professional_id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_patient_services_patient_id ON patient_services(patient_id);
CREATE INDEX idx_patient_services_service_id ON patient_services(service_id);
CREATE INDEX idx_patient_services_professional_id ON patient_services(professional_id);

CREATE INDEX idx_patient_health_records_patient_id ON patient_health_records(patient_id);
CREATE INDEX idx_patient_health_records_professional_id ON patient_health_records(professional_id);

-- Insert some sample data
INSERT INTO patients (name, date_of_birth, gender, address, phone_number)
VALUES 
('John Doe', '1990-01-01', 'M', 'Rua ABC, 123', '1234567890'),
('Jane Doe', '1995-06-15', 'F', 'Avenida DEF, 456', '9876543210');

INSERT INTO health_professionals (name, role, crm, address, phone_number)
VALUES 
('Dr. Smith', 'MEDIC', '123456', 'Rua GHI, 789', '5555555555'),
('Nurse Johnson', 'NURSE', '789012', 'Avenida JKL, 321', '4444444444');

INSERT INTO services (name, description, price)
VALUES 
('Consultation', 'Medical consultation', 100.00),
('Exam', 'Medical exam', 200.00);

INSERT INTO patient_services (patient_id, service_id, professional_id, service_date, description)
VALUES 
(1, 1, 1, '2022-01-01', 'Initial consultation'),
(2, 2, 2, '2022-06-15', 'Medical exam');

INSERT INTO patient_health_records (patient_id, professional_id, record_date, description)
VALUES 
(1, 1, '2022-01-01', 'Patient has a fever'),
(2, 2, '2022-06-15', 'Patient is healthy');
```
