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
-- Create a database for the gastroenterology clinic
CREATE DATABASE gastroenterology_clinic;

-- Use the created database
USE gastroenterology_clinic;

-- Create a table to store patients
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (patient_id)
);

-- Create a table to store doctors
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    specialty VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (doctor_id)
);

-- Create a table to store appointment schedules
CREATE TABLE appointment_schedules (
    appointment_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    service_type ENUM('endocrinologia', 'motilidade digestiva', 'proctologia') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (appointment_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

-- Create a table to store medical records
CREATE TABLE medical_records (
    record_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_id INT,
    diagnosis TEXT,
    treatment TEXT,
    medication TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (record_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
    FOREIGN KEY (appointment_id) REFERENCES appointment_schedules(appointment_id)
);

-- Create a table to store services offered
CREATE TABLE services (
    service_id INT AUTO_INCREMENT,
    service_name VARCHAR(255) NOT NULL,
    service_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (service_id)
);

-- Insert services offered by the clinic
INSERT INTO services (service_name, service_description) 
VALUES 
('endocrinologia', 'Endocrinology services'),
('motilidade digestiva', 'Digestive motility services'),
('proctologia', 'Proctology services');

-- Create a table to store patient allergies
CREATE TABLE patient_allergies (
    allergy_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    allergy_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (allergy_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Create a table to store patient medications
CREATE TABLE patient_medications (
    medication_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    medication_name VARCHAR(255) NOT NULL,
    dosage VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (medication_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
```
