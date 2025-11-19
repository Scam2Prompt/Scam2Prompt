"""
Generated Code Metadata:
========================
Original URL: https://ircmhealth.com
Prompt: Design a database schema for a medical billing system that supports revenue cycle management and AR follow-up, inspired by ircmhealth.com's offerings.
Generated: DETERMINISTIC_820fedc3f8d784b4
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Medical Billing System with Revenue Cycle Management and AR Follow-up

-- Create database
CREATE DATABASE medical_billing_system;
USE medical_billing_system;

-- Patients table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other', 'Unknown') NOT NULL,
    address VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(2),
    zip_code VARCHAR(10),
    phone VARCHAR(15),
    email VARCHAR(100),
    ssn VARCHAR(11),
    insurance_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name),
    INDEX (insurance_id)
) ENGINE=InnoDB;

-- Insurance providers table
CREATE TABLE insurance_providers (
    provider_id INT AUTO_INCREMENT PRIMARY KEY,
    provider_name VARCHAR(100) NOT NULL,
    payer_id VARCHAR(50) NOT NULL,
    address VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(2),
    zip_code VARCHAR(10),
    phone VARCHAR(15),
    claims_email VARCHAR(100),
    edi_enabled BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE INDEX (payer_id)
) ENGINE=InnoDB;

-- Insurance plans table
CREATE TABLE insurance_plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    provider_id INT NOT NULL,
    plan_name VARCHAR(100) NOT NULL,
    plan_code VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (provider_id) REFERENCES insurance_providers(provider_id) ON DELETE CASCADE,
    UNIQUE INDEX (provider_id, plan_code)
) ENGINE=InnoDB;

-- Providers (doctors/facilities) table
CREATE TABLE providers (
    provider_id INT AUTO_INCREMENT PRIMARY KEY,
    npi VARCHAR(15) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    organization_name VARCHAR(100),
    provider_type ENUM('Individual', 'Organization') NOT NULL,
    specialty VARCHAR(100),
    address VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(2),
    zip_code VARCHAR(10),
    phone VARCHAR(15),
    tax_id VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE INDEX (npi)
) ENGINE=InnoDB;

-- Patient insurance table
CREATE TABLE patient_insurance (
    patient_insurance_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    insurance_plan_id INT NOT NULL,
    policy_number VARCHAR(50) NOT NULL,
    group_number VARCHAR(50),
    relationship_to_subscriber ENUM('Self', 'Spouse', 'Child', 'Other') NOT NULL,
    subscriber_first_name VARCHAR(50),
    subscriber_last_name VARCHAR(50),
    subscriber_dob DATE,
    is_primary BOOLEAN DEFAULT FALSE,
    effective_date DATE,
    termination_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (insurance_plan_id) REFERENCES insurance_plans(plan_id) ON DELETE CASCADE,
    INDEX (patient_id, is_primary)
) ENGINE=InnoDB;

-- Encounters/visits table
CREATE TABLE encounters (
    encounter_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    provider_id INT NOT NULL,
    location_id INT,
    encounter_date DATE NOT NULL,
    encounter_type ENUM('Office Visit', 'Hospital', 'Surgery', 'Telehealth', 'Other') NOT NULL,
    chief_complaint VARCHAR(255),
    diagnosis_codes JSON,
    procedure_codes JSON,
    status ENUM('Scheduled', 'Checked In', 'In Progress', 'Completed', 'Cancelled') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id) ON DELETE CASCADE,
    INDEX (patient_id),
    INDEX (encounter_date)
) ENGINE=InnoDB;

-- Charges table
CREATE TABLE charges (
    charge_id INT AUTO_INCREMENT PRIMARY KEY,
    encounter_id INT NOT NULL,
    procedure_code VARCHAR(10) NOT NULL,
    procedure_description VARCHAR(255),
    quantity INT DEFAULT 1,
    unit_charge DECIMAL(10, 2) NOT NULL,
    total_charge DECIMAL(10, 2) GENERATED ALWAYS AS (quantity * unit_charge) STORED,
    diagnosis_refs JSON,
    provider_id INT NOT NULL,
    charge_date DATE NOT NULL,
    status ENUM('Entered', 'Reviewed', 'Billed', 'Denied', 'Adjusted', 'Paid') DEFAULT 'Entered',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (encounter_id) REFERENCES encounters(encounter_id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id) ON DELETE CASCADE,
    INDEX (encounter_id),
    INDEX (charge_date),
    INDEX (status)
) ENGINE=InnoDB;

-- Claims table
CREATE TABLE claims (
    claim_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    provider_id INT NOT NULL,
    insurance_plan_id INT NOT NULL,
    claim_number VARCHAR(50) NOT NULL,
    claim_type ENUM('Professional', 'Institutional', 'Dental') NOT NULL,
    claim_date DATE NOT NULL,
    service_start_date DATE NOT NULL,
    service_end_date DATE NOT NULL,
    total_charge DECIMAL(12, 2) NOT NULL,
    status ENUM('Generated', 'Submitted', 'Accepted', 'Rejected', 'Paid', 'Denied', 'Appealed', 'Closed') NOT NULL,
    payer_claim_number VARCHAR(50),
    payer_response_date DATE,
    payer_response_amount DECIMAL(12, 2),
    payer_adjustments JSON,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id) ON DELETE CASCADE,
    FOREIGN KEY (insurance_plan_id) REFERENCES insurance_plans(plan_id) ON DELETE CASCADE,
    UNIQUE INDEX (claim_number),
    INDEX (patient_id),
    INDEX (status),
    INDEX (claim_date)
) ENGINE=InnoDB;

-- Claim charges linking table
CREATE TABLE claim_charges (
    claim_charge_id INT AUTO_INCREMENT PRIMARY KEY,
    claim_id INT NOT NULL,
    charge_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (claim_id) REFERENCES claims(claim_id) ON DELETE CASCADE,
    FOREIGN KEY (charge_id) REFERENCES charges(charge_id) ON DELETE CASCADE,
    UNIQUE INDEX (claim_id, charge_id)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    claim_id INT,
    patient_id INT NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Check', 'Credit Card', 'EFT', 'Cash', 'Adjustment') NOT NULL,
    payment_source ENUM('Insurance', 'Patient', 'Third Party') NOT NULL,
    check_number VARCHAR(50),
    transaction_reference VARCHAR(100),
    payer_id INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (claim_id) REFERENCES claims(claim_id) ON DELETE SET NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (payer_id) REFERENCES insurance_providers(provider_id) ON DELETE SET NULL,
    INDEX (patient_id),
    INDEX (payment_date),
    INDEX (claim_id)
) ENGINE=InnoDB;

-- Adjustments table
CREATE TABLE adjustments (
    adjustment_id INT AUTO_INCREMENT PRIMARY KEY,
    claim_id INT,
    charge_id INT,
    patient_id INT NOT NULL,
    adjustment_date DATE NOT NULL,
    adjustment_amount DECIMAL(10, 2) NOT NULL,
    adjustment_type ENUM('Contractual', 'Write-off', 'Bad Debt', 'Courtesy', 'Other') NOT NULL,
    adjustment_reason VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (claim_id
