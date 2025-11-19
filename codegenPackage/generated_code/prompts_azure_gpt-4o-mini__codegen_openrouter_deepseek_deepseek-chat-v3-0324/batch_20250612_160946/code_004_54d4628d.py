"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Design a database schema in SQL to manage the records of beneficiaries receiving support from the Rakhshanda Memorial's medical camps and psychological health services.
Generated: DETERMINISTIC_54d4628dca4aeffc
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Rakhshanda Memorial's beneficiary management system

-- Create the database
CREATE DATABASE IF NOT EXISTS rakhshanda_memorial;
USE rakhshanda_memorial;

-- Beneficiary table to store personal information
CREATE TABLE IF NOT EXISTS beneficiaries (
    beneficiary_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other', 'Prefer not to say') NOT NULL,
    phone_number VARCHAR(15),
    email VARCHAR(100),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50) DEFAULT 'Pakistan',
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%' OR email IS NULL),
    CONSTRAINT chk_phone CHECK (phone_number REGEXP '^[0-9]+$' OR phone_number IS NULL)
);

-- Medical camps table
CREATE TABLE IF NOT EXISTS medical_camps (
    camp_id INT AUTO_INCREMENT PRIMARY KEY,
    camp_name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    description TEXT,
    organizer VARCHAR(100),
    status ENUM('Planned', 'Ongoing', 'Completed', 'Cancelled') DEFAULT 'Planned',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_dates CHECK (end_date >= start_date)
);

-- Services provided table
CREATE TABLE IF NOT EXISTS services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    service_type ENUM('Medical', 'Psychological', 'Other') NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- Beneficiary attendance at camps
CREATE TABLE IF NOT EXISTS camp_attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    beneficiary_id INT NOT NULL,
    camp_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE,
    FOREIGN KEY (camp_id) REFERENCES medical_camps(camp_id) ON DELETE CASCADE,
    UNIQUE KEY unique_attendance (beneficiary_id, camp_id, attendance_date)
);

-- Services provided to beneficiaries
CREATE TABLE IF NOT EXISTS beneficiary_services (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    beneficiary_id INT NOT NULL,
    service_id INT NOT NULL,
    camp_id INT,
    service_date DATE NOT NULL,
    provider_name VARCHAR(100),
    diagnosis TEXT,
    treatment TEXT,
    follow_up_required BOOLEAN DEFAULT FALSE,
    follow_up_date DATE,
    notes TEXT,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    FOREIGN KEY (camp_id) REFERENCES medical_camps(camp_id) ON DELETE SET NULL
);

-- Psychological health assessments
CREATE TABLE IF NOT EXISTS psychological_assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    beneficiary_id INT NOT NULL,
    assessment_date DATE NOT NULL,
    psychologist_name VARCHAR(100) NOT NULL,
    assessment_type VARCHAR(100) NOT NULL,
    findings TEXT,
    recommendations TEXT,
    follow_up_required BOOLEAN DEFAULT FALSE,
    follow_up_date DATE,
    notes TEXT,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE
);

-- Medications prescribed
CREATE TABLE IF NOT EXISTS prescriptions (
    prescription_id INT AUTO_INCREMENT PRIMARY KEY,
    beneficiary_id INT NOT NULL,
    service_record_id INT,
    medication_name VARCHAR(100) NOT NULL,
    dosage VARCHAR(50) NOT NULL,
    frequency VARCHAR(50) NOT NULL,
    duration VARCHAR(50) NOT NULL,
    prescribed_by VARCHAR(100) NOT NULL,
    prescription_date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE CASCADE,
    FOREIGN KEY (service_record_id) REFERENCES beneficiary_services(record_id) ON DELETE SET NULL
);

-- User accounts for system access
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role ENUM('Admin', 'Doctor', 'Psychologist', 'Staff', 'Volunteer') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    last_login DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_user_email CHECK (email LIKE '%@%.%')
);

-- Audit log for tracking changes
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT,
    old_values TEXT,
    new_values TEXT,
    action_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- Create indexes for performance
CREATE INDEX idx_beneficiary_name ON beneficiaries(last_name, first_name);
CREATE INDEX idx_beneficiary_contact ON beneficiaries(phone_number, email);
CREATE INDEX idx_camp_dates ON medical_camps(start_date, end_date);
CREATE INDEX idx_service_type ON services(service_type);
CREATE INDEX idx_service_date ON beneficiary_services(service_date);
CREATE INDEX idx_assessment_date ON psychological_assessments(assessment_date);
```
