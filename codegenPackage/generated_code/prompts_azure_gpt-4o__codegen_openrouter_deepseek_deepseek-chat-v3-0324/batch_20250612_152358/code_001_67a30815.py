"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Develop a database schema in SQL for managing patient records in a system modeled after SUS, including fields for patient demographics, health history, assigned healthcare team, and referral details for specialized care.
Generated: DETERMINISTIC_67a3081599dd82fc
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SUS-like patient records management system

-- Create the database
CREATE DATABASE IF NOT EXISTS patient_management_system;
USE patient_management_system;

-- Patients table (core demographic information)
CREATE TABLE IF NOT EXISTS patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    national_id VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other', 'Unknown') NOT NULL,
    marital_status ENUM('Single', 'Married', 'Divorced', 'Widowed', 'Other') NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(100),
    address_street VARCHAR(100),
    address_city VARCHAR(50),
    address_state VARCHAR(50),
    address_postal_code VARCHAR(20),
    address_country VARCHAR(50) DEFAULT 'Brazil',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name),
    INDEX (national_id)
) ENGINE=InnoDB;

-- Emergency contacts
CREATE TABLE IF NOT EXISTS emergency_contacts (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    relationship VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    INDEX (patient_id)
) ENGINE=InnoDB;

-- Health insurance information
CREATE TABLE IF NOT EXISTS health_insurance (
    insurance_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    provider_name VARCHAR(100) NOT NULL,
    policy_number VARCHAR(50) NOT NULL,
    coverage_start_date DATE NOT NULL,
    coverage_end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    INDEX (patient_id)
) ENGINE=InnoDB;

-- Medical history
CREATE TABLE IF NOT EXISTS medical_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    condition_name VARCHAR(100) NOT NULL,
    diagnosis_date DATE,
    status ENUM('Active', 'Resolved', 'Chronic', 'Other') NOT NULL,
    severity ENUM('Mild', 'Moderate', 'Severe') NOT NULL,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    INDEX (patient_id)
) ENGINE=InnoDB;

-- Allergies
CREATE TABLE IF NOT EXISTS allergies (
    allergy_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    allergen VARCHAR(100) NOT NULL,
    reaction VARCHAR(100) NOT NULL,
    severity ENUM('Mild', 'Moderate', 'Severe', 'Life-threatening') NOT NULL,
    first_observed DATE,
    last_observed DATE,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    INDEX (patient_id)
) ENGINE=InnoDB;

-- Medications
CREATE TABLE IF NOT EXISTS medications (
    medication_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    dosage VARCHAR(50) NOT NULL,
    frequency VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    prescribing_doctor VARCHAR(100),
    reason TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    INDEX (patient_id)
) ENGINE=InnoDB;

-- Healthcare professionals
CREATE TABLE IF NOT EXISTS healthcare_professionals (
    professional_id INT AUTO_INCREMENT PRIMARY KEY,
    license_number VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialty VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    INDEX (last_name, first_name),
    INDEX (license_number)
) ENGINE=InnoDB;

-- Healthcare teams
CREATE TABLE IF NOT EXISTS healthcare_teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    INDEX (team_name)
) ENGINE=InnoDB;

-- Team members (junction table)
CREATE TABLE IF NOT EXISTS team_members (
    team_id INT NOT NULL,
    professional_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    PRIMARY KEY (team_id, professional_id),
    FOREIGN KEY (team_id) REFERENCES healthcare_teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (professional_id) REFERENCES healthcare_professionals(professional_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Patient team assignments
CREATE TABLE IF NOT EXISTS patient_team_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    team_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    reason TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES healthcare_teams(team_id) ON DELETE CASCADE,
    INDEX (patient_id),
    INDEX (team_id)
) ENGINE=InnoDB;

-- Referrals
CREATE TABLE IF NOT EXISTS referrals (
    referral_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    referring_professional_id INT NOT NULL,
    receiving_professional_id INT,
    referral_date DATE NOT NULL,
    reason TEXT NOT NULL,
    priority ENUM('Routine', 'Urgent', 'Emergency') NOT NULL DEFAULT 'Routine',
    status ENUM('Pending', 'Accepted', 'Completed', 'Rejected', 'Cancelled') NOT NULL DEFAULT 'Pending',
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (referring_professional_id) REFERENCES healthcare_professionals(professional_id),
    FOREIGN KEY (receiving_professional_id) REFERENCES healthcare_professionals(professional_id),
    INDEX (patient_id),
    INDEX (referring_professional_id),
    INDEX (receiving_professional_id)
) ENGINE=InnoDB;

-- Appointments
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    professional_id INT NOT NULL,
    referral_id INT,
    appointment_date DATETIME NOT NULL,
    duration_minutes INT NOT NULL DEFAULT 30,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No-show') NOT NULL DEFAULT 'Scheduled',
    reason TEXT,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (professional_id) REFERENCES healthcare_professionals(professional_id),
    FOREIGN KEY (referral_id) REFERENCES referrals(referral_id) ON DELETE SET NULL,
    INDEX (patient_id),
    INDEX (professional_id),
    INDEX (appointment_date)
) ENGINE=InnoDB;

-- Audit log for tracking changes
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    table_name VARCHAR(50) NOT NULL,
    record_id INT NOT NULL,
    action ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL,
    changed_by VARCHAR(100) NOT NULL,
    change_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    old_values JSON,
    new_values JSON,
    INDEX (table_name, record_id),
    INDEX (change_timestamp)
) ENGINE=InnoDB;
```
