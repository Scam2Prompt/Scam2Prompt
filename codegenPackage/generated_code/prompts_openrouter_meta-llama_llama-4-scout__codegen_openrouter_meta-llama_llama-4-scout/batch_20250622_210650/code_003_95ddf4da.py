"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Design a database schema for a healthcare services company that handles patient data, billing, and medical records, taking into account the services provided by Vital Corporate Solutions.
Generated: DETERMINISTIC_95ddf4dab6d65feb
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for healthcare services
CREATE DATABASE healthcare_services;

-- Use the healthcare_services database
USE healthcare_services;

-- Create a table for patients
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (patient_id)
);

-- Create a table for medical records
CREATE TABLE medical_records (
    medical_record_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT,
    visit_date DATE NOT NULL,
    diagnosis VARCHAR(255) NOT NULL,
    treatment_plan VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (medical_record_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Create a table for doctors
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    specialty VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (doctor_id)
);

-- Create a table for services provided
CREATE TABLE services (
    service_id INT AUTO_INCREMENT,
    service_name VARCHAR(255) NOT NULL,
    service_description VARCHAR(255) NOT NULL,
    service_cost DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (service_id)
);

-- Create a table for patient services
CREATE TABLE patient_services (
    patient_service_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    service_id INT NOT NULL,
    service_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (patient_service_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- Create a table for billing
CREATE TABLE billing (
    bill_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    bill_date DATE NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL,
    payment_status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (bill_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Create a table for payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT,
    bill_id INT NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (bill_id) REFERENCES billing(bill_id)
);

-- Create a table for insurance providers
CREATE TABLE insurance_providers (
    insurance_provider_id INT AUTO_INCREMENT,
    insurance_provider_name VARCHAR(255) NOT NULL,
    insurance_provider_description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (insurance_provider_id)
);

-- Create a table for patient insurance
CREATE TABLE patient_insurance (
    patient_insurance_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    insurance_provider_id INT NOT NULL,
    policy_number VARCHAR(255) NOT NULL,
    coverage DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (patient_insurance_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (insurance_provider_id) REFERENCES insurance_providers(insurance_provider_id)
);

-- Create a stored procedure to add a new patient
DELIMITER //
CREATE PROCEDURE add_patient(
    IN p_first_name VARCHAR(255),
    IN p_last_name VARCHAR(255),
    IN p_date_of_birth DATE,
    IN p_email VARCHAR(255),
    IN p_phone_number VARCHAR(20),
    IN p_address VARCHAR(255)
)
BEGIN
    INSERT INTO patients (first_name, last_name, date_of_birth, email, phone_number, address)
    VALUES (p_first_name, p_last_name, p_date_of_birth, p_email, p_phone_number, p_address);
END//
DELIMITER ;

-- Create a stored procedure to add a new medical record
DELIMITER //
CREATE PROCEDURE add_medical_record(
    IN p_patient_id INT,
    IN p_doctor_id INT,
    IN p_visit_date DATE,
    IN p_diagnosis VARCHAR(255),
    IN p_treatment_plan VARCHAR(255)
)
BEGIN
    INSERT INTO medical_records (patient_id, doctor_id, visit_date, diagnosis, treatment_plan)
    VALUES (p_patient_id, p_doctor_id, p_visit_date, p_diagnosis, p_treatment_plan);
END//
DELIMITER ;

-- Create a stored procedure to add a new service
DELIMITER //
CREATE PROCEDURE add_service(
    IN p_service_name VARCHAR(255),
    IN p_service_description VARCHAR(255),
    IN p_service_cost DECIMAL(10, 2)
)
BEGIN
    INSERT INTO services (service_name, service_description, service_cost)
    VALUES (p_service_name, p_service_description, p_service_cost);
END//
DELIMITER ;

-- Create a stored procedure to add a new bill
DELIMITER //
CREATE PROCEDURE add_bill(
    IN p_patient_id INT,
    IN p_bill_date DATE,
    IN p_total_cost DECIMAL(10, 2)
)
BEGIN
    INSERT INTO billing (patient_id, bill_date, total_cost, payment_status)
    VALUES (p_patient_id, p_bill_date, p_total_cost, 'unpaid');
END//
DELIMITER ;

-- Create a stored procedure to make a payment
DELIMITER //
CREATE PROCEDURE make_payment(
    IN p_bill_id INT,
    IN p_payment_date DATE,
    IN p_payment_amount DECIMAL(10, 2),
    IN p_payment_method VARCHAR(20)
)
BEGIN
    INSERT INTO payments (bill_id, payment_date, payment_amount, payment_method)
    VALUES (p_bill_id, p_payment_date, p_payment_amount, p_payment_method);
    
    UPDATE billing
    SET payment_status = 'paid'
    WHERE bill_id = p_bill_id;
END//
DELIMITER ;
```
